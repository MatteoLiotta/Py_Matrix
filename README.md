# Py_Matrix
> Module for matrix creation and matrix manipulation. Programming Language: Python.

![image](https://github.com/MatteoLiotta/Py_Matrix/blob/main/Picture%20(For%20Readme%20file)/Py_Matrix%20image.png)

|`Project Repository` on GitHub: https://github.com/MatteoLiotta/Py_Matrix|
|----------------------------------------------------------------------------------------|
|`Author`: Matteo Liotta, 2022|
|`File`: [Py_Matrix.py](https://github.com/MatteoLiotta/Py_Matrix/blob/main/Code/Py_Matrix.py)|
|`License`: [License](https://github.com/MatteoLiotta/Py_Matrix/blob/main/LICENSE)|


#### LIST OF FUNCTIONS:

##### Matrix

 >- **.matrix_c(\[elements\], rows, columns):**\
 >   creates a matrix from a selected (if not, uses the self.v) dataset, number of rows and columns (if not selected, it uses self.r and self.c)

>- **.\_\_str\_\_():**\
>   print in a pretty and comprehensible way the matrix.

> - **.elem(i,j):**\
>    Return a specific element of the matrix. User has to choose row and column, then the element in that row and column is returned.

> - **.elem_change(i,j, value):**\
>    It changes a specific element of the matrix. User has to choose row and column, then the element in that row and column is changed whit the entered value.
>    It is also possible to refer to the matrix as self.matrix[i][j], whitout using this function.

>- **+ :**\
>    It makes possible to add two differents matrix. It return a new matrix, istance of Matrix class.
>    Matrix must have same rows and columns
>    \[it returns a new Matrix object\]

>- **\* :**\
>    Two possibilities: if 'other' is a number or if it is a matrix.
>   - if other is a matrix, it uses the rule for this operation. So the operation returns the matrix obtained with the multiplication between matrix.
>   - if other is not a matrix, but an integer or a floating point number, it multiplies every element of the matrix for the number.
>     \[it returns a new Matrix object\]

>- **.t():**\
>    The function returns a new matrix which is the transpose of the given matrix. The transpose matrix is define by definition as:
>    With A as a matrix (Aij), A.t() is (tAij), so:
>    tAij = Aji
>    So the transpose switches the index of the original matrix. The new matrix is returned. Original matrix is not changed.

>- **.elementary_op1(row1, row2):**\
>    The function returns a Matrix where row1 and row2 of self are switched.
>    It is the first elementary operation.

>- **.elementary_op2(row, value):**\
>    The function returns a Matrix where row1 of self is multiplied by a chosen number.
>    It is the second elementary operation.
 
>- **.elementary_op3(rowtochange, row, value):**\
>    The function returns a Matrix where every element of rowtochange is added with a multiple (val) of the row entered.
>    Value is required.
>    It is the third elementary operation.

>- **.sub(i,j):**\
>    The function returns the submatrix obtained deleting the row "rowdeleted" and the column "column_deleted".
>    The matrix avoid taking elements with row_deleted or column deleted ad indices.
>    The submatrix number of row and coulmns is, if nxn, the sqrt of the number of rows (so elements of matrix list). If mxn, it is the number of rows and columns - 1.
>    To unify cases, it will all be done in the second way.
 
>- **det_nxn(Matrix):**\
>   The function returns the determinant of a matrix.
>   The determinant is recursively obtained using Laplace Formula, as sum of multiplication between
>   elements (i,j) and the cofactor(i,j).
>   In case of a 1x1 matrix, is returned the element (0,0) of the matrix.

>- **.cofactor(i,j):**\
>   The function returns the cofactor of a matrix, using definition.

>- **.cof_matrix():**\
>   The function returns the cofactor of a matrix, using definition.
>- **.inverse():**\
>   Using the definition for the inverse of a matrix (tcof(A)*1/detA), the function returns the inverse of the matrix.

>- **switch_columns(column1, column2)**:\
>   The function returns a matrix where the column_A of A is switched with columns_from_B of the matrix B

>- **cramer_rule(Matrix, Matrix)**:\
>   For linear systems with square system matrix, without using invert matrix.
>   Used the definition of the Cramer Rule for linear systems.

>- **square_linear_systems(Matrix, Matrix)**:\
>   Use the function if you have to solve a linear system where A matrix of the system is a square matrix.
>   It uses the definition: X = A^-1*B.
>   The vector that solves the system is returned.

>- **.info()**:\
>   The function print all relevant informations about the matrix:
>    - rows
>    - columns
>    - transpose
>    - if square
>         - determinant
>         - inverse matrix
>         - cofactor matrix

>- **.\_\_iter\_\_()**:\
>    The function let the matrix be iterable

>- **.\_\_next\_\_()**:\
>    The function update the iterator and return the element self.elem(i,j)

>-  **len(Matrix)**:\
>    The function returns the number of elements in the Matrix

>- **.find_pivot(row)**:\
>    The function returns the pivot of a selected row. A pivot is the first element != 0 of a row.\
>    WARNING: i and j are not in the usual order. It is because i need to sort the list in other methods.

>- **.pivot_list()**:\
>    The function return a list with all the pivots of the matrix and their indices. Example: \[(j, i, val), (j2,i2, val2)...\]\
>    WARNING: i and j are not in the usual order. It is because i need to sort the list in other methods.
            
>- **.is_triangular()**:\
>    Check if the Matrix is or not triangular \|
>    Being triangular means that the pivot in a low j must be in low i.
>    It is not triangular if pivot are on the same column.
            
>- **.sort()**:\
>    The function sort the matrix in order to make it triangular
                
>- **.pivot_before(row)**:\
>    The function returns True if the pivot in the previous row is in the same column of the pivot of the selected row. Else: False.
            
>- **.gaussian_elimination()**:\
>    The function returns a matrix where it was done the Gaussian Elimination.

>- **.from_num_to_str(self)**:\
>    Method to convert a Matrix in a String Matrix

>- **.characteristic_polynomial()**:\
>    Method that returns the str version of the C. Poly. from  a Numerical Matrix.

##### String_Matrix

>- **.__add__(self, other):from_str_to_num(self)**:\
>    The function returns a string Matrix where the elements are the sum of the strings, with "+"
>    Example: "3"+"+"+"4" --> "3+4"

>- **.def sub(self, row_deleted, column_deleted)**:\
>    The function returns a string sub matrix.
                
>- **.characteristic_polynomial(self)**:\
>    The function returns the Char. Polynomial of a string matrix. It is required a string Matrix, in order to let there be variables.
>    The function is returned as a string.

>- **.check_C_Poly(self)**:\
>    A function used for testing

>- **.from_str_to_num(self)**:\
>    Method to convert a String Matrix in a Matrix

>- **str_det_nxn(mat, row, col)**:\
>    Determinant of a string matrix. It returns a string, using the Laplace Formula.

#### SAMPLES:
1) _Import the [module](https://github.com/MatteoLiotta/Py_Matrix/blob/main/Code/Py_Matrix.py):_ 
   ```
   >>> import Py_Matrix as py_m 
   ```
   
2) _Create a Matrix from a dataset:_ 
   ```
   >>> A = py_m.Matrix([1,2,3,4], 2, 2)
   ```

3) _Print a Matrix:_
   ```
   >>> A = py_m.Matrix([1,2,3,4], 2, 2)
   >>> print(A)
   ```
   > Output:
   ```
   0| 1     2     
   1| 3     4     
      --    --
      0     1
   ```
   
4) _Print an element of the matrix, with row and column:_ 
   ```
   >>> print(A.elem(1,0) #A previously declared
   ```
   > Output:
   ```
   3
   ```
   
