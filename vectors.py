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

# test