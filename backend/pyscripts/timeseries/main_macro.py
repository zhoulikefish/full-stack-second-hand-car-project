# -*- coding: utf-8 -*-
import sys

# 获取参数
if len(sys.argv) >= 4:
    brand = sys.argv[1]
    model = sys.argv[2]
    license_time = sys.argv[3]



import joblib
import pickle
from datetime import datetime
import pandas as pd
import xgboost as xgb
import lightgbm as lgb
import warnings
import numpy as np

from basic import get_unique_values
from basic import preprocess_license_time
from basic import preprocess_update_time
from basic import preprocess_mileage
from basic import preprocess_displacement
from basic import preprocess_num_transfer
from basic import preprocess_pure_elec_range
from basic import preprocess_fast_charge_time
from basic import preprocess_battery_capacity
from basic import preprocess_slow_charge_time
from basic import map_unique_value_to_df
from basic import group_by

warnings.filterwarnings("ignore")
_future_points = 5
_unit_predict_range = 12

def load_models_macro():
    model_xgb = joblib.load("model/model_xgb.pkl")
    model_lgb = joblib.load("model/model_lgb.pkl")
    return model_xgb, model_lgb

def load_weights():
    with open("model/weights_macro.pkl", "rb") as file:
        weight_xgb, weight_lgb = pickle.load(file)
    return weight_xgb, weight_lgb

def rank_feature_importance(model_xgb: xgb.XGBRegressor, model_lgb: lgb.LGBMRegressor, weight_xgb, weight_lgb, df: pd.DataFrame):
    # Feature importance ranking
    feature_importance_xgb = model_xgb.feature_importances_
    feature_importance_lgb = model_lgb.feature_importances_

    # Combine feature importance from both models
    combined_importance = weight_xgb * feature_importance_xgb + weight_lgb * feature_importance_lgb

    # Create a DataFrame to store feature names and their importance scores
    feature_importance_df = pd.DataFrame({'Feature': df.columns, 'Importance': combined_importance})
    
    # Rank the features by importance score in descending order
    ranked_features = feature_importance_df.sort_values('Importance', ascending=False)
    
    return ranked_features

def predict_price(vehicle_info):
    
    model_xgb, model_lgb = load_models_macro()
    model_xgb._n_classes = 1
    model_lgb._n_classes = 1
    weight_xgb, weight_lgb = load_weights()
    # print(vehicle_info.columns)
    # 进行预测的处理...
    y_xgb = model_xgb.predict(vehicle_info)
    y_lgb = model_lgb.predict(vehicle_info)

    
    
    
    # results ensemble
    predict_y_xlgb = y_xgb * weight_xgb + y_lgb * weight_lgb  # weighted average
    result_xlgb = pd.DataFrame()
    # result_xlgb["SaleID"] = vehicle_info["SaleID"]
    result_xlgb["price"] = predict_y_xlgb
    result_xlgb.loc[result_xlgb["price"] < 2, "price"] = 2.0


    lits = []
    for i in range(_future_points):

        vehicle_info['used_time'] = vehicle_info['used_time'] + _unit_predict_range

        y_xgb = model_xgb.predict(vehicle_info)
        y_lgb = model_lgb.predict(vehicle_info)

        # results ensemble
        predict_y_xlgb = y_xgb * weight_xgb + y_lgb * weight_lgb  # weighted average
        # result_xlgb["SaleID"] = _test_data["SaleID"]


        column_name = "price_{}".format(i)
        result_xlgb[column_name] = predict_y_xlgb
        result_xlgb.loc[result_xlgb[column_name] < 2, column_name] = 2.0

    
    
    
    # 判断结果是否在正常范围内
    if(predict_y_xlgb<0):
        predict_y_xlgb = 0
    
        
    # feature importance
    ranked_feat_res = rank_feature_importance(model_xgb, model_lgb, weight_xgb, weight_lgb, vehicle_info)
    
    ranked_feat = pd.DataFrame()
    # ranked_feat['Feature'] = ranked_min_feat['Feature']
    # ranked_feat['Importance'] = ranked_min_feat['Importance']+ranked_max_feat['Importance']
    ranked_feat = ranked_feat_res.sort_values('Importance', ascending=False)
    ranked_feat = ranked_feat_res.drop('Importance', axis = 1 ,inplace=False)
    # print(ranked_feat)
    
    # 首先将pandas读取的数据转化为array
    ranked_feat = np.array(ranked_feat)
    # 然后转化为list形式
    ranked_feat =ranked_feat.tolist()
    # ranked_feat.remove('image')
    
    return result_xlgb, ranked_feat

