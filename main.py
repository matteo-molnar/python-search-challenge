# search a map searching algorithm challenge
map = [
  [True, False, False],
  [True, True, False],
  [False, True, True]
]


def is_reachable(from_column, from_row, to_column, to_row, map_matrix):

  # need a way to track where I've checked already, maybe a copy of the array

  if (map_matrix[from_column][from_row] == False):
    return False
  elif (from_column == to_column and from_row == to_row):
    return True

  if (map_matrix[from_column+1][from_row] == True):
    pass


print(is_reachable(0, 0, 2, 2, map))
