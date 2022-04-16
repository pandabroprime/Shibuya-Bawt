#Increases a count by 1.
def increase(count):
  c = open('data/counts/' + count + '.txt', 'r')
  co = int(c.read())
  c.close()
  c = open('data/counts/' + count + '.txt', 'w')
  co = co + 1
  c.write(str(co))
  c.close()

#Returns a count.
def get(count):
  c = open('data/counts/' + count + '.txt', 'r')
  co = int(c.read())
  c.close()
  return(co)

#Sets a count to a number specified.
def set(count, new):
  c = open('data/counts/' + count + '.txt', 'w')
  c.write(str(new))
  c.close()

#Resets a count to 0.
def reset(count):
  c = open('data/counts/' + count + '.txt', 'w')
  c.write(str(0))
  c.close()