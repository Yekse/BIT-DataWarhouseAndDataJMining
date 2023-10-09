import numpy as np
from MIC import CyrusMIC
import seaborn as sns
from scipy.stats import pearsonr
from scipy.stats import spearmanr
import matplotlib.pyplot as plt

x = np.arange(0, 1, 0.01)
noise = np.random.random(x.size) * 10

i = 0

x1 = np.arange(0, 1, 0.01)
x2 = np.arange(-1.3, 1.1, 0.0242)
noise2 = np.random.random(x2.size) * 10
x3 = np.arange(0, 10, 0.1)
noise3 = np.random.random(x3.size) * 10
x4 = np.arange(-0.5, 0.5, 0.01)
noise4 = np.random.random(x4.size) * 10

Linear_LowF = 0.2 * np.sin(4 * (2 * x1 - 1)) + 11 / 10 * (2 * x1 - 1)
Linear_MediumF = np.sin(10 * np.pi * x1) + x1
Linear_HighF = 0.1 * np.sin(10.6 * (2 * x1 - 1)) + 11 / 10 * (2 * x1 - 1)
Linear_HighF2 = 0.2 * np.sin(10.6 * (2 * x1 - 1)) + 11 / 10 * (2 * x1 - 1)
Cosine_LowF = np.cos(7 * np.pi * x1)
Cosine_HighF = np.cos(14 * np.pi * x1)
Cubic = 4 * x2 ** 3 + x2 ** 2 - 4 * x2
Cubic_Y = 41 * (4 * x2 ** 3 + x2 ** 2 - 4 * x2)
L_shaped = np.array([i / 99 if (i <= 99 / 100) else 99 * i - 98 for i in x1])
Exp2 = 2 ** x3
Exp10 = 10 ** x3
Line = x1
Parabola = 4 * (x4 ** 2)
ran = np.random.random(x1.size)
Sine_nF = np.sin(9 * np.pi * x1)
Sine_LowF = np.sin(8 * np.pi * x1)
Sine_HighF = np.sin(16 * np.pi * x1)
Sigmoid = np.array([0 if (i <= 0.49) else 1 if (i > 0.51) else 50 * (i - 0.5) + 0.5 for i in x1])
Cosine_VF = np.cos(5 * np.pi * x1 * (1 + x1))
Sine_VF = np.sin(6 * np.pi * x1 * (1 + x1))
Spike = np.array([20 * i if (i < 0.05) else (-i / 9 + 1 / 9) if i >= 0.01 else (-18 * i + 1.9) for i in x1])
Lopsided_L = np.array([200 * i if i < 0.005 else (-i / 99 + 1 / 99) if i >= 0.01 else (-198 * i + 1.98) for i in x1])

arr = np.zeros((6 , 3))

ran_mine = CyrusMIC()
Linear_MediumF_mine = CyrusMIC()
Cubic_mine = CyrusMIC()
Exp10_mine = CyrusMIC()
Sine_nF_mine = CyrusMIC()
Sine_VF_mine = CyrusMIC()

m1 = ran_mine.mic(x1, ran + noise * i)
m2 = Linear_MediumF_mine.mic(x1, Linear_MediumF + noise * i)
m3 = Cubic_mine.mic(x2, Cubic + noise2 * i)
m4 = Exp10_mine.mic(x3, Exp10 + noise3 * i)
m5 = Sine_nF_mine.mic(x1, Sine_nF + noise * i)
m6 = Sine_VF_mine.mic(x1, Sine_VF + noise * i)

s1 = spearmanr(x1, ran + noise * i).correlation
s2 = spearmanr(x1, Linear_MediumF + noise * i).correlation
s3 = spearmanr(x2, Cubic + noise2 * i).correlation
s4 = spearmanr(x3, Exp10 + noise3 * i).correlation
s5 = spearmanr(x1, Sine_nF + noise * i).correlation
s6 = spearmanr(x1, Sine_VF + noise * i).correlation

p1 = pearsonr(x1, ran + noise * i).statistic
p2 = pearsonr(x1, Linear_MediumF + noise * i).statistic
p3 = pearsonr(x2, Cubic + noise2 * i).statistic
p4 = pearsonr(x3, Exp10 + noise3 * i).statistic
p5 = pearsonr(x1, Sine_nF + noise * i).statistic
p6 = pearsonr(x1, Sine_VF + noise * i).statistic

print(type(m2))

arr[0][0] = m1
arr[0][1] = s1
arr[0][2] = p1

arr[1][0] = m2
arr[1][1] = s2
arr[1][2] = p2

arr[2][0] = m3
arr[2][1] = s3
arr[2][2] = p3

arr[3][0] = m4
arr[3][1] = s4
arr[3][2] = p4

arr[4][0] = m5
arr[4][1] = s5
arr[4][2] = p5

arr[5][0] = m6
arr[5][1] = s6
arr[5][2] = p6

fig = plt.figure()
sns_plot=sns.heatmap(arr, annot = True)
plt.show()