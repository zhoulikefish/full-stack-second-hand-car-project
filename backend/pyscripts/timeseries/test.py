import random

def generate_fake_predictions(future_points=5, unit_predict_range=12):
    result = []
    ranked_feat = []

    for i in range(future_points):
        # 生成随机的车价数据（范围可以根据实际情况调整）
        price = random.uniform(350000, 500000)
        result.append(price)

        # 生成随机的特征名称
        feature = f"Feature_{i}"
        ranked_feat.append(feature)

    return result, ranked_feat

if __name__ == '__main__':
    _future_points = 5
    _unit_predict_range = 12

    result, ranked_feat = generate_fake_predictions(_future_points, _unit_predict_range)

    print(result)
