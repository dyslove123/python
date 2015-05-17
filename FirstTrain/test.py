import Image
import json
import neurolab as nl
import matplotlib.pyplot as pl
entry=[]
with open("input.txt","r") as input_file:
	entry=json.load(input_file)
target=[]
input=[]
for i in range(0,50):
	if(i%5==0):
		target.append(entry[1][i])
		input.append(entry[0][i])
structure=[]
net=nl.load("train.data")

result=net.sim(input)
print result
#print euclidean_distance(target, result)  
