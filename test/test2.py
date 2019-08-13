with open("somefile","r") as sf:
   print(sf.read(13))
   print(sf.read(2))
   print(sf.readline())
   print(sf.readline())
   print(sf.readlines())