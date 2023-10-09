from MIC import CyrusMIC
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

x = np.arange(0, 1, 0.01)
noise = np.random.random(x.size)

i = 0

x1 = np.arange(0, 1, 0.01)
x2 = np.arange(-1.3, 1.1, 0.0242)
noise2 = np.random.random(x2.size)
x3 = np.arange(0, 10, 0.1)
noise3 = np.random.random(x3.size)
x4 = np.arange(-0.5, 0.5, 0.01)
noise4 = np.random.random(x4.size)

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

Linear_LowF_mine = CyrusMIC()
Linear_MediumF_mine = CyrusMIC()
Linear_HighF_mine = CyrusMIC()
Linear_HighF2_mine = CyrusMIC()
Cosine_LowF_mine = CyrusMIC()
Cosine_HighF_mine = CyrusMIC()
Cubic_mine = CyrusMIC()
Cubic_Y_mine = CyrusMIC()
L_shaped_mine = CyrusMIC()
Exp2_mine = CyrusMIC()
Exp10_mine = CyrusMIC()
Line_mine = CyrusMIC()
Parabola_mine = CyrusMIC()
ran_mine = CyrusMIC()
Sine_nF_mine = CyrusMIC()
Sine_LowF_mine = CyrusMIC()
Sine_HighF_mine = CyrusMIC()
Sigmoid_mine = CyrusMIC()
Cosine_VF_mine = CyrusMIC()
Sine_VF_mine = CyrusMIC()
Spike_mine = CyrusMIC()
Lopsided_L_mine = CyrusMIC()

while i <= 10:

    plt.scatter(i, Linear_LowF_mine.mic(x1, Linear_LowF + noise * i), c='blue', marker='D')
    plt.scatter(i, Linear_MediumF_mine.mic(x1, Linear_MediumF + noise * i), c='purple', marker='x')
    plt.scatter(i, Linear_HighF_mine.mic(x1, Linear_HighF + noise * i), c='purple', marker='D')
    plt.scatter(i, Linear_HighF2_mine.mic(x1, Linear_HighF2 + noise * i), c='green', marker='^')
    plt.scatter(i, Cosine_LowF_mine.mic(x1, Cosine_LowF + noise * i), c='green', marker=matplotlib.markers.TICKDOWN)
    plt.scatter(i, Cosine_HighF_mine.mic(x1, Cosine_HighF + noise * i), c='lightseagreen', marker='s')
    plt.scatter(i, Cubic_mine.mic(x2, Cubic + noise2 * i), c='blue', marker='x')
    plt.scatter(i, Cubic_Y_mine.mic(x2, Cubic_Y + noise2 * i), c='red', marker='h')
    plt.scatter(i, L_shaped_mine.mic(x1, L_shaped + noise * i), c='green', marker='o')
    plt.scatter(i, Exp2_mine.mic(x3, Exp2 + noise3 * i), c='purple', marker='+')
    plt.scatter(i, Exp10_mine.mic(x3, Exp10 + noise3 * i), c='blue', marker=matplotlib.markers.TICKRIGHT)
    plt.scatter(i, Line_mine.mic(x1, Line + noise * i), c='yellow', marker=matplotlib.markers.TICKDOWN)
    plt.scatter(i, Parabola_mine.mic(x4, Parabola + noise4 * i), c='darkorange', marker=matplotlib.markers.TICKRIGHT)
    plt.scatter(i, ran_mine.mic(x1, ran + noise * i), c='brown', marker='s')
    plt.scatter(i, Sine_nF_mine.mic(x1, Sine_nF + noise * i), c='pink', marker='x')
    plt.scatter(i, Sine_LowF_mine.mic(x1, Sine_LowF + noise * i), c='blue', marker='h')
    plt.scatter(i, Sine_HighF_mine.mic(x1, Sine_HighF + noise * i), c='darkorange', marker='o')
    plt.scatter(i, Sigmoid_mine.mic(x1, Sigmoid + noise * i), c='pink', marker='+')
    plt.scatter(i, Cosine_VF_mine.mic(x1, Cosine_VF + noise * i), c='darkorange', marker=matplotlib.markers.TICKRIGHT)
    plt.scatter(i, Sine_VF_mine.mic(x1, Sine_VF + noise * i), c='purple', marker='D')
    plt.scatter(i, Lopsided_L_mine.mic(x1, Lopsided_L + noise*i), c='darkorange', marker='^')
    i += 0.1

plt.show()
