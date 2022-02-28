'''
#===================================================================================#
  Py_Matrix
  ==========
  Module for matrix creation and matrix manipulation.
  Matrix are made as object class while metods are for matrix calculus and properties.
|-----------------------------------------------------------------------------------|
  Project Repository on GitHub: https://github.com/MatteoLiotta/Py_Matrix
|-----------------------------------------------------------------------------------|
  Author: Matteo Liotta, 2022
|-----------------------------------------------------------------------------------|
  License: https://github.com/MatteoLiotta/Py_Matrix/blob/main/LICENSE
#===================================================================================#

LIST OF FUNCTIONS:
            - .matrix_c([elements], rows, columns):
                creates a matrix from a selected (if not, uses the self.v) dataset, number of rows and columns (if not selected, it uses self.r and self.c)
                
            - .__str__():
                print in a pretty and comprehensible way the matrix.
            - .elem(i,j):
            
                Return a specific element of the matrix. User has to choose row and column, then the element in that row and column is returned.
            - .elem_change(i,j, value):
                It changes a specific element of the matrix. User has to choose row and column, then the element in that row and column is changed whit the entered value.
                It is also possible to refer to the matrix as self.matrix[i][j], whitout using this function.
                
            - + :
                It makes possible to add two differents matrix. It return a new matrix, istance of Matrix class.
                Matrix must have same rows and columns
                [it returns a new Matrix object]
                
            - * :
                Two possibilities: if 'other' is a number or if it is a matrix.
                - if other is a matrix, it uses the rule for this operation. So the operation returns the matrix obtained with the multiplication between matrix.
                - if other is not a matrix, but an integer or a floating point number, it multiplies every element of the matrix for the number.
                [it returns a new Matrix object]
                
            - .t():
                The function returns a new matrix which is the transpose of the given matrix. The transpose matrix is define by definition as:
                    With A as a matrix (Aij), A.t() is (tAij), so:
                    tAij = Aji
                So the transpose switches the index of the original matrix. The new matrix is returned. Original matrix is not changed.
                
            - .elementary_op1(row1, row2):
                The function returns a Matrix where row1 and row2 of self are switched.
                It is the first elementary operation.
                
            - .elementary_op2(row, value):
                The function returns a Matrix where row1 of self is multiplied by a chosen number.
                It is the second elementary operation.
                
            - .elementary_op3(rowtochange, row, value):
                The function returns a Matrix where every element of rowtochange is added with a multiple (val) of the row entered.
                Value is required.
                It is the third elementary operation.

            - .elementary_op3_to0(rowtochange, row):
                The function returns a Matrix where every element of rowtochange is added with a multiple (val) of the row entered. The value is the one that makes the pivot 0.
                Value is not required.
                It is the third elementary operation used in the gaussian elimination
            
            - .sub(i,j):
                The function returns the submatrix obtained deleting the row "rowdeleted" and the column "column_deleted".
                The matrix avoid taking elements with row_deleted or column deleted ad indices.
                The submatrix number of row and coulmns is, if nxn, the sqrt of the number of rows (so elements of matrix list). If mxn, it is the number of rows and columns - 1.
                To unify cases, it will all be done in the second way.
                
            - det_nxn(matrix):
                The function returns the determinant of a matrix.
                The determinant is recursively obtained using Laplace Formula, as sum of multiplication between
                elements (i,j) and the cofactor(i,j).
                In case of a 1x1 matrix, is returned the element (0,0) of the matrix.
                
            - .cofactor(i,j):
                The function returns the cofactor of a matrix, using definition.
                
            - .cof_matrix():
                The function returns the cofactor of a matrix, using definition.
                
            - .inverse():
                Using the definition for the inverse of a matrix (tcof(A)*1/detA), the function returns the inverse of the matrix.
                
            - switch_columns(column, column):
                The function returns a matrix where the column_A of A is switched with columns_from_B of the matrix B
                
            - cramer_rule(Matrix, Matrix):
                For linear systems with square system matrix, without using invert matrix.
                Used the definition of the Cramer Rule for linear systems.
                
            - square_linear_systems(Matrix, Matrix):
                Use the function if you have to solve a linear system where A, matrix of the system, is a square matrix.
                It uses the definition: X = A^-1*B.
                The vector that solves the system is returned.
                
            - .info():
                The function print all relevant informations about the matrix:
                - rows
                - columns
                - transpose
                - if square
                    - determinant
                    - inverse matrix
                    - cofactor matrix
                    
            - .__iter__():
                The function let the matrix be iterable
                
            - .__next__():
                The function update the iterator and return the element self.elem(i,j)

            -  len(Matrix):
                The function returns the number of elements in the Matrix

            - .find_pivot(row):
                The function returns the pivot of a selected row. A pivot is the first element != 0 of a row.
                WARNING: i and j are not in the usual order. It is because i need to sort the list in other methods.

            - .pivot_list():
                The function return a list with all the pivots of the matrix and their indices. Example: [(j, i, val), (j2,i2, val2)...]
                WARNING: i and j are not in the usual order. It is because i need to sort the list in other methods.
            
            - .is_triangular():
                Check if the Matrix is or not triangular \|
                Being triangular means that the pivot in a low j must be in low i.
                It is not triangular if pivot are on the same column.
            
            - .sort()
                The function sort the matrix in order to make it triangular
                
            - .pivot_before(row):
                The function returns True if the pivot in the previous row is in the same column of the pivot of the selected row. Else: False.
            
            - .gaussian_elimination():
                The function returns a matrix where it was done the Gaussian Elimination.
'''

