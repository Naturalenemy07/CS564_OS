class Register:
    # Register memory
    def __init__(self, size = 8):
        self.memory = [0] * size

class Cache:
    # Cache memory
    def __init__(self, size = 1024):
        self.memory = [0] * size

class Main:
    # RAM
    def __init__(self, size = 1048576):
        self.memory = [0] * size

def load_mem():
    pass

def search_mem():
    pass

def defragment_mem():
    pass
