import math

class Vector:

    # Construct a new Vector object with numeric Cartesian coordinates
    # given in array a.
    def __init__(self, a):
        # Make a defensive copy to ensure immutability.
        self._coords = a[:] # Cartesian coordinates
        self._n = len(a)    # Dimension.

    # Return the ith Cartesian coordinate of self.
    def __getitem__(self, i):
        return self._coords[i]

    # Return the sum of self and Vector object other.
    def __add__(self, other):
        result = [0] * self._n
        for i in range(self._n):
            result[i] = self._coords[i] + other._coords[i]
        return Vector(result)

    # Return the difference of self and Vector object other.
    def __sub__(self, other):
        result = [0] * self._n
        for i in range(self._n):
            result[i] = self._coords[i] - other._coords[i]
        return Vector(result)

    # Return the product of self and numeric object alpha.
    def scale(self, alpha):
        result = [0] * self._n
        for i in range(self._n):
            result[i] = alpha * self._coords[i]
        return Vector(result)

    # Return the inner product of self and Vector object other.
    def dot(self, other):
        result = 0
        for i in range(self._n):
            result += self._coords[i] * other._coords[i]
        return result

    # Return the magnitude, that is, the Euclidean norm, of self.
    def __abs__(self):
        return math.sqrt(self.dot(self))

    # Return the unit vector of self.
    def direction(self):
        return self.scale(1.0 / abs(self))

    # Return a string representation of self.
    def __str__(self):
        return str(self._coords)

    # Return a string representation of self.
    def str(self):
        # strlist = ["{:.2e}".format(e) for e in self._coords]
        return '[{}]'.format(','.join(['{:.2e}'.format(e) for e in self._coords]))
        
    # Return the dimension of self.
    def __len__(self):
        return self._n
        
#-----------------------------------------------------------------------

# For testing.
# Create and use some Vector objects.

def main():

    xCoords = [1.0, 2.0, 3.0, 4.0]
    yCoords = [5.0, 2.0, 4.0, 1.0]

    x = Vector(xCoords)
    y = Vector(yCoords)

    print('x        = ' + str(x))
    print('y        = ' + str(y))
    print('x + y    = ' + str(x + y))
    print('10x      = ' + str(x.scale(10.0)))
    print('|x|      = ' + str(abs(x)))
    print('<x, y>   = ' + str(x.dot(y)))
    print('|x - y|  = ' + str(abs(x - y)))

if __name__ == '__main__':
    main()

#-----------------------------------------------------------------------

# python vector.py
# x        = [1.0, 2.0, 3.0, 4.0]
# y        = [5.0, 2.0, 4.0, 1.0]
# x + y    = [6.0, 4.0, 7.0, 5.0]
# 10x      = [10.0, 20.0, 30.0, 40.0]
# |x|      = 5.477225575051661
# <x, y>   = 25.0
# |x - y|  = 5.0990195135927845

