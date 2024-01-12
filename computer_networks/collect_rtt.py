#!/usr/bin/env python3
# collect_rtt.py
import subprocess

def collect_rtt(host1, host2):
    print(f"Pinging {host2} from {host1}...")
    result = subprocess.run(['ping', '-c', '4', host2], stdout=subprocess.PIPE, text=True)
    print(result.stdout)

if __name__ == '__main__':
    host1 = '10.0.0.1' 
    host2 = '10.0.0.2'  
    collect_rtt(host1, host2)
