import numpy as np

def numerical_diff(f, x):
  h = 1e-4
  return ((f(x+h)) - f(x-h))/(2*h)


if __name__ == "__main__":
  import matplotlib.pylab as plt
  def f1(x):
    return 0.01*x**2 + 0.1*x

  x = np.arange(0, 20, 0.1)
  y1 = f1(x)
  plt.plot(x,y1)
  
  y2 = numerical_diff(f1, 10)*(x - 10) + f1(10)
  plt.plot(x,y2)
  plt.show()