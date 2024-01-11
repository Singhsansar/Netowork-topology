#!/bin/bash

topologies=("single" "linear" "tree")

for topo in "${topologies[@]}"; do
    echo "Running experiment with $topo topology..."
    sudo mn --custom custom_topology.py --topo $topo
    echo "Experiment with $topo topology completed."
done
