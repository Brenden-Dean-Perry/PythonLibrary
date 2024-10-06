import pandas


class FileUtilities:

    @staticmethod
    def read_csv(file_path):
        df = pandas.read_csv(file_path)
        return df

    @staticmethod
    def read_text_file(file_path):
        with open(file_path, 'r') as file:
            data = file.read()
        return data

    @staticmethod
    def test2():
        return 0
