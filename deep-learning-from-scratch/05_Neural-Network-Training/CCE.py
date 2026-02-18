import numpy as np

def cross_entropy_error(y, t):
  delta = 1e-7 # 0이 되었을때 로그의 무한대 값 방지
  return -np.sum(t*np.log(y+delta))

if __name__ == "__main__":
  y = np.array([0.1, 0.05, 0.6, 0.0,0.05,0.1,0,0.1,0,0])
  t = np.array([0,0,1,0,0,0,0,0,0,0])
  print(cross_entropy_error(y, t))

  t = np.array([0,1,0,0,0,0,0,0,0,0])
  print(cross_entropy_error(y, t))