5) _Add two Matrix (Matrix + Matrix):_ 
   > WARNING: Matrix must have same rows and columns
   ```
   >>> A = py_m.Matrix([1,2,3,4], 2, 2) 
   >>> B = py_m.Matrix([4,3,2,1], 2, 2) 
   >>> print(A+B) 
   ```
   > Output:
   ```
   0| 5     5     
   1| 5     5     
      --    --
      0     1
   ```
   
6) _Matrix * Matrix:_ 
   > WARNING: Matrix multiplication is not commutative
   ```
   >>>print(A\*B) #A and B previously declared
   ```
   > Output:
   ```
   0| 8     5     
   1| 20    13    
      --    --
      0     1
   ```
   
7) _Matrix * number:_ 
   > WARNING: 2\*A is not implemented.
   ```
   >>> print(A\*2) #A and B previously declared
   ```
   > Output:
   ```
   0| 2     4     
   1| 6     8     
      --    --    
      0     1  
   ```
   
8) _Transpose of a Matrix:_ 
   ```
   >>> print(A.t()) #A previously declared
   ```
   > Output:
   ```
   0| 1     3     
   1| 2     4     
      --    --    
      0     1 
   ```
   
9) _Elementary operation 3:_ 
   ```
   >>> A.elementary_op3(0,1,-3)
   ```
   > Output:
   ```
   0| 1     2     
   1| 0     -2    
      --    --    
      0     1
   ```
   
