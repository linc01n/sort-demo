def merge(left,right):
  result = []
  while(len(left) and len(right)):
    if(left[0] < right[0]):
      result.append(left.pop(0))
    else:
      result.append(right.pop(0))

  while(len(left)):
    result.append(left.pop(0))
  while(len(right)):
    result.append(right.pop(0))
  return result

def sort(a):
  if(len(a) < 2):
    return a
  mid = len(a)/2
  left = sort(a[:mid])
  right = sort(a[mid:])
  return merge(left,right)

