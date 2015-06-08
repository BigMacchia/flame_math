import vector

class Matrix(object):
    def __init__(self, rows, columns ):
        """
        COLUMN MAJOR 
        """
        self.data = [vector.Vector([0]*rows) for c in xrange(columns)]
        self.__columns = columns
        self.__rows = rows

    def reset_to_value(self, value):

        for r in xrange(self.__rows):

            for c in xrange(self.__columns):
                self.data[c][r] = value

    def zero(self):

        self.reset_to_value(0)



    def __str__(self):

        to_return = ""
        for r in xrange(self.__rows):
            tmp = ""
            for c in xrange(self.__columns):
                tmp += (str(self.data[c][r]) + " ")
            
            tmp += "\n"
            to_return +=tmp

        return to_return
         
    def columns(self):
        return len(self.data)

    def rows(self):
        return len(self.data[0])
    
    def column_iterator(self):
        return len(self.data[0]) 

    def __getitem__(self, index):
       
        return self.data[index]

    def __setitem__(self, index ,data):

        self.data[index] = data


class ColumnIterator(object):
    def __init__(self, data):

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
    
    def merge(self, index, data):

        self.data[index] = data

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
        
        for r in xrange(4):
            self.data[r][r] = 1
