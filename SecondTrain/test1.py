
import neurolab as nl
import numpy as np
import numpy as np
import neurolab as nl
input = np.random.uniform(-0.5, 0.5, (10, 2))
target = (input[:, 0] + input[:, 1]).reshape(10, 1)
#Create network with 2 inputs, 5 neurons in input layer and 1 in output layer
net = nl.net.newff([[-0.5, 0.5], [-0.5, 0.5]], [5, 1])

net.train(input, target, show=15)
print net.sim([[0.2,0.3]])
