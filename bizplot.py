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


class Axis:
    def __init__(
            self,
            df,
            column,
            label,
            value_format,
            plot_type='line'
    ):

        self.data = df

        self.column = column if column else self.data.columns[0]
        if self.column not in self.data.columns:
            print(f"Column \'{self.column}\' not found in DataFrame. Available columns are:")
            for col in self.data.columns:
                print(f"  {col}")
            return None

        self.label = label

        self.value_format = value_format

        self.plot_type = plot_type.lower()
        if self.plot_type not in global_vars['plot_types']:
            print("Invalid plot_type. Valid options_are:")
            for plot_type in global_vars['plot_types']:
                print(f"  {plot_type}")
            return None


class Plot:
    def __init__(
            self,
            df,
            x,
            y,
            x_label=None,
            y_labels=None,
            plot_types=None,
            figsize=global_vars['figsize'],
            y_formats=None,
            x_format=None,
            title='Plot Title'
    ):

        self.data = df

        self.x = x

        self.y = [y] if isinstance(y, str) else y

        self.y_labels = y_labels if y_labels else self.y
        self.x_label = x_label if x_label else x
        self.title = title
        self.y_formats = y_formats
        self.x_format = x_format
        self.plot_types = plot_types if plot_types else ['line' for count in y]
        self.y_formats = y_formats if y_formats else ['default' for count in y]

        self.y_axes = []
        for i in range(0, len(self.y)):
            self.y_axes.append(Axis(
                df=self.data,
                column=self.y[i],
                label=self.y_labels[i],
                value_format=self.y_formats[i]
            ))

        plt.figure(figsize=figsize)
        self.pyplot_axes = [plt.subplot(111)]

        if len(self.y) > 1:
            self.pyplot_axes += [self.axes[0].twinx() for i in len(self.y_axes) - 1]

        for ax in self.pyplot_axes:
            hide_ax_spines(ax)
            ax.xaxis.set_tick_params(labelsize=global_vars['fontsize']['tick'])
            ax.yaxis.set_tick_params(labelsize=global_vars['fontsize']['tick'])

    def plot(self):

        for i in range(0, len(self.pyplot_axes)):
            if self.y_axes[i].plot_type == 'line':
                self.pyplot_axes[i].plot(
                    self.data.index,
                    self.data[self.y_axes[i].column],
                    color=global_vars['colours'][i]
                )
            elif self.y_axes[i].plot_type == 'bar':
                self.pyplot_axes[i].bar(
                    self.data.index,
                    self.data[self.y_axes[i].column],
                    color=global_vars['colours'][i]
                )
            else:
                pass

#         if self.y_labels:
#             for i in range(0, len(self.axes)):
#                 try:
#                     self.axes[i].set_ylabel(
#                         self.y_labels[i],
#                         fontsize=global_vars['fontsize']['axis'],
#                         fontname=global_vars['fontname']['axis']
#                     )
#                 except IndexError:
#                     print("Warning: Length of y_labels parameter does not match the DataFrame shape.")
#                     self.axes[i].set_ylabel(
#                         self.data.columns[i],
#                         fontsize=global_vars['fontsize']['axis'],
#                         fontname=global_vars['fontname']['axis']
#                     )
#         else:
#             for i in range(0, len(self.axes)):
#                 self.axes[i].set_ylabel(
#                     self.data.columns[i],
#                     fontsize=global_vars['fontsize']['axis'],
#                     fontname=global_vars['fontname']['axis']
#                 )

#         if self.x_label:
#             for i in range(0, len(self.axes)):
#                 try:
#                     self.axes[i].set_xlabel(
#                         self.x_label,
#                         fontsize=global_vars['fontsize']['axis'],
#                         fontname=global_vars['fontname']['axis']
#                     )
#                 except IndexError:
#                     print("Warning: Length of x_label parameter does not match the DataFrame shape.")
#                     self.axes[i].set_xlabel(
#                         self.data.index.name,
#                         fontsize=global_vars['fontsize']['axis'],
#                         fontname=global_vars['fontname']['axis']
#                     )
#         else:
#             for i in range(0, len(self.axes)):
#                 self.axes[i].set_xlabel(
#                     self.data.index.name,
#                     fontsize=global_vars['fontsize']['axis'],
#                     fontname=global_vars['fontname']['axis']
#                 )


#         if self.x_format:
#             try:
#                 self.axes[0].xaxis.set_major_locator(self.x_format[0])
#             except IndexError:
#                 print("Warning: no major locator in x_label parameter.")

#             try:
#                 self.axes[0].xaxis.set_minor_locator(self.x_format[1])
#             except IndexError:
#                 print("Warning: no minor locator in x_label parameter.")

#             try:
#                 self.axes[0].xaxis.set_major_formatter(self.x_format[2])
#             except IndexError:
#                 print("Warning: no major formatter in x_label parameter.")


#         if self.y_formats:
#             for i in range(0, len(self.y_formats)):
#                 try:
#                     self.axes[i].yaxis.set_major_formatter(self.y_formats[i])
#                 except TypeError:
#                     print("Warning: y_formats parameter is illogical.")
#                     pass
#         else:
#             pass


#         handles_labels = []
#         for ax in self.axes:
#             handles_labels.append(ax.get_legend_handles_labels())

#         h = handles_labels[0][0]
#         l = handles_labels[0][1]

#         if len(handles_labels) > 1:
#             for i in range(1, len(handles_labels)):
#                 h += handles_labels[i][0]
#                 l += handles_labels[i][1]

#         self.axes[0].legend(h, l, loc=2)
#         self.axes[0].set_title(
#             self.title,
#             fontsize=global_vars['fontsize']['title'],
#             fontname=global_vars['fontname']['title']
#         )