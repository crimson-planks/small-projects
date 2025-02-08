import numpy as np
import collections.abc
class MathObject():
    def __str__(self):
        return self.__repr__()
    def __mul__(self, other):
        return Multiplication([self,other])
    def differentiate(self, respect):
        raise NotImplementedError
class Constant(MathObject):
    value: float
    def __init__(self, value):
        self.value = float(value)
    def __repr__(self):
        return f"Constant[{self.value}]"
    def differentiate(self, respect):
        return Constant(0)
class Variable(MathObject):
    symbol: str
    def __init__(self, symbol):
        self.symbol = symbol
    def __repr__(self):
        return f"Variable[{self.symbol}]"
    def differentiate(self, respect):
        if self.symbol == respect.symbol:
            return Constant(1)
        return Constant(0)
class Addition(MathObject):
    operands: list
    def __init__(self, operands):
        self.operands = operands
    def __repr__(self):
        return f"Addition{self.operands}"
    def differentiate(self, respect):
        return Addition([operand.differentiate(respect) for operand in self.operands])
class Multiplication(MathObject):
    operands: list
    def __init__(self, operands):
        self.operands = operands
    def __repr__(self):
        return f"Multiplication{self.operands}"
    def differentiate(self, respect):
        product = []
        for i in self.operands:
            product.append([operand.differentiate(respect) if i==j else operand for j,operand in enumerate(self.operands)])
        return Addition(product)
class Exponentiation(MathObject):
    base: MathObject
    power: MathObject
    def __init__(self, base, power):
        self.base = base
        self.power = power
    def __repr__(self):
        return f"Exponentiation[{self.base},{self.power}]"
    def differentiate(self, respect):
        return super().differentiate(respect)
print((Constant(2)*Variable('x')).differentiate(Variable('x')))