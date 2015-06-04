import vector
reload(vector)


emp = vector.Vector([])
print emp.size()
v1 = vector.Vector([1,2,3,4,5,6])
top,bottom = vector.part(v1,0)
print top, bottom
x0, x1,x2 = vector.slice_(top,bottom,1)
print x0,x1,x2

top,bottom = vector.compose(x0,x1,x2)

print top,bottom


print "------------------------"
top,bottom = vector.part(v1)
print top,bottom
for i in range(v1.size()):
    top,bottom = vector.compose(*vector.slice_(top,bottom))
    print top,bottom
    
v1 = vector.Vector([1,1,1])

print vector.dot_product(v1,v1)

v1 = vector.Vector([6,5,4])
v2 = vector.Vector([1,2,3])

print vector.dot_product(v1,v2)


print "--------------------------"

v1 = vector.Vector([1,2,1]);
v2 = vector.Vector([2,2,2]);

vector.axpy(v1,v2,3)

print v2

print v1+v2

