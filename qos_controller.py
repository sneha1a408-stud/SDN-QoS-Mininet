from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.packet import ethernet, icmp

log = core.getLogger()

def _handle_PacketIn(event):
    packet = event.parsed

    msg = of.ofp_packet_out()
    msg.data = event.ofp
    msg.in_port = event.port

    if packet.type == ethernet.IP_TYPE:
        ip_packet = packet.payload

        # HIGH PRIORITY → ICMP
        if isinstance(ip_packet.payload, icmp):
            log.info("High priority ICMP packet detected")
        else:
            log.info("Low priority traffic")

    msg.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))
    event.connection.send(msg)

def launch():
    core.openflow.addListenerByName("PacketIn", _handle_PacketIn)
    log.info("QoS Controller Loaded")
