import merge,insert
def sort(a):
  if(len(a) < 7):
    return insert.sort(a)

  mid = len(a)/2
  left = merge.sort(a[:mid])
  right = merge.sort(a[mid:])
  return merge.merge(left,right)


