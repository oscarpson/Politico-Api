office_list = []


class OfficeClass():
    def __init__(self, type, name):
        self.id = len(office_list) + 1
        self.type = type
        self.name = name
