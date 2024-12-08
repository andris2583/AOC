import itertools
import math


data = [
[".",".",".",".",".",".",".",".",".",".",".","g",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".","e",".","g",".",".",".",".",".",".","s",".",".",".",".",".",".",".",".",".",".",".",".",".","R",".",".",".",".",".",".",".",".",".",".",".","I",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".",".",".",".",".","g",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","I",".",".",".",".",".",".",".",".",".",".",".","."],
[".",".","b",".",".",".",".",".",".","Q",".",".",".",".","s",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","P",".",".",".",".",".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".","e",".",".","T",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","K",".",".",".",".",".",".",".",".",".",".",".","P",".",".",".","F",".",".","."],
[".",".",".",".",".","g",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","U",".",".",".",".",".",".",".",".",".",".",".",".",".","4",".",".",".",".",".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".",".","b",".",".",".",".",".",".",".",".",".",".","4",".",".","R","U",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","1",".","F",".",".",".","."],
[".",".",".",".","a",".",".",".",".",".","Q",".",".",".",".",".",".",".",".",".",".","b",".",".",".",".",".",".",".",".","R",".",".","U",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","1"],
[".","S",".",".",".","T",".",".",".",".",".",".",".",".",".",".",".",".","s",".",".",".",".",".",".",".",".",".",".",".",".",".","I",".",".",".",".",".",".",".",".",".","f",".",".",".",".",".",".","."],
[".",".",".","A",".",".",".",".","T",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","I",".",".",".",".",".",".",".",".","."],
[".",".",".",".",".","Q","a",".",".",".",".",".",".",".",".",".",".",".",".","A",".","G",".",".",".","K",".",".",".",".",".",".",".",".",".",".",".","P",".",".",".",".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","G",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","1",".",".",".",".","."],
[".",".",".","D",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","4",".","f",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","k",".",".",".",".",".",".",".","R",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","t",".",".",".","."],
[".",".",".",".",".",".",".",".",".","T",".","e",".",".",".",".",".",".",".",".",".",".",".",".",".",".","K",".",".",".",".",".",".",".",".","u",".",".",".",".",".",".",".","t",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","A",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".","S",".",".",".",".","a",".",".",".",".",".",".",".",".",".",".",".",".",".","F",".",".",".",".",".",".",".",".",".",".",".","K","G",".",".",".",".",".",".",".",".",".",".","."],
[".",".",".",".","D",".",".",".","h",".",".",".",".",".",".","k",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
[".",".","D",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","k",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","4",".","."],
[".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","i",".",".","."],
[".",".",".",".",".",".",".",".",".","S",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","d",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".","Q","U",".",".",".",".","S",".",".",".",".",".",".","s",".",".","d",".",".",".","G",".",".",".",".",".",".",".",".",".",".",".",".","i",".",".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".",".",".",".","d",".",".",".",".","9",".",".",".","F",".","h",".",".",".","E",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","d",".",".",".",".","B",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
[".",".",".","h",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","H",".",".",".",".",".",".",".","t",".",".",".",".",".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".",".","h",".","B",".",".","3",".","E",".",".",".",".",".",".",".",".",".",".",".",".",".","H",".",".","r",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".","E",".",".",".",".",".",".","B",".",".",".",".",".",".","2",".",".",".","5",".",".",".",".",".","H",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
[".","z",".",".",".",".",".",".",".",".",".",".",".","9",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","t",".",".","."],
[".",".",".",".",".","9",".",".",".","D",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
[".",".",".",".",".","Z",".",".",".",".",".",".",".","3","9",".",".","a",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".",".",".","3",".",".",".",".",".",".",".",".",".",".",".",".",".","r",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","E","r",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","7",".",".","."],
[".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","J",".",".",".","k",".","r",".","q",".",".",".",".",".",".",".","i",".","8",".","p",".",".",".","."],
[".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","u",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","H",".","p",".",".","q",".",".",".",".","."],
[".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","i",".","u","6",".",".",".",".",".",".",".",".","p",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","0",".",".",".",".",".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","3",".",".","J",".",".",".",".","P",".",".",".","0",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","2","j",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","j","2","B","0",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","J",".",".","2",".",".",".","5",".",".",".",".",".","6",".",".",".",".",".",".","p",".",".",".",".","8",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".",".",".",".",".","y",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","7",".",".",".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".",".",".",".",".",".",".","5",".",".",".",".",".",".",".",".",".","y",".",".",".",".",".",".",".",".",".",".",".","6",".",".",".",".",".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","j",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","Y",".","J",".",".",".",".",".","0",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","y",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","Z",".",".",".","u","y",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","q",".",".",".",".",".","."],
[".",".",".",".",".",".",".","z",".",".",".",".",".",".",".",".",".","Z",".",".",".",".",".",".",".",".",".",".",".",".","Y",".","6",".",".",".",".",".",".",".",".",".",".",".",".",".","8",".",".","."],
["z",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","Y",".",".",".",".",".",".",".",".",".",".","7",".",".",".",".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","Z",".",".",".","5",".",".","Y",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
]

result = []

def hashcoords(i,j):
  return str(i)+"|"+str(j)

def combinations(array, tuple_length, prev_array=[]):
    if len(prev_array) == tuple_length:
        # prev_array.append([-prev_array[0],-prev_array[1]])
        return [prev_array]
    combs = []
    for i, val in enumerate(array):
        prev_array_extended = prev_array.copy()
        prev_array_extended.append(val)
        combs += combinations(array[i:], tuple_length, prev_array_extended)
    return combs


adj_positions = combinations([x for x in range(-len(data),len(data))], 2)
data_copy = [row[:] for row in data]

for i in range(len(data)):
  for j in range(len(data[i])):
    freq =  data[i][j]
    if freq != ".":
      for adj_pos in adj_positions:
        try:
          # if(i == 1 and j == 8):
          #   print(adj_pos,[i+adj_pos[0],j+adj_pos[1]],[i+(-adj_pos[0]),j+(-adj_pos[1])])
          if (data[i+adj_pos[0]][j+adj_pos[1]] == freq) and not ((i+adj_pos[0]) < 0 or (j+adj_pos[1]) < 0 or (i+2*adj_pos[0]) < 0 or (j+2*adj_pos[1]) < 0):
            for m in range(0,max(len(data),len(data[0]))):
              if i+m*adj_pos[0] < 0 or j+m*adj_pos[1] < 0:
                raise ValueError("asd")
              if hashcoords(i+m*adj_pos[0],j+m*adj_pos[1]) not in result:
                data_copy[i+m*adj_pos[0]][j+m*adj_pos[1]] = "#"
                result.append(hashcoords(i+m*adj_pos[0],j+m*adj_pos[1]))
          # if(i == 1 and j == 8):
          #   print(adj_pos,[i+(-adj_pos[0]),j+(-adj_pos[1])],[i+(-2*adj_pos[0]),j+(-2*adj_pos[1])])
        except:
           None
        try:
          if(data[i+(-adj_pos[0])][j+(-adj_pos[1])] == freq) and not ((i+(-adj_pos[0])) < 0 or (j+(-adj_pos[1])) < 0 or (i+2*(-adj_pos[0])) < 0 or (j+2*(-adj_pos[1])) < 0):
            for m in range(0,max(len(data),len(data[0]))):
              if i+m*(-adj_pos[0]) < 0 or j+m*(-adj_pos[1]) < 0:
                raise ValueError("asd")
              if hashcoords(i+m*(-adj_pos[0]),j+m*(-adj_pos[1])) not in result:
                data_copy[i+m*(-adj_pos[0])][j+m*(-adj_pos[1])] = "#"
                result.append(hashcoords(i+m*(-adj_pos[0]),j+m*(-adj_pos[1])))
        except:
           None

# print(result)
print(len(result))
print('\n'.join([''.join(['{:2}'.format(item) for item in row]) 
      for row in data_copy]))

# print(adj_positions)