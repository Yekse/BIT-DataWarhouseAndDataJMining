import numpy as np
from minepy import MINE
import matplotlib.pyplot as plt
from MIC import CyrusMIC


def get_mic(x, y):
    mine = CyrusMIC()
    return mine.mic(x,y)


def plot_G(x, y):
    fig = plt.figure(figsize=(20, 5))
    mic_list = []
    for i in range(10):
        n = y + np.random.uniform(-i * 0.05, 0.05 * i, 10000)
        mic = get_mic(x, n)
        mic_list.append(mic)
        if i == 1:
            plt.subplot(1, 4, 1)
            plt.scatter(x, n)
        if i == 3:
            plt.subplot(1, 4, 2)
            plt.scatter(x, n)
        if i == 5:
            plt.subplot(1, 4, 3)
            plt.scatter(x, n)
        if i == 7:
            plt.subplot(1, 4, 4)
            plt.scatter(x, n)
    plt.show()


def figure_G(type):
    half_x = np.linspace(0, 1, 5000)
    x = np.concatenate((half_x, half_x))
    if type == 1:
        pass
    if type == 'line and parabola':
        y = np.concatenate((half_x, -np.power(half_x, 2)))
        plot_G(x, y)
    if type == 'X':
        y = np.concatenate((half_x, 1 - half_x))
        plot_G(x, y)
    if type == 'ellipse':
        theta = np.arange(0, 2 * np.pi, np.pi / 2500)
        x = 2 * np.cos(theta)
        y = 1 * np.sin(theta)
        fig = plt.figure(figsize=(40, 5))
        for i in range(20):
            n = y + np.random.uniform(-i * 0.02, 0.02 * i, 5000)
            mic = get_mic(x, n)
            if i == 0:
                plt.subplot(1, 4, 1)
                plt.scatter(x, n)
            if i == 1:
                plt.subplot(1, 4, 2)
                plt.scatter(x, n)
            if i == 8:
                plt.subplot(1, 4, 3)
                plt.scatter(x, n)
            if i == 18:
                plt.subplot(1, 4, 4)
                plt.scatter(x, n)
        plt.show()
    if type == 'sin':
        half_x = np.linspace(0, 1, 5000)
        x = np.concatenate((half_x, half_x))
        y = np.concatenate((np.sin(5 * np.pi * half_x), np.sin(2 * np.pi * half_x)))
        fig = plt.figure(figsize=(20, 5))
        for i in range(20):
            n = y + np.random.uniform(-i * 0.02, 0.02 * i, 10000)
            mic = get_mic(x, n)
            if i == 0:
                plt.subplot(1, 4, 1)
                plt.scatter(x, n)
            if i == 1:
                plt.subplot(1, 4, 2)
                plt.scatter(x, n)
            if i == 9:
                plt.subplot(1, 4, 3)
                plt.scatter(x, n)
            if i == 17:
                plt.subplot(1, 4, 4)
                plt.scatter(x, n)
        plt.show()
    if type == 'Non-coexistence':
        x1 = np.linspace(0, 0.1, 4500)
        x2 = np.linspace(0.1, 1, 4500)
        x3 = np.linspace(0, 1, 1000)
        x = np.concatenate((x1, x2, x3))
        y1 = np.random.uniform(0, 1, 4500)
        y2 = np.random.uniform(0, 0.1, 4500)
        y3 = np.random.uniform(0, 1, 1000)
        y = np.concatenate((y1, y2, y3))
        # figsize(a,b) a为宽 b为高
        fig = plt.figure(figsize=(20, 5))
        # plt.scatter(x,y)
        # plt.show()
        mic_list = []
        for i in range(20):
            m = x + np.random.uniform(-i * 0.03, 0.03 * i, 10000)
            n = y + np.random.uniform(-i * 0.01, 0.01 * i, 10000)
            if i == 0:
                plt.subplot(1, 4, 1)
                plt.scatter(m, n)
            if i == 1:
                plt.subplot(1, 4, 2)
                plt.scatter(m, n)
            if i == 9:
                plt.subplot(1, 4, 3)
                plt.scatter(m, n)
            if i == 17:
                plt.subplot(1, 4, 4)
                plt.scatter(m, n)
        plt.show()


if __name__ == '__main__':
    figure_G('line and parabola')

# if __name__ == '__main__':
#     figure_G('X')
#
# if __name__ == '__main__':
#     figure_G('ellipse')
#
# if __name__ == '__main__':
#     figure_G('sin')
#
# if __name__ == '__main__':
#     figure_G('Non-coexistence')

