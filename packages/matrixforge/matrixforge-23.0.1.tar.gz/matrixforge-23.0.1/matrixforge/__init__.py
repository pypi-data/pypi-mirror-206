'''
MatrixForge
===========
Copyright (C) 2023 Kacper Popek 
All rights reserved(FOR MORE INFORMATIONS READ LICENCE)
'''

from numpy import *
from matrixforge.activation import *

class createLayer:
    def __init__(self, nodes, activation=''):
        self.nodes = nodes
        self.activation = activation
        if activation == 'relu':
            self.activation = relu
            self.derivative = d_relu
        elif activation == 'sigmoid':
            self.activation = sigmoid
            self.derivative = d_sigmoid
        elif activation == 'softmax':
            self.activation = softmax
            self.derivative = d_softmax
        elif activation == 'softplus':
            self.activation = softplus
            self.derivative = d_softplus
        elif activation == 'tanh':
            self.activation = tanhh
            self.derivative = d_tanh
        else:
            raise ValueError("Unsupported activation function")
class Model:
    def __init__(self, inputs, hiddens, outputs, hiddenlayeram):
        self.inputlayer = inputs
        self.hiddenlayer = hiddens
        self.outputlayer = outputs
        self.hiddenlayeram = hiddenlayeram
class forwardPropagation:
    def __init__(self, model, biasvalue):
        self.model = model
        self.biasvalue = biasvalue
        self.inputlayer = model.inputlayer
        self.inputr = model.inputlayer.activation(random.randn(model.inputlayer.nodes))
        self.inputweights = random.randn(model.inputlayer.nodes, model.hiddenlayer.nodes)
        self.hiddenweights = random.randn(model.hiddenlayer.nodes, model.outputlayer.nodes)
        self.input_activation = model.inputlayer.activation
        self.hidden_activation = model.hiddenlayer.activation
        self.output_activation = model.outputlayer.activation
        self.hiddenlayer = model.hiddenlayer
        self.outputlayer = model.outputlayer
        self.hiddenlfp = self.hidden_activation(biasvalue+dot(ones((1, self.inputlayer.nodes)), self.inputweights))
        self.outputlfp = self.output_activation(biasvalue+dot(self.hiddenlfp, self.hiddenweights))
class backPropagation:
    def __init__(self, model, expectedvalue, learning_rate):
        self.model = model
        self.neurons = model.inputr, model.hiddenlfp, model.outputlfp
        self.error = expectedvalue-model.outputlfp
        self.derivative = model.inputlayer.derivative, model.hiddenlayer.derivative, model.outputlayer.derivative
        self.weights = model.inputweights, model.hiddenweights
        self.learning_rate = learning_rate
        self.biasvalue = model.biasvalue
class modelTrain:
    def __init__(self,model,epochs):
        self.model = model
        self.epochs = epochs
class Visualize:
    def __init__(self, model):
        print("Bias Value:", model.biasvalue,'\n')
        print("Input Layer Value:", model.inputr,'\n')
        print("Hidden Layer Value:", model.hiddenlfp,'\n')
        print("Output Layer Value:", model.outputlfp,'\n')
        print("Activation Functions:","\n","Input Layer:",model.input_activation,"\n","Hidden Layer:",model.hidden_activation,"\n","Output Layer:",model.output_activation)
