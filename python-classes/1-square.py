class Square:
    def _init_(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def _str_(self):
        return f"{type(self)}\n{'Squaresize': {self._size}}"