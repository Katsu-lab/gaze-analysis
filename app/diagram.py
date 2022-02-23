import configparser
import matplotlib.pyplot as plt
import matplotlib.animation as animation

import gaze

config = configparser.ConfigParser()
config.read('config.ini', encoding='utf-8')

csv = gaze.CsvSetting()

class Diagram():

    def __init__(self, user, span, mode):
        if user == 'b':
            self.user = 'BEREAVED FAMILY'
        elif user == 'n':
            self.user = 'NURSE'
        if span == 's':
            self.span = 'SHORT'
        elif span == 'l':
            self.span = 'LONG'
        if mode == 'l':
            self.mode = 'LINE'
        elif mode == 'p':
            self.mode = 'POINT'
        self.X_COORDINATE = 0
        self.Y_COORDINATE = 1
        self.ELAPSED_TIME = 2

    def display_scatter_diagram(self):
        gaze = csv.set_data(config.get(self.user, 'Gaze'))
        self.create_scatter_diagram(gaze[self.X_COORDINATE], gaze[self.Y_COORDINATE], gaze[self.ELAPSED_TIME])

    def display_scatter_diagrams(self):
        gaze1 = csv.set_data(config.get('BEREAVED FAMILY', 'Gaze'))
        gaze2 = csv.set_data(config.get('NURSE', 'Gaze'))
        self.create_scatter_diagrams(gaze1[self.X_COORDINATE], gaze1[self.Y_COORDINATE], gaze1[self.ELAPSED_TIME], gaze2[self.X_COORDINATE], gaze2[self.Y_COORDINATE], gaze2[self.ELAPSED_TIME])

    def create_scatter_diagram(self, x, y, t):
        figure = plt.figure()
        axes = figure.add_subplot(111)
        axes.patch.set_facecolor('#' + config.get('FIGURE', 'Background_color'))
        axes.set_xlim([0, config.getint('FIGURE', 'Pc_width')])
        axes.set_ylim([0, config.getint('FIGURE', 'Pc_height')])
        line, = axes.plot(x[0], y[0], c='red', marker='.')

        def update(list_index):
            # line, = axes.plot(x[0], y[0], c='red', marker='.')
            if self.mode == 'LINE':
                line.set_data(x[:list_index], y[:list_index])
            elif self.mode == 'POINT':
                line.set_data(x[list_index], y[list_index])

            time = str(round(t[list_index]))
            axes.set_title(config.get(self.user, 'Username') + config.get('FIGURE', 'Title') + '\nTime = ' + time + 'msec')

        ani = animation.FuncAnimation(figure, update, interval = 30)
        # ani.save('../../plot.gif', writer='ffmpeg', dpi=300)

        plt.show()

    def create_scatter_diagrams(self, x1, y1, t1, x2, y2, t2):
        figure = plt.figure()
        figure.subplots_adjust(hspace=0.7)

        axes1 = figure.add_subplot(config.getint('BEREAVED FAMILY', 'PlotNumber'))
        axes1.patch.set_facecolor('#' + config.get('FIGURE', 'Background_color'))
        axes1.set_xlim([0, config.getint('FIGURE', 'Pc_width')])
        axes1.set_ylim([0, config.getint('FIGURE', 'Pc_height')])
        line1, = axes1.plot(x1[0], y1[0], c='red', marker='.')

        def update1(i):
            line1.set_data(x1[:i], y1[:i])
            time1 = str(round(t1[i]))
            axes1.set_title(config.get('BEREAVED FAMILY', 'Username') + config.get('FIGURE', 'Title') + '\nTime = ' + time1 + 'msec')

        ani1 = animation.FuncAnimation(figure, update1, interval = 30)

        axes2 = figure.add_subplot(config.getint('NURSE', 'PlotNumber'))
        axes2.patch.set_facecolor('#' + config.get('FIGURE', 'Background_color'))
        axes2.set_xlim([0, config.getint('FIGURE', 'Pc_width')])
        axes2.set_ylim([0, config.getint('FIGURE', 'Pc_height')])
        line2, = axes2.plot(x2[0], y2[0], c='blue', marker='.')

        def update2(i):
            line2.set_data(x2[:i], y2[:i])
            time2 = str(round(t2[i]) - 858)
            axes2.set_title(config.get('NURSE', 'Username') + config.get('FIGURE', 'Title') + '\nTime = ' + time2 + 'msec')
        ani2 = animation.FuncAnimation(figure, update2, interval = 30)

        plt.show()