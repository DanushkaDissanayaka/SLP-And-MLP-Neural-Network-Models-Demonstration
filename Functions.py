import math

class Sigmoid(object):
    def get_value(self, x):
        x *= -1
        value = (1/(1+math.exp(x)))
        if value > 0.8:
            return 1.0
        elif value < 0.2:
            return 0.0
        return value

    def get_first_derivative_value(self,x):
        value = self.get_value(x)
        return value * (1-value)

class Relu(object):

    def get_value(self, x):
        if x > 0:
            return x
        return 0
    def get_first_derivative_value(self,x):
        if x > 0:
            return 1
        return 0

if __name__ == "__main__":
    sigmoid = Sigmoid()
    value = sigmoid.get_value(1.0)

    print(value)
