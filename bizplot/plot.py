import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker

from bizplot.utility import global_vars, hide_ax_spines
from bizplot.axis import Axis


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
