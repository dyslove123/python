import json
import neurolab as nl
import matplotlib.pyplot as pl
entry=[]
with open("input.txt","r") as input_file:
	entry=json.load(input_file)

structure=[]
for i in range(0,16*16):
	structure.append([0,4])
net = nl.net.newp(structure, 10)

error = net.train(entry[0], entry[1], epochs=100, show=10, lr=0.01)
net.save("train.data")
# Plot results

pl.plot(error)
pl.xlabel('Epoch number')
pl.ylabel('Train error')
pl.grid()
pl.show()