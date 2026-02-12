import numpy as np
from and_gate import AND
from nand_gate import NAND
from or_gate import OR

def XOR(x1, x2):
  x = np.array([x1,x2])
  layer_nand = NAND(*x)
  layer_or = OR(*x)
  output = AND(layer_nand, layer_or)
  return output

if __name__ == '__main__':
  input_arr = np.array([[0,0], [0,1], [1,0], [1,1]])
  for i in input_arr:
    print(f"input{i}" + "->" + f"{XOR(*i)}")