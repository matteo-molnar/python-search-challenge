# Python Search Challenge
from traceback import print_exc

max_column = None
max_row = None
visited = None


def is_reachable(from_column, from_row, to_column, to_row, map_matrix):
  global max_column
  global max_row
  global visited

  # Initialize visited list if it hasn't been generated yet
  if (max_column is None):
    max_column = len(map_matrix)-1
  if (max_row is None):
    max_row = len(map_matrix[from_column])-1
  if (visited is None):
    visited = [[False for i in range(len(map_matrix[j]))] for j in range(len(map_matrix))]

  if (map_matrix[from_column][from_row] == False):
    return False 
  visited[from_column][from_row] = True

  route_exists = traverse(from_column, from_row, to_column, to_row, map_matrix)
  if (route_exists):
    return True;
  return False

def traverse(from_column, from_row, to_column, to_row, map_matrix):
  print('-------------------------')
  print(f'from_column: {from_column}')
  print(f'from_row: {from_row}')

  # Check if we have reached our destination
  if (from_column == to_column and from_row == to_row):
    print('Reached Destination!!!')
    return True

  # Traverse Down
  if (from_column+1 <= max_column
      and visited[from_column+1][from_row] != True
      and map_matrix[from_column+1][from_row] == True):
    print('Traverse Down...')
    route_exists = is_reachable(from_column+1, from_row, to_column, to_row, map_matrix)
    if (route_exists):
      return route_exists
  #Traverse Right
  if (from_row+1 <= max_row
      and visited[from_column][from_row+1] != True
      and map_matrix[from_column][from_row+1] == True):
    print('Traverse Right...')
    route_exists = is_reachable(from_column, from_row+1, to_column, to_row, map_matrix)
    if (route_exists):
      return route_exists
  #Traverse Up
  if (from_column-1 >= 0
      and visited[from_column-1][from_row] != True
      and map_matrix[from_column-1][from_row] == True):
    print('Traverse Up...')
    route_exists = is_reachable(from_column-1, from_row, to_column, to_row, map_matrix)
    if (route_exists):
      return route_exists
  #Traverse Left
  if (from_row-1 >= 0
      and visited[from_column][from_row-1] != True
      and map_matrix[from_column][from_row-1] == True):
    print('Traverse Left...')
    route_exists = is_reachable(from_column, from_row-1, to_column, to_row, map_matrix)
    if (route_exists):
      return route_exists


# CASE 1
# map = [
#   [True, True, False],
#   [False, True, False],
#   [False, True, True]
# ]
# print(is_reachable(0, 0, 2, 2, map))

# CASE 2
# map2 = [
#   [True, True, False],
#   [False, True, False],
#   [False, True, True],
#   [False, False, True],
#   [True, True, True],
#   [True, False, False],
#   [True, True, False],
#   [False, True, True],
# ]
# print(is_reachable(0, 0, 6, 0, map2))

#CASE 3
map3 = [
  [True,  True,  True,  True],
  [False, True,  False, False],
  [False, True,  True,  True],
  [False, False, False, True],
  [True,  True,  True,  True],
  [True,  False, False, False],
  [True,  True,  False, True],
  [False, True,  True,  True],
]
print(is_reachable(4, 2, 0, 0, map3))
