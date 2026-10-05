import re


class NotStringError(TypeError):
    pass


class Palindrome(str):
    """
    Class to process potential palindrome strings.
    """

    def __init__(self, string: str):
        if not isinstance(string, str):
            raise NotStringError("You must initialise with a string.")
        self.__text = string

    def is_palindrome(self) -> bool:
        self.__clean_palindrome()
        return self.__text == self.__text[::-1]

    def __clean_palindrome(self) -> None:
        self.__text = re.sub("[^a-z]", "", self.__text, flags=re.I).lower()
