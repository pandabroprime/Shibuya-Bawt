def toList(list):
  f = open('trackers/' + list + '.txt', 'r')
  l = f.read().split("\n")
  f.close()
  return l