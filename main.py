import math as m

points = [(-3, 10), (0, 7), (10, 8), (10, -7), (-7, 1), (6, 8), (-3, -4),
          (-5, 7), (-2, 1), (3, 10), (3, 1), (-9, -10), (-8, -10), (6, 9),
          (5, -8), (6, 5), (6, 6), (5, -9), (1, 1), (-6, 3)]

copyP = points.copy()

def euclideanDistance(a: tuple, b: tuple):
  return m.sqrt((b[1] - a[1])**2 + (b[0] - a[0])**2)

distances = []
nearestPoints = []

#d = 0
for i in points:
  for j in copyP:
    result = euclideanDistance(i,j)
    if(result not in distances):
      distances.append(result)
    if(result==1.0):
      nearestPoints.append((i,j))
    #d+=1
  copyP.remove(i)
  #print(copyP)

distances.sort(reverse=True)
distances.remove(0)
s="En yakın noktalar: "
a = min(distances)
for k in nearestPoints:
  s += f"\n {k[0]} ve {k[1]}"
print(s,"\nAralarındaki uzaklıklar: "+str(a))
