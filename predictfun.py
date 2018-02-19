#!/usr/bin/env python3
# Define predict_with_network()
def predict_with_network(input_data_row, weights):

    # Calculate node 0 value
    node_0_input = ____
    node_0_output = ____

    # Calculate node 1 value
    node_1_input = ____
    node_1_output = ____

    # Put node values into array: hidden_layer_outputs
    hidden_layer_outputs = np.array([node_0_output, node_1_output])
    
    # Calculate model output
    input_to_final_layer = ____
    model_output = ____
    
    # Return model output
    return(model_output)


# Create empty list to store prediction results
results = []
for input_data_row in input_data:
    # Append prediction to results
    results.append(____)

# Print results
print(results)
