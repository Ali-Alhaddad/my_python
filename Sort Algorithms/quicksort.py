
def quicksort(a: list, l: int, u: int) -> None:
  '''Sort the given list a in non-descending order.
  Precondition: 0 <= l and u < len(a)'''

  if l < u:
    mid = (l + u) // 2
    three = [a[l], a[mid], a[u]]
    three.sort() 
    if three[1] == a[l]:
      pivot_loc = l
    elif three[1] == a[u]:
      pivot_loc = u
    else:
      pivot_loc = mid
    a[u], a[pivot_loc] = a[pivot_loc], a[u]
    pivot = a[u]    
    i = partition(a, l, u - 1, pivot)
    
    a[(i[0])], a[u] = a[u], a[i[0]]
    quicksort(a, l, i[0] - 1)
    quicksort(a, i[0] + 1, u)






def partition (a: list, l: int, u: int, pivot: object) -> 'tuple of two ints':
  '''Alternate partition: This new partition procedure maintains two
  split points, dividing the list into those elements that are smaller
  than the pivot, those exactly equal to the pivot, and those strictly
  larger than the pivot. Return a tuple of the indices of the two split points.

  >>> l = [-19, 1, 1, 1, 18, 18, 104, 418]
  >>> partition(l, 0, len(l)-1, 18)
  (4, 6)
  >>> l
  [-19, 1, 1, 1, 18, 18, 418, 104]
  '''
  
  i = l
  j = l
  k = u
  while j <= k:
    if a[j] < pivot:
      a[i], a[j] = a[j], a[i]
      i += 1
      j += 1
    elif a[j] == pivot:
      j += 1
    else:
      a[j], a[k] = a[k], a[j]
      k -= 1
  return (i, j)