#==============#
# Class Matrix #
#==============#
class Matrix():

    #===================#
    # __init__() Method #
    #===================#
    def __init__(self, values_list=[], rows=2, columns=2):
        """ The function build a Matrix object. It requires a dataset, in order to put values inside the matrix. It also requires rows and columns, to correctly divide the dataset in sub-lists.
            Function check: The dataset must respect the exaxt possible number; user must enter rows*columns elements. Error is raised.
            Dataset type must be a list. Error is eventually raised.
        """
        #..............................#
        # Check rows and columns type: #
        #..............................#
        #I must check for the type of the input. Rows and Columns must be integer. If not, an error is not raised, they are set as 2 instead.
        
        if type(rows)!=int or type(columns)!=int: #their type must be integer. If not, are assigned as 2  
            rows=2
            columns=2
        else:
            pass
        
        #..............................#
        #       Check data type:       #
        #..............................#
        #The data, the list of element used in the matrix creation, must respect some rules:
        # - Must be a list 
        # - All the elements must be integers or float.
        #If not ok in some point, the current element is set as 0.

        #..............................#
        # Check if it is not a list:   #
        #..............................#
        #If not, a flag is 'activated'
        
        value_type = True #it is a list = True. Variable used for check the type of the dataset
        try:
            if type(values_list)!=list: #if it is not a list
                value_type=False #the variable is set as False.
                #raise TypeError
        except Exception as e:
            print("You must list type for the dataset. Error:", e)

        #................................#
        # Check lenght of the list data: #
        #................................#
        #Check: lenght of the dataset. Must be rows*columns or minus
        if value_type!=False: #so, it is a list
            for i,e in enumerate(values_list): #change values, if not correct
                #for every element
                    
                if type(e)!=int or type(e)==list: #check if it is not and integer
                    #...........................................#
                    # If element is not a int? if it is a list? #
                    #...........................................#
                        
                    if type(e) == float:
                        #..............................#
                        # It may be a float. If it is: #
                        #..............................#
                        pass
                        #No prolem
                    else:
                        #......................#
                        # Not int, not a float #
                        #......................#

                        if isinstance(e, str):
                            #..............................#
                            # It may be a float in str:    #
                            #..............................#
                            if "." in e:
                                try:
                                    values_list[i] = float(e)
                                    continue
                                except:
                                    values_list[i]=0 #it is changed in 0
                                    continue

                            #..............................#
                            # It may be an integer in str: #
                            #..............................#
                            if not "." in e:
                                try:
                                    values_list[i] = int(e)
                                    continue
                                except:
                                    values_list[i]=0 #it is changed in 0
                                    continue

                            #........................#
                            # Can't help it no more  # [Must be set as 0]
                            #........................#
                            else:
                                values_list[i] = 0
                                continue
                                
                        if isinstance(e, list):
                            #..........................................#
                            # It may be a number in str in len=1 list: #
                            #..........................................#
                            if len(e) == 1 and isinstance(e[0], str):
                                if "." in e[0]:
                                    try:
                                        values_list[i] = float(e[0])
                                        continue
                                    except:
                                        values_list[i]=0 #it is changed in 0
                                        continue

                                if not "." in e:
                                    try:
                                        values_list[i] = int(e[0])
                                        continue
                                    except:
                                        values_list[i]=0 #it is changed in 0
                                        continue
                                        
                            #...................................#
                            # It may be a number in len=1 list: #
                            #...................................#
                            if len(e) == 1 and isinstance(e[0], int):
                                #................#
                                # If an integer: #
                                #................#
                                values_list[i] = int(e[0])
                                continue
                                
                            if len(e) == 1 and isinstance(e[0], float):
                                #.............#
                                # If a float: #
                                #.............#
                                values_list[i] = float(e[0])
                                continue
                            else:
                                values_list[i] = 0
                        else:
                            values_list[i] = 0

                            
            if len(values_list)!=(rows*columns): #it is a list but it has not enough elements
                #...............................#
                # Not enought elements in data: #
                #...............................#
                #I must add the number of elements that are required (Based on the number of rows and columns
                #If it is like [1,2] with rows: 2, columnss: 2 --> [0,0] ==> [1,2] + [0,0] = [1,2,0,0] ==> Ok!
                    
                adding_list = []
                for t in range(len(values_list), rows*columns): #For (rows*columns - len( 'data' )) times
                    adding_list.append(0) #append 0 to the tmp list

                #Once built the list, append it to dataset
                values_list = values_list+adding_list #do create a list, which has n-k elements - those that are missing
                    
                
        else: #it is not a list or it is not correct. It creates a list
            #.................................#
            # Not a list. Create a list of 0: #
            #.................................#
            adding_list = []
            for t in range(0, rows*columns): #for rows*columns times add 0 to the tmp list
                adding_list.append(0)
            values_list = adding_list #dataset is [0,0,0,0,...,0]
        
        #....................................#
        # Once all corrected: SELF VARIABLES #
        #....................................#
        #after all the data-check, it is possible to create the self variables.
        self.v = values_list
        self.r = rows
        self.c = columns
        self.matrix = self.matrix_c()

        #.............................#
        # Something more: Determinant #
        #.............................#
        #determinant
        self.det = det_nxn(self)


    #========================================#
    # CREATE A MATRIX: step 2) Divide a list #
    #========================================#   
    def divide_list(self, lista, minimo, massimo):
        '''
        Used to create lists for matrix rows
        '''
        list = []
        for i in range(minimo, massimo):
            list.append(lista[i])
        return list

    #=================#
    # CREATE A MATRIX #
    #=================#      
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
                    1  2  3 ||  4   5  6 || 7   8  9
            index   0  1  2 ||  3   4  5 || 6   7  8
            so:     0          0+c         0+c+c
        Then valoremin (minimum) is the 0 at the beginning, and valoremax (maximum) is exactly 3, as the counter cont. Divide_list cuts from 0 to 3-1 (range excludes 1)
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

        if r_chosen == 1 or c_chosen == 1: #if there is just a row or a column
            if r_chosen ==1 and c_chosen == 1: #if it is 1x1
                return [[self.v[0]]]
            
        #======== Usefull Variables ==========#
        self.matrix = []
        cont = 0
        list_tmp = []
        matrix = []
        valoremin = 0
        valoremax = 0
        cicliannullamento = 0
        #=====================================#

        
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


    #======================================#
    # Get a specific element of the matrix #
    #======================================#
    def elem(self, i, j):
        """
        Return a specific element of the matrix. User has to choose row and column, then the element in that row and column is returned.
        """
        elem=self.matrix[i][j] #select the element j in row i
        return elem #return that element

    #=========================================#
    # CHANGE a specific element of the matrix #
    #=========================================#
    def elem_change(self, i, j, value):
        """
        It changes a specific element of the matrix. User has to choose row and column, then the element in that row and column is changed whit the entered value.
        It is
        """
        self.matrix[i][j]=value
        return self

    def update_matrix(self):
        matx_list = [i for i in self]
        return Matrix(matx_list, self.r, self.c)
            
    #==================#
    # PRINT the matrix #
    #==================#
    def __str__(self):
        """
        Function used to print a matrix in order to make it more pretty
        """
        self.string = ""
        if len(self.matrix)>1: #it must have at least 2 rows.
            #......................................#
            # If the len of the list of list is >1 # [It has at least 2 rows]
            #......................................#

            for i in range(0, self.r): #For all the rows: (Not used list iteration cause the self.matrix is not always updated. Must b fixed)
                #print(i, end="| ") #Print the beginning, like: 1|
                self.string += "{}| ".format(i) 
                for j in range(0, self.c): #For all the elements in each row
                    if j == self.c -1:
                        #...............................#
                        # If it is the last of the line # [It should not have the 5 spaces]
                        #...............................#
                        if type(self.elem(i,j))==float:
                            #.............................#
                            # If an element is a float:   #
                            #.............................#
                            #print("%-5.3f" %(self.matrix[i][j]), end=" ")
                            self.string +="%.3f"%self.matrix[i][j]
                        else:
                            #.....................#
                            # If it is a integer: #
                            #.....................#
                            #print("%-5d" %(self.matrix[i][j]), end=" ")
                            self.string +="%d"%self.matrix[i][j]
                    else:
                        if type(self.elem(i,j))==float:
                            #.............................#
                            # If an element is a float:   #
                            #.............................#
                            #print("%-5.3f" %(self.matrix[i][j]), end=" ")
                            self.string +="%-5.3f "%self.matrix[i][j]
                        else:
                            #.....................#
                            # If it is a integer: #
                            #.....................#
                            #print("%-5d" %(self.matrix[i][j]), end=" ")
                            self.string +="%-5d "%self.matrix[i][j]
                        
                #print("") # Go to the next line
                self.string +="\n"
                
            #print("   ", end="") #Create space between columns indices.
            self.string +="   "

            #........................................#
            # Columns Indices at the end and spaces: #
            #........................................#
            #=== Spaces and lines ===#
            for u in range(0, self.c):
                if u == self.c -1: #If it is the last one it should not have spaces
                    self.string +="--"
                    break #the subsequent line is avoided
                #print("--"+4*" ", end="")
                self.string +="--    "
            #print("")
            self.string +="\n"
            #print("   ", end="")
            self.string +="   "
            k=0

            #=== Numbers and indices ===#
            while (k<self.c):
                if k==self.c -1: #If it is the last one it should not have spaces
                    self.string += "{}".format(k)
                    break #the subsequent lines are avoided
                #print(k, end="     ")
                self.string += "{}     ".format(k)
                k+=1
            #print("")
            self.string += "\n"

            #print(self.string)
            return self.string

        
        else: #it only has a row. So, it is like: [[a,b,c,d,...,z]]
            #...................................#
            # There is only a row in the matrix #
            #...................................#
            #print("0|", end =" ")
            self.string += "0| "
            for j in range(0, self.c): #Must only iterate on the number of columns. Row == 1
                if j == self.c -1:
                    #...............................#
                    # If it is the last of the line # [It should not have the 5 spaces]
                    #...............................#
                    if type(self.elem(0,j))==float:
                        #.............................#
                        # If an element is a float:   #
                        #.............................#
                        #print("%-5.3f" %(self.matrix[i][j]), end=" ")
                        self.string +="%.3f"%self.matrix[0][j]
                    else:
                        #.....................#
                        # If it is a integer: #
                        #.....................#
                        #print("%-5d" %(self.matrix[i][j]), end=" ")
                        self.string +="%d"%self.matrix[0][j]
                else:
                    if type(self.elem(0,j))==float:
                        #.............................#
                        # If an element is a float:   #
                        #.............................#
                        #print("%-5.3f" %(self.matrix[i][j]), end=" ")
                        self.string +="%-5.3f "%self.matrix[0][j]
                    else:
                        #.....................#
                        # If it is a integer: #
                        #.....................#
                        #print("%-5d" %(self.matrix[i][j]), end=" ")
                        self.string +="%-5d "%self.matrix[0][j]

            #........................................#
            # Columns Indices at the end and spaces: #
            #........................................#
            #=== Spaces and lines ===#
            #print("")
            self.string += "\n"
            #print("   ", end="")
            self.string += "   "
            for u in range(0, self.c):
                if u == self.c -1: #If it is the last one it should not have spaces
                    self.string +="--"
                    break #the subsequent line is avoided
                #print("--"+4*" ", end="")
                self.string +="--    "
            #print("")
            self.string +="\n"
            #print("   ", end="")
            self.string +="   "
            k=0

            #=== Numbers and indices ===#
            while (k<self.c):
                #print(k, end="     ")
                if k==self.c -1: #If it is the last one it should not have spaces
                    self.string += "{}".format(k)
                    break #the subsequent lines are avoided
                self.string += "{}     ".format(k)
                k+=1
            #print("")
            self.string += "\n"
            return self.string

    #=======================#
    # __add__() Method: SUM #
    #=======================#       
    def __add__(self, other):
        """
        It makes possible to add two differents matrix. It return a new matrix, istance of Matrix class.
        Matrix must have same rows and columns, if not, "None" is returned.
        """
        #....................................#
        # Check if they are Matrix instances #
        #....................................#
        if not isinstance(self, Matrix) or not isinstance(other, Matrix): #operation between Matrix and Matrix
            return None
        
        #.............................................#
        # If it is possible to sum element by element #
        #.............................................#
        try:
            #................................................#
            # If the number of rows and columns are the same #
            #................................................#
            if self.r == other.r and self.c == other.c:
                #=== Instance ===#
                C = Matrix([],self.r, self.c)
                #================#

                for i in range(0, self.r): #for every row
                    for j in range(0, self.c): #for every columns (elements of rows)
                        #............................................................#
                        # Change the current element with the sum of the ij elements #
                        #............................................................#
                        C.elem_change(i,j, self.elem(i,j) + other.elem(i, j))
                        
                #=== Once done, return the Matrix ===#
                return C.update_matrix() #To be sure, instead of C, it returns a matrix instance
                #====================================#
            #................................................#
            # If the number of rows and columns are the same #
            #................................................#
            else:
                raise ValueError
                #An exception is raised
            
        except Exception as e:
            print("Not possible to add two Matrix objects with different rows and columns")
            return None #None is returned.
        
    #==================================#
    # __mul__() Method: MULTIPLICATION # [Between Matrix and Matrix or Matrix and a number]
    #==================================#
    def __mul__(self, other):
        """
        Two possibilities: if 'other' is a number or if it is a matrix.
        - if other is a matrix, it uses the rule for this operation. So the operation returns the matrix obtained with the multiplication between matrix.
        - if other is not a matrix, but an integer or a floating point number, it multiplies every element of the matrix for the number.
        """
        #-----------------#
        # MATRIX * MATRIX #
        #-----------------#        
        if isinstance(self, Matrix) and isinstance(other, Matrix): #operation between Matrix and Matrix
            if self.c == other.r:
                #=== Instance ===#
                C = Matrix([], self.r, other.c) #create a matrix
                #================#
                for i in range(0, C.r): #for every row
                    for j in range(0, other.c): # for each column
                        sum_m = 0 #to store the sum.

                        #Another iteration on columns
                        #.....................................#
                        # Matrix multiplication by definition #
                        #.....................................#
                        for k in range(0, self.c):
                            a_ik = self.elem(i,k)
                            b_kj = other.elem(k,j)
                            sum_m = sum_m + (a_ik * b_kj)
                        #=== Update elements of the Instance ===#
                        C.elem_change(i, j, sum_m)
                        #=======================================#
                #Once done, return
                return C.update_matrix() #To be sure, instead of C, it returns a matrix instance
            else:
                print("Must respect columns and rows rule. A*B is possible if A.c == B.r. None is returned")
                return None

        #-----------------#
        # MATRIX * NUMBER #
        #-----------------#  
        if isinstance(self, Matrix) and (isinstance(other, int) or isinstance(other, float)): #operation between Matrix and (int or float)

            #=== Instance ===#
            C = Matrix([], self.r, self.c) #create a matrix
            #================#
            for i in range(0, self.r): #For each row
                for j in range(0, self.c): #Iteration on elements of the row
                    #............................................#
                    # Matrix scalar multiplication by definition # [Each element is multiplied by the number]
                    #............................................#
                    C.elem_change(i,j, other*self.elem(i,j))
            return C.update_matrix() #To be sure, instead of C, it returns a matrix instance

    #==================#
    # Transpose Matrix #
    #==================#
    def t(self):
        """
        The function returns a new matrix which is the transpose of the given matrix. The transpose matrix is define by definition as:
            With A as a matrix (Aij), A.t() is (tAij), so:
            tAij = Aji
        So the transpose switches the index of the original matrix. The new matrix is returned. Original matrix is not changed.
        """
        #=== Instance ===#
        C = Matrix([], self.c, self.r) #because it will have switched self.matrix indices, c and r are switched.
        #================#

        for i in range(0, self.r):
                for j in range(0, self.c):
                    #..........................................................#
                    # Transpose Matrix by definition - Change (i,j) with (j,i) #
                    #..........................................................#
                    C.elem_change(j,i, self.elem(i,j)) #Change C element with (j,i) from self.matrix. [Elements of C were originally set as 0 with declaration]
        return C.update_matrix() #To be sure, instead of C, it returns a matrix instance

    #=========================#
    # ELEMENTARY OPERATION: 1 # [Switch]
    #=========================#
    def elementary_op1(self, row1, row2):
        """
        The function returns a Matrix where row1 and row2 of self are switched.
        It is the first elementary operation.
        """
        #=== Instance ===#
        C = Matrix([], self.r, self.c)
        #================#

        #.............................#
        # Create a copy of the matrix #
        #.............................#
        for i in range(0, self.r):
            for j in range(0, self.c):
                C.elem_change(i, j, self.elem(i,j))
        #C is now a copy of the A Matrix.
 
        hold = C.matrix[row1] #hold the row not to be deleted
        C.matrix[row1] = C.matrix[row2] #changes the rows
        C.matrix[row2] = hold
        
        return C.update_matrix() #To be sure, instead of C, it returns a matrix instance

    #=========================#
    # ELEMENTARY OPERATION: 2 # [Multiply by a number]
    #=========================#
    def elementary_op2(self, row, val):
        """
        The function returns a Matrix where row1 of self is multiplied by a chosen number.
        It is the second elementary operation.
        """
        #=== Instance ===#
        C = Matrix([], self.r, self.c)
        #================#

        #.............................#
        # Create a copy of the matrix #
        #.............................#
        for i in range(0, self.r):
            for j in range(0, self.c):
                C.elem_change(i, j, self.elem(i,j))
        #C is now a copy of the A Matrix.

        for j in range(0, self.c): #for each column
            C.elem_change(row, j, val*C.elem(row, j)) #Multiply all elements by a value
            
        return C.update_matrix() #To be sure, instead of C, it returns a matrix instance

    #=========================#
    # ELEMENTARY OPERATION: 3 # [Add a multiple of a row element by element]
    #=========================#
    def elementary_op3(self, rowtochange, row, val):
        """
        The function returns a Matrix where every element of rowtochange is added with a multiple (val) of the row entered.
        Value is required.
        It is the third elementary operation.

        Example:
        0| 1     2     
        1| 3     4     
           --    --    
           0     1
        >>> A.elementary_op3(0,1,-3)
        Then:
        0| 1           2     
        1| 3+(1)*(-3)  4+(2)*(-3)
           --          --    
           0           1
        Output:
        0| 1     2     
        1| 0     -2    
           --    --    
           0     1
        """
        #=== Instance ===#
        C = Matrix([], self.r, self.c)
        #================#
        #.............................#
        # Create a copy of the matrix #
        #.............................#
        for i in range(0, self.r):
            for j in range(0, self.c):
                C.elem_change(i, j, self.elem(i,j))
        #C is now a copy of the A Matrix.

        for j in range(0, self.c):
            C.elem_change(rowtochange, j, (self.elem(rowtochange, j) + self.elem(row,j)*val))
        return C.update_matrix() #To be sure, instead of C, it returns a matrix instance

    #=========================#
    # ELEMENTARY OPERATION: 3 # [Operation 3 in order to obtain 0 in the rowtochange as value under the pivot of row]
    #=========================#
    def elementary_op3_to0(self, rowtochange, row):
        '''
        The function returns a Matrix where every element of rowtochange is added with a multiple (val) of the row entered. The value is the one that makes the pivot 0.
        Value is not required.
        It is the third elementary operation used in the gaussian elimination
        '''
        #=== Instance ===#
        C = Matrix([], self.r, self.c)
        #================#

        #.............................#
        # Create a copy of the matrix #
        #.............................#
        for i in range(0, self.r):
            for j in range(0, self.c):
                C.elem_change(i, j, self.elem(i,j))
        #C is now a copy of the A Matrix.

        a = self.find_pivot(rowtochange)[0]
        b = self.find_pivot(row)[0]
        c = self.find_pivot(row)[2]
        d = self.find_pivot(rowtochange)[2]
        if a == b:
            if (d>0 and c>0) or (d<0 and c<0):
                for j in range(0, self.c):
                    C.elem_change(rowtochange, j, (self.elem(rowtochange, j) - self.elem(row,j)*d/c))
                return C.update_matrix() #To be sure, instead of C, it returns a matrix instance
            else:
                for j in range(0, self.c):
                    C.elem_change(rowtochange, j, (self.elem(rowtochange, j) - self.elem(row,j)*d/c))
                return C.update_matrix() #To be sure, instead of C, it returns a matrix instance
        else:
            return C.update_matrix() #To be sure, instead of C, it returns a matrix instance

    #===========#
    # Submatrix #
    #===========#
    def sub(self, row_deleted, column_deleted):
        """
        The function returns the submatrix obtained deleting the row "rowdeleted" and the column "column_deleted".
        The matrix avoid taking elements with row_deleted or column deleted ad indices.
        The submatrix number of row and coulmns is, if nxn, the sqrt of the number of rows (so elements of matrix list). If mxn, it is the number of rows and columns - 1.
        To unify cases, it will all be done in the second way.
        """

        list_sub = [] #list to store the elements
        for i in range(0, self.r):
            for j in range(0, self.c):
                if i != row_deleted and j != column_deleted: #avoiding 'deleted' row and column elements
                    list_sub.append(self.elem(i,j)) #append to the list
        #=== Instance ===#
        C = Matrix(list_sub, self.r-1, self.c-1)
        #================#
        return C.update_matrix() #To be sure, instead of C, it returns a matrix instance

    #======================#
    # Cofactor of a Matrix #
    #======================#
    def cofactor(self, row, column):
        """
        The function returns the cofactor of a matrix, using definition.
        """
        return ((-1)**(row+column))*det_nxn(self.sub(row,column))

    #=================#
    # Cofactor Matrix #
    #=================#
    def cof_matrix(self):
        """
        The function return the cofactor matrix, obtained changing each element (i,j) with the cofactor (i,j).
        It uses the cofactor matrix definition.
        """
        #=== Instance ===#
        C = Matrix([], self.r, self.c)
        #================#
        for i in range(self.r):
            for j in range(self.c):
                C.elem_change(i,j, self.cofactor(i,j)) #create a matrix where each element is the relative cofactor.
        return C.update_matrix() #To be sure, instead of C, it returns a matrix instance

    #================#
    # Inverse Matrix #
    #================#
    def inverse(self):
        """
        Using the definition for the inverse of a matrix (tcof(A)*1/detA), the function returns the inverse of the matrix
        """
        if self.det!=0:
            #.............................#
            # If the determinant is not 0 #
            #.............................#
            C = self.cof_matrix() #C is the cofactor matrix of matrix A
            tC = C.t() #tC is the transpose of the cofactor matrix of matrix A
            a = 1/self.det #to store the reciprocal value of the determinant
            for i in range(self.r):
                for j in range(self.c):
                    #tC.elem_change(i,j,tC.elem(i,j)*a) #multiply the tC by a
                    tC = tC * a
            return tC.update_matrix() #To be sure, instead of tC, it returns a matrix instance
        return None

    #==============================#
    # Information about the matrix #
    #==============================#
    def info(self):
        """
        The function print all relevant informations about the matrix.
        In particular:
        - rows
        - columns
        - transpose
        - if square
            - determinant
            - inverse matrix
            - cofactor matrix
        """
        print("MATRIX")
        print(self)
        print("-> Rows:", self.r)    
        print("-> Columns:", self.c)
        print("-> Transpose Matrix:")
        print(self.t())
        if self.r == self.c: #square
            print("-> Determinant:", self.det)
            print("-> Inverse:")
            print(self.inverse())
            print("-> Cofactor Matrix:")
            print(self.cof_matrix())
        return None

    #==============================#
    # __iter__() Method: Iteration #
    #==============================# 
    def __iter__(self):
        '''It makes the matrix iterable'''
        self.iter_i=0
        self.iter_j=0
        return self

    #==============================#
    # __next__() Method: Iteration #
    #==============================#      
    def __next__(self):
        '''It returns the element and update the iterator'''
        if self.iter_i<self.r: #check for possible errors
            #...........................#
            # Result (will be returned) #
            #...........................#
            result = self.elem(self.iter_i, self.iter_j) #the result is the element in the relative row and column

            #.........................#
            # Ready for the next call #
            #.........................#
            self.iter_j+=1 #while result stores the element, I must prepare the iterator for the next call. Add 1 to the column iterator
            #.........................#
            # Must go in the next row #
            #.........................#
            if self.iter_j>=self.c: #if bigger or equal to the number of columns - so it reaches the end of the row
                self.iter_i+=1 #change row
                self.iter_j=0 #go back to 0
            return result #when everything is ready, return
        else:
            #..............................#
            # No more rows - STOPITERATION #
            #..............................#
            raise StopIteration #if in the next iteration the number of rows is wrong, stop the iteration

    #=================================#
    # __len__() Method: Matrix length #
    #=================================# 
    def __len__(self):
        ''' The function returns the number of elements of the matrix '''
        number = 0
        for i in self:
            number+=1
        return number

    #GAUSSIAN ELIMINATION and PIVOT
    
    #==================================#
    # Find the pivot of a selected row #
    #==================================# 
    def find_pivot(self, row):
        '''The function returns the pivot of the selected row.

           WARNING: i and j are not in the usual order. It is because i need to sort the list in other methods.
        '''
        for i,e in enumerate(self.matrix[row]): #the matrix is a list of lists
            if e == 0: #if the element is a 0, nothing to do
                continue
            else: #if there is a value != 0, it is a pivot. It returns.
                return (i, row, e)
        return None #If here, there is no pivot for that row

    #========================#
    # Pivot list of a matrix #
    #========================# 
    def pivot_list(self):
        '''The function return a list with all the pivots of the matrix and their indices. Example: [(j, i, val), (j2,i2, val2)...]
           WARNING: i and j are not in the usual order. It is because i need to sort the list in other methods.
        '''
        pivot_list = []
        for i,e in enumerate(self.matrix):#for every row
            pivot_list.append(self.find_pivot(i)) #add to the list the pivot of the row i
        return pivot_list

    #=================================#
    # Is the matrix upper triangular? #
    #=================================# 
    def is_triangular(self):
        '''Check if the Matrix is or not triangular \|
           Being triangular means that the pivot in a lower j must be in low i.
           It is not triangular if pivot are on the same column.
        '''
        # Example: [(0, 0, 10), (1, 0, 7), (2, 2, 15), (3, 0, 125), (4, 0, 5642)]
        j_list = []
        for i in self.pivot_list():
            #for every pivot:
            #extract the j's
            j_list.append(i[1])
        #now I have all the j

        # now I sort it. If the result is different, it is not triangular.
        new_list = sorted(j_list)
        
        if sum(j_list) == j_list[0]*len(j_list): #It must not have same elements!!!
            return False

        for i in j_list:
            number = j_list.count(i)
            if number >1:
                return False
        
        return j_list==new_list #True or False

    #===========================================#
    # Sort a matrix to make it upper triangular #
    #===========================================# 
    def sort(self):
        ''' The function sort the matrix in order to make it triangular'''
        #=== Instance ===#
        C = Matrix([],self.r, self.c)
        #================#

        #.............................#
        # Create a copy of the matrix #
        #.............................#
        for i in range(self.r):
            for j in range(self.c):
                C.elem_change(i,j, self.elem(i,j))

        list_pivot = self.pivot_list()
        
        try:
            #...................................................#
            # If it is possible to sort, obtain the sorted list #
            #...................................................#
            sorted_list = sorted(list_pivot)
        except:
            #...............................#
            # If it is not possible to sort #
            #...............................#
            print("Sorry. Not Possible")
            return None
        
        number = 0
        for i,e in enumerate(sorted_list):
            #...........................................#
            # For each element of the sorted pivot list #
            #...........................................#
            index = list_pivot.index(e)
            if index != i:
                number = number +1
                #........................#
                # Elementary operation 1 #
                #........................#
                C = C.elementary_op1(index, i)
                
                hold = list_pivot[index]
                list_pivot[index] = list_pivot[i]
                list_pivot[i] = hold
                
        return C.update_matrix() #To be sure, instead of C, it returns a matrix instance

    #========================================================================#
    # There is a pivot in the same column in two subsequent rows? True/False #
    #========================================================================# 
    def pivot_before(self, row):
        '''The function returns True if the pivot in the previous row is in the same column of the pivot of the selected row. Else: False.'''
        #..........................#
        # If there is only one row #
        #..........................#
        if row==0: return False
        else:
            #.....................#
            # If there are 2 rows #
            #.....................#
            j_pivot = self.find_pivot(row)[0] #in the tuple take the j
            j_pivot_before = self.find_pivot(row-1)[0]#in the row before, look where the pivot is
            
            if j_pivot == j_pivot_before:
                #.............................#
                # If the columns are the same #
                #.............................#
                return True
            else:
                #..................................................#
                # If the columns are the same or the pivot is None #
                #..................................................#
                return False

    #===========================================================#
    # GAUSSIAN ELIMINATION - Matrix --> Upper Triangular Matrix #
    #===========================================================# 
    def gaussian_elimination(self):
        '''
        The function returns a matrix where it was done the Gaussian Elimination.
        '''
        #=== Instance ===#
        C = Matrix([],self.r, self.c)
        #================#

        #.............................#
        # Create a copy of the matrix #
        #.............................#
        for i in range(self.r):
            for j in range(self.c):
                C.elem_change(i,j, self.elem(i,j))
        
        try:
            #......................................#
            # If possible to sort, sort the matrix #
            #......................................#
            C = C.sort()
            for j in range(self.c):
                for i in range(self.r): #for every row
                    #.............................#
                    # For each element of the row #
                    #.............................#
                    if C.pivot_before(i) == True:
                        #..............................................................#
                        # If there is a pivot in the same column of the subsequent row #
                        #..............................................................#
                        C = C.elementary_op3_to0(i, i-1)
                        C = C.sort()
                        
            return C.update_matrix() #To be sure, instead of C, it returns a matrix instance
        
        except:
            #......................#
            # If an error occurred #
            #......................#
            print("Sorry. Not Possible")
            return None



