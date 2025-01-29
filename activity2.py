set1={1,2,2,5,5,5,8,8,8,8,7,7,7,7,4,4,4,4}
print("Set 1 is ",set1)

set1.add(6)
print("Updated set 1 is ",set1)

set2={2,5,7,3,9,11,21}
print("Set 2 is ",set2)
print("Difference between set 1 and set 2 is ",set1.difference(set2))
print("Difference between set 2 and set 1 is ",set2.difference(set1))

print("Symmetric Difference between set 1 and set 2 is ",set1.symmetric_difference(set2))
print("Symmetric Difference between set 2 and set 1 is ",set2.symmetric_difference(set1))