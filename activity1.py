tup1=(1,2,3,4,5)
print("Tuple is ",tup1)
tup2=(6,)
print("Tuple 2 is ",tup2)
tup1=tup1+tup2
print("Updated Tuple 1 is ",tup1)

tup3=("Hello",[4,5,6],8)
print(tup3[0])
print(tup3[1])
print(tup3[2])
print(tup3[0][2])
print(tup3[1][1])

tup4=('c','h','i','m','i')
for tup in tup4:
    print("Hello",tup)