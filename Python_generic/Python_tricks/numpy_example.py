import numpy as np

b = np.array(
    [
        (1, 2, 3),
        (10, 20, 30)
    ]
)
c = b
print(f'Memory Allocated for Numpy:\n {b.size * b.itemsize}')
print(f'Get the Size, Shape , data type & dimension of Numpy:\n {b.size, b.shape, b.dtype, b.ndim}')
print(f'Transforming 2*3 to 3*2 Matrix with reshape:\n {b.reshape(3, 2)}')
a = np.zeros((1, 2))  # Returns the Array of given dimension 0s
a = np.ones((1, 2))  # Returns the array of Given dimension with 1s
a = np.linspace(1, 2, 10)  # Returns the evenly spaced numbers over a specified interval.
a = np.transpose(b)  # Transpose N * M to M * N arrays
a = np.flatten(b)  # Flatten the N*M dimensional arrays to single list
a = np.concatenate(b, c, axis=1)  # Concatenate the two Arrays via X-Axis  i.e Row wise.
a = np.vstack((b, c))  # Stacks two Arrays vertically
a = np.hstack((b, c))  # Stacks two Arrays Horizontally
x = a[0, 2]  # Slicing of Arrays - Row = 0 & Column = 2
x = a[0:, 2]  # Slicing of Arrays - Rows - every rows and Column = 2 only
x = np.identity(3)  # Prints the Identity Matrix of size 3*3
y = np.eye(8, 7, k=1)  # 8 X 7 Dimensional array with first upper diagonal 1. k=0 is same as identity
y = np.eye(8, 7, k=-1)  # 8 X 7 Dimensional array with first lower diagonal 1.
res = np.flipud(b)  # using flipud method to reverse
np.set_printoptions(legacy='1.13')  # For better alignments of Numpy Operations.
print(np.floor(a))
print(np.ceil(a))
print(np.rint(a))
print(np.std(a))
print(np.mean(a))
print(np.dot(a, b))  # Gives Dot product i.e Matrix Multiplication
print(np.cross(a, b))  # Gives Cross product 
print(np.linalg.det([[1, 2], [2, 1]]))  # The linalg.det tool computes the determinant of an array.
print(np.linalg.inv([[1, 2], [2, 1]]))  # The linalg.inv tool computes the (multiplicative) inverse of a matrix.
vals, vecs = np.linalg.eig([[1, 2], [2, 1]])  # The linalg.eig computes the eigenvalues and right eigenvectors of a
# square array.
print(np.poly([-1, 1, 1, 10]))  # The poly tool returns the coefficients of a polynomial with the given sequence of
# roots.
print(np.roots([1, 0, -1]))  # The roots tool returns the roots of a polynomial with the given coefficients.
print(np.polyint([1, 1, 1]))  # The polyint tool returns an antiderivative (indefinite integral) of a polynomial.
print(np.polyder([1, 1, 1, 1]))     # The polyder tool returns the derivative of the specified order of a polynomial.
print(np.polyval([1, -2, 0, 2], 4))   # The polyval tool evaluates the polynomial at specific value.
print(np.polyfit([0,1,-1, 2, -2], [0,1,1, 4, 4], 2)) # The polyfit tool fits a polynomial of a specified order to a
# set of data using a least-squares approach. The functions polyadd, polysub, polymul, and polydiv also handle proper
# addition, subtraction, multiplication, and division of polynomial coefficients, respectively. 
