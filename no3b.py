def orderedCari(listData, data)
  ind = 0
  found = False
  stop = False
  position = []
  while ind < len(listData) and not found and not stop:
    if listData[ind] == data:
      found = True
      position.append(ind)
     else:
      if listData [ind] > data:
        stop = True
      else:
        ind = ind+1
        
  if found:
    return ind
  else:
    return ('Data tidak ada')
  
a= [3,4,5,6,7,8,9,1,11,12]
ind = orderedCari(a,7)
print(ind)
