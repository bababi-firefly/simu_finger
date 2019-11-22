class vec:


    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __sig(self):
        print("aaaa")

    def __str__(self):
        return 'vec(%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        return vec(self.a + other.b, self.b + other.a)


a = vec(1, 10)
b = vec(2, 8)
c = a+b
print()
