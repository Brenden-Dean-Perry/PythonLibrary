import pandas as pd


class DataFrameUtilities:

    @staticmethod
    def dataframe_to_matrix(data_frame: pd.DataFrame):
        return data_frame.to_numpy()

    @staticmethod
    def json_to_dataframe(json):
        dataframe = pd.DataFrame.from_dict(json, orient='index')
        dataframe.reset_index(level=0, inplace=True)
        return dataframe

    @staticmethod
    def update_dataframe_field_names(dataframe: pd.DataFrame, original_field_names: [], new_field_names: []):
        i = 0
        while i < len(original_field_names):
            dataframe = dataframe.rename(columns={original_field_names[i]: new_field_names[i]})
            i = i + 1
        dataframe = dataframe[new_field_names]
        return dataframe

    @staticmethod
    def update_dataframe_datatypes(dataframe: pd.DataFrame):
        dataframe = dataframe.astype(float)
        dataframe.index = pd.to_datetime(dataframe.index)
        return dataframe
