def fmt(a):
  first = len(tri_length)-1
  b = len(str(tri_length[a]))
  for x in range(len(tri_length)):
      nowlen = len(str(tri_length[x]))
      diflen = a - nowlen
      nowstring = tri_length[x]
      s = ''
      for y in range(diflen+5):
          s += ' '
      newstring = f"{nowstring}{s}"
      tri_length[x] = newstring

print("------------------------------------")
res = "\n".join("{} {}".format(x, y) for x, y in zip(tri_length, tri_surface))
print(res)
