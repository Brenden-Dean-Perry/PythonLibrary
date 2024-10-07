from CustomObjects.Enums.TimeSeriesPurpose import TimeSeriesPurpose


class TimeSeries:
    _time_series_purpose = TimeSeriesPurpose.Unclassified
    _time_series_title = ''
    _data = {}

    def __init__(self, data: dict[float],  time_series_title: str, time_series_purpose=TimeSeriesPurpose.Unclassified):
        self._data = data
        self._time_series_title = time_series_title
        self._time_series_purpose = time_series_purpose

    def get_time_series_purpose(self) -> TimeSeriesPurpose:
        return self._time_series_purpose

    def get_time_series_title(self) -> str:
        return self._time_series_title

    def get_series_index(self):
        return self._data.keys()

    def get_series_values(self):
        return self._data.values()

