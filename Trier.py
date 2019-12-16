def index_of_the_smallest(t):
  i=0
  j=1
  for elements in t:
      if t[i]<t[j]:
          return i
      else:
          return j

def trier(t):
    for j in range(l, len(t)):
        T=t[j]
        i =j- 1
        while i>=0 and t[i]>T:
            t[i+1]=t[i]
            i=i-1
        t[i+1]= T
    return t