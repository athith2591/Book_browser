import re

class TextAnalyzer:
    """A class to analyze and to perform operations on the text.
    """

    def __init__(self, text):
        """The constructor that initializes the class

        Args:
            text (str): The text upon which different operations are performed
        """
        self.text = text

    def count_pattern(self):
        """A class method to count the patters.

        Args:
            pattern (str): The text pattern to be counted within the text

        Returns:
            int: The total count of occurances.
        """
        pattern = input('Please input the desired pattern to be counted: ')
        count = len(re.findall(pattern, self.text))
        print(f'The total instances of the pattern "{pattern}" is {count}')
        return count

    def count_spaces(self):
        """A class method to count the spaces.

        Returns:
            int: The total count of spaces within the text
        """
        count = len(re.findall(r'\s+', self.text))
        print(f'The total space count is : {count}')
        return count
    
    def count_words(self):
        """A class method to count the total words.

        Returns:
            int: The total count of words.
        """
        count = len(re.findall(r'\w+', self.text))
        print(f'he total word count is : {count}')
        return count

    def count_lines(self):
        """A class method to count the total lines.

        Returns:
            int: The total count of lines
        """
        count = len(self.text.splitlines())
        print(f'The total number of lines are {count}')
        return count