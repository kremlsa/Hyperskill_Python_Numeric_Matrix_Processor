import math


class MyMatrix:
    def __init__(self, rows_, columns_):
        self.rows = rows_
        self.columns = columns_
        self.body = []

    def create_matrix(self):
        for i_ in range(self.rows):
            self.body.append([float(x_) for x_ in input().split()])

    def print_matrix(self):
        for i_ in range(self.rows):
            # print(" ".join(str(x_) for x_ in self.body[i_]))
            print(" ".join(str(x_) for x_ in self.body[i_]))

    def get_column(self, col_):
        return [x[col_] for x in self.body]

    def __add__(self, other):
        if self.rows != other.rows or self.columns != other.columns:
            print("The operation cannot be performed.")
            return None
        result_ = MyMatrix(self.rows, self.columns)
        for i_ in range(self.rows):
            result_.body.append([x + y for x, y in zip(self.body[i_], other.body[i_])])
        return result_

    def __mul__(self, other):
        if isinstance(other, float):
            result_ = MyMatrix(self.rows, self.columns)
            for i_ in range(self.rows):
                result_.body.append([x * other for x in self.body[i_]])
            return result_
        if isinstance(other, MyMatrix):
            result_ = MyMatrix(self.rows, other.columns)
            if self.columns != other.rows:
                print("The operation cannot be performed.")
                return None
            for i_ in range(self.rows):
                vector_ = []
                for j_ in range(other.columns):
                    vector_.append(sum([x * y for x, y in zip(self.body[i_], other.get_column(j_))]))
                result_.body.append(vector_)
            return result_
        return None

    def transpose_main(self):
        result_ = MyMatrix(self.columns, self.rows)
        for i_ in range(self.columns):
            result_.body.append(self.get_column(i_))
        return result_

    def transpose_side(self):
        result_ = MyMatrix(self.columns, self.rows)
        for i_ in range(self.columns - 1, -1, -1):
            result_.body.append(self.get_column(i_)[::-1])
        return result_

    def transpose_vert(self):
        result_ = MyMatrix(self.rows, self.columns)
        for i_ in range(self.rows):
            result_.body.append(self.body[i_][::-1])
        return result_

    def transpose_hor(self):
        result_ = MyMatrix(self.columns, self.rows)
        for i_ in range(self.columns - 1, -1, -1):
            result_.body.append(self.body[i_])
        return result_

    def determinant(self, matrix_):
        det_ = 0
        if matrix_.rows == 1 and matrix_.columns == 1:
            return matrix_.body[0][0]
        if matrix_.rows == 2 and matrix_.columns == 2:
            return matrix_.body[0][0] * matrix_.body[1][1] - matrix_.body[0][1] * matrix_.body[1][0]
        else:
            for i_ in range(matrix_.rows):
                det_ += self.determinant(self.minor(matrix_, 0, i_)).__mul__(self.cofactor_det(matrix_, 0, i_))
            return det_

    def minor(self, matrix_, r_, c_):
        result_ = MyMatrix(matrix_.rows - 1, matrix_.columns - 1)
        for j_ in range(0, matrix_.rows):
            vector_ = []
            if j_ == r_:
                continue
            for k_ in range(matrix_.columns):
                if k_ != c_:
                    vector_.append(matrix_.body[j_][k_])
            result_.body.append(vector_)
        return result_

    def cofactor_det(self, matrix_, r_, c_):
        return matrix_.body[r_][c_] * pow((-1.0), c_)

    def cofactor(self, matrix_, r_, c_):
        # return matrix_.body[j_][i_] * pow((-1.0), i_)
        return self.determinant(self.minor(matrix_, r_, c_)) * pow((-1.0), c_ + r_ )

    def get_cmatrix(self, matrix_):
        result_ = MyMatrix(matrix_.rows, matrix_.columns)
        for i_ in range(matrix_.rows):
            vector_ = []
            for j_ in range(matrix_.columns):
                vector_.append(self.cofactor(matrix_, i_ , j_))
            result_.body.append(vector_)
        result_ = result_.transpose_main()
        return result_

    def inverse(self, matrix_):
        det_ = self.determinant(matrix_)
        cmatrix_ = self.get_cmatrix(matrix_)
        if det_ == 0:
            return None
        else:
            return cmatrix_.__mul__(1 / det_)


def main_menu():
    while True:
        print("1. Add matrices")
        print("2. Multiply matrix by a constant")
        print("3. Multiply matrices")
        print("4. Transpose matrix")
        print("5. Calculate a determinant")
        print("6. Inverse matrix")
        print("0. Exit")
        print("Your choice:")
        option_ = input()
        if option_ == "1":
            addition()
        if option_ == "2":
            multiply_const()
        if option_ == "3":
            multiply()
        if option_ == "4":
            transpose()
        if option_ == "5":
            det()
        if option_ == "6":
            inverse()
        if option_ == "0":
            break


def addition():
    print("Enter size of first matrix: ")
    sizes = input().split()
    a = MyMatrix(int(sizes[0]), int(sizes[1]))
    print("Enter first matrix:")
    a.create_matrix()
    print("Enter size of second matrix: ")
    sizes = input().split()
    b = MyMatrix(int(sizes[0]), int(sizes[1]))
    print("Enter second matrix:")
    b.create_matrix()
    c = a.__add__(b)
    if c is not None:
        print("The result is:")
        c.print_matrix()


def multiply_const():
    print("Enter size of matrix: ")
    sizes = input().split()
    a = MyMatrix(int(sizes[0]), int(sizes[1]))
    print("Enter matrix:")
    a.create_matrix()
    print("Enter constant:")
    const_ = float(input())
    c = a.__mul__(const_)
    c.print_matrix()


def multiply():
    print("Enter size of first matrix: ")
    sizes = input().split()
    a = MyMatrix(int(sizes[0]), int(sizes[1]))
    print("Enter first matrix:")
    a.create_matrix()
    print("Enter size of second matrix: ")
    sizes = input().split()
    b = MyMatrix(int(sizes[0]), int(sizes[1]))
    print("Enter second matrix:")
    b.create_matrix()
    c = a.__mul__(b)
    if c is not None:
        print("The result is:")
        c.print_matrix()


def transpose():
    print("1. Main diagonal")
    print("2. Side diagonal")
    print("3. Vertical line")
    print("4. Horizontal line")
    print("Your choice:")
    option_ = input()
    print("Enter matrix size: ")
    sizes = input().split()
    a = MyMatrix(int(sizes[0]), int(sizes[1]))
    print("Enter matrix:")
    a.create_matrix()
    if option_ == "1":
        a = a.transpose_main()
    if option_ == "2":
        a = a.transpose_side()
    if option_ == "3":
        a = a.transpose_vert()
    if option_ == "4":
        a = a.transpose_hor()
    print("The result is:")
    a.print_matrix()


def det():
    print("Enter matrix size:")
    sizes = input().split()
    a = MyMatrix(int(sizes[0]), int(sizes[1]))
    print("Enter matrix:")
    a.create_matrix()
    b = MyMatrix(int(sizes[0]), int(sizes[1]))
    deter = b.determinant(a)
    print("The result is:")
    print(deter)


def inverse():
    print("Enter matrix size:")
    sizes = input().split()
    a = MyMatrix(int(sizes[0]), int(sizes[1]))
    print("Enter matrix:")
    a.create_matrix()
    b = MyMatrix(int(sizes[0]), int(sizes[1]))
    invert = b.inverse(a)
    if invert is not None:
        print("The result is:")
        invert.print_matrix()
    else:
        print("This matrix doesn't have an inverse.")

main_menu()
