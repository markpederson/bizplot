from utility import global_vars


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