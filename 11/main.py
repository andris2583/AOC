import functools

data = [4022724, 951333, 0, 21633, 5857, 97, 702, 6]

# data = [125, 17]

@functools.cache
def calc(val, d):
    if d == 0:
       return 1
    if val == 0:
      return calc(val+1,d-1)
    elif len(str(val)) % 2 == 0:
      return calc(int(str(val)[0:int(len(str(val))/2)]),d-1) + calc(int(str(val)[int(len(str(val))/2):]),d-1)
    else:
      return calc(val*2024,d-1)

result = 0
for val in data:    
    result += calc(val,75)
print(result)

