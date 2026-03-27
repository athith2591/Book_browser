
class Dispaly:
    """A class that has methods to display books and analysis options
    """

    def __init__(self, books: dict):
        """Intializing method

        Args:
            books (dict): The dict that contains book titles and thier contents.
        """
        self.books = books
        self.__list_of_operations = ['count_pattern', 'count_spaces', 'count_words', 'count_lines' ]

    def display_books(self):
        """Method that displays the books and assigns serial numbers to each books
           to facililate thier choosing.

        Returns:
            dict: Dictionary containing the serial number and book titles.
            Eg: {'1': 'Harry Potter', "2":...}
        """
        serial_no_book_dict = {}

        titles = list(self.books.keys())
        max_len = max(len(title) for title in titles)
        width = max(max_len, len('Book Title'))

        print(f"\n+----+-{'-' * width}-+") # Adjusts the width based on the max title length
        print(f"| No | {'Book Title'.ljust(width)} |")
        print(f"+----+-{'-' * width}-+")

        for serial_no, title in enumerate(titles, start=1):
            print(f"| {serial_no:<2} | {title.ljust(width)} |") # Padding the spaces to give box a uniform look.
            serial_no_book_dict[str(serial_no)] = title

        print(f"+----+-{'-' * width}-+")
        return serial_no_book_dict
    
    def display_analysis_options(self):
        """Displays the available analysis options

        Returns:
            dict: Dictionary containing the serial number and analysis operations.
            Eg: {"1":"count_pattern",....}
        """
        serial_no_operation ={}

        max_len = max(len(operation) for operation in self.__list_of_operations )
        width = max(max_len, len('Operations'))

        print(f"\n+----+-{'-' * width}-+")
        print(f"| No | {'Operations'.ljust(width)} |")
        print(f"+----+-{'-' * width}-+")

        for serial_no , operation in enumerate(self.__list_of_operations, start=1):
            print(f"| {serial_no:<2} | {operation.ljust(width)} |")
            serial_no_operation[str(serial_no)] = operation

        print(f"+----+-{'-' * width}-+")
        return serial_no_operation


class ChooseOption:

    def choose_book(self, serial_no_book_dict):
        """A method that takes the user input, validates its correctfullness and returns it.

        Args:
            serial_no_book_dict (dict): A dict containing the serial number and book title as key pair values.

        Returns:
            str/List: Returns the title of the book if a single book is choosen or returns a list of books.
        """
        number_of_books = len(serial_no_book_dict)
        while True: 
            user_choice = input("Please give your choice of book based on the corresponding serial number or give 0 for all books: ")
            try: 
                int(user_choice)
            except ValueError:
                print("Not a valid number")
                continue
            if int(user_choice) > number_of_books:
                print('Invalid input, the entered serial number is not associated to any book')
                continue
            else:
                if int(user_choice) != 0:
                    print("Your choosen book is :", serial_no_book_dict[user_choice])
                    return serial_no_book_dict[user_choice]
                else:
                    print("You chose all books")
                    return list(serial_no_book_dict.values())


    def choose_analysis(self, serial_no_operation):
        """Method that interacts with the user to receive the innput and return the value

        Args:
            serial_no_operation (dict): The dict containing sr.no and operation key pair values

        Returns:
            str: Returns the operation choosen.
        """
        number_of_operations = len(serial_no_operation)
        while True: 
            user_choice = input("Please give your choice of the operation: ")
            try: 
                int(user_choice)
            except ValueError:
                print("Not a valid number")
                continue
            if int(user_choice) > number_of_operations or int(user_choice) == 0 :
                print('Invalid input, the entered serial number is not associated with any operation')
                continue
            else:
                print("You chose the operation: ", serial_no_operation[user_choice])
                return serial_no_operation[user_choice]
