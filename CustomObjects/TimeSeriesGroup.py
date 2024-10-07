from CustomObjects.TimeSeries import TimeSeries


class TimeSeriesGroup:
    _data = []

    def __int__(self):
        pass

    def add_series(self, series: TimeSeries):
        self._data.append(series)

    def remove_series_by_name(self, time_series_name: str):
        self._data = [x for x in self._data if x.get_time_series_name() != time_series_name]

    def get_all_series(self):
        return self._data
