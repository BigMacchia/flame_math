import math

class Vector (object):
    """
    This is a vector class emulating the flame notation, as explanied 
    on the LAFF course on edx.org
    """
    def __init__(self, values):
        """
        This is the constructor
        Args:
        
        :values: list[float], the values to initialize the vector with 
        """ 
        self.values = values

    @classmethod
    def copy(cls, v):
        """
        This is the copy constructor

        Args:

        :v: Vector, the vector we wish to copy
        :returns: vector instance
        """

        return cls(v[:])
    
    def __getitem__ (self , index):
        """
        The indexing operator
        
        Args:
        
        :index: int, slice objcet,  the index to acces or a slice object defining the items we want
        to access
        """

        return self.values[index]

    def size(self):
        """
        Returns the size of the vector

        :returns: int
        """
        return len(self.values)
    
    def __len__(self):
        """
        This procedure returns the length of the vector
        :return: int
        """ 
        return self.size()
    
    def __str__(self):
        """
        Pretty print of the class
        """
        return str(self.values)

    def __add__(self  ,v):
        """
        This procedure sums the two vectors togheter
        Args:
        :v: Vector() the vector to sum
        :return : Vector()
        """
        return self.__class__([value + v[idx] for value,idx in enumerate(self.values)])
        
    def __iadd__(self, v):
        """
        In place sum operator
        :v: Vector() the vector to sum
        """
        self.values = [value + v[idx] for value,idx in enumerate(self.values)]
        
    def __rmul__ (self, scal):
        """
        Right multiplication , assuming int or float , performing scalar multiplication
        
        Args:
        :scal: int/float , scalar value for the operation
        :return: Vector instance
        """ 
        return Vector([ x * scal for x in self.values])

class Bucket(object):
    FLA_BOTTOM = 0
    FLA_TOP = 1

FLA_BOTTOM = Bucket.FLA_BOTTOM
FLA_TOP = Bucket.FLA_TOP
BUCKETS = [FLA_BOTTOM, FLA_TOP]

def part (vec, size=0, bucket= FLA_TOP):
    
    if not bucket in BUCKETS:
        raise InputValueError("bucket argument is not a valid one")
    
    v_size = vec.size()
    if v_size < size:
        raise InputValueError("lol")

    if bucket == Bucket.FLA_TOP:
        new_top = Vector(vec[:size])
        new_end = Vector(vec[size:])
    else:
       
        new_top = Vector(vec[:v_size-size]) 
        new_end = Vector(vec[v_size-size:])

    return new_top, new_end


def slice_( top_vector, bottom_vector, size=1, bucket = FLA_BOTTOM):

    """
    """
    if not bucket in BUCKETS:
        raise InputValueError("bucket argument is not a valid one")

    if size <= 0:
        raise InputValueError("size must be an integer greater then 0")

    if bucket == Bucket.FLA_TOP:
        new_top = top_vector[:-size] 
        new_end = bottom_vector 
        value = top_vector[-size:]
    else:
        new_top = top_vector 
        new_end = Vector(bottom_vector[size:])
        value = bottom_vector[:size]
    
    if size ==1:
        #if size ==1 , we extract the value from the list ov value, since
        #it would be a list with one element
        return new_top, value[0], new_end
    else:
        return new_top, value, new_end

def compose(top_vector, value, bottom_vector, bucket =FLA_TOP):

    
    if not bucket in BUCKETS:
        raise InputValueError("bucket argument is not a valid one")
    
    if bucket == Bucket.FLA_TOP:
        top_vector.values.append(value)
        return top_vector, bottom_vector
    else:
        bottom_vector.values.append(value)
        return top_vector, bottom_vector

def dot_product(x,y):

    xT,xB = part(x)
    yT,yB = part(y)

    res= 0.0
    while (xT.size() < x.size()):
        
        x0,x1,x2 = slice_(xT,xB,1, Bucket.FLA_BOTTOM)
        y0,y1,y2 = slice_(yT,yB,1, Bucket.FLA_BOTTOM)

        res += (x1 * y1)
        
        xT, xB = compose(x0, x1, x2, Bucket.FLA_TOP)
        yT, yB = compose(y0, y1, y2, Bucket.FLA_TOP)

    return res

def axpy(x,y ,alpha=1.0):
    """
    This function is an axpy meaning that we will scale the x
    vector times the scalar alpha and sum it with the y vector
    The operation is an "in place" operation, it overrides the y
    input vector with the result of the operation

    Args:

    :x: Vector, first vector for the operation
    :y: Vector, second vector for the operation
    :alpha: float, the scalar value used to scale x
    """

    xT,xB = part(x)
    yT,yB = part(y)

    while (xT.size() < x.size()):
        
        x0,x1,x2 = slice_(xT,xB,1, Bucket.FLA_BOTTOM)
        y0,y1,y2 = slice_(yT,yB,1, Bucket.FLA_BOTTOM)

        y1 = (alpha * x1) + y1 
        
        xT, xB = compose(x0, x1, x2, Bucket.FLA_TOP)
        yT, yB = compose(y0, y1, y2, Bucket.FLA_TOP)
    
    y.values = yT.values + yB.values
