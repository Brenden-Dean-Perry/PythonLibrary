import matplotlib.pyplot as plt
import numpy as np


class Charting:

    @staticmethod
    def scatter_plot(x: [], y: [], x_label='x-axis', y_label='y-axis', title='', show_plot=True):
        x_data = np.array(x)
        y_data = np.array(y)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(title)
        plt.scatter(x, y)

        if show_plot == True:
            plt.show()

        return plt

    @staticmethod
    def line_chart(x: [], y: [], x_label='x-axis', y_label='y-axis', title='', show_plot=True):
        plt.plot(x, y)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(title)

        if show_plot == True:
            plt.show()

        return plt

    @staticmethod
    def bar_chart(categories: [], values: [], x_label='x-axis', y_label='y-axis', title='', show_plot=True,
                  horizontal=False):

        if horizontal == False:
            plt.bar(categories, values)
        else:
            plt.barh(categories, values)

        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(title)

        if show_plot == True:
            plt.show()

        return plt

    @staticmethod
    def donut_chart(categories: [], values: [], title='', show_plot=True, radius=0.7, donut_width=0.4):
        fig, ax = plt.subplots()
        ax.pie(values, labels=categories, wedgeprops=dict(width=donut_width))
        my_circle = plt.Circle((0, 0), radius, color='white')
        p = plt.gcf()
        p.gca().add_artist(my_circle)
        plt.title(title)

        if show_plot == True:
            plt.show()

        return plt

    @staticmethod
    def pie_chart(categories: [], values: [], title='',show_plot=True):
        plt.pie(values, labels=categories)
        plt.title(title)

        if show_plot == True:
            plt.show()

        return plt

    @staticmethod
    def histogram(values: [], x_label='x-axis', y_label='y-axis', title='', show_plot=True, density=False, bins=30):
        plt.hist(values, density=density, bins=bins)  # density=False would make counts
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)

        if show_plot == True:
            plt.show()

        return plt

    @staticmethod
    def optimal_bin_width_freedman_diaconis_method(data: []):
        quartile_25, quartile_75 = np.percentile(data, [25, 75])
        inter_quartile_range = quartile_75 - quartile_25
        bin_width = 2 * inter_quartile_range * len(data) ** (-1/3)
        optimal_bin_count = round((data.max() - data.min()) / bin_width)
        return optimal_bin_count



