import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker

years = mdates.YearLocator()  # every year
months = mdates.MonthLocator()  # every month
years_fmt = mdates.DateFormatter('%b-%y')
spend_fmt = mticker.StrMethodFormatter('${x:,g} K')

global_vars = {
    # tableau default colours
    'colours':
        [
            (r / 255., g / 255., b / 255.) for r, g, b in
            [(31, 119, 180), (174, 199, 232), (255, 127, 14), (255, 187, 120),
             (44, 160, 44), (152, 223, 138), (214, 39, 40), (255, 152, 150),
             (148, 103, 189), (197, 176, 213), (140, 86, 75), (196, 156, 148),
             (227, 119, 194), (247, 182, 210), (127, 127, 127), (199, 199, 199),
             (188, 189, 34), (219, 219, 141), (23, 190, 207), (158, 218, 229)]
        ],
    'figsize': (20, 10),
    'fontsize': {'title': 25, 'axis': 16, 'tick': 14},
    'fontname': {'title': 'Arial', 'axis': 'Arial', 'tick': 'Arial'},
    'plot_types': ['line', 'bar']
}


def hide_ax_spines(ax):
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)