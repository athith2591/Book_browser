import os

# def read_and_create_title_text_dict(folder_path):
#     """To load and extract the info from the text file.

#     Args:
#         folder_path (str): The path of the folder Books.

#     Returns:
#         dict: Returns a dictionary with title as the key and the text content as the pair.
#     """
#     result = {}

#     for filename in os.listdir(folder_path):
#         if filename.endswith(".txt"):
#             file_path = os.path.join(folder_path, filename)

#             with open(file_path, "r", encoding="utf-8") as f:
#                 content = f.read()

#             title, content = find_title_in_text(content)

#         # If file name isnt found
#             if not title:
#                 title = filename
#             result[title] = content

#     return result

# def find_title_in_text(content):
#     """To find the title in the text

#     Args:
#         content (str): The text content of the book

#     Returns:
#         str: Return the title along with the content.
#     """
#     title = None
#     for line in content.splitlines():
#         if line.strip().startswith("Title:"):
#             title = line.split("Title:")[1].strip()
#             break
#     return title, content

# if __name__ == "__main__":
#     print(len(read_and_create_title_text_dict('books')))

class DataLoader:
    """A class to load the data
    """

    def __init__(self, folder_path):
        """Initializing constructor

        Args:
            folder_path (str): Path of the file containing the data
        """
        self.path = folder_path

    def load_books(self):
        """Class method that loads the data and returns a dict with title as key and content as pair.

        Returns:
            dict: A dict with title as key and content as pair.
        """
        result = dict()
        for filename in os.listdir(self.path):
            if filename.endswith(".txt"):
                file_path = os.path.join(self.path, filename)

                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
            result[filename] = content
        
        return result 
        
if __name__ == "__main__":
    load_data = DataLoader('data')
    data = load_data.load_books()
    print(data.keys())