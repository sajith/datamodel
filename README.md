# datamodel

Each domain, proxied by the customized SDX-LC who communicates between the SDX-controller and the domain (1) provisioning system (eg, Kytos) and (2) monitoring system (BAPM).

Therefore, in the whole SDX system, two types of topology models are needed: 
Domain substrate description model: used by the intra-domain system. 
Domain declaration/advertisement model: generated/passed by the SDX-LC to the SDX-controller for inter-domain topology assembly to support (a) inter-domain path computation; and (b) inter-domain path monitoring and reconfiguration. It would consist of three types of information: (1) Topology abstraction; (2) network resources available for inter-domain connections and their QoS metrics (eg, bw, latency, packet loss, vlan ranges, etc); (3) switching capability (eg, vlan, Q-in-Q, etc).

