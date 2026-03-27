import os

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
            filename = filename.replace('.txt', '')
            result[filename] = content
        
        return result 
        
# if __name__ == "__main__":
#     load_data = DataLoader('data')
#     data = load_data.load_books()
#     print(data.keys())