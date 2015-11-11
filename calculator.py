import math
class Calculator:
    def __init__(self):
        self.base_numeral_system = 10

    def add(self, x, y):
         return x + y       

    def subtract(self, x, y):
      return x - y

   

    def multiply(self, x, y):
        return x * y

     

    def divide(self, x, y):
        return x / y

      

    def evaluate(self, expression):
         def __init__(self, left, op, right):
        self.__left = left
        self.__op = op
        self.__right = right

    def Evaluate(self, dictionary):
        # NEW code
        if self.__op == '=':
            assert isinstance(self.__left, Variable), 'Must Assign to Variable'
            name = self.__left._Variable__name
            value = self.__right.Evaluate(dictionary)
            dictionary[name] = value
            return value
        # END code
        x = self.__left.Evaluate(dictionary)
        y = self.__right.Evaluate(dictionary)
        if self.__op == '+':
            return x + y
        if self.__op == '-':
            return x - y
        if self.__op == '*':
            return x * y
        if self.__op == '/':
            return x / y

        