import pandas
import PyPDF2


class File:

    @staticmethod
    def get_csv_data(file_path):
        df = pandas.read_csv(file_path)
        return df

    @staticmethod
    def get_text_file_data(file_path):
        with open(file_path, 'r') as file:
            data = file.read()
        return data

    @staticmethod
    def get_pdf_data():
        reader = PyPDF2.PdfReader('example.pdf')
        pages = []

        for page in reader.pages:
            pages.append(page.extract_text())

        return pages

