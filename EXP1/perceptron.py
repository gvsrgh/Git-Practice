import numpy as np
# Step-1: Initialize Input and Output Variables
features=np.array([
    [0,0]
    ,[0,1]
    ,[1,0]
    ,[1,1]
])
labels= np.array([0, 0, 0, 1])#AND Gate
# step-2: Intialize the netwrok parameters
# epoch( Training Iterations)
# Bias=1, Learning Rate=(0to1)
# input Weights (w1,w2)
epochs = int(input('Enter the Epochs:'))
threshold= float(input('Enter the Threshold:'))
Learning_rate = float(input('Enter the Learning Rate'))
a=[]
a.append(float(input('Enter the weights for x0')))
a.append(float(input('Enter the weights for x1')))
w=np.array(a)
for j in range(0,epochs):
    print("epoch", j)
    global_delta = 0
    for i in range(0,features.shape[0]):
        #print(features[i])
        actual = labels[i]
        instance = features[i]
        x0 = instance[0]
        x1 = instance[1]
        sum_unit = x0 * w[0] + x1 * w[1]
        if sum_unit > threshold:
            fire =1
        else:
            fire =0
        #print("prediction:",fire,"where as actual was", labels[i]) 
        delta = actual - fire
        global_delta = global_delta + abs(delta)
        print("prediction:",fire,"where as actual was", actual, " (error:",delta,")")
        w[0] = w[0] + delta * Learning_rate
        w[1] = w[1] + delta * Learning_rate
    print("--------------------")
    if global_delta == 0:
        break
    print (w)