#DETERMINANT

#=============================#
# Determinant of a 2x2 Matrix #
#=============================#
def det_2x2(mat):
    """
    The function returns the determinant of a matrix 2x2.
    It is used as the base case in the recursion for the nxn determinant.
    A control is implemented: matrix must be a square matrix and must be 2x2.
    """
    if isinstance(mat, Matrix): #mat must be a Matrix
        if mat.c==mat.r and mat.c == 2: #mat must be 2x2
            #......................#
            # If the matrix is 2x2 #
            #......................#
            #Using the definition:
            det_mat = 1*(mat.elem(0,0)*mat.elem(1,1)) + (-1)*(mat.elem(1,0)*mat.elem(0,1))
            return det_mat
        else:
            #print("Matrix must be 2x2")
            return None
    else:
        #print("Not a Matrix")
        return None

#=============================#
# Determinant of a nxn Matrix #
#=============================#
def det_nxn(mat):
    """
    The function returns the determinant of a matrix.
    The determinant is recursively obtained using Laplace Formula, as sum of multiplication between
    elements (i,j) and the cofactor(i,j).

    In case of a 1x1 matrix, is returned the element (0,0) of the matrix.
    """
    if isinstance(mat, Matrix): #mat must be a matrix
        if mat.c == mat.r: #mat must be a square matrix
            #...............................#
            # If the matrix a square matrix #
            #...............................#

            #=== BASE CASE ===#
            if mat.c == 2: return det_2x2(mat) #BASE CASE for the recursion
            if mat.c == 1: return int(mat.elem(0,0)) #if 1x1, the determinant is a number: it is the element of the 1x1 matrix
            #=================#

            #=== RECURSION ===#
            else:
                somma = 0
                i = 0
                #...........................................#
                # Iteration - j from 0 to number of columns #
                #...........................................#
                for j in range (0, mat.c): #Iteration: row = 0, column = (0 to self.c-1)
                    #.................#
                    # Laplace Formula #
                    #.................#
                    C = mat.sub(i,j) #C is a submatrix obtained deleting the row i and column j
                    add = mat.elem(i, j)*((-1)**(i+j))*det_nxn(C) #cofactor calcolus, used in the following expression
                    #--- add the result to the variable ---#
                    somma = somma + add

                #...............................................#
                # Once finished the iteration, return the value #
                #...............................................#
                return somma
            #=================#
        else:
            #print("Matrix is not a square matrix")
            return None
    else:
        #print("Not a matrix")
        return None

