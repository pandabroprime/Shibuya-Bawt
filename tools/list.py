def toList(list):
  f = open('data/lists/' + list + '.txt', 'r')
  l = f.read().split("\n")
  f.close()
  return l