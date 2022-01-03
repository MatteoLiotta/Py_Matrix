# Py_Matrix
Module for matrix creation and matrix manipulation.\
Matrix are made as object class while metods are for matrix calculus and properties.
> Programming Language: Python.

#### FILE:
> You can find the file .py here: [Py_Matrix.py](https://github.com/MatteoLiotta/Py_Matrix/blob/main/Code/Py_Matrix.py)

### LIST OF FUNCTIONS:
-------
 >- **.matrix_c(...):**\
 >   creates a matrix from a selected (if not, uses the self.v) dataset, number of rows and columns (if not selected, it uses self.r and self.c)

>- **.__str__():**\
>   print in a pretty and comprehensible way the matrix.

> - **.elem(...):**\
>    Return a specific element of the matrix. User has to choose row and column, then the element in that row and column is returned.

> - **.elem_change(...):**\
>    It changes a specific element of the matrix. User has to choose row and column, then the element in that row and column is changed whit the entered value.
>    It is also possible to refer to the matrix as self.matrix[i][j], whitout using this function.

>- **+ :**\
>    It makes possible to add two differents matrix. It return a new matrix, istance of Matrix class.
>    Matrix must have same rows and columns
>    [it returns a new Matrix object]

>- **\* :**\
>    Two possibilities: if 'other' is a number or if it is a matrix.
>   - if other is a matrix, it uses the rule for this operation. So the operation returns the matrix obtained with the multiplication between matrix.
>   - if other is not a matrix, but an integer or a floating point number, it multiplies every element of the matrix for the number.
>     [it returns a new Matrix object]

>- **.t():**\
>    The function returns a new matrix which is the transpose of the given matrix. The transpose matrix is define by definition as:
>    With A as a matrix (Aij), A.t() is (tAij), so:
>    tAij = Aji
>    So the transpose switches the index of the original matrix. The new matrix is returned. Original matrix is not changed.

>- **.elementary_op1(...):**\
>    The function returns a Matrix where row1 and row2 of self are switched.
>    It is the first elementary operation.

>- **.elementary_op2(...):**\
>    The function returns a Matrix where row1 of self is multiplied by a chosen number.
>    It is the second elementary operation.
 
>- **.elementary_op3(...):**\
>    The function returns a Matrix where every element of rowtochange is added with a multiple (val) of the row entered.
>    Value is required.
>    It is the third elementary operation.

>- **.sub(...):**\
>    The function returns the submatrix obtained deleting the row "rowdeleted" and the column "column_deleted".
>    The matrix avoid taking elements with row_deleted or column deleted ad indices.
>    The submatrix number of row and coulmns is, if nxn, the sqrt of the number of rows (so elements of matrix list). If mxn, it is the number of rows and columns - 1.
>    To unify cases, it will all be done in the second way.
 
>- **det_nxn(matrix):**\
>   The function returns the determinant of a matrix.
>   The determinant is recursively obtained using Laplace Formula, as sum of multiplication between
>   elements (i,j) and the cofactor(i,j).
>   In case of a 1x1 matrix, is returned the element (0,0) of the matrix.

>- **.cofactor(...):**\
>   The function returns the cofactor of a matrix, using definition.

>- **.cof_matrix():**\
>   The function returns the cofactor of a matrix, using definition.
>- **.inverse():**\
>   Using the definition for the inverse of a matrix (tcof(A)*1/detA), the function returns the inverse of the matrix.

>- **switch_columns(...)**:\
>   The function returns a matrix where the column_A of A is switched with columns_from_B of the matrix B

>- **cramer_rule(...)**:\
>   For linear systems with square system matrix, without using invert matrix.
>   Used the definition of the Cramer Rule for linear systems.

>- **square_linear_systems(...)**:\
>   Use the function if you have to solve a linear system where A matrix of the system is a square matrix.
>   It uses the definition: X = A^-1*B.
>   The vector that solves the system is returned.

### SAMPLES
-------
| Input/Code |
| --- |
|1) _Import the module:_ >>> import Py_Matrix as py_m |
|2) _Create a Matrix from a dataset:_ >>> A = py_m.Matrix([1,2,3,4], 2, 2) |
|3) _Print a Matrix:_ >>> print(A) #A previously declared|
|4) _Print an element of the matrix, knowing row and column:_ >>> print(A.elem(1,0) #A previously declared|
|5) _Add two Matrix (Matrix + Matrix):_ > WARNING: Matrix must have same rows and columns|
|>>> A = py_m.Matrix([1,2,3,4], 2, 2) >>> B = py_m.Matrix([4,3,2,1], 2, 2) >>> print(A+B) 
|6) _Matrix * Matrix:_ > WARNING: Matrix multiplication is not commutative|
|>>>print(A\*B) #A and B previously declared|
|7) _Matrix * number:_ WARNING: 2\*A is not implemented.|
|>>> print(A\*2) #A and B previously declared|
|8) _Transpose of a Matrix:_ >>> print(A.t()) #A previously declared|
|9) _Elementary operation 3:_ >>> A.elementary_op3(0,1,-3)|
|10) _Submatrix of a matrix:_ >>> print(A.sub(0,0)) #A previously declared|
|11) _Determinant of a matrix (2 ways)_ 
|1. >>> print(A.det) #it returns a number |
|2. >>> print(det_nxn(A)) #it returns a number|
|12) _Cofactor of a Matrix:_ #deleting the element in (0,0) >>> print(A.cofactor(0,0)) #A previously declared|
|13) _Inverse Matrix_: >>> print(A.inverse()) #A previously declared |
|14) _Cramer Rule on Linear System_:  >>> B = Matrix([4,3],2,1) >>> print(cramer_rule(A,B)) #A previously declared|

#### LICENSE
> You can find license here: [LICENSE](https://github.com/MatteoLiotta/Py_Matrix/blob/main/LICENSE)
