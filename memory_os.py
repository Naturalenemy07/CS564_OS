# Constants
REGISTER_SIZE = 8
CACHE_SIZE = 1024
RAM_SIZE = 16384
STACK_SIZE = 1024

class Register:
    # Register memory
    def __init__(self, size = REGISTER_SIZE):
        self.reg_memory = [0] * size

    def read(self, reg_address):
        """Reads value at address and returns"""
        if 0 <= reg_address < len(self.reg_memory):
            return self.reg_memory[reg_address]
        else:
            print("Memory Error: Tried to access outside of register")

    def write(self, value, reg_address):
        """Writes a value at a designated position"""
        if 0 <= reg_address < len(self.reg_memory):
            self.reg_memory[reg_address] = value

class Cache:
    # Cache memory
    def __init__(self, size = CACHE_SIZE):
        self.cac_memory = [0] * size

    def read(self, cac_address):
        """Reads value at address and returns"""
        if 0 <= cac_address < len(self.cac_memory):
            return self.cac_memory[cac_address]
        else:
            print("Memory Error: Tried to read outside the cache")

    def write(self, value, cac_address):
        """Writes a value at a designated position"""
        if 0 <= cac_address < len(self.cac_memory):
            self.cac_memory[cac_address] = value
        else:
            print("Memory Error: tried to write outside of cache")

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
        if address >= self.stack_top_index: # Prevents memory access inside the designated stack
            print("Memory Error: Tried to write inside the stack")
        self.memory[address] = value
    
    def push(self, value):
        """Pushes value to top of stack"""
        if self.stack_pointer <= self.stack_top_index: # Prevents push access outside of designated stack
            print("Memory Error: Push tried to access outside of the stack")
        else:
            self.memory[self.stack_pointer] = value
            self.stack_pointer -= 1

    def pop(self):
        """Pops value off top of stack"""
        if self.stack_pointer <= self.stack_top_index: # Prevents pop access outside of designated stack
            print("Memory Error: Pop tried to access outside of the stack")
        else:
            self.stack_pointer += 1
            temp_value = self.memory[self.stack_pointer]
            self.memory[self.stack_pointer] = 0
            return temp_value
