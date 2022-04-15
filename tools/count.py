def increase(count):
  c = open('data/counts/' + count + '.txt', 'r')
  co = int(c.read())
  c.close()
  c = open('data/counts/' + count + '.txt', 'w')
  co = co + 1
  c.write(str(co))
  c.close()

def get(count):
  c = open('data/counts/' + count + '.txt', 'r')
  co = int(c.read())
  c.close()
  return(co)
 