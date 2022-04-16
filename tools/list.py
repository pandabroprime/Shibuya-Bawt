#Turns a .txt file to a list.
def toList(list):
  f = open('data/lists/' + list + '.txt', 'r')
  l = f.read().split("\n")
  f.close()
  return l

#Adds a new line to a .txt file.
def add(line, list):
  f = open('data/lists/' + list + '.txt', 'a')
  f.write(line + '\n')
  f.close()