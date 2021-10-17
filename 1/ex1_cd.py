import numpy as np

# define matrix or ndarray to be checked
x = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])

z = x.ndim # dimension of matrix    


def check_orthogonality(x):

    y=np.identity(3)

    if np.allclose(x*x.T,y):  # x*x'==Identity property of orthogonality
        print(x*x.T)
        print("x is orthogonal")
    else:
        print(x*x.T)
        print("x is not orthogonal")


print(check_orthogonality(x))
print(np.linalg.det(x))
