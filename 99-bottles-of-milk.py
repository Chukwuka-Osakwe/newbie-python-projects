'''
Found this exercise in the Big Book Of Small Python Problems and I'm just slightly amused that it took only a few lines of code to get it done so here it is. 
'''

'''
99 bottles of milk on the wall,
99 bottles of milk,
Take one down, pass it around,
98 bottles of milk on the wall!

98 bottles of milk on the wall,
98 bottles of milk,
Take one down, pass it around,
97 bottles of milk on the wall!
'''


x = 99

while x > 0:
   if x == 2:
      print(f"{x} bottles of milk on the wall,\n{x} bottles of milk,\nTake one down, pass it around,\n{x-1} bottle of milk on the wall!\n\n")
   elif x == 1:
      print(f"{x} bottle of milk on the wall,\n{x} bottle of milk,\nTake one down, pass it around,\n{x-1} bottles of milk on the wall!\n\n")
   else:
      print(f"{x} bottles of milk on the wall,\n{x} bottles of milk,\nTake one down, pass it around,\n{x-1} bottles of milk on the wall!\n\n")
      
   x-=1