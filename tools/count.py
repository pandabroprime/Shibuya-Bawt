def increase(count):
  c = open('trackers/' + count + '.txt', 'r')
  co = int(c.read())
  c.close()
  c = open('trackers/' + count + '.txt', 'w')
  co = co + 1
  c.write(str(co))
  c.close()

def get(count):
  c = open('trackers/' + count + '.txt', 'r')
  co = int(c.read())
  c.close()
  return(co)
 