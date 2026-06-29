class HashTable:
    def __init__(self):
        self.collection = {}
    def hash(self, string):
        ord_list = [ord(x) for x in string]
        return sum(ord_list)
    def add(self, key, value):
        hashed_key=self.hash(key)
        if hashed_key not in self.collection:
            self.collection[hashed_key] = {}
            self.collection[hashed_key][key] = value
        else:
            self.collection[hashed_key][key] = value
    def remove(self, key):
        hashed_key=self.hash(key)
        if hashed_key not in self.collection:
            return
        elif key not in self.collection[hashed_key]:
            return
        else:
            self.collection[hashed_key].pop(key)
    def lookup(self, key):
        hashed_key=self.hash(key)
        if hashed_key not in self.collection:
            return None
        elif key not in self.collection[hashed_key]:
            return None
        else:
            return self.collection[hashed_key][key]
