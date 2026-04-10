def det(m):
    # Standard 3x3 Determinant Formula
    a, b, c = m[0][0], m[0][1], m[0][2]
    d, e, f = m[1][0], m[1][1], m[1][2]
    g, h, i = m[2][0], m[2][1], m[2][2]
    
    return a*(e*i - f*h) - b*(d*i - f*g) + c*(d*h - e*g)

# Input conversion to integers using List Comprehension
m1 = [int(x) for x in input("Enter row 1 (comma separated): ").split(",")]
m2 = [int(x) for x in input("Enter row 2 (comma separated): ").split(",")]
m3 = [int(x) for x in input("Enter row 3 (comma separated): ").split(",")]

matrix = [m1, m2, m3]
print("Determinant of matrix:", det(matrix))