#LINEAR SYSTEMS
def switch_columns(A,B, column_A, column_from_B):
    """
    The function returns a matrix where the column_A of A is switched with columns_from_B of the matrix B
    """
    if isinstance(A, Matrix) and isinstance(B, Matrix):
        if A.r == B.r:
            #.......................................#
            # If A has the same number of rows of B #
            #.......................................#
            #=== Instance ===#
            C = Matrix([], A.r, A.c)
            #================#

            #.............................#
            # Create a copy of the matrix #
            #.............................#
            for i in range(A.r):
                for j in range(A.c):
                    C.elem_change(i,j,A.elem(i,j))
            
            for i in range(A.r):
                for j in range(A.c):
                    if j == column_A:
                        #...........................#
                        # If in the selected column #
                        #...........................#
                        C.elem_change(i,j, B.elem(i, column_from_B))
                        
            return C.update_matrix() #To be sure, instead of C, it returns a matrix instance
        
        else:
            #Not possible to switch
            return None
    else:
        #Not a matrix
        return None

def cramer_rule(A,B):
    """
    For linear systems with square system matrix, without using invert matrix.
    Used the definition of the Cramer Rule for linear systems.
    """
    if isinstance(A, Matrix) and isinstance(B, Matrix):
        if A.det!=0 and B.c==1 :
            #........................................#
            # If det of A is not 0 and B is a column #
            #........................................#
            #=== Instance ===#
            C = Matrix([], A.r, A.c)
            #================#

            #.............................#
            # Create a copy of the matrix #
            #.............................#
            for i in range(A.r):
                for j in range(A.c):
                    C.elem_change(i,j,A.elem(i,j))
            
            #for each column
                    
            #..........................................#
            # Obtaining the dataset for the new matrix #
            #..........................................#
            list_x = []
            for j in range(A.c):
                a = switch_columns(A,B, j, 0) #a is the matrix obtained switching the j row of A, whit B
                list_x.append((det_nxn(a)/A.det)) #x_i is det(a)/det(A) for all i
                
            #=== Instance ===#
            X = Matrix(list_x, A.r, 1) #X is the matrix made of the results obtained during the iteration
            #================#
            return X.update_matrix() #To be sure, instead of X, it returns a matrix instance
        else: return None #Not possible
    else: return None #Not a matrix

def square_linear_system(A,B):
    """
    Use the function if you have to solve a linear system where A, matrix of the system, is a square matrix.
    It uses the definition: X = A^-1*B.
    The vector that solves the system is returned.
    """
    if isinstance(A, Matrix) and isinstance(B, Matrix):
        if A.det!=0 and B.c ==1:
            Ai = A.inverse()
            #=== Rule: X=A^-1 * B ===#
            X = Ai * B
            #========================#
            return X.update_matrix() #To be sure, instead of X, it returns a matrix instance
