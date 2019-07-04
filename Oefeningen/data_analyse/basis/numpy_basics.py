from functools import wraps
import numpy as np

def showcase_numpy(fn):
  @wraps(fn)
  def exec(title=None, *args, **kwargs):
    print(f"\n\n*********************** {title} ********************\n" if title is not None else f"\n\n*********  SCHEID ;) ********\n")
    return fn(title=None, *args, **kwargs)
  return exec

@showcase_numpy
def help_numpy(title=None):
  print(help(np.array))

@showcase_numpy
def dir_numpy():
  print(dir(np))

@showcase_numpy
def arrays(title=None):
  # int arrays
  np_arr = np.array([el for el in range(0, 50)])
  print(f"integer array: {np_arr}")
  # change first element to float
  np_arr[0] = 99.14
  print(f"\nstill integer array, 99.14 is converted to 99: {np_arr}")

@showcase_numpy
def float_array(title=None):
  # standard float (64)
  float_arr = np.array([3.14, 6, 10, 27, 19])
  print([type(el) for el in float_arr])

  # explicit float 32
  other_float = np.array([el for el in range(0, 4)], dtype='float32')
  print(f"\n{[type(el) for el in other_float]}")

@showcase_numpy
def square_matrix(title):
  matrix = np.array([range(i, i+3) for i in [2,4,6]])
  print(f"\nSquare matrix: \nnp.array([range(i, i+3) for i in [2,4,6]]) \n {matrix}")
  matrix2 = np.full((3,5), 3.14)
  print(f"\n3x5 matrix, filled with 3.14: np.full((3,5), 3.14): \n {matrix2}")

@showcase_numpy
def array_attributes(title):
  print(f"3 DIM ARRAY: \nnp.random.randint(10, size=(3, 4, 5))")
  x = np.random.randint(10, size=(3, 4, 5))
  print(f"\n{x}\n")
  print(f"x ndim: {x.ndim}")  
  print(f"x shape: {x.shape}")  
  print(f"x size: {x.size}")
  print(f"x dtype: {x.dtype}")
  print(f"x itemsize: {x.itemsize}")
  print(f"x nbytes: {x.nbytes}")

@showcase_numpy
def array_operations(title):
  array = np.array([['a', 'b', 'c'], ['g', 'h', 'i']])
  grid = np.array([['D', 'E', 'F'], ['x', 'y', 'z']])
  print(np.dstack([array, grid]))

if __name__ == "__main__":
  arrays("NUMPY ARRAY")
  float_array("FLOAT NUMPY ARRAY")
  square_matrix("A SQUARE MATRIX")
  array_attributes("ARRAY ATTRIBUTES")
  array_operations("SOME ARRAY OPERATIONS")