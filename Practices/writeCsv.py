# writing data on csv file


def writedata():
    data = [('Name', 'age', 'sex'), ('Veer', 23, 'male'), ('Kashif', 24, 'male', 'Fatima', 21, 'female')]
    with open('userData.csv', 'w') as writefile:
        for wr in data:
            writefile.write(str(wr))


def readdata():
    with open('userData.csv', 'r') as readfile:
        datalist = readfile.readlines()
        for lin in datalist:
            print(f'{lin}\n')


readdata()
