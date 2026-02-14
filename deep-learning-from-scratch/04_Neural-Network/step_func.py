import numpy as np

def step_function(x):
  return np.array(x>0, dtype=np.int64)




if __name__ == "__main__":
  x = np.array([-1.0, 1.0, 2.0])
  print(step_function(x))