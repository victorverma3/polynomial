class X:
    def __init__(self):
        pass

    def __repr__(self):
        return "X"

    def evaluate(self, x_value):
        return x_value


class Int:
    def __init__(self, i):
        self.i = i

    def __repr__(self):
        return str(self.i)

    def evaluate(self, x_value):
        return self.i


class Add:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return repr(self.p1) + " + " + repr(self.p2)

    def evaluate(self, x_value):
        return self.p1.evaluate(x_value) + self.p2.evaluate(x_value)


class Sub:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return repr(self.p1) + " - " + repr(self.p2)

    def evaluate(self, x_value):
        return self.p1.evaluate(x_value) - self.p2.evaluate(x_value)


class Mul:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        if isinstance(self.p1, (Add, Sub)):
            if isinstance(self.p2, (Add, Sub)):
                return "( " + repr(self.p1) + " ) * ( " + repr(self.p2) + " )"
            return "( " + repr(self.p1) + " ) * " + repr(self.p2)
        if isinstance(self.p2, (Add, Sub)):
            return repr(self.p1) + " * ( " + repr(self.p2) + " )"
        return "( " + repr(self.p1) + " * " + repr(self.p2) + " )"

    def evaluate(self, x_value):
        return self.p1.evaluate(x_value) * self.p2.evaluate(x_value)


class Div:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        if isinstance(self.p1, (Add, Sub)):
            if isinstance(self.p2, (Add, Sub)):
                return "( " + repr(self.p1) + " ) / ( " + repr(self.p2) + " )"
            return "( " + repr(self.p1) + " ) / " + repr(self.p2)
        if isinstance(self.p2, (Add, Sub)):
            return repr(self.p1) + " / ( " + repr(self.p2) + " )"
        return "( " + repr(self.p1) + " / " + repr(self.p2) + " )"

    def evaluate(self, x_value):
        denominator = self.p2.evaluate(x_value)
        if denominator == 0:
            raise ValueError("division by 0")
        return self.p1.evaluate(x_value) / denominator


poly = Add(Add(Int(4), Int(3)), Add(X(), Mul(Int(1), Add(Mul(X(), X()), Int(1)))))
print(poly)
print(poly.evaluate(3))

poly = Add(Add(Mul(Int(2), X()), Sub(Int(8), X())), Div(Int(4), Int(2)))
print(poly)
print(poly.evaluate(3))
