import pandas as pd 
import numpy as np                  
import matplotlib.pyplot as plt
import seaborn as sns
import geopandas as gpd
import torch
import torch.nn as nn
import torch.nn.functional as F

input_tensor = torch.tensor([[0.3445, 0.4546, -0.2356, -0.3457,0.2345,  -0.6474]])  
# create a 1x6 tensor with random values

model = nn.Sequential( nn.Linear(6,1),        # input layer                                     
                          nn.Linear(1,1))

output_tensor = model(input_tensor)
print(output_tensor)