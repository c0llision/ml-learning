#!/usr/bin/env python3
import numpy as np

def relu(input):
    return max(0, input)

if __name__ == '__main__':
    input_layer = np.array([2, 3])
    weights = {'node_0': np.array([1, 1]),
               'node_1': np.array([-1, 1]),
               'output': np.array([2, -2])
                }

    node_0 = (input_layer * weights['node_0']).sum()
    node_1 = (input_layer * weights['node_1']).sum()

    hidden_layer = np.array([node_0, node_1])

    print(hidden_layer)

    output = (hidden_layer * weights['output']).sum()

    print(output)
