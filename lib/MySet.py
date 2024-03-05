class MySet:

    def __init__(self, enumerable = []):
        self.dictionary = {}
        for value in enumerable:
            self.dictionary[value] = True

    def has(self, value):
        return value in self.dictionary
    
    def add(self, value):
        self.dictionary[value] = True
    
    def delete(self, value):
        self.dictionary.pop(value, None)
        return self
    def size(self):
        return len(self.dictionary)
    
    def clear(self):
        self.dictionary = {}

    def __str__(self):
        return f"MySet: {self.dictionary.keys()}"