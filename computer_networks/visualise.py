#!/usr/bin/env python3
# visualize_results.py
import matplotlib.pyplot as plt

def plot_rtt(file_path):
    with open(file_path, 'r') as f:
        rtt_data = f.readlines()
    rtt_values = [float(line.split()[6][5:-2]) for line in rtt_data]
    plt.plot(rtt_values, marker='o')
    plt.xlabel('Ping Number')
    plt.ylabel('Round-Trip Time (ms)')
    plt.title('Round-Trip Time Over Pings')
    plt.show()

if __name__ == '__main__':
    rtt_file_path = 'rtt_data.txt'
    plot_rtt(rtt_file_path)
