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

    def update(i):
        if i != 0:
            plt.plot(linewidth=None)

        line, = plt.plot(x[0], y[0], c='red', marker='.')
        line.set_data(x[:i], y[:i])
        time = str(round(t[i]))
        axes.set_title('Gaze on PC screen(From ' + config.get(user, 'Username') + ')\nTime = ' + time + 'msec')

    ani = animation.FuncAnimation(figure, update, interval = 30)
    # ani.save('../../plot.gif', writer='ffmpeg', dpi=300)

    plt.show()

def scatter_diagrams(x1, y1, x2, y2):
    figure = plt.figure()
    figure.subplots_adjust(hspace=0.5)

    axes1 = figure.add_subplot(config.getint('BEREAVED FAMILY', 'PlotNumber'))
    axes1.patch.set_facecolor('#00FF00')
    axes1.set_title('Gaze on PC screen(' + config.get('BEREAVED FAMILY', 'Username') + ')')
    plt.xlim([0, config.getint('PC', 'Width')])
    plt.ylim([0, config.getint('PC', 'Height')])
    def update1(i):
        line1, = axes1.plot(x1[0], y1[0], c='red', marker='.')
        line1.set_data(x1[:i], y1[:i])
    ani1 = animation.FuncAnimation(figure, update1, interval = 30)

    axes2 = figure.add_subplot(config.getint('NURSE', 'PlotNumber'))
    axes2.patch.set_facecolor('#00FF00')
    axes2.set_title('Gaze on PC screen(' + config.get('NURSE', 'Username') + ')')
    plt.xlim([0, config.getint('PC', 'Width')])
    plt.ylim([0, config.getint('PC', 'Height')])
    def update2(i):
        line2, = axes2.plot(x2[0], y2[0], c='blue', marker='.')
        line2.set_data(x2[:i], y2[:i])
    ani2 = animation.FuncAnimation(figure, update2, interval = 30)

    plt.show()