import numpy as np
import matplotlib.pyplot as plt

def sigmoid(inputs):
    """
    Calculate the sigmoid for the give inputs (array)
    :param inputs:
    :return:
    """
    sigmoid_scores = [1 / float(1 + np.exp(- x)) for x in inputs]
    return sigmoid_scores

def line_graph(x, y, x_title, y_title):
    """
    Draw line graph with x and y values
    :param x:
    :param y:
    :param x_title:
    :param y_title:
    :return:
    """
    plt.plot(x, y)
    plt.xlabel(x_title)
    plt.ylabel(y_title)
    plt.show()


sigmoid_inputs = [2, 3, 5, 6]
print("Sigmoid Function Output :: {}".format(sigmoid(sigmoid_inputs)))
graph_x = range(0, 21)
graph_y = sigmoid(graph_x)
print("Graph X readings: {}".format(graph_x))
print("Graph Y readings: {}".format(graph_y))
line_graph(graph_x, graph_y, "Inputs", "Sigmoid Scores")