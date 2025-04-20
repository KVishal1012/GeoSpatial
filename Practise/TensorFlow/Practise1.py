from IPython import get_ipython
from IPython.display import display

# %%
get_ipython().system('pip install geoai-py leafmap')

# %%
import geoai
import leafmap
import pandas as pd
from geoai.download import (
    download_naip,
    download_overture_buildings,
    extract_building_stats,
)
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split