class Parser:

    def __init__(self, string_list):
        self.string_list = string_list

    def convert_to_int(self):
        for i in range(len(self.string_list)):
            self.string_list[i] = int(self.string_list[i])
        return self.string_list
