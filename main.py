from menu import Dispaly, ChooseOption
from text_analysis import TextAnalyzer
from data_loader import DataLoader

PATH = 'data'

def start_book_browser():
    """The main method to start the book browser.
    """
    load_data = DataLoader(PATH)
    text = load_data.load_books()
    display_items = Dispaly(text)
    choose_options = ChooseOption()
    while True:
        sr_no_book_dict = display_items.display_books()
        choosen_books = choose_options.choose_book(sr_no_book_dict)
        serial_no_operation = display_items.display_analysis_options()
        analysis =choose_options.choose_analysis(serial_no_operation)

        # Checks if all the books are choosen and prepare the content accordingly.
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