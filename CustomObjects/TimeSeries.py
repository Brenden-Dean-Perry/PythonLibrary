from CustomObjects.Enums.TimeSeriesPurpose import TimeSeriesPurpose


class TimeSeries:
    _time_series_purpose = TimeSeriesPurpose.Unclassified
    _time_series_title = ''
    _x_axis_label = ''
    _y_axis_label = ''
    _data = {}

    def __init__(self, data: dict,  time_series_title: str, x_axis_label='Date', y_axis_label='Price', time_series_purpose=TimeSeriesPurpose.Unclassified):
        self._data = data
        self._time_series_title = time_series_title
        self._x_axis_label = x_axis_label
        self._y_axis_label = y_axis_label
        self._time_series_purpose = time_series_purpose

    def get_time_series_purpose(self) -> TimeSeriesPurpose:
        return self._time_series_purpose

    def get_time_series_title(self) -> str:
        return self._time_series_title

    def get_series_index(self):
        return self._data.keys()

    def get_series_values(self):
        return self._data.values()

    def get_x_axis_label(self):
        return self._x_axis_label

    def get_x_axis_label(self):
        return self._y_axis_label
