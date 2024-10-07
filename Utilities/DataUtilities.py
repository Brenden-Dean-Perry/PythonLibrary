import pandas as pd


class DataUtilities:

    @staticmethod
    def dataframe_to_matrix(data_frame: pd.DataFrame):
        return data_frame.to_numpy()

    @staticmethod
    def json_to_dataframe(json):
        # converting json dataset from dictionary to dataframe
        train = pd.DataFrame.from_dict(json, orient='index')
        train.reset_index(level=0, inplace=True)
        return train