def read_input():
    # input_list = {
    #     'brand':[input(f"请输入品牌（brand）: ")], 
    #     'model':[input(f"请输入车型（model）的值: ")], 
    #     'license_year':[input(f"请输入上牌年份: ")], 
    #     'license_month':[input(f"请输入上牌月份: ")], 
    #     'update_time':[], 
    #     'mileage':[input(f"请输入里程数: ")], 
    #     'transmission':[input(f"请输入自动/手动: ")], 
    #     'emission_standards':[input(f"请输入排放标准: ")], # {nan: 0, '国III+OBD': 1, '欧V': 2, '国VI': 3, '国III': 4, '国IV/京V': 5, '国V': 6, '国V(国VI)': 7, '国V+OBD': 8, '欧IV': 9, '-': 10, '国IV/国V': 11, '国IV+OBD': 12, '国IV': 13, '国IV(国V)+OBD': 14, '国IV(国V)': 15, '欧IV+OBD': 16, '欧V+OBD': 17, '欧III': 18, '欧II': 19, '欧VI': 20, '国II': 21}
    #     'displacement':[input(f"请输入发动机容积的值: ")], 
    #     'inspection_due':[], 
    #     'insurance_due':[], 
    #     'num_of_transfer':[input(f"请输入转手次数的值: ")], 
    #     'location':[input(f"请输入地点: ")], # {'台州': 0, '武汉': 1, nan: 2, '威海': 3, '滁州': 4, '丽江': 5, '扬州': 6, '长沙': 7, '盐城': 8, '滨州': 9, '运城': 10, '四平': 11, '柳州': 12, '江门': 13, '葫芦岛': 14, '揭阳': 15, '荆州': 16, '巴中': 17, '盘锦': 18, '驻马店': 19, '承德': 20, '百色': 21, '淮安': 22, '临汾': 23, '益阳': 24, '朝阳': 25, '随州': 26, '黔西南': 27, '焦作': 28, '廊坊': 29, '梅州': 30, '阿坝': 31, '云浮': 32, '包头': 33, '莱芜': 34, '汕头': 35, '青岛': 36, '常州': 37, '大理': 38, '福州': 39, '钦州': 40, '丹东': 41, '十堰': 42, '惠州': 43, '洛阳': 44, '济宁': 45, '延安': 46, '苏州': 47, '邯郸': 48, '镇江': 49, '马鞍山': 50, '北海': 51, '南充': 52, '烟台': 53, '咸阳': 54, '广元': 55, '绍兴': 56, '金华': 57, '齐齐哈尔': 58, '吉安': 59, '泰州': 60, '清远': 61, '遵义': 62, '鹤壁': 63, '广州': 64, '衡阳': 65, '泉州': 66, '昭通': 67, '西宁': 68, '银川': 69, '嘉兴': 70, '德州': 71, '本溪': 72, '永州': 73, '东营': 74, '内江': 75, '鄂尔多斯': 76, '绵阳': 77, '郴州': 78, '哈尔滨': 79, '茂名': 80, '忻州': 81, '黄冈': 82, '漯河': 83, '潜江': 84, '牡丹江': 85, '泰安': 86, '长治': 87, '六安': 88, '宣城': 89, '连云港': 90, '营口': 91, '肇庆': 92, '聊城': 93, '济源': 94, '吉林': 95, '重庆': 96, '龙岩': 97, '太原': 98, '济南': 99, '上饶': 100, '咸宁': 101, '厦门': 102, '佛山': 103, '毕节': 104, '周口': 105, '万宁': 106, '定西': 107, '南京': 108, '沧州': 109, '玉溪': 110, '湛江': 111, '宜昌': 112, '抚顺': 113, '淄博': 114, '朔州': 115, '呼和浩特': 116, '吴忠': 117, '中卫': 118, '濮阳': 119, '昌吉': 120, '佳木斯': 121, '宿迁': 122, '锦州': 123, '南阳': 124, '延边': 125, '来宾': 126, '丽水': 127, '日照': 128, '临沂': 129, '海口': 130, '漳州': 131, '平顶山': 132, '淮南': 133, '郑州': 134, '长春': 135, '保定': 136, '张家口': 137, '三明': 138, '湘潭': 139, '桂林': 140, '榆林': 141, '沈阳': 142, '武威': 143, '莆田': 144, '无锡': 145, '宜春': 146, '开封': 147, '汕尾': 148, '衡水': 149, '上海': 150, '眉山': 151, '北京': 152, '南通': 153, '凉山': 154, '杭州': 155, '渭南': 156, '萍乡': 157, '甘孜': 158, '新余': 159, '文山': 160, '南昌': 161, '昆明': 162, '防城港': 163, '唐山': 164, '襄阳': 165, '菏泽': 166, '乌鲁木齐': 167, '淮北': 168, '鞍山': 169, '赤峰': 170, '汉中': 171, '玉林': 172, '宿州': 173, '鹤岗': 174, '枣庄': 175, '河源': 176, '三亚': 177, '兰州': 178, '张掖': 179, '衢州': 180, '徐州': 181, '潮州': 182, '大连': 183, '安庆': 184, '巴音郭楞': 185, '达州': 186, '宜宾': 187, '石家庄': 188, '潍坊': 189, '红河': 190, '蚌埠': 191, '临沧': 192, '常德': 193, '张家界': 194, '成都': 195, '天津': 196, '芜湖': 197, '邵阳': 198, '南宁': 199, '岳阳': 200, '景德镇': 201, '遂宁': 202, '曲靖': 203, '庆阳': 204, '深圳': 205, '乌兰察布': 206, '九江': 207, '邢台': 208, '雅安': 209, '保山': 210, '晋中': 211, '铜仁': 212, '合肥': 213, '黄山': 214, '亳州': 215, '湖州': 216, '秦皇岛': 217, '乐山': 218, '安顺': 219, '池州': 220, '白银': 221, '抚州': 222, '自贡': 223, '阳江': 224, '宁德': 225, '乌海': 226, '商丘': 227, '娄底': 228, '晋城': 229, '阜阳': 230, '株洲': 231, '东莞': 232, '大庆': 233, '安阳': 234, '贵港': 235, '西双版纳': 236, '铜陵': 237, '信阳': 238, '泸州': 239, '大同': 240, '珠海': 241, '三门峡': 242, '梧州': 243, '中山': 244, '新乡': 245, '舟山': 246, '南平': 247, '温州': 248, '德阳': 249, '韶关': 250, '西安': 251, '许昌': 252, '宁波': 253, '河池': 254, '六盘水': 255, '通辽': 256, '贵阳': 257, '赣州': 258, '黔南': 259}
    #     'engine':[], 
    #     'color':[input(f"请输入颜色: ")], 
    #     'fuel_standard':[input(f"请输入燃油类型 95/92/98/89: ")], 
    #     'drive_model':[input(f"请输入驱动方式: ")], #{nan: 0, '前置后驱': 1, '双电机四驱': 2, '前置四驱': 3, '-': 4,'中置后驱': 5, '前置前驱': 6, '中置四驱': 7, '后置四驱': 8, '后置后驱': 9}
    #     'highlight':[], 
    #     'description':[], 
    #     'image':[], 
    #     'fuel_type':[input(f"请输入燃料类型: ")], # {nan: 0, '插电混动': 1, '纯电动': 2, '增程式': 3}
    #     'pure_elec_range':[input(f"请输入纯电续航里程: ")], 
    #     'fast_charge_time':[input(f"请输入快速充电时间: ")], 
    #     'battery_capacity':[input(f"请输入电池容量: ")], 
    #     'slow_charge_time':[input(f"请输入慢速充电时间: ")],
    #     'update_year':[],
    #     'update_month':[],
    #     'update_day':[],
    #     # 'deal':[],
    #     # 'gdp':[]
    # }
    
    input_list = {
        'brand':["大众"], 
        'model':["迈特威"], 
        'license_year':[2008], 
        'license_month':[4], 
        'update_time':[], 
        'mileage':[12.6], 
        'transmission':["自动"], 
        'emission_standards':["国V"], 
        'displacement':[2], 
        'inspection_due':[], 
        'insurance_due':[], 
        'num_of_transfer':[0], 
        'location':["大连"], 
        'engine':[], 
        'color':["黑色"], 
        'fuel_standard':[95], 
        'drive_model':["前置后驱"], #{nan: 0, '前置后驱': 1, '双电机四驱': 2, '前置四驱': 3, '-': 4,'中置后驱': 5, '前置前驱': 6, '中置四驱': 7, '后置四驱': 8, '后置后驱': 9}
        'highlight':[], 
        'description':[], 
        'image':[], 
        'fuel_type':["插电混动"], # {nan: 0, '插电混动': 1, '纯电动': 2, '增程式': 3}
        'pure_elec_range':[], 
        'fast_charge_time':[], 
        'battery_capacity':[], 
        'slow_charge_time':[],
        'update_year':[],
        'update_month':[],
        'update_day':[],
        # 'deal':[],
        # 'gdp':[]

    }
    if len(sys.argv) >= 4:
        # brand = sys.argv[1]
        # model = sys.argv[2]
        # license_time = sys.argv[3]
        input_list[brand] = brand
        input_list[model] = model
        input_list[license_time] = license_time
    


    
    raw_data = pd.DataFrame.from_dict(input_list, orient='index')
    
    return raw_data.T
