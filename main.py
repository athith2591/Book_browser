import os
from book_browser import StartBookBrowsing

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(BASE_DIR, 'data')

if __name__ =="__main__":
    start_browsing = StartBookBrowsing(PATH)
    start_browsing.start()