import numpy as np
import logging
import sys


class CyrusMIC(object):
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    screen_handler = logging.StreamHandler(sys.stdout)
    screen_handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(module)s.%(funcName)s:%(lineno)d - %(levelname)s - %(message)s')
    screen_handler.setFormatter(formatter)
    logger.addHandler(screen_handler)

    def __init__(self, x_num=[None, None], y_num=[None, None]):
        self.x_max_num = x_num[1]
        self.x_min_num = x_num[0]
        self.y_min_num = y_num[0]
        self.y_max_num = y_num[1]

        self.x = None
        self.y = None

    def cal_mut_info(self, p_matrix):
        """
        计算互信息值
        :param p_matrix: 变量X和Y的构成的概率矩阵
        :return: 互信息值
        """
        mut_info = 0
        p_matrix = np.array(p_matrix)
        for i in range(p_matrix.shape[0]):
            for j in range(p_matrix.shape[1]):
                if p_matrix[i, j] != 0:
                    mut_info += p_matrix[i, j] * np.log2(p_matrix[i, j] / (p_matrix[i, :].sum() * p_matrix[:, j].sum()))
        return mut_info / np.log2(min(p_matrix.shape[0], p_matrix.shape[1]))

    def divide_bin(self, x_num, y_num):
        """
        指定在两个变量方向上需划分的网格数，返回概率矩阵
        :param x_num:
        :param y_num:
        :return: p_matrix
        """
        p_matrix = np.zeros([x_num, y_num])
        x_bin = np.linspace(self.x.min(), self.x.max() + 1, x_num + 1)
        y_bin = np.linspace(self.y.min(), self.y.max() + 1, y_num + 1)
        for i in range(x_num):
            for j in range(y_num):
                p_matrix[i, j] = sum([1 if (
                        x_bin[i + 1] > self.x[value] >= x_bin[i] and y_bin[j + 1] > self.y[value] >= y_bin[j])
                                      else
                                      0 for value in range(self.x.shape[0])]) / self.x.shape[0]
        return p_matrix

    def mic(self, x, y):
        self.x = np.array(x).reshape((-1,))
        self.y = np.array(y).reshape((-1,))
        if not self.x_max_num:
            self.x_max_num = int(round(self.x.shape[0] ** 0.3, 0))
            self.y_max_num = self.x_max_num
            self.x_min_num = 2
            self.y_min_num = 2
        mics = []
        for i in range(self.x_min_num, self.x_max_num + 1):
            for j in range(self.y_min_num, self.x_max_num + 1):
                mics.append(self.cal_mut_info(self.divide_bin(i, j)))
        print("MIC {}".format(max(mics)))
        return max(mics)
