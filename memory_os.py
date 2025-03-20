# Constants
REGISTER_SIZE = 8
CACHE_SIZE = 1024
RAM_SIZE = 1048576
STACK_SIZE = 1024

class Register:
    # Register memory
    def __init__(self, size = REGISTER_SIZE):
        self.memory = [0] * size

    def read(self, address):
        """Reads value at address and returns"""
        return self.memory[address]

    def write(self, value, address):
        """Writes a value at a designated position"""
        self.memory[address] = value

class Cache:
    # Cache memory
    def __init__(self, size = CACHE_SIZE):
        self.memory = [0] * size

    def read(self, address):
        """Reads value at address and returns"""
        return self.memory[address]

    def write(self, value, address):
        """Writes a value at a designated position"""
        self.memory[address] = value

class Main:
    # RAM
    def __init__(self, size = RAM_SIZE, stack_size = STACK_SIZE):
        self.memory = [0] * size
        self.stack_pointer = size - 1
        self.stack_top_index = size - stack_size - 1

    def read(self, address):
        """Reads value at address and returns"""
        return self.memory[address]

    def write(self, value, address):
        """Writes a value at a designated position"""
        self.memory[address] = value
    
    def push(self, value):
        """Pushes value to top of stack"""
        if self.stack_pointer <= self.stack_top_index:
            print("Memory Error: Push tried to access outside of the stack")
        else:
            self.memory[self.stack_pointer] = value
            self.stack_pointer -= 1

    def pop(self):
        """Pops value off top of stack"""
        self.stack_pointer += 1
        temp_value = self.memory[self.stack_pointer]
        self.memory[self.stack_pointer] = 0
        return temp_value
