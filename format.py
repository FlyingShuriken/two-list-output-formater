def fmt(a):
  f = len(a)-1                                                      #get the first elemen's index
  m = len(str(a[f]))                                                #get the first elemen
  for x in range(len(a)):                                           #process in every elemen
      nowlen = len(str(a[x]))                                       #the length of string now processing
      diflen = f - nowlen                                           #calculate the spaces that needed
      nowstring = a[x]                                              #get the elemen in string that are processing now
      s = ''                                                        #set an empty string as 's'
      for y in range(diflen+5):                                     #adding spaces into s, 5 is a random number for looking better in the output
          s += ' '                                                  #start to add space into s
      newstring = f"{nowstring}{s}"                                 #using f string instead of + in string
      a[x] = newstring                                              #replace the int to the formated string
  return a                                                          #return the formated list

if __name__ == "__main__":
  a = fmt(a)
  res = "\n".join("{} {}".format(x, y) for x, y in zip(a,b))        #print two list in same line
  print(res)
