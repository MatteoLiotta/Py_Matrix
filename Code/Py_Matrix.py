'''
Matrix module
'''

class Matrix():
    def __init__(self, values_list, rows=2, columns=2):
        """ The function build a Matrix object. It requires a dataset, in order to put values inside the matrix. It also requires rows and columns, to correctly divide the dataset in sub-lists.
            Function check: The dataset must respect the exaxt possible number; user must enter rows*columns elements. Error is raised.
            Dataset type must be a list. Error is eventually raised"""
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
                value_type!=False #the variable is set as False.
                raise TypeError
        except Exception as e:
            print("You must list type for the dataset. Error:", e)
            
        #Check: lenght of the dataset. Must be rows*columns or minus
        try:
            for i,e in enumerate(values_list):
                if type(e)!=int:
                    values_list[i]=0
            if value_type!=False: #so, it is a list
                if len(values_list)!=(rows*columns): #it is a list but it has not enough elements
                    values_list = values_list+[i for i in range(len(values_list, row*columns))] #do create a list, which has n-k elements - those that are missing
                    #raise ValueError
            else: #it is not a list or it is not correct. It creates a list
                values_list = [i for i in range(0, rows*columns)]
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
            
    def matrix_c(self):
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
        '''
        self.matrix = []
        cont = 0
        list_tmp = []
        matrix = []
        valoremin = 0
        valoremax = 0
        cicliannullamento = 0
        while(len(matrix)<self.r): #until the number of rows is not as declared
            if cont<self.c: #common case -> no cut
                cont+=1
                valoremax+=1
            else: #it has to cut the dataset
                valoremin = 0;
                valoremin = 0 + self.c*cicliannullamento;
                cicliannullamento += 1 #because it will cut. The counter has to be encreased.
                cont = 0 #reset the counter for the cut
                #matrix list - add the row
                matrix.append(self.divide_list(self.v, valoremin, valoremax ))
        return matrix #return the list created
    
    def __str__(self):
        """
        Function used to print a matrix in order to make it more pretty
        """
        for index,elem in enumerate(self.matrix): #for each row of the matrix
            print(index, end="| ")
            for r,j in enumerate(elem):
                #print("("+str(e)+","+str(r)+")", j, end="")
                print("%-5d"%(j), end=" ")        
            print("")
        print("   ", end="")
        print("-"*len(self.matrix)*2*5, end="\n")
        print("   ", end="")
        k=0
        while (k<self.c):
            print(k, end="     ")
            k+=1
        return ""

    
A = Matrix([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], 3, 5)
A_matrice = A.matrix

print(A)

            
            
            
