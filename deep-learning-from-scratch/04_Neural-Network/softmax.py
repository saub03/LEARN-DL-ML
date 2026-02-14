import numpy as np

def softmax(x):
  max = np.max(x)
  x = x-max
  exp_arr = np.exp(x)
  exp_sum = np.sum(exp_arr)
  return exp_arr/exp_sum




if __name__ == '__main__':
  a = np.array([0.3, 2.0, 4.0])
  print(softmax(a))