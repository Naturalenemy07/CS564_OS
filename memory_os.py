class Register:
    # Register memory
    def __init__(self, size = 8):
        self.memory = [0] * size

    def read(self, address):
        """Reads value at address and returns"""
        return self.memory[address]

    def write(self, value, address):
        """Writes a value at a designated position"""
        self.memory[address] = value

class Cache:
    # Cache memory
    def __init__(self, size = 1024):
        self.memory = [0] * size

    def read(self, address):
        """Reads value at address and returns"""
        return self.memory[address]

    def write():
        pass

class Main:
    # RAM
    def __init__(self, size = 1048576):
        self.memory = [0] * size

    def read(self, address):
        """Reads value at address and returns"""
        return self.memory[address]

    def write():
        pass

    def defragment_mem():
        pass

r1 = Register()
r1.write(10,0)
r1.write(20,4)
for i in range(8):
    print(r1.read(i))
