import unittest
class matrix:
    def __init__(self, mat):
        self.m = mat

    def show(self):
        return self.m

    def __add__(self, other):
        if(len(self.m) == len(other.m) and len(self.m[0]) == len(other.m[0])):
            addM = []
            for i in range(0, len(self.m)):
                add_row = [self.m[i][j] + other.m[i][j] for j in range(len(self.m[0]))]
                addM.append(add_row)
            return addM
        else:
            return "Matrices should be of same order for addition"


    def __sub__(self, other):
        if(len(self.m) == len(other.m) and len(self.m[0]) == len(other.m[0])):
            subM = []
            for i in range(0, len(self.m)):
                sub_row = [self.m[i][j] - other.m[i][j] for j in range(len(self.m[0]))]
                subM.append(sub_row)
            return subM
        else:
            return "Matrices should be of same order for subtraction"

    def __mul__(self, other):
        if(len(self.m[0]) == len(other.m)):
            mul_mat = matrix([])
            mul_mat.m = [[0 for i in range(len(other.m[0]))] for j in range(len(self.m))]
            for i in range(len(self.m)):
                for j in range(len(other.m[0])):
                    for k in range(len(other.m)):

                        mul_mat.m[i][j] += self.m[i][k] * other.m[k][j]
            return mul_mat
        else:
            return "Matrix multiplication for matrices of such order not possible"
    def __pow__(self, x, modulo=None):
        if(len(self.m) == len(self.m[0])):
            exp = matrix([])
            exp.m = self.m
            # print(exp.m)
            for k in range(x-1):
                exp = exp * self
            return exp.m
        else:
            return "Not a square matrix so exponentiation not possible"

    def det(self):
        # print(len(self.m))
        if len(self.m) == len(self.m[0]):
            temp = [0] * len(self.m)
            total = 1
            x = 1
            if(len(self.m) == 2):
                x = self.m[0][0] * self.m[1][1] - self.m[0][1]*self.m[1][0]
                return x
            else:
                for i in range(len(self.m)):
                    index = i
                    while (self.m[index][i] == 0 and index < len(self.m)):
                        index += 1

                    if (index == len(self.m)):
                        continue

                    if (index != i):
                        for j in range(len(self.m)):
                            self.m[index][j], self.m[i][j] = self.m[i][j], self.m[index][j]
                        x = x * int(pow(-1, index - i))
                    for j in range(len(self.m)):
                        temp[j] = self.m[i][j]
                    for j in range(i + 1, len(self.m)):
                        n1 = temp[i]
                        n2 = self.m[j][i]
                        for k in range(len(self.m)):
                            self.m[j][k] = (n1 * self.m[j][k]) - (n2 * temp[k])

                        total = total * n1
                for i in range(len(self.m)):
                    x = x * self.m[i][i]

                return int(x / total)

        else:
            return "Not a square matrix so cannot find determinant"




# p1 = matrix([[2,3,4], [4,3,7], [5,4,1]])
# print(p1**3)
# p1 = matrix([[2, 3, 6], [4, 5, 8]])
# p2 = matrix([[2, 3, 7], [4, 5, 7], [1, 1, 1]])
# print(p1+p2)
# print(p1-p2)
# print((p1*p2).show())
# print(p1.det())


class Testing(unittest.TestCase):
    def test_add(self):
        p1 = matrix([[2, 3, 6], [4, 5, 8]])
        p2 = matrix([[2, 3, 7], [4, 5, 7]])
        add = p1+p2
        self.assertEqual(add, [[4,6,13], [8, 10, 15]])
    def test_sub(self):
        p1 = matrix([[2, 3, 6], [4, 5, 8]])
        p2 = matrix([[2, 3, 7], [4, 5, 7]])
        sub = p1-p2
        self.assertEqual(sub, [[0,0,-1], [0, 0, 1]])
    def test_mul(self):
        p1 = matrix([[2, 3, 6], [4, 5, 8]])
        p2 = matrix([[2, 3, 7], [4, 5, 7], [1, 1, 1]])
        multi = p1*p2
        self.assertEqual(multi.show(), [[22, 27, 41], [36, 45, 71]])
    def test_det(self):
        p1 = matrix([[2,3,4], [4,3,7], [5,4,1]])
        deter = p1.det()
        self.assertEqual(deter, 47)
    def test_pow(self):
        p1 = matrix([[2, 3, 4], [4, 3, 7], [5, 4, 1]])
        power = p1**3
        self.assertEqual(power, [[361, 333, 394], [526, 488, 607], [431, 382, 390]])


if __name__ == "__main__":
    unittest.main()





