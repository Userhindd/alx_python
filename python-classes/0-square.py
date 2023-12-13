class Square:
    def _init_(self, size):
        self.__size = size

    def _str_(self):
        return f"{type(self)}\n{'Squaresize': {self._size}}"