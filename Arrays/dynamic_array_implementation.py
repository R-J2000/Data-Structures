# DYNAMIC ARRAY IMPLEMENTATION (for reference)

class DynamicArray:
    def __init__(self):
        self.size = 0               # Current number of elements in the array
        self.capacity = 1           # Initial capacity of the array
        self.array = self._create_array(self.capacity)   # Internal array to store the elements
    
    def __len__(self):
        return self.size            # Return the current number of elements in the array
    
    def __getitem__(self, index):
        if not 0 <= index < self.size:
            raise IndexError('Index out of range!')
        return self.array[index]    # Retrieve the element at the specified index
    
    def append(self, element):
        if self.size == self.capacity:
            self._resize(2 * self.capacity)   # Double the capacity if array is full
        self.array[self.size] = element      # Add the new element to the end
        self.size += 1                       # Increment the size of the array
    
    def _resize(self, new_capacity):
        new_array = self._create_array(new_capacity)    # Create a new array with the new capacity
        for i in range(self.size):
            new_array[i] = self.array[i]                # Copy elements from the old array to the new array
        self.array = new_array                          # Update the array reference
        self.capacity = new_capacity                    # Update the capacity
    
    def _create_array(self, capacity):
        return [None] * capacity    # Create an array with the specified capacity
