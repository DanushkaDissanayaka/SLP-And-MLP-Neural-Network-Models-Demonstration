import Functions
import numpy as np

class Neuron():
    def __init__(self,activation,weight:list, lr:float):
        self._weight = weight
        self._lr = lr
        self._lat_output = 0.0
        self._last_sum = 0.0
        if(activation == 'relu'):
            self._activation_function = Functions.Relu()
        elif activation == 'sigmoid':
            self._activation_function = Functions.Sigmoid()

    def sigma (self, i:list) -> float:
        i.append(1)
        if len(self._weight) != len(i):
            raise 'Input vector and weight vector not equal'

        value = 0
        """ 
            Initialize empty value to hold 
            summention of weight and the
            input value
        """
        for v in range(len(self._weight)):
            value += i[v] * self._weight[v]

        return value

    def output(self, i:list) -> float:
        value = self.sigma(i)
        self._lat_output = self._activation_function.get_value(value)
        return self._lat_output

    def error(self, real_value) -> float:
        return real_value - self._lat_output

    def out_error(self, real_value) -> float:
        return (self._activation_function.get_first_derivative_value() 
        * (real_value - self._lat_output))

    def update_weight(self, error: float, i:list) -> bool:
        i.append(1)
        if len(self._weight) != len(i):
            raise 'Input vector and weight vector not equal'

        for v in range(len(self._weight)):

            self._weight[v] += self._lr * i[v] * error

        return True





if __name__ == "__main__":
    neuron = Neuron(activation = 'sigmoid', weight=np.array([0.4,1.4,-2.4]), lr = 0.01)
    data =[
        [[0,0],0],
        [[0,1],0],
        [[1,0],0],
        [[1,1],1]
    ]

    for i in range(10000):
        print ('Epoc' , i)
        error = 0
        for e in data:
            value = neuron.output(e[0][:])
            error += neuron.error(e[1])

        error /= len(data)
        neuron.update_weight(error, e[0][:])
        print(error)
        print(neuron._weight)
        """
            Do the prediction end of each epoc and if prediction close to the
            real value terminate traning
        """
        v1 = neuron.output([1,1])
        v2 = neuron.output([0,1])
        error = ((abs(1-v1) + abs(0-v2))/2)
        print ('Test Error = ',error)

        if error < 0.01:
            break
    