def calculate_month_difference(start_year, start_month, end_year, end_month):
    
    if start_year is None or start_month is None or end_year is None or end_month is None:
        return None
    
    
    # Construct the start date and end date datetime objects
    start_date = datetime(int(start_year), int(start_month), 1)
    end_date = datetime(int(end_year), int(end_month), 1)

    # Calculate the month difference
    month_difference = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)

    return month_difference

def encode_macroeconomics(df:pd.DataFrame):
    # read file
    gdp_df = pd.read_csv("./dataset/GDP_df.csv")
    gdp_df['year'] = gdp_df['year'].astype(int)
    gdp_df['month'] = gdp_df['month'].astype(int)
    gdp_df.drop(['year', 'month'],axis = 1, inplace= False)
    
    merged_df = df.merge(gdp_df, left_on=['license_year', 'license_month'], right_on=['year', 'month'], how='left')
    
    # 交易量
    deal_df = pd.read_csv("./dataset/Deal_df.csv")
    deal_df['year'] = deal_df['year'].astype(int)
    deal_df['month'] = deal_df['month'].astype(int)
    deal_df.drop(['year', 'month'],axis = 1, inplace= False)
    
    merged_df = merged_df.merge(deal_df, left_on=['license_year', 'license_month'], right_on=['year', 'month'], how='left')
    # print(merged_df.columns)
    return merged_df
    

