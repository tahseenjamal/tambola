from tabulate import tabulate
import numpy as np

ticket = np.full(27,1).reshape(9,3)
ticket[:4,:] *= 0
[np.random.shuffle(ticket[:,i]) for i in range(3)]

for i in range(9):
    num = np.arange(1,11)
    np.random.shuffle(num)
    num = np.sort(num[:3])
    ticket[i,:] *= (num + i * 10)


table = tabulate(ticket.T, tablefmt="fancy_grid")
print(table)
