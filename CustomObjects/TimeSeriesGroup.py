from CustomObjects.TimeSeries import TimeSeries


class TimeSeriesGroup:
    _data = []
    _x_axis_label = ''
    _y_axis_label = ''

    def __init__(self, x_axis_label='Date', y_axis_label='Price'):
        self._x_axis_label = x_axis_label
        self._y_axis_label = y_axis_label

    def add_series(self, series: TimeSeries):
        self._data.append(series)

    def remove_series_by_name(self, time_series_name: str):
        self._data = [x for x in self._data if x.get_time_series_name() != time_series_name]

    def get_all_series(self) -> [TimeSeries]:
        return self._data

    def get_x_axis_label(self) -> str:
        return self._x_axis_label

    def get_y_axis_label(self) -> str:
        return self._y_axis_label
