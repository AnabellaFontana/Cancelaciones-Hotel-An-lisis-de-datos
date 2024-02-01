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
def lectura_fichero(nombre):
  return pd.read_csv(nombre, index_col=0)
 
# %%
df_cancelaciones = lectura_fichero("../hotel-bookings.csv")
df_cancelaciones.head()
#%%
#EDA: info, tipo de variables, nulos, value_counts
def exploracion (dataframe):
    print(dataframe.shape)
    dataframe.info()

    print(" ------ ")
    nulos_esta_cat = dataframe[dataframe.columns[dataframe.isnull().any()]].select_dtypes(include = "O").columns
    print("Las columnas categóricas que tienen nulos son : \n ")
    print(nulos_esta_cat)
    print(" ----- ")
    nulos_cate_num = dataframe[dataframe.columns[dataframe.isnull().any()]].select_dtypes(exclude = "O").columns
    print("Las columnas numéricas que tienen nulos son : \n ")
    print(nulos_cate_num)

    for columna in dataframe:
        print(dataframe[columna].value_counts().head())

#%%
exploracion(df_cancelaciones)
 
# %%
df_cancelaciones.isnull().sum()
# %%
#Cambiar el formato de lead_time de float a int 
#Cambiar  arrival date year de float a int 
#cambiar arrival_date_week_number de float a int 
#cambiar arrival_date_day_of_month de float a int 
#cambiar de float a int stays_in_weekend_nights,stays_in_week_nights,adults,children, babies, is_repeated_guest
#previous_cancellations, previous_bookings_not_canceled, booking_changes,agent,company
# days_in_waiting_list , required_car_parking_spaces ,total_of_special_requests   
#Cambiar reservation_status_date por formato fecha
#Eliminar la columna 0
#Mirar reseverve room type y 'assigned_room_type', completar una con otra. Son iguales
# %%
df_cancelaciones.select_dtypes(include= 'O')
df_cancelaciones.duplicated().sum()
#%%
df_cancelaciones[df_cancelaciones.duplicated(keep=False)]
# %%
