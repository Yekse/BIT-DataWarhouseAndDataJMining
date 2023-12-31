import matplotlib.pyplot as plt
import random
import numpy as np
from numpy import exp

MAX = 100000


def nearestNeighbor(index):
    dd = MAX
    neighbor = -1
    for i in range(length):
        if dist[index, i] < dd and rho[index] < rho[i]:
            dd = dist[index, i]
            neighbor = i
    if result[neighbor] == -1:
        result[neighbor] = nearestNeighbor(neighbor)
    return result[neighbor]


# Read data


fileName = input("Enter the file's name: ")
location = []
label = []
for line in open(fileName, "r"):
    items = line.strip("\n").split(",")
    label.append(int(items.pop()))
    tmp = []
    for item in items:
        tmp.append(float(item))
    location.append(tmp)
location = np.array(location)
label = np.array(label)
length = len(location)

# Calculate distance
dist = np.zeros((length, length))
ll = []
begin = 0
while begin < length - 1:
    end = begin + 1
    while end < length:
        dd = np.linalg.norm(location[begin] - location[end])
        dist[begin][end] = dd
        dist[end][begin] = dd
        ll.append(dd)
        end = end + 1
    begin = begin + 1
ll = np.array(ll)
# Algorithm
# percent = float(raw_input("Enter the average percentage of neighbours: "))
percent = 2.0
position = int(len(ll) * percent / 100)
sortedll = np.sort(ll)
dc = sortedll[position]  # threshold value

# Find the local density of points

rho = np.zeros((length, 1))
begin = 0
while begin < length - 1:
    end = begin + 1
    while end < length:
        rho[begin] = rho[begin] + exp(-(dist[begin][end] / dc) ** 2)
        rho[end] = rho[end] + exp(-(dist[begin][end] / dc) ** 2)
        # if dist[begin][end] < dc:
        #    rho[begin] = rho[begin] + 1
        #    rho[end] = rho[end] + 1
        end = end + 1
    begin = begin + 1

# Find the minimum distance from a point whose
# local density is greater than that of a point

delta = np.ones((length, 1)) * MAX
maxDensity = np.max(rho)
begin = 0
while begin < length:
    if rho[begin] < maxDensity:
        end = 0
        while end < length:
            if rho[end] > rho[begin] and dist[begin][end] < delta[begin]:
                delta[begin] = dist[begin][end]
            end = end + 1
    else:
        delta[begin] = 0.0
        end = 0
        while end < length:
            if dist[begin][end] > delta[begin]:
                delta[begin] = dist[begin][end]
            end = end + 1
    begin = begin + 1

rate1 = 0.5
# Aggregation Spiral 0.6
# Jain Flame 0.8
# Compound 0.5

thRho = rate1 * (np.max(rho) - np.min(rho)) + np.min(rho)

rate2 = 0.08
# Aggregation Spiral 0.2
# Jain Flame 0.2
# Compound 0.08

thDel = rate2 * (np.max(delta) - np.min(delta)) + np.min(delta)

# determining the initial cluster centers
result = np.ones(length, dtype=np.int) * (-1)
center = 0
# items = range(length)
# random.shuffle(items)
for i in range(length):  # items:
    if rho[i] > thRho and delta[i] > thDel:
        result[i] = center
        center = center + 1
# 赋予每个点聚类类标
for i in range(length):
    dist[i][i] = MAX

for i in range(length):
    if result[i] == -1:
        result[i] = nearestNeighbor(i)
    else:
        continue

plt.plot(rho, delta, '.')
plt.xlabel('rho'), plt.ylabel('delta')
plt.show()

R = list(range(256))
random.shuffle(R)
R = np.array(R) / 255.0
G = list(range(256))
random.shuffle(G)
G = np.array(G) / 255.0
B = list(range(256))
random.shuffle(B)
B = np.array(B) / 255.0
colors = []
for i in range(256):
    colors.append((R[i], G[i], B[i]))

plt.figure()
for i in range(length):
    index = result[i]
    plt.plot(location[i][0], location[i][1], color=colors[index], marker='.')
plt.xlabel('x'), plt.ylabel('y')
plt.show()


