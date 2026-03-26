from data_loader import read_and_create_title_text_dict
import pandas as pd

# def show_books(books:dict):
#     """A method that displays a list of books available to be choosen along with a serial number.

#     Args:
#         books (dict): A dictionary with book_title as key and it's content as pair.

#     Returns:
#         Dict: A dictionary with the serial number as key and title as pair
#     """
#     serial_no_book_dict ={}
#     list_of_books = books.keys()
#     for serial_no , title in enumerate(list_of_books, start=1):
#         print(serial_no, ": ", title )
#         serial_no_book_dict[str(serial_no)] = title
#     return serial_no_book_dict

# def choose_book(serial_no_book_dict):
#     """A method that takes the user input, validates its correctfullness and returns it.

#     Args:
#         serial_no_book_dict (dict): A dict containing the serial number and book title as key pair values.

#     Returns:
#         str/List: Returns the title of the book if a single book is choosen or returns a list of books.
#     """
#     number_of_books = len(serial_no_book_dict)
#     while True: 
#         user_choice = input("Please give your choice of book based on the corresponding serial number or give 0 for all books: ")
#         try: 
#             int(user_choice)
#         except ValueError:
#             print("Not a valid number")
#             continue
#         if int(user_choice) > number_of_books:
#             print('Invalid input, the entered serial number is not associated to any book')
#             continue
#         else:
#             if int(user_choice) != 0:
#                 print("Your choosen book is :", serial_no_book_dict[user_choice])
#                 return serial_no_book_dict[user_choice]
#             else:
#                 print("You chose all books")
#                 return list(serial_no_book_dict.values())


# def display_analysis_options():
#     """_summary_

#     Returns:
#         _type_: _description_
#     """
#     serial_no_operation ={}
#     list_of_operations = ['count_pattern', 'count_spaces', 'count_words', 'count_lines' ]
#     for serial_no , operation in enumerate(list_of_operations, start=1):
#         print(serial_no, ": ", operation )
#         serial_no_operation[str(serial_no)] = operation
#     return serial_no_operation

# def choose_analysis(serial_no_operation):
#     number_of_operations = len(serial_no_operation)
#     while True: 
#         user_choice = input("Please give your choice of the operation: ")
#         try: 
#             int(user_choice)
#         except ValueError:
#             print("Not a valid number")
#             continue
#         if int(user_choice) > number_of_operations or int(user_choice) == 0 :
#             print('Invalid input, the entered serial number is not associated with any operation')
#             continue
#         else:
#             print("You chose the operation: ", serial_no_operation[user_choice])
#             return serial_no_operation[user_choice]

# if __name__ =="__main__":
#     books = read_and_create_title_text_dict('books')
#     sr_no_book_dict = show_books(books)
#     choose_book(sr_no_book_dict)
#     serial_no_operation =display_analysis_options()
#     choose_analysis(serial_no_operation)


class Dispaly:

    def __init__(self, books: dict):
        self.books = books
        self.__list_of_operations = ['count_pattern', 'count_spaces', 'count_words', 'count_lines' ]

    def display_books(self):
        serial_no_book_dict = {}

        titles = list(self.books.keys())
        max_len = max(len(title) for title in titles)
        width = max(max_len, len('Book Title'))

        print(f"\n+----+-{'-' * width}-+")
        print(f"| No | {'Book Title'.ljust(width)} |")
        print(f"+----+-{'-' * width}-+")

        for serial_no, title in enumerate(titles, start=1):
            print(f"| {serial_no:<2} | {title.ljust(width)} |")
            serial_no_book_dict[str(serial_no)] = title

        print(f"+----+-{'-' * width}-+")
        return serial_no_book_dict
    
    def display_analysis_options(self):
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

    def __init__(self):
        pass

    def choose_book(serial_no_book_dict):
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


    def choose_analysis(serial_no_operation):
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
