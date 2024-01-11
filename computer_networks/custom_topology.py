#!/usr/bin/env python3
# custom_topology.py
from mininet.net import Mininet
from mininet.node import OVSSwitch, RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel

def create_openflow_topology(topo_type, num_hosts, controller_ip='127.0.0.1', controller_port=6633):
    net = Mininet(controller=RemoteController, switch=OVSSwitch)
    controller = net.addController('controller', ip=controller_ip, port=controller_port)

    # Create OpenFlow topology based on the specified type
    if topo_type == 'single':
        switch = net.addSwitch('s1')
        hosts = [net.addHost('h{}'.format(i)) for i in range(1, num_hosts + 1)]
        for host in hosts:
            net.addLink(host, switch)

    elif topo_type == 'linear':
        prev_switch = None
        for i in range(1, num_hosts + 1):
            switch = net.addSwitch('s{}'.format(i))
            host = net.addHost('h{}'.format(i))
            net.addLink(host, switch)
            if prev_switch:
                net.addLink(prev_switch, switch)
            prev_switch = switch

    elif topo_type == 'tree':
        switch = net.addSwitch('s1')
        hosts = [net.addHost('h{}'.format(i)) for i in range(1, num_hosts + 1)]
        for host in hosts:
            net.addLink(host, switch)

    net.build()
    controller.start()
    net.start()

    # CLI(net)
    # net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    create_openflow_topology('single', 4)
