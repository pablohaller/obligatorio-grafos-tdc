class Graph():
    def __init__(self, name, path):
        self.name = name
        self.path = path

    def __str__(self):
        return f"Name: {self.name} | Path: {str(self.path)}\n"

