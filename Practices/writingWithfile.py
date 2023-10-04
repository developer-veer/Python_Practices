# perform writing operation on file
with open('alphabets.txt', 'w') as alpha:
    for lin in range(65, 97):
        alpha.write(chr(lin))

# the below code read the data from file
with open('alphabets.txt', 'r') as readAlpha:
    al = readAlpha.read()
    for lin in al:
        print(f'{lin} \n')
