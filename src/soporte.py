#%% 
import pandas as pd
import numpy as np
pd.set_option('display.float_format', '{:.2f}'.format)
# Visualización
# ------------------------------------------------------------------------------
import matplotlib.pyplot as plt
import seaborn as sns

# Evaluar linealidad de las relaciones entre las variables
# y la distribución de las variables
# ------------------------------------------------------------------------------
import scipy.stats as stats
from scipy.stats import ttest_ind, norm, chi2_contingency, f_oneway
from sklearn.impute import SimpleImputer
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn.impute import KNNImputer
# Configuración
# -----------------------------------------------------------------------
pd.set_option('display.max_columns', None) # para poder visualizar todas las columnas de los DataFrames
pd.set_option('display.float_format', '{:.2f}'.format)

# Gestión de los warnings
# -----------------------------------------------------------------------
import warnings
warnings.filterwarnings("ignore")
# %%
df_cancelaciones = pd.read_csv("../fichero/hotel-bookings.csv", index_col=0)
print("Leemos fichero")
# %%
df_cancelaciones.head()
#%%
#EDA: info, tipo de variables, nulos, value_counts
def exploracion (dataframe):
    
    