import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")
pd.set_option("display.max_columns", 100)

from sklearn.linear_model import LinearRegression, SGDRegressor, Ridge, Lasso, ElasticNet
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import GradientBoostingRegressor, AdaBoostRegressor
from sklearn.tree import DecisionTreeRegressor, ExtraTreeRegressor
from xgboost import XGBRegressor
from sklearn.svm import SVR
from sklearn.neural_network import MLPRegressor

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.preprocessing import StandardScaler

def algo_test(x, y):
    # Veriyi eğitim ve test olarak bölme
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=42)
    
    # Özellikleri ölçeklendirme
    scaler = StandardScaler()
    x_train_scaled = scaler.fit_transform(x_train)
    x_test_scaled = scaler.transform(x_test)
    
    # Modelleri ve isimlerini bir sözlükte saklama
    models = {
        'Linear Regression': LinearRegression(),
        'Ridge': Ridge(),
        'Lasso': Lasso(),
        'ElasticNet': ElasticNet(),
        'SGDRegressor': SGDRegressor(),
        'Extra Tree': ExtraTreeRegressor(),
        'Gradient Boosting': GradientBoostingRegressor(),
        'KNeighborsRegressor': KNeighborsRegressor(),
        'AdaBoost': AdaBoostRegressor(),
        'Decision Tree': DecisionTreeRegressor(),
        'XGBRegressor': XGBRegressor(),
        'SVR': SVR(),
        'MLPRegressor': MLPRegressor()
    }
    
    results = []

    for name, model in models.items():
        # Ölçeklendirilmiş verileri kullanan modeller
        if name in ['SGDRegressor', 'KNeighborsRegressor', 'SVR', 'MLPRegressor']:
            model.fit(x_train_scaled, y_train)
            predictions = model.predict(x_test_scaled)
        else:
            model.fit(x_train, y_train)
            predictions = model.predict(x_test)
        
        r2 = r2_score(y_test, predictions)
        rmse = mean_squared_error(y_test, predictions, squared=False)
        mae = mean_absolute_error(y_test, predictions)
        
        results.append({
            'Model': name,
            'R_Squared': r2,
            'RMSE': rmse,
            'MAE': mae
        })
    
    result_df = pd.DataFrame(results)
    result_df = result_df.sort_values('R_Squared', ascending=False)
    
    # Sonuçları görselleştirme (isteğe bağlı)
    import matplotlib.pyplot as plt
    plt.figure(figsize=(10, 6))
    plt.barh(result_df['Model'], result_df['R_Squared'])
    plt.xlabel('R_Squared')
    plt.title('Modellerin R^2 Skorları')
    plt.gca().invert_yaxis()
    plt.show()
    
    return result_df
