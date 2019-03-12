
def knuth_lexical_permute( v):
  n = len(v)
  a = [0] + list(sorted(v))
  while True:
    yield a[1:]

    j = n-1
    while a[j] >= a[j+1]:
      j -= 1

    if j == 0: return

    l = n
    while a[j] >= a[l]:

      l -= 1

    a[l],a[j] = a[j],a[l]

    a[j+1:] = a[n:j:-1]
