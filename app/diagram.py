import configparser
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.animation as animation

import gaze_csv_setting
from orality_calculation import return_gaze_object, return_facial_expression, return_paralanguage
from tools import print_result_to_csv

config = configparser.ConfigParser()
config.read('../config.ini', encoding='utf-8')
csv = gaze_csv_setting.CsvSetting()

class Diagram():

    def __init__(self, user, span, mode, graph):
        if user == 'b':
            self.user = 'BEREAVED FAMILY'
        elif user == 'n':
            self.user = 'NURSE'
        elif user == 'a':
            self.user = 'ALL'
        if span == 's':
            self.span = 'SHORT'
        elif span == 'l':
            self.span = 'LONG'
        if mode == 'l':
            self.mode = 'LINE'
        elif mode == 'p':
            self.mode = 'POINT'
        if graph == 's':
            self.graph = 'SEPARATE'
        elif graph == 'o':
            self.graph = 'OVERLAP'
        self.X_COORDINATE = 0
        self.Y_COORDINATE = 1
        self.ELAPSED_TIME = 2

    def set_csv_data(self, user):
        return csv.set_data(config.get(user, 'Gaze'))

    def display_scatter_diagram(self):
        gaze = self.set_csv_data(self.user)
        self.create_scatter_diagram(gaze[self.X_COORDINATE], gaze[self.Y_COORDINATE], gaze[self.ELAPSED_TIME])

    def display_scatter_diagrams(self):
        gaze1 = self.set_csv_data('BEREAVED FAMILY')
        gaze2 = self.set_csv_data('NURSE')
        if self.graph == 'SEPARATE':
            self.create_scatter_diagrams(gaze1[self.X_COORDINATE], gaze1[self.Y_COORDINATE], gaze1[self.ELAPSED_TIME], gaze2[self.X_COORDINATE], gaze2[self.Y_COORDINATE], gaze2[self.ELAPSED_TIME])
        elif self.graph == 'OVERLAP':
            self.create_scatter_diagrams_together(gaze1[self.X_COORDINATE], gaze1[self.Y_COORDINATE], gaze1[self.ELAPSED_TIME], gaze2[self.X_COORDINATE], gaze2[self.Y_COORDINATE])

    def set_diagram_design(self, axes):
        axes.patch.set_facecolor('#' + config.get('FIGURE', 'Background_color'))
        axes.set_xlim([0, config.getint('FIGURE', 'Pc_width')])
        axes.set_ylim([0, config.getint('FIGURE', 'Pc_height')])

    def create_scatter_diagram(self, x, y, t):
        figure = plt.figure(config.get(self.user, 'Username') + config.get('FIGURE', 'Title'), figsize=(11.4, 6.3))
        axes = figure.add_subplot(111)
        self.set_diagram_design(axes)

        if self.span == 'SHORT':
            line1, = axes.plot(x[0], y[0], c=config.get(self.user, 'Plot_color'), marker='.')

        def update(list_index):
            if self.span == 'LONG':
                line2, = axes.plot(x[0], y[0], c=config.get(self.user, 'Plot_color'), marker='.')
            if self.mode == 'LINE':
                line2.set_data(x[:list_index], y[:list_index])
            if self.span == 'SHORT' and self.mode == 'POINT':
                line1.set_data(x[list_index], y[list_index])
            elif self.span == 'LONG' and self.mode == 'POINT':
                line2.set_data(x[list_index], y[list_index])

            time = str(round(t[list_index]))
            gaze = return_gaze_object.calculate_bereavement_coordinate_information(x[list_index], y[list_index],1)
            face = return_facial_expression.example()
            voice = return_paralanguage.example()
            print_result_to_csv.output_data(time, gaze, face, voice)

            variable = '\nTime: ' + time + 'msec' + '\nGaze: ' + gaze + '\nFacial Impression: ' + face + '\nParalanguage: ' + voice
            axes.set_title(variable, loc='left', size=10, weight=10)

        ani = animation.FuncAnimation(figure, update, interval = 10)
        plt.show()

    def create_scatter_diagrams(self, x1, y1, t1, x2, y2, t2):
        figure = plt.figure(figsize=(11.4, 6.3))
        figure.subplots_adjust(hspace=0.7)

        axes1 = figure.add_subplot(config.getint('BEREAVED FAMILY', 'Plot_number'))
        self.set_diagram_design(axes1)
        line1, = axes1.plot(x1[0], y1[0], c=config.get('BEREAVED FAMILY', 'Plot_color'), marker='.')

        def update1(i):
            # line1, = axes1.plot(x1[0], y1[0], c='red', marker='.')
            line1.set_data(x1[i], y1[i])
            time1 = str(round(t1[i]))
            axes1.set_title(config.get('BEREAVED FAMILY', 'Username') + config.get('FIGURE', 'Title') + '\nTime = ' + time1 + 'msec')

        ani1 = animation.FuncAnimation(figure, update1, interval = 30)

        axes2 = figure.add_subplot(config.getint('NURSE', 'Plot_number'))
        self.set_diagram_design(axes2)
        line2, = axes2.plot(x2[0], y2[0], c=config.get('NURSE', 'Plot_color'), marker='.')

        def update2(i):
            # line2, = axes2.plot(x2[0], y2[0], c='blue', marker='.')
            line2.set_data(x2[i], y2[i])
            time2 = str(round(t2[i]) - 858) # This is time difference
            axes2.set_title(config.get('NURSE', 'Username') + config.get('FIGURE', 'Title') + '\nTime = ' + time2 + 'msec')
        ani2 = animation.FuncAnimation(figure, update2, interval = 30)

        plt.show()

    def create_scatter_diagrams_together(self, x1, y1, t1, x2, y2):
        figure = plt.figure(figsize=(11.4, 6.3))
        axes = figure.add_subplot(111)
        self.set_diagram_design(axes)
        # line1, = axes.plot(x1[0], y1[0], c=config.get('BEREAVED FAMILY', 'Plot_color'), marker='.', label='BEREAVED FAMILY')
        # line2, = axes.plot(x2[0], y2[0], c=config.get('NURSE', 'Plot_color'), marker='.', label='NURSE')
        axes.legend(loc='lower right')

        def update1(list_index):
            line1, = axes.plot(x1[0], y1[0], c='red', marker='.', label='BEREAVED FAMILY')
            line1.set_data(x1[:list_index], y1[:list_index])
            time = str(round(t1[list_index]))
            axes.set_title('All participant\'s gaze information at the time of online Bereavement Care' + '\nTime = ' + time + 'msec')

        def update2(list_index):
            line2, = axes.plot(x2[0], y2[0], c='blue', marker='.', label='NURSE')
            line2.set_data(x2[:list_index], y2[:list_index])

        ani1 = animation.FuncAnimation(figure, update1, interval = 30)
        ani2 = animation.FuncAnimation(figure, update2, interval = 30)
        plt.grid()
        plt.show()