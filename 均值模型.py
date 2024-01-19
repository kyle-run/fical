import numpy as np
import pandas as pd
from scipy.optimize import minimize

# 假設我們有三個資產的歷史回報數據
data = {
    'Asset1': [0.12, 0.10, 0.11, 0.09, 0.15],
    'Asset2': [0.04, 0.05, 0.06, 0.03, 0.07],
    'Asset3': [0.10, 0.12, 0.11, 0.13, 0.14]
}

df = pd.DataFrame(data)

# 計算預期回報和風險
mean_returns = df.mean()
cov_matrix = df.cov()

# 最優化函數
def portfolio_volatility(weights, mean_returns, cov_matrix):
    return np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))

# 約束條件：資產權重總和為1
constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})

# 資產權重的範圍限制
bounds = tuple((0, 1) for asset in range(len(mean_returns)))

# 初始猜測（平均分配）
init_guess = len(mean_returns) * [1. / len(mean_returns),]

# 最優化求解
optimal = minimize(portfolio_volatility, init_guess, args=(mean_returns, cov_matrix), method='SLSQP', bounds=bounds, constraints=constraints)

# 輸出最優權重
print(optimal.x)
