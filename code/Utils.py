import kohonen
import numpy as np
from math import log

def computeUMatrix(kohonenMap):
    neuronD = np.zeros((2*kohonenMap.neurons.shape[0]-1,2*kohonenMap.neurons.shape[1]-1))
    for row in range(0, neuronD.shape[0]):
        for col in range(0, neuronD.shape[1]):
            if row%2 != 0 and col%2 != 0:
                
                neuron1r = (row-1) / 2
                neuron1c = (col-1) / 2
                neuron2r = (row+1) / 2
                neuron2c = (col+1) / 2
                neuron1 = kohonenMap.neurons[neuron1r, neuron1c, :]
                neuron2 = kohonenMap.neurons[neuron2r, neuron2c, :]
                part1 = kohonenMap._metric(neuron1, neuron2)
                
                neuron1r = (row+1) / 2
                neuron1c = (col-1) / 2
                neuron2r = (row-1) / 2
                neuron2c = (col+1) / 2
                neuron1 = kohonenMap.neurons[neuron1r, neuron1c, :]
                neuron2 = kohonenMap.neurons[neuron2r, neuron2c, :]
                part2 = kohonenMap._metric(neuron1, neuron2)
                neuronD[row,col] = (part1+part2)/2.
            else:
                if row%2 != 0 or col%2 != 0:
                    if row%2 != 0:
                        neuron1 = (row-1) / 2
                        neuron2 = (row+1) / 2
                        neuron1 = kohonenMap.neurons[neuron1, col/2,:]
                        neuron2 = kohonenMap.neurons[neuron2, col/2,:]
                        neuronD[row,col] = kohonenMap._metric(neuron1, neuron2)
                    else:
                        neuron1 = (col-1) / 2
                        neuron2 = (col+1) / 2
                        neuron1 = kohonenMap.neurons[row/2, neuron1,:]
                        neuron2 = kohonenMap.neurons[row/2, neuron2,:]
                        neuronD[row,col] = kohonenMap._metric(neuron1, neuron2)
                else:
                    neuronD[row,col] = -1
    
    masked_array = np.ma.array(neuronD, mask=neuronD==-1)
    return masked_array

def constructSamplesForNeurons(kohonenMap, matrix):
    samplesDict = dict()
    for i, row in enumerate(matrix):
        j = kohonenMap.winner(row)
        x,y = kohonenMap.flat_to_coords(j)
        key = str(x) + "," + str(y)
        if key not in samplesDict.keys():
            samplesDict[key] = list()
        samplesDict[key].append(i)
    return samplesDict

class Timeseries(object):
    '''Represents some sort of value that changes over time.'''

    def __init__(self):
        '''Set up this timeseries.'''
        super(Timeseries, self).__init__()
        self.ticks = 0

    def __call__(self):
        '''Call this timeseries.'''
        t = self.ticks
        self.ticks += 1
        return t

class ExponentialTimeseries(Timeseries):
    '''Represents an exponential decay process.'''

    def __init__(self, initial=1, final=0.2, n_iter=10):
        '''Create a new exponential timeseries object.'''
        super(ExponentialTimeseries, self).__init__()
        assert final > 0, "Final learning rate has to be greater than zero!"
        self.initial = log(initial-final)
        self.final = log(final)
        self.n_iter = n_iter
        self.values = np.exp(np.linspace(self.initial, self.final, self.n_iter))

    def __call__(self):
        '''Return an exponentially-decreasing series of values.'''
        if self.ticks < self.n_iter:
            super(ExponentialTimeseries, self).__call__()
        return self.values[self.ticks - 1]