import configparser
import matplotlib.pyplot as plt
import matplotlib.animation as animation

config = configparser.ConfigParser()
config.read('config.ini', encoding='utf-8')

def scatter_diagram(x, y, t, user):
    figure = plt.figure()
    axes = figure.add_subplot(111)
    axes.patch.set_facecolor('#00FF00')
    plt.xlim([0, config.getint('PC', 'Width')])
    plt.ylim([0, config.getint('PC', 'Height')])

    def update(list_index):
        gaze_update_mode = [':list_index', 'list_index' ]
        gaze_plot_mode = ['short', 'long']
        if list_index != 0:
            pass
        line, = plt.plot(x[0], y[0], c='red', marker='.')
        line.set_data(x[list_index], y[list_index])
        time = str(round(t[list_index]))
        axes.set_title('Gaze on PC screen(From ' + config.get(user, 'Username') + ')\nTime = ' + time + 'msec')

    ani = animation.FuncAnimation(figure, update, interval = 30)
    # ani.save('../../plot.gif', writer='ffmpeg', dpi=300)

    plt.show()

def scatter_diagrams(x1, y1, t1, x2, y2, t2):
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
        time2 = str(round(t2[i]))
        axes2.set_title('Gaze on PC screen(' + config.get('NURSE', 'Username') + ')\nTime = ' + time2 + 'msec')
    ani2 = animation.FuncAnimation(figure, update2, interval = 30)

    plt.show()