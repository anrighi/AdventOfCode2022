class FileReader:

    def __init__(self, file_path):
        self.file_path = file_path
        self.file = open(file_path, "r")

    def read_file(self, optional_divider=None):
        if optional_divider is not None:
            return self.file.read().split(optional_divider)
        else:
            return self.file.read().split()
