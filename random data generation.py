# coding=utf-8
import numpy as np
from scipy.stats import norm
import pandas as pd


def LHS_norm(N, mean, cv):
    """
    :param std:数据标准差
    :param mean:数据均值
    :param N:拉丁超立方层数
    :return:样本数据
    """
    result = np.empty([N])
    d = 1.0 / N
    for j in range(N):
        result[j] = np.random.uniform(low=j * d, high=(j + 1) * d, size=1)[0]
    np.random.shuffle(result)

    result = norm.ppf(result)
    result = pd.Series(result * cv * mean + mean)
    return result


if __name__ == '__main__':
    job = []
    n = 300
    for i in range(100, 300):
        job.append('job%d'%(i+1))
    job = pd.Series(job)
    Fatigue_1 = LHS_norm(n, 1576, 0.05)
    Fatigue_2 = LHS_norm(n, 0.162, 0.05)
    Fatigue_3 = LHS_norm(n, -0.086, 0.01)
    Fatigue_4 = LHS_norm(n, -0.58, 0.01)
    Creep_fai = LHS_norm(n, 114.8, 0.05)
    Creep_n1 = LHS_norm(n, 0.14, 0.05)
    Creep_wfcrit = LHS_norm(n, 46, 0.05)
    Density = LHS_norm(n, 8.24E-009, 0.00063)
    Creep_temp360 = LHS_norm(n, 5.772E-029, 0.05)
    Creep_temp480 = LHS_norm(n, 1.02E-025, 0.05)
    Creep_temp500 = LHS_norm(n, 3.1E-025, 0.05)
    Creep_temp550 = LHS_norm(n, 5.4E-024, 0.05)
    Creep_temp650 = LHS_norm(n, 1.8231E-023, 0.05)
    Creep_temp800 = LHS_norm(n, 5.8231E-023, 0.05)
    E_temp20 = LHS_norm(n, 203000, 0.05)
    E_temp360 = LHS_norm(n, 191700, 0.05)
    E_temp550 = LHS_norm(n, 185333, 0.05)
    E_temp650 = LHS_norm(n, 182000, 0.05)
    C1_temp20 = LHS_norm(n, 438590, 0.05)
    C1_temp360 = LHS_norm(n, 378590, 0.05)
    C1_temp550 = LHS_norm(n, 368590, 0.05)
    C1_temp650 = LHS_norm(n, 388590, 0.05)
    C2_temp20 = LHS_norm(n, 17000, 0.05)
    C2_temp360 = LHS_norm(n, 18000, 0.05)
    C2_temp550 = LHS_norm(n, 20000, 0.05)
    C2_temp650 = LHS_norm(n, 40000, 0.05)
    C3_temp20 = LHS_norm(n, 30, 0.05)
    C3_temp360 = LHS_norm(n, 30, 0.05)
    C3_temp550 = LHS_norm(n, 30, 0.05)
    C3_temp650 = LHS_norm(n, 30, 0.05)
    data = pd.DataFrame(zip(job, Fatigue_1, Fatigue_2, Fatigue_3, Fatigue_4,
                            Creep_fai, Creep_n1, Creep_wfcrit, Density,
                            Creep_temp360, Creep_temp480, Creep_temp500, Creep_temp550, Creep_temp650, Creep_temp800,
                            E_temp20, E_temp360, E_temp550, E_temp650,
                            C1_temp20, C1_temp360, C1_temp550, C1_temp650,
                            C2_temp20, C2_temp360, C2_temp550, C2_temp650,
                            C3_temp20, C3_temp360, C3_temp550, C3_temp650))
    data.to_csv('material_simple_data1.csv', index=False)

