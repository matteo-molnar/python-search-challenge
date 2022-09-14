# Python Search Challenge


max_row = None
max_column = None
visited = None


def determine_route_exists(from_row, from_column, to_row, to_column, map_matrix):
  global max_row
  global max_column
  global visited

  # Initialize globals if they haven't been set yet
  if (max_row is None):
    max_row = len(map_matrix)-1
  if (max_column is None):
    max_column = len(map_matrix[from_row])-1
  if (visited is None):
    visited = [[False for i in range(len(map_matrix[j]))] for j in range(len(map_matrix))]

  route_exists = is_reachable(from_row, from_column, to_row, to_column, map_matrix)

  # Clear globals for next case
  max_row = None
  max_column = None
  visited = None

  print(route_exists)


def is_reachable(from_row, from_column, to_row, to_column, map_matrix):
  # Check if we are starting on a valid cell
  if (map_matrix[from_row][from_column] == False):
    return False 
  visited[from_row][from_column] = True

  route_exists = traverse(from_row, from_column, to_row, to_column, map_matrix)
  if (route_exists):
    return True;
  return False


def traverse(from_row, from_column, to_row, to_column, map_matrix):
  # Check if we have reached our destination
  if (from_row == to_row and from_column == to_column):
    return True

  # Traverse Down
  if (from_row+1 <= max_row
      and visited[from_row+1][from_column] != True
      and map_matrix[from_row+1][from_column] == True):
    route_exists = is_reachable(from_row+1, from_column, to_row, to_column, map_matrix)
    if (route_exists):
      return True

  #Traverse Right
  if (from_column+1 <= max_column
      and visited[from_row][from_column+1] != True
      and map_matrix[from_row][from_column+1] == True):
    route_exists = is_reachable(from_row, from_column+1, to_row, to_column, map_matrix)
    if (route_exists):
      return True

  #Traverse Up
  if (from_row-1 >= 0
      and visited[from_row-1][from_column] != True
      and map_matrix[from_row-1][from_column] == True):
    route_exists = is_reachable(from_row-1, from_column, to_row, to_column, map_matrix)
    if (route_exists):
      return True

  #Traverse Left
  if (from_column-1 >= 0
      and visited[from_row][from_column-1] != True
      and map_matrix[from_row][from_column-1] == True):
    route_exists = is_reachable(from_row, from_column-1, to_row, to_column, map_matrix)
    if (route_exists):
      return True



# CASE 1
map = [
  [True,  True, False],
  [False, True, False],
  [False, True, True]
]
print('CASE #1')
determine_route_exists(0, 0, 2, 2, map)

# CASE 2
map2 = [
  [True,  True,  False],
  [False, True,  False],
  [False, True,  True],
  [False, False, True],
  [True,  True,  True],
  [True,  False, False],
  [True,  True,  False],
  [False, True,  True],
]
print()
print('CASE #2')
determine_route_exists(0, 0, 6, 0, map2)

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
print()
print('CASE #3')
determine_route_exists(4, 2, 0, 0, map3)
