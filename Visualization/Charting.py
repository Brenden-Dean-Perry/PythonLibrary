import matplotlib.pyplot as plt
import numpy as np


class Charting:

    @staticmethod
    def scatter_plot(x: [], y: []):
        x_data = np.array(x)
        y_data = np.array(y)
        plt.scatter(x, y)
        return plt
