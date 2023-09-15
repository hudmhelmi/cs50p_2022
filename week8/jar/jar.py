class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if n > 0 and (n + self.size) <= self.capacity:
            self.size += n
        else:
            raise ValueError("Please enter a valid number of cookies.")

    def withdraw(self, n):
        if n <= self.size:
            self.size -= n
        else:
            raise ValueError("Please enter a valid number of cookies.")

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        try:
            capacity = int(capacity)
        except ValueError:
            print("Please enter a valid number of cookies.")
        else:
            if capacity < 0:
                raise ValueError("Please enter a valid number of cookies.")
            self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        try:
            size = int(size)
        except ValueError:
            print("Please enter a valid number of cookies.")
        else:
            if size < 0:
                raise ValueError("Please enter a valid number of cookies.")
            self._size = size
