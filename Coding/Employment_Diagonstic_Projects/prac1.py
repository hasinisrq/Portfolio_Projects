import pandas as pd
from matplotlib import pyplot as plt

Minutes = [1, 2, 3, 4, 5, 6, 7, 8, 9]
Player1 = [1, 2, 3, 3, 4, 4, 4, 4, 5]
Player2 = [1, 1, 1, 1, 2, 2, 2, 3, 4]
Player3 = [1, 1, 1, 2, 2, 2, 3, 3, 3]

plt.stackplot = [Minutes, Player1, Player2, Player3 ]
plt.show()

