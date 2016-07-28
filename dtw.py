#!/usr/bin/env python
# encoding: utf-8

import numpy as np
import editdistance


def levenshtein(x, y):

    return editdistance.eval(x, y)


def euclidean(x, y):

    return (x - y)**2


def path_cost(x, y, accumulated_cost, distances):

    path = [[len(x) - 1, len(y) - 1]]

    cost = 0
    i = len(y) - 1
    j = len(x) - 1

    while i>0 and j>0:
        if i==0:
            j = j - 1
        elif j==0:
            i = i - 1
        else:
            if accumulated_cost[i-1, j] == min(accumulated_cost[i-1, j-1], accumulated_cost[i-1, j], accumulated_cost[i, j-1]):
                i = i - 1
            elif accumulated_cost[i, j-1] == min(accumulated_cost[i-1, j-1], accumulated_cost[i-1, j], accumulated_cost[i, j-1]):
                j = j - 1
            else:
                i = i - 1
                j = j - 1
        path.append([j, i])
    path.append([0,0])

    for [y, x] in path:
        cost = cost + distances[x, y]

    return path, cost


def dtw(x, y, f=euclidean):

    distances = np.zeros((len(y), len(x)))

    for i in range(len(y)):
        for j in range(len(x)):
            distances[i,j] = f(x[j], y[i])

    accumulated_cost = np.zeros((len(y), len(x)))

    accumulated_cost[0,0] = distances[0,0]

    for i in range(1, len(y)):
        for j in range(1, len(x)):
            accumulated_cost[i, j] = min(accumulated_cost[i-1, j-1], accumulated_cost[i-1, j], accumulated_cost[i, j-1]) + distances[i, j]

    path, cost = path_cost(x, y, accumulated_cost, distances)

    path_x = [point[0] for point in path]
    path_y = [point[1] for point in path]

    return path, cost


if __name__ == '__main__':

    x = np.array([1, 1, 2, 3, 2, 0])
    y = np.array([0, 1, 1, 2, 3, 2, 1])

    path, cost=dtw(x, y, euclidean)

    print path
    print cost

    x = 'fsffvfdsbbdfvvdavavavavavava'
    y = 'fvdaabavvvvvadvdvavavadfsfsdafvvav'

    path, cost=dtw(x, y, levenshtein)

    print path
    print cost
