# from menu import show_books, choose_book, choose_analysis,display_analysis_options,choose_analysis
# from text_analysis import count_pattern, count_spaces, count_lines, count_words
# from data_loader import read_and_create_title_text_dict

from menu import Dispaly, ChooseOption
from text_analysis import TextAnalyzer
from data_loader import DataLoader

# def start_book_browser():
#     text = read_and_create_title_text_dict('books')
#     while True:
#         sr_no_book_dict = show_books(text)
#         books =choose_book(sr_no_book_dict)
#         serial_no_operation =display_analysis_options()
#         analysis =choose_analysis(serial_no_operation)

#         if isinstance(books, list):
#             temp_var = ''
#             for book in books:
#                 temp_var += text[book]
#             content = temp_var
#         else:
#             content = text[books]

#         if analysis == 'count_pattern':
#             count_pattern(content)
#         elif analysis == 'count_spaces':
#             count_spaces(content)
#         elif analysis == 'count_words':
#             count_words(content)
#         else:
#             count_lines(content)
        
#         while True:
#             futher_operation = input('Do you want to have perform another operation on another book of your choice Y/N:\n')
#             if futher_operation.lower() != 'y' and futher_operation.lower() != 'n':
#                 print('Please enter Y or N')
#                 continue
#             break

#         if futher_operation.lower() == 'y':
#             continue
#         else:
#             break

PATH = 'data'

def start_book_browser():
    load_data = DataLoader(PATH)
    text = load_data.load_books()
    display_items = Dispaly(text)
    choose_options = ChooseOption()
    while True:
        sr_no_book_dict = display_items.display_books()
        choosen_books = choose_options.choose_book(sr_no_book_dict)
        serial_no_operation = display_items.display_analysis_options()
        analysis =choose_options.choose_analysis(serial_no_operation)

        if isinstance(choosen_books, list):
            temp_var = ''
            for book in choosen_books:
                temp_var += text[book]
            content = temp_var
        else:
            content = text[choosen_books]

        text_analysis = TextAnalyzer(content)
        if analysis == 'count_pattern':
            text_analysis.count_pattern()
        elif analysis == 'count_spaces':
            text_analysis.count_spaces()
        elif analysis == 'count_words':
            text_analysis.count_words()
        else:
            text_analysis.count_lines()
        
        while True:
            futher_operation = input('Do you want to have perform another operation on another book of your choice Y/N:\n')
            if futher_operation.lower() != 'y' and futher_operation.lower() != 'n':
                print('Please enter Y or N')
                continue
            break

        if futher_operation.lower() == 'y':
            continue
        else:
            break


if __name__ == "__main__":
    start_book_browser()