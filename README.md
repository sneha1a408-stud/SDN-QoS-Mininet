# SDN QoS Priority Controller

## Objective
To implement a QoS-based SDN controller that prioritizes ICMP traffic over other traffic.

## Tools Used
- Mininet
- POX Controller
- Ubuntu VM

## Implementation
- A custom POX controller was developed.
- ICMP packets are classified as high priority.
- TCP traffic (generated using iperf) is treated as low priority.
- Implemented using OpenFlow packet inspection and match-action rules.

## Testing
- pingall → ICMP traffic (High priority)
- iperf → TCP traffic (Low priority)

## Output
- Controller logs show classification:
  - "High priority ICMP packet detected"
  - "Low priority traffic"
