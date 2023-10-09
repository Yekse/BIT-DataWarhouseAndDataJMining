import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from scipy.stats import spearmanr

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

while i <= 1:
    plt.scatter(i, spearmanr(x1, Linear_LowF + noise * i).correlation, c='blue', marker='D')

    plt.scatter(i, spearmanr(x1, Linear_MediumF + noise * i).correlation, c='purple', marker='x')

    plt.scatter(i, spearmanr(x1, Linear_HighF + noise * i).correlation, c='purple', marker='D')

    plt.scatter(i, spearmanr(x1, Linear_HighF2 + noise * i).correlation, c='green', marker='^')

    plt.scatter(i, spearmanr(x1, Cosine_LowF + noise * i).correlation, c='green',
                marker=matplotlib.markers.TICKDOWN)

    plt.scatter(i, spearmanr(x1, Cosine_HighF + noise * i).correlation, c='lightseagreen', marker='s')

    plt.scatter(i, spearmanr(x2, Cubic + noise2 * i).correlation, c='blue', marker='x')

    plt.scatter(i, spearmanr(x2, Cubic_Y + noise2 * i).correlation, c='red', marker='h')

    plt.scatter(i, spearmanr(x1, L_shaped + noise * i).correlation, c='green', marker='o')

    plt.scatter(i, spearmanr(x3, Exp2 + noise3 * i).correlation, c='purple', marker='+')

    plt.scatter(i, spearmanr(x3, Exp10 + noise3 * i).correlation, c='blue', marker=matplotlib.markers.TICKRIGHT)

    plt.scatter(i, spearmanr(x1, Line + noise * i).correlation, c='yellow', marker=matplotlib.markers.TICKDOWN)

    plt.scatter(i, spearmanr(x4, Parabola + noise4 * i).correlation, c='darkorange',
                marker=matplotlib.markers.TICKRIGHT)

    plt.scatter(i, spearmanr(x1, ran + noise * i).correlation, c='brown', marker='s')

    plt.scatter(i, spearmanr(x1, Sine_nF + noise * i).correlation, c='pink', marker='x')

    plt.scatter(i, spearmanr(x1, Sine_LowF + noise * i).correlation, c='blue', marker='h')

    plt.scatter(i, spearmanr(x1, Sine_HighF + noise * i).correlation, c='darkorange', marker='o')

    plt.scatter(i, spearmanr(x1, Sigmoid + noise * i).correlation, c='pink', marker='+')

    plt.scatter(i, spearmanr(x1, Cosine_VF + noise * i).correlation, c='darkorange',
                marker=matplotlib.markers.TICKRIGHT)

    plt.scatter(i, spearmanr(x1, Sine_VF + noise * i).correlation, c='purple', marker='D')

    plt.scatter(i, spearmanr(x1, Lopsided_L + noise * i).correlation, c='darkorange', marker='^')

    i += 0.01

plt.show()
