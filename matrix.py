import vector

class Matrix(object):
    def __init__(self, rows, columns ):
        """
        This is the constructor for the generic matrix
        Args:

        :rows: int, how many rows you want in the matrix
        :columns: int, how many columns you want in the matrix
        """
        self.data = [vector.Vector([0]*rows) for c in xrange(columns)]
        self.__columns = columns
        self.__rows = rows

    def set_to_value(self, value):
        """
        This function sets the whole matrix to a specifc value
        Args:

        :value: float, the value to set the matrix to
        """
        it = self.column_iterator()
        for c in it:
            c.set_to_value(value)
            it.merge(c)
            
    def zero(self):
        """
        Zero out the matrix
        """
        self.reset_to_value(0)

    def __str__(self):
        """
        Print out the matrix

        :todo: aligning caracters based maybe on float precision?
        """
        to_return = ""
        for r in xrange(self.__rows):
            tmp = ""
            for c in xrange(self.__columns):
                tmp += (str(self.data[c][r]) + " ")
            
            tmp += "\n"
            to_return +=tmp

        return to_return
         
    def columns(self):
        """
        Retunrs the orizontal size of the matrix
        """
        return len(self.data)

    def rows(self):
        """
        Returns the vertical size of the matrix
        """
        return len(self.data[0])
    
    def column_iterator(self):
        """
        Return a column iterator for the matrix
        
        :returns: iterator
        """
        return ColumnIterator(self)

    def diagonal_iterator(self):
        """
        Returns a diagonal iteerator for the matrix

        :returns: iterator
        """
        return DiagonalIterator(self)

    def __getitem__(self, index):
        """
        Subsctiption operator returns the colum vector
        at the given index not tested with slice object

        :index: int, the index we want to access
        """
        return self.data[index]

    def __setitem__(self, index ,data):
        """
        Subscrition setter operator, not tested with slice object

        :index: int, the index we want to set
        :data: Vector, no checks has been done whatsoever on the dimension of the
                vector compared to the matrix, it is up to the user to do not make
                mistakes.
        """
        self.data[index] = data


class ColumnIterator(object):
    """
    This class implements a column iterator for the given matrix,
    it will slice out one at the time the column and give it to the user
    for manipulation
    """
    def __init__(self, data):
        """
        This is the constructor
        Args:

        :data: Matrix, the matrix to iterate over
        """
        self.data = data
        self.counter = 0
        self.columns = data.columns()
        self.rows =  data.rows()
    def __iter__(self):
        
        return self
    
    def next(self):

        if self.counter < self.columns:
            
            to_return =  self.data[self.counter]
            self.counter +=1
            return to_return
        else:
            raise StopIteration()
    
    def merge(self, data):

        self.data[self.counter -1] = data


    def reset(self):
        self.counter = 0



class DiagonalIterator(object):
    def __init__(self, data):
        """
        This is the interator used to iterate the matrix in a diagonal
        fashion
        """

        self.data = data
        self.counter = 0
        self.columns = data.columns()
        self.rows =  data.rows()
    def __iter__(self):
        return self

    def next(self):

        if self.counter < self.columns:

           if self.counter == 0:
               TL = vector.Vector([])
           else:
               TL = vector.Vector(self.data[self.counter][:self.counter])
           value = self.data[self.counter][self.counter]
           BL = vector.Vector(self.data[self.counter][self.counter+1:])
           self.counter +=1
           return [TL, value, BL]
        else:
           raise StopIteration()

    def merge(self, TL, value, BL):

        self.data[self.counter -1] = vector.Vector(TL.values + [value] + BL.values)


class Matrix44(Matrix):
    def __init__(self, identity =True):
        Matrix.__init__(self,4,4)

        if identity:
            self.identity()

    def identity(self):
           
        dt = self.diagonal_iterator()
        for TL, value, BL in dt:
            TL.zero()
            value=1
            BL.zero()

            dt.merge(TL, value, BL)
