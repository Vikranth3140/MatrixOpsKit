from sympy import Matrix

#reading matrix from the file
f = open("matrix.txt")
line1 = f.read().splitlines()

main_matrix = []
for i in line1:
    i = i.split(' ')    
    main_matrix.append(i)
count_rows = len(main_matrix)
count_columns = len(main_matrix[0])

for i in main_matrix:
    for j in range(len(i)):
        i[j] = int(i[j])
f.close()
main_matrix = Matrix(main_matrix)

rref_matrix,pivots = main_matrix.rref()
M = rref_matrix.tolist()

print('                 RREF :')
for i in M:
    for j in i:
        print(j,end = '\t')
    print()
print('-------------------------------------------------------------------------------------------------')
def parametric(matrix,column):
    global column_list
    global column_list_copy
    column_list = []
    for i in range(column):
        l1 = []
        for j in range(count_rows):
            l1.append(matrix[j][i])
        column_list.append(l1)

    print('             Column Matrix :')
    for i in column_list:
        for j in i:
            print(j,end='\t')
        print()
    print('-------------------------------------------------------------------------------------------------')

parametric(M,count_columns)

def identity_matrix(size):
    identity_list = []
    for row in range(0, size):
        temp_list = []
        for col in range(0, size):
            if (row == col):
                temp_list.append(1)
            else:
                temp_list.append(0)
        identity_list.append(temp_list)
    return identity_list

def deciding_size_of_identity(column,row):
    if column < row:
        x = column
    else:
        x = row
    return x
size_of_identity = deciding_size_of_identity(count_columns,count_rows)
identity_mat = identity_matrix(size_of_identity)

def comparing_collist_with_identity(identity_mat,column_list):
    column_list_copy = []
    for i in column_list:
        if i in identity_mat:
            pass
        else:
            column_list_copy.append(i)
    return column_list_copy

column_list_copy = comparing_collist_with_identity(identity_mat,column_list)

main_list_1 = []
no_pivot_ind = []
ind = 0

for i in column_list_copy:
    q = 0
    par_list = [0 for i in range(count_columns)]
    for m in range(len(column_list)):
        if column_list[m] in identity_mat:
            par_list[m] = -column_list_copy[ind][q]
            q += 1
    ind += 1
    main_list_1.append(par_list)

ind_1 = 0
for p in main_list_1:
    if p not in identity_mat:
        for i in p:
            non_pivot_ind = column_list.index(column_list_copy[ind_1])
            p[non_pivot_ind] = 1
        ind_1 += 1

for k in range(len(column_list)):
    if column_list[k] not in identity_mat:
        no_pivot_ind.append(k)

print('             Parametric Form :')
for v in range(len(main_list_1)):
    print('x_' + str(no_pivot_ind[v]) + str(main_list_1[v]) , end = ' + ')
print('\n')
print('-------------------------------------------------------------------------------------------------')