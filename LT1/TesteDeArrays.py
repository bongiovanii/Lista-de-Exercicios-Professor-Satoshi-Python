def loadArray(array):

   for i in range(20):
     id = "Name",i
     user = {
        "id": id,
        "age": 10 + i
     }
     array.append(user)

   return array

data = []
data = loadArray(data)

print(data)


