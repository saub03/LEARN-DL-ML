import numpy as np

def sigmoid(x):
  return 1/(1+np.exp(-x))

if __name__ == "__main__":
  print(sigmoid(1))
  print(sigmoid(-3))
  print(sigmoid(5))
  print(sigmoid(np.array([1,3,-2])))