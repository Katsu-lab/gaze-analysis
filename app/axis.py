import configparser
import matplotlib.pyplot as plt
import matplotlib.animation as animation

config = configparser.ConfigParser()
config.read('../config.ini', encoding='utf-8')

def plot(figure, user, x, y):
    axes = figure.add_subplot(config.getint(user, 'Plot_number'))
    axes.patch.set_facecolor('#00FF00')
    axes.set_title('Gaze on PC screen(' + config.get(user, 'Username') + ')')
    plt.xlim([0, config.getint('FIGURE', 'Pc_width')])
    plt.ylim([0, config.getint('FIGURE', 'Pc_Height')])

    def plot_update(i):
        line, = axes.plot(x[0], y[0], c='red', marker='.')
        line.set_data(x[:i], y[:i])
    ani = animation.FuncAnimation(figure, plot_update, interval = 30)