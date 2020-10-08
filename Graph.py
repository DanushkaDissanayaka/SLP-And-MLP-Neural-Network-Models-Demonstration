import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import time

class Graph(object):
    def __init__(self):
        style.use('fivethirtyeight')
        self.xs = []
        self.ys = []
        self.fig = plt.figure()
        self.ax1 = self.fig.add_subplot(1,1,1)
    def animate(self, i):
        graph_data = open('data.txt','r').read()
        lines = graph_data.split('\n')
        self.xs = []
        self.ys = []
        for line in lines:
            if len(line) > 1:
                x, y = line.split(',')
                self.xs.append(float(x))
                self.ys.append(float(y))
        self.ax1.clear()
        self.ax1.plot(self.xs, self.ys)

    def show(self):
        ani = animation.FuncAnimation(self.fig, self.animate, interval=1000)
        plt.show()

    def populate(self, x:float, y:float):
        self.xs.append(x)
        self.ys.append(y)

if __name__ == "__main__":
    graph = Graph()
    graph.show()