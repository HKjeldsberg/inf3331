import sys,numpy as np

cost = 1
prize = 10
funds = 0
n = int(sys.argv[1])
m = int(sys.argv[2])
win = 0
loss = 0
for j in range(m):
    for i in range(n):
        values = np.random.random_integers(1,6,4)
        if np.sum(values) < 9:
            funds += prize
            win += 1
        else:
            funds -= cost
            loss += 1

print "Was it worth it?"
print "Wins: %i \tLosses: %i" %(win,loss)
