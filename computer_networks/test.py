from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.net import Mininet
from mininet.node import RemoteController

def create_openflow_topology(topo_type, num_hosts, controller_ip='127.0.0.1', controller_port=6633):
    net = Mininet(controller=RemoteController)
    controller = net.addController('c0', port=controller_port)

    # Create OpenFlow topology based on the specified type
    if topo_type == 'single':
        switch = net.addSwitch('s1')
        h1 = net.addHost('h1')
        h2 = net.addHost('h2')
        net.addLink(h1, switch)
        net.addLink(h2, switch)

    elif topo_type == 'linear':
        prev_switch = None
        for i in range(1, num_hosts + 1):
            switch = net.addSwitch('s{}'.format(i))
            host = net.addHost('h{}'.format(i))
            net.addLink(host, switch)
            if prev_switch:
                net.addLink(prev_switch, switch)
            prev_switch = switch
        h1 = net.get('h1')
        h2 = net.get('h2')

    elif topo_type == 'tree':
        switch = net.addSwitch('s1')
        hosts = [net.addHost('h{}'.format(i)) for i in range(1, num_hosts + 1)]
        for host in hosts:
            net.addLink(host, switch)
        h1 = net.get('h1')
        h2 = net.get('h2')

    net.build()
    controller.start()
    net.start()
    h1.cmd('ping -c 1 h2')
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    create_openflow_topology('single', 2)
