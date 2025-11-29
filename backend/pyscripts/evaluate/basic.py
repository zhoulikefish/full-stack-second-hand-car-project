from tqdm import tqdm
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import xgboost as xgb
import lightgbm as lgb
import warnings
import pandas as pd
import re

warnings.filterwarnings("ignore")


_train_data = pd.read_csv("./dataset/train.csv")
_test_data = pd.read_csv("./dataset/test.csv")
# print(_test_data.columns)
_train_data['SaleID'] = range(1, len(_train_data) + 1)
_test_data['SaleID'] = range(1, len(_test_data) + 1)

def get_unique_values(column: str, df: pd.DataFrame):
    """This function is for mapping the Chinese character into a unique 
    integer value.
    Input: string, represent the name of the dataframe column
    Output: a dictionary, with each value mapped."""
    unique_values = list(set(df[column]))
    value_to_int = {value: i for i, value in enumerate(unique_values)}
    
    return value_to_int

def extract_numbers_from_string(string):
    # 使用正则表达式匹配数字部分
    numbers = re.findall(r'\d+\.\d+|\d+', string)
    # 将匹配到的数字部分转换为浮点数
    numbers = [float(num) for num in numbers]
    return numbers

def preprocess_license_time(df: pd.DataFrame):
    # df['license_year'] = df['license_time'].str.extract('(\d+)年')
    # df['license_month'] = df['license_time'].str.extract('(\d+)月')
    # # 在接受输入的时候也要把 license time 拆解一下
    # df['license_year'] = pd.to_numeric(df['license_year'])
    # df['license_month'] = pd.to_numeric(df['license_month'])
    pass
    
    
def preprocess_update_time(df: pd.DataFrame):
    # df['update_time'] = pd.to_datetime(df['update_time'])
    # df['update_year'] = df['update_time'].dt.year
    # df['update_month'] = df['update_time'].dt.month
    # df['update_day'] = df['update_time'].dt.day
    pass
    
    
def preprocess_mileage(df: pd.DataFrame):
    # df['mileage'] = df['mileage'].str.replace('万公里', '').astype(float)
    df['mileage'] = df['mileage'].astype(float)
    
def preprocess_displacement(df: pd.DataFrame):
    # df['displacement'] = df['displacement'].str.replace('L', '').astype(float)
    df['displacement'] = df['displacement'].astype(float)
    
def preprocess_num_transfer(df: pd.DataFrame):
    # df['num_of_transfer'] = df['num_of_transfer'].str.replace('次（以车辆登记证为准）', '').astype(float)
    df['num_of_transfer'] = df['num_of_transfer'].astype(float)
    
def preprocess_pure_elec_range(df: pd.DataFrame):
    # df['pure_elec_range'] = df['pure_elec_range'].str.replace('km', '').astype(float)
    df['pure_elec_range'] = df['pure_elec_range'].astype(float)
    
def preprocess_fast_charge_time(df):
    # df["fast_charge_time"] = df["fast_charge_time"].str.extract(r'(\d+\.\d+|\d+)', expand=False)
    # df["fast_charge_time"] = df["fast_charge_time"].replace('-', '0.0')
    df["fast_charge_time"] = df["fast_charge_time"].astype(float)
    return df

def preprocess_battery_capacity(df: pd.DataFrame):
    # df['battery_capacity'] = df['battery_capacity'].str.replace('kwh', '').astype(float)
    df['battery_capacity'] = df['battery_capacity'].astype(float)
    
def preprocess_slow_charge_time(df):
    # df["slow_charge_time"] = df["slow_charge_time"].str.extract(r'(\d+\.\d+|\d+)', expand=False)
    # df["slow_charge_time"] = df["slow_charge_time"].replace('-', '0.0')
    df["slow_charge_time"] = df["slow_charge_time"].astype(float)
    return df

def preprocess_engine(df: pd.DataFrame) -> pd.DataFrame:
    # Extract the last two characters using regex
    # df['engine'] = df['engine'].str.extract(r'([A-Za-z]\d{1,2}\b)')
    pass

def map_unique_value_to_df(df: pd.DataFrame, feature_name: str, mapping_dict: dict) -> pd.DataFrame:
    """Maps unique values in a column of a DataFrame using a given dictionary.
    Inputs:
    - df: pandas DataFrame
    - feature_name: string, the name of the column to map
    - mapping_dict: dictionary, containing the mapping of keys to values
    Returns:
    - df: modified DataFrame with the mapped column
    """
    df[feature_name] = df[feature_name].map(mapping_dict)
    return df

def group_by(df: pd.DataFrame, attributes):
    group_cols = attributes
    
    df['min_price'] = df.groupby(group_cols)['price'].transform('min')
    df['max_price'] = df.groupby(group_cols)['price'].transform('max')
    
    return df
