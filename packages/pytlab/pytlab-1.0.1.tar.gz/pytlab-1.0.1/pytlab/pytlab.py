from numpy import *
def matinput(rows, columns, data_type=""):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(columns):
            if data_type == "int":
                value = int(input("Enter element [{}][{}]: ".format(i, j)))
            elif data_type == "float":
                value = float(input("Enter element [{}][{}]: ".format(i, j)))
            else:
                value = input("Enter element [{}][{}]: ".format(i,j))
            row.append(value)
        matrix.append(row)
    return matrix
