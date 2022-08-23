for a in range(int(input())):
    input()
    flag = True
    sudoku = []
    for i in range(0, 9):
        sudoku.append(input().split(' '))
    for i in range(0, 9):
        numbers = [1,2,3,4,5,6,7,8,9]
        for j in range(9):
            if int(sudoku[i][j]) in numbers:
                numbers.remove(int(sudoku[i][j]))
            else:
                flag = False
                break
    for i in range(0, 9):
        numbers = [1,2,3,4,5,6,7,8,9]
        for j in range(9):
            if int(sudoku[j][i]) in numbers:
                numbers.remove(int(sudoku[j][i]))
            else:
                flag = False
                break
    if(flag):
        print('Resuelto')
    else:
        print('No resuelto')