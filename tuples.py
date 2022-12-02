#tuples can't be modify / change / assign
tp1 = ()    #empty tuple
tp2 = (1,) #single element tuple comma is compulsary
tp = (1,2,3,4,1,2,6,3,1,1) 
print(tp)
print(tp1)
print(tp2)
print(tp.count(1))
print(tp.index(6))


#program
a = (7,0,8,0,0,0,0,0,0,9)
print(a.count(0))