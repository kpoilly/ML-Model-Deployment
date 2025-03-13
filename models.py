import numpy as np
import torch
import torch.nn as nn
from sklearn.preprocessing import StandardScaler

class Network(nn.Module):
    """
Class representing the Artificial Neural Network
    """
    def __init__(self, n_inputs: int, n_layers: int, n_neurons: int, n_outputs: int):
        super(Network, self).__init__()
        self.network = nn.ModuleList()
        
        self.network.append(nn.Linear(n_inputs, n_neurons))
        self.network.append(nn.ReLU())
        
        for _ in range(n_layers):
            self.network.append(nn.Linear(n_neurons, n_neurons))
            self.network.append(nn.ReLU())
         
        self.network.append(nn.Linear(n_neurons, n_outputs))
        self.network.append(nn.Softmax(dim=1))
        
        self.scaler = StandardScaler()
        self.params = ""
        self.train_losses = []
        self.train_accu = []
        self.val_losses = []
        self.val_accu = []
    
    def forward(self, x):
        for layer in self.network:
            x = layer(x)
        return x
    
    def predict(self, input_data: np.ndarray) -> np.ndarray:
        """
        Model's prediction function.
        """
        X = self.scaler.transform(input_data.reshape(1, -1).astype(float))
        input_tensor = torch.from_numpy(X).float()
        self.eval()
        
        with torch.no_grad():
            output_tensor = self.forward(input_tensor)
        
        prediction = output_tensor.cpu().numpy()
        return prediction
