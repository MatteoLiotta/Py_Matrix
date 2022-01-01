'''
Matrix module

LIST OF FUNCTIONS:
            - matrix_c():
                creates a matrix from a selected (if not, uses the self.v) dataset, number of rows and columns (if not selected, it uses self.r and self.c)
            - __str__():
                print in a pretty and comprehensible way the matrix.
            - elem():
                Return a specific element of the matrix. User has to choose row and column, then the element in that row and column is returned.
            - elem_change():
                It changes a specific element of the matrix. User has to choose row and column, then the element in that row and column is changed whit the entered value.
                It is also possible to refer to the matrix as self.matrix[i][j], whitout using this function.
            - __add__():
                It makes possible to add two differents matrix. It return a new matrix, istance of Matrix class.
                Matrix must have same rows and columns
                [it returns a new Matrix object]
            - __mul__():
                Two possibilities: if 'other' is a number or if it is a matrix.
                - if other is a matrix, it uses the rule for this operation. So the operation returns the matrix obtained with the multiplication between matrix.
                - if other is not a matrix, but an integer or a floating point number, it multiplies every element of the matrix for the number.
                [it returns a new Matrix object]
            - t():
                The function returns a new matrix which is the transpose of the given matrix. The transpose matrix is define by definition as:
                    With A as a matrix (Aij), A.t() is (tAij), so:
                    tAij = Aji
                So the transpose switches the index of the original matrix. The new matrix is returned. Original matrix is not changed.
                
SAMPLES:
0) Import the module:
    >>> import Py_Matrix as py_m
    
1) Create a Matrix from a dataset:
    >>> A = py_m.Matrix([1,2,3,4], 2, 2)
    
2) Print a Matrix:
    >>> print(A) #A previously declared
    Output:
    0| 1     2     
    1| 3     4     
       --    --
       0     1

3) Print an element of the matrix, knowing row and column:
    WARNING: the first row is number 0, same as first column. It does not starts with 1
    >>> print(A.elem(1,0) #A previously declared
    Output: 3

4) Add two Matrix (Matrix + Matrix):
    WARNING: Matrix must have same rows and columns
    >>> A = py_m.Matrix([1,2,3,4], 2, 2)
    >>> B = py_m.Matrix([4,3,2,1], 2, 2)
    >>> print(A+B)
    Output:
    0| 5     5     
    1| 5     5     
       --    --
       0     1

5) Matrix * Matrix:
    WARNING: Matrix multiplication is not commutative
    >>>print(A*B) #A and B previously declared
    Output:
    0| 8     5     
    1| 20    13    
       --    --    
       0     1 
    
6) Matrix * number
    WARNING: 2*A is not implemented.
    >>> print(A*2) #A and B previously declared
    Output:
    0| 2     4     
    1| 6     8     
       --    --    
       0     1   
    
'''

