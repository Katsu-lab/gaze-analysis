import configparser
import matplotlib.pyplot as plt
import matplotlib.animation as animation

import gaze

config = configparser.ConfigParser()
config.read('config.ini', encoding='utf-8')

csv = gaze.CsvSetting()

class Diagram():

    def __init__(self, user, span, mode):
        self.user = user
        self.span = span
        self.mode = mode
        self.X_COORDINATE = 0
        self.Y_COORDINATE = 1
        self.ELAPSED_TIME = 2

    def display_scatter_diagram(self, user):
        if user == 'b':
            user = 'BEREAVED FAMILY'
        elif user == 'n':
            user = 'NURSE'

        gaze = csv.set_data(config.get(user, 'Gaze'))
        self.create_scatter_diagram(gaze[self.X_COORDINATE], gaze[self.Y_COORDINATE], gaze[self.ELAPSED_TIME], user)

    def display_scatter_diagrams(self):
        gaze1 = csv.set_data(config.get('BEREAVED FAMILY', 'Gaze'))
        gaze2 = csv.set_data(config.get('NURSE', 'Gaze'))
        self.create_scatter_diagrams(gaze1[X_COORDINATE], gaze1[Y_COORDINATE], gaze1[ELAPSED_TIME], gaze2[X_COORDINATE], gaze2[Y_COORDINATE], gaze2[ELAPSED_TIME])

    def create_scatter_diagram(self, x, y, t, user):
        figure = plt.figure()
        axes = figure.add_subplot(111)
        axes.patch.set_facecolor('#00FF00')
        plt.xlim([0, config.getint('PC', 'Width')])
        plt.ylim([0, config.getint('PC', 'Height')])

        def update(list_index):
            # gaze_update_mode = [':list_index', 'list_index' ]
            # gaze_plot_mode = ['short', 'long']
            if list_index != 0:
                pass

            mode = 'p'
            line, = plt.plot(x[0], y[0], c='red', marker='.')
            if mode == 'l':
                line.set_data(x[:list_index], y[:list_index])
            elif mode == 'p':
                line.set_data(x[list_index], y[list_index])

            time = str(round(t[list_index]))
            axes.set_title('Gaze on PC screen(From ' + config.get(user, 'Username') + ')\nTime = ' + time + 'msec')

        ani = animation.FuncAnimation(figure, update, interval = 30)
        # ani.save('../../plot.gif', writer='ffmpeg', dpi=300)

        plt.show()

    def create_scatter_diagrams(self, x1, y1, t1, x2, y2, t2):
        figure = plt.figure()
        figure.subplots_adjust(hspace=0.7)

        axes1 = figure.add_subplot(config.getint('BEREAVED FAMILY', 'PlotNumber'))
        axes1.patch.set_facecolor('#00FF00')
        plt.xlim([0, config.getint('PC', 'Width')])
        plt.ylim([0, config.getint('PC', 'Height')])
        def update1(i):
            line1, = axes1.plot(x1[0], y1[0], c='red', marker='.')
            line1.set_data(x1[:i], y1[:i])
            time1 = str(round(t1[i]))
            axes1.set_title('Gaze on PC screen(' + config.get('BEREAVED FAMILY', 'Username') + ')\nTime = ' + time1 + 'msec')

        ani1 = animation.FuncAnimation(figure, update1, interval = 30)

        axes2 = figure.add_subplot(config.getint('NURSE', 'PlotNumber'))
        axes2.patch.set_facecolor('#00FF00')
        plt.xlim([0, config.getint('PC', 'Width')])
        plt.ylim([0, config.getint('PC', 'Height')])
        def update2(i):
            line2, = axes2.plot(x2[0], y2[0], c='blue', marker='.')
            line2.set_data(x2[:i], y2[:i])
            time2 = str(round(t2[i]) - 858)
            axes2.set_title('Gaze on PC screen(' + config.get('NURSE', 'Username') + ')\nTime = ' + time2 + 'msec')
        ani2 = animation.FuncAnimation(figure, update2, interval = 30)

        plt.show()