def cari (listData, data)
  ind = 0
  found = False
  while ind < len(listData) and not found:
    if listData(ind) == data:
      found = True
    else: 
      ind = ind+1
  return found

a = [2,3,1,5,7,8,6,10,12,15]
cari (a,1)