10) _Submatrix of a matrix:_ 
    ```
    >>> print(A.sub(0,0)) #A previously declared
    ```
    > Output:
    ```
    0| 4       
       --   
       0
    ```
    
11) _Determinant of a matrix (2 ways)_ 
    ```
    >>> print(A.det) #it returns determinant as a number
    >>> print(det_nxn(A)) #it returns determinant a number
    ```
    > Output:
    ```
    -2
    ```
    
12) _Cofactor of a Matrix:_ 
    > deleting the element in (0,0)
    ```
    >>> print(A.cofactor(0,0)) #A previously declared
    ```
    > Output:
    ```
    4
    ```
    
13) _Inverse Matrix_: 
    ```
    >>> print(A.inverse()) #A previously declared 
    ```
    > Output:
    ```
    0| -2.000 1.000 
    1| 1.500 -0.500 
       --    --    
       0     1  
    ```
    
14) _Cramer Rule on Linear System_:  
    ```
    >>> B = py_m.Matrix([4,3],2,1) 
    >>> print(cramer_rule(A,B)) #A previously declared
    ```

15) _Matrix Informations_:
    ```
    >>> A.info() #A previously declared
    ```
    
16) _Matrix iteration_:
    ```
    >>> A = py_m.Matrix([1,2,3,4,5,6],2,3)
    >>> for i in A:
            print(i)
    ```
    > Output:
    ```
    1
    2
    3
    4
    ```
    
17) _Lenght_:
    ```
    >>> print(len(A)) #A previously declared as Matrix([1,2,3,4],2,2)
    ```
    > Output:
    ```
    4
    ```

18) _Find Pivot_:
    ```
    >>> print(A) #A previously declared as Matrix([1,2,0,4],2,2)
    ```
    > Output:
    ```
    0| 1     2     
    1| 0     4    
       --    --    
       0     1
    ```
    ```
    >>> print(A.find_pivot(1)) 
    ```
    > Output:
    ```
    4
    ```

18) _Pivot List_:
    ```
    >>> A = py_m.Matrix([1,2,3,4], 2, 2)
    >>> print(A.pivot_list())
    ```
    > Output:
    ```
    [(0, 0, 1), (0, 1, 3)]
    ```

19) _Sort a Matrix_:
    ```
    >>> A = py_m.Matrix([0,1,3,4], 2, 2)
    >>> print(A.sort())
    ```
    > Output:
    ```
    0| 3     4     
    1| 0     1     
       --    --    
       0     1
    ```
    
20) _Gaussian Elimination_:
    ```
    >>> A = py_m.Matrix([0,1,3,4], 2, 2)
    >>> print(A.gaussian_elimination())
    ```
    > Output:
    ```
    0| 5     1     3     
    1| 0.000 2.600 -3.200 
    2| 0.000 0.000 -7.077 
       --    --    --    
       0     1     2   
    ```

21) _Characteristic Polynomial_:
    ```
    >>> A = py_m.Matrix([0,1,3,4], 2, 2)
    >>> print(A.characteristic_polynomial())
    ```
    > Output:
    ```
    '(((0+-x)*(4+-x)) + (-1)*((3+0)*(1+0)))'
    ```