class Matrix():
    def __init__(self, values_list=[], rows=2, columns=2):
        """ The function build a Matrix object. It requires a dataset, in order to put values inside the matrix. It also requires rows and columns, to correctly divide the dataset in sub-lists.
            Function check: The dataset must respect the exaxt possible number; user must enter rows*columns elements. Error is raised.
            Dataset type must be a list. Error is eventually raised.
        """
        #Check rows and columns type:
        if type(rows)!=int or type(columns)!=int: #their type must be integer. If not, are assigned as 2  
            rows=2
            columns=2
        else:
            pass
        
        #Check: dataset type
        value_type = True #it is a list = True. Variable used for check the type of the dataset
        try:
            if type(values_list)!=list: #if it is not a list
                value_type=False #the variable is set as False.
                #raise TypeError
        except Exception as e:
            print("You must list type for the dataset. Error:", e)
            
        #Check: lenght of the dataset. Must be rows*columns or minus
        try:
            if value_type!=False: #so, it is a list
                for i,e in enumerate(values_list):
                    if type(e)!=int or type(e)==list:
                        values_list[i]=0
                if len(values_list)!=(rows*columns): #it is a list but it has not enough elements
                    adding_list = []
                    for t in range(len(values_list), rows*columns):
                        adding_list.append(0)
                    values_list = values_list+adding_list #do create a list, which has n-k elements - those that are missing
                    #raise ValueError
            else: #it is not a list or it is not correct. It creates a list
                adding_list = []
                for t in range(0, rows*columns):
                    adding_list.append(0)
                values_list = adding_list
        except Exception as e:
            print("The dataset was missing, not correct or not enought long. It has been completed or created. The dataset is now:", self.v,". Error:", e)
        

        #after all the data-check, it is possible to create the variables.
        self.v = values_list
        self.r = rows
        self.c = columns
        self.matrix = self.matrix_c()
        #print(self.v, self.r, self.c, self.matrix)

    def divide_list(self, lista, minimo, massimo):
        '''
        Used to create lists for matrix rows
        '''
        list = []
        for i in range(minimo, massimo):
            list.append(lista[i])
        return list
            
    def matrix_c(self, r_chosen = 0, c_chosen = 0):
        '''
        Build the matrix from data previously entered.
        The process:
        - From the dataset (ex. [1,2,3,4,5,6,7,8,9] the function cuts the list
        - Each cut is made exactly after the precise number of columns.
        - the cut: used the auxiliary function "divide_list", that returns the list that it has cutted
        - After the cut the returned list is added to the "matrix" list. At the beginning it was void.
        So the matrix is a list of list of elements. Each sub-list of the "matrix" is a row of it.

        For the process are also used valoremin and valoremax, in order to correctly cut the dataset.
        The cut is made, for a 3x3, with dataset: [1,2,3,4,5,6,7,8,9]
                    1 2 3 | 4   5 6 | 7     8 9
            index   0 1 2 | 3   4 5 | 6     7 8
            so:     0       0+c     0+c+c
        Then valoremin (minimum) is the 0 at the beginning, and valoremax (maximum) is exactly 3, as the counter cont. Divide_list cuts from 0 to 3-1 (range exclude 1)
        Then when the function has to re-cut the dataset, valoremin is self.c (columns) * cicliannullamento (a counter that counts the times that the function has cutted the dataset).
        So, in this case, it is 3 * 1 = 3. Then it starts from 3 (as index) to valoremax, which is now 6. The function cuts from 3 to 5 (6-1 because of the range) and creates [3,4,5].
        And so on.

        Warning:
            A matrix made of 0 rows and columns doesn't have any purpose. It is automatically changed to the self.r and self.c
            If you do not choose a number of rows or columns, it is automatically set as 0; then, if is satisfied.
            It could be usefull to automatically choose the rows and columns from the existing variables self.r and self.c
        '''
        #ROWS and COLUMNS default:
        #A matrix made of 0 rows and columns doesn't have any purpose. It is automatically changed to the self.r and self.c
        #If you do not choose a number of rows or columns, it is automatically set as 0; then, if is satisfied.
        #It could be usefull to automatically choose the rows and columns from the existing variables self.r and self.c
        if r_chosen == 0 or c_chosen == 0:
            r_chosen = self.r
            c_chosen = self.c
            
        self.matrix = []
        cont = 0
        list_tmp = []
        matrix = []
        valoremin = 0
        valoremax = 0
        cicliannullamento = 0
        while(len(matrix)<r_chosen): #until the number of rows is not as declared
            if cont<c_chosen: #common case -> no cut
                cont+=1
                valoremax+=1
            else: #it has to cut the dataset
                valoremin = 0;
                valoremin = 0 + c_chosen*cicliannullamento;
                cicliannullamento += 1 #because it will cut. The counter has to be encreased.
                cont = 0 #reset the counter for the cut
                #matrix list - add the row
                matrix.append(self.divide_list(self.v, valoremin, valoremax ))
        return matrix #return the list created

    def elem(self, i, j):
        """
        Return a specific element of the matrix. User has to choose row and column, then the element in that row and column is returned.
        """
        elem=self.matrix[i][j] #select the element j in row i
        return elem #return that element

    def elem_change(self, i, j, value):
        """
        It changes a specific element of the matrix. User has to choose row and column, then the element in that row and column is changed whit the entered value.
        It is
        """
        self.matrix[i][j]=value
        return self
    
    def __str__(self):
        """
        Function used to print a matrix in order to make it more pretty
        """
        for i in range(0, self.r):
            print(i, end="| ")
            for j in range(0, self.c):
                print("%-5d" %(self.matrix[i][j]), end=" ")
            print("")
        print("   ", end="")
        for u in range(0, self.c):
            print("--"+4*" ", end="")
        print("")
        print("   ", end="")
        k=0
        while (k<self.c):
            print(k, end="     ")
            k+=1
        return ""

    def __add__(self, other):
        """
        It makes possible to add two differents matrix. It return a new matrix, istance of Matrix class.
        Matrix must have same rows and columns, if not, "None" is returned.
        """
        try:
            if self.r == other.r and self.c == other.c:
                C = Matrix([],self.r, self.c)
                for i in range(0, self.r):
                    for j in range(0, self.c):
                        #working with row i, column j
                        C.elem_change(i,j, self.elem(i,j) + other.elem(i, j))
                return C
            else:
                raise ValueError
        except Exception as e:
            print("Not possible to add two Matrix objects with different rows and columns")
            return None
        
    def __mul__(self, other):
        """
        Two possibilities: if 'other' is a number or if it is a matrix.
        - if other is a matrix, it uses the rule for this operation. So the operation returns the matrix obtained with the multiplication between matrix.
        - if other is not a matrix, but an integer or a floating point number, it multiplies every element of the matrix for the number.
        """
        #MATRIX * MATRIX
        if isinstance(self, Matrix) and isinstance(other, Matrix): #operation between Matrix and Matrix
            C = Matrix([], self.r, other.c) #create a matrix
            for i in range(0, C.r):
                for j in range(0, other.c):
                    sum_m = 0 #to store the sum
                    for k in range(0, self.c):
                        a_ik = self.matrix[i][k] #self.elem(i,k)
                        b_kj = other.matrix[k][j] #other.elem(k,j)
                        sum_m = sum_m + (a_ik * b_kj)
                    C.elem_change(i, j, sum_m)
            return C

        #MATRIX * NUMBER
        if isinstance(self, Matrix)==True and (isinstance(other, int) or isinstance(other, float))==True: #operation between int or float and Matrix
            C = Matrix([], self.r, self.c) #create a matrix
            for i in range(0, self.r):
                for j in range(0, self.c):
                    C.elem_change(i,j, 2*self.elem(i,j))
            return C
    def t(self):
        """
        The function returns a new matrix which is the transpose of the given matrix. The transpose matrix is define by definition as:
            With A as a matrix (Aij), A.t() is (tAij), so:
            tAij = Aji
        So the transpose switches the index of the original matrix. The new matrix is returned. Original matrix is not changed.
        """
        C = Matrix([], self.c, self.r) #because it will have switched self.matrix indices, c and r are switched.
        for i in range(0, self.r):
                for j in range(0, self.c):
                    C.elem_change(j,i, self.elem(i,j)) #Change C element with (j,i) from self.matrix. [Elements of C were originally set as 0 with declaration]
        return C


A = Matrix([1,2,3,4], 2, 2)
B = Matrix([4,3,2,1], 2, 2)
E = Matrix([1,2,3,4,5,6,7,8,9], 2,2)

#print(A)
#print("")
#print(B)
#print("Result")
print(E)
print(E.t())
print(E)

            
            
            