def preprocess_input(data:pd.DataFrame):
    """This function takes in the raw dataframe, output the dataframe for feeding model"""
    _test_data = pd.read_csv("./dataset/test.csv")
    _test_data = _test_data.drop(['img_url','url'], axis=1, inplace=False)
    # preprocess_engine(data)
    brand_to_int = get_unique_values("brand", _test_data)
    model_to_int = get_unique_values("model", _test_data)
    transmission_to_int = get_unique_values("transmission", _test_data)
    emission_standards_to_int = get_unique_values("emission_standards", _test_data)
    location_to_int = get_unique_values("location", _test_data)
    new_fuel_engine_to_int = get_unique_values("engine", _test_data)
    color_to_int = get_unique_values("color", _test_data)
    fuel_standard_to_int = get_unique_values("fuel_standard", _test_data)
    drive_model_to_int = get_unique_values("drive_model", _test_data)
    fuel_type_to_int = get_unique_values("fuel_type", _test_data)
    preprocess_license_time(data)
    preprocess_update_time(data)
    #print(data)
    preprocess_mileage(data)
    preprocess_displacement(data)
    preprocess_num_transfer(data)
    preprocess_pure_elec_range(data)
    preprocess_fast_charge_time(data)
    preprocess_battery_capacity(data)
    preprocess_slow_charge_time(data)

    data = map_unique_value_to_df(data, "brand", brand_to_int)
    data = map_unique_value_to_df(data, "model", model_to_int)
    data = map_unique_value_to_df(data, "transmission", transmission_to_int)
    data = map_unique_value_to_df(data, "emission_standards", emission_standards_to_int)
    data = map_unique_value_to_df(data, "location", location_to_int)
    data = map_unique_value_to_df(data, "engine", new_fuel_engine_to_int)
    data = map_unique_value_to_df(data, "color", color_to_int)
    data = map_unique_value_to_df(data, "fuel_standard", fuel_standard_to_int)
    data = map_unique_value_to_df(data, "drive_model", drive_model_to_int)
    data = map_unique_value_to_df(data, "fuel_type", fuel_type_to_int)

    # print(data)

    # encode month difference
    # Convert NaN values to None in the dataframe
    data = data.replace({np.nan: None})
    # Get the current date
    current_date = datetime.now()
    # Calculate the month difference for each row in the dataframe
    data['used_time'] = data.apply(lambda row: calculate_month_difference(row['license_year'], row['license_month'], current_date.year, current_date.month), axis=1)
    data = data.replace({None : np.nan})
    
    # print("===")
    # print(data.columns)
    data = encode_macroeconomics(data)
    # print("===")
    # print(data.columns)
    # last hard code process before feed in model
    data = data.fillna(0.0)
    data = data.drop(['update_time', 'license_year', 'license_month'], axis=1, inplace=False) 
        
    # print(data.columns)
    
    features = [i for i in ['brand', 'model', 'mileage', 'transmission', 'emission_standards', 'displacement', 'inspection_due', 'insurance_due', 'num_of_transfer', 'location', 'engine', 'color', 'fuel_standard', 'drive_model', 'highlight', 'description', 'image', 'fuel_type', 'pure_elec_range', 'fast_charge_time', 'battery_capacity', 'slow_charge_time', 'update_year', 'update_month', 'update_day', 'used_time', 'gdp', 'year_x', 'month_x', 'deal', 'year_y', 'month_y']]
    X_test = data[features]
    X_test = X_test[['brand', 'model', 'mileage', 'transmission', 'emission_standards', 'displacement', 'inspection_due', 'insurance_due', 'num_of_transfer', 'location', 'engine', 'color', 'fuel_standard', 'drive_model', 'highlight', 'description', 'image', 'fuel_type', 'pure_elec_range', 'fast_charge_time', 'battery_capacity', 'slow_charge_time', 'update_year', 'update_month', 'update_day', 'used_time', 'gdp', 'year_x', 'month_x', 'deal', 'year_y', 'month_y']]
    # ['brand', 'model', 'mileage', 'transmission', 'emission_standards', 'displacement', 'inspection_due', 'insurance_due', 'num_of_transfer', 'location', 'engine', 'color', 'fuel_standard', 'drive_model', 'highlight', 'description', 'image', 'fuel_type', 'pure_elec_range', 'fast_charge_time', 'battery_capacity', 'slow_charge_time', 'update_year', 'update_month', 'update_day', 'used_time', 'gdp', 'year_x', 'month_x', 'deal', 'year_y', 'month_y']

    
    
    
    return X_test

if __name__ == '__main__':
    _future_points = int(input("输入预测未来点数 (defalut = 5):"))
    _unit_predict_range = int(input("输入未来点数的间距 (defalut = 12):"))
    raw_df = read_input()
    X_test = preprocess_input(raw_df)
    # print(X_test.columns)
    result_xlgb, ranked_feat = predict_price(X_test)
    result = result_xlgb.iloc[:, 1:].values.flatten().tolist()

    ranked_feat = [item[0] for item in ranked_feat]
    print(result) # float
    # print(max) # float
