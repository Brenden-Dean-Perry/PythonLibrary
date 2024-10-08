from string import digits


class StringUtilties:

    @staticmethod
    def remove_all_numbers(string: str):
        remove_digits = str.maketrans('', '', digits)
        return string.translate(remove_digits)

    @staticmethod
    def remove_all_spaces(string: str):
        return string.replace(' ', '')

    @staticmethod
    def capitalize_each_word(string: str):
        return string.title()
