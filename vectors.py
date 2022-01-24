class VectorVariableSize:

    def __init__(self, *args):
        self.coords = list(args)

    def __add__(self, other):
        size = max(len(self.coords), len(other.coords)) - min(len(self.coords), len(other.coords))
        return VectorVariableSize(
            *[sum(x) for x in zip(*map(lambda x: x + [0] * size if len(x) < size else x, [self.coords, other.coords]))]
        )

    def __repr__(self):
        return "Vector [{0}]".format(','.join(map(str, self.coords)))


a = [1,2,3,5,6,7,8]
b = [2,3]
size = max(len(a), len(b)) - min(len(a), len(b))

print(*map(lambda x: x + [0] * size if len(x) < size else x, [a, b]))
print(*zip(*map(lambda x: x + [0] * size if len(x) < size else x, [a, b])))
print([sum(x) for x in zip(*map(lambda x: x + [0] * size if len(x) < size else x, [a, b]))])



class VectorSameSize:

    def __init__(self, *args):
        self.coords = list(args)

    def __add__(self, other):
        if len(other.coords) != len(self.coords):
            raise BaseException("Cannot add different sized vectors!")
        else:
            return VectorSameSize(*[self.coords[i] + other.coords[i] for i in range(len(self.coords))])

    def __repr__(self):
        return "Vector [{0}]".format(','.join(map(str, self.coords)))

""""
first = VectorSameSize(5, 7, 1)
second = VectorSameSize(5, 2)
third = VectorVariableSize(1, 2, 3, 43, 5)
fourth = VectorVariableSize(1, 2, 3, 4, 5, 6, 7, 8, 9)

try:
    res = first + second
    res2 = second + third
    print(res)
    print(res2)

except:
    pass

print([third.coords, fourth.coords])
res3 = fourth + third
print(res3)
"""