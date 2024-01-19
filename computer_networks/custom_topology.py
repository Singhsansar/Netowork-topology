import os 
from mininet.node import OVSSwitch, RemoteController
from mininet.cli import CLI
from mininet.net import Mininet
from mininet.node import Controller, OVSSwitch

def create_openflow_topology():
    
    net = Mininet(controller=Controller, switch=OVSSwitch)

    net.delController('controller')

    new_controller = net.addController('new_controller', controller=RemoteController, ip='127.0.0.1', port=6633)

    
    
    
    c0 = net.addController('c0')

    # Add a switch
    s1 = net.addSwitch('s1')

    # Add hosts and link them to the switch
    h1 = net.addHost('h1')
    h2 = net.addHost('h2')
    net.addLink(h1, s1)
    net.addLink(h2, s1)

    # Start the network and the controller
    net.start()
    net.stop()
# Call the collect_rtt function
    h1, h2 = net.get('h1', 'h2')
    print(f"Collecting RTT between {h1.IP()} and {h2.IP()}...")
    collect_rtt(h1.IP(), h2.IP(), 'rtt_data.txt')

    CLI(net)
    net.stop()



def collect_rtt(host1, host2, filename):
    print(f"Pinging {host2} from {host1}...")
    result = os.popen(f'ping -c 4 {host2}').read()
    if result:  # Check if the ping command returned any output
        print(result)
        try:
            with open(filename, 'w') as f:
                f.write(result)
            print(f"RTT data saved to {filename}")
        except IOError as e:
            print(f"Error writing to file: {e}")
    else:
        print("Error: The ping command did not return any output.")


if __name__ == '__main__':
    create_openflow_topology()
