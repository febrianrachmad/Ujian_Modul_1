# Soal 1
print('Soal 1 Year Of Investment')
def calculate_years(principal, interest, tax, desired):
    principal = ''
    interest = ''
    tax = ''
    desired = ''
    inputP = input('Masukan Principal : ')
    inputI = input('Masukan Interest: ')
    inputT = input('Masukan Tax: ')
    inputD = input('Masukan Desired: ')



# Soal 2
print ('Soal 2:')
def expandedForm(num):
    X = []
    while num // 10 > 0:
        angka = num % 10
        X.append(angka)
        num = num // 10
        if num < 10:
            num += 10
            angka = num % 10
            X.append(angka)
            break
    z = ''
    for i in range(len(X)-1,-1,-1):
        if i == len(X)-1:
            z += str(X[i]*(10**i))
        elif X[i]*(10**i) == 0:
            continue
        else:
            z += ' + '
            z += str(X[i]*(10**i))
        
    print (z)




# Soal 3
print('Build Tower')
def tower_builder(n_floor, block_size):
        w, h = block_size
inputF = int(input('Masukan Floor: '))
inputW = int(input('Masukan Width: '))
inputH = int(input('Masukan Height: '))
n_floor = ' '
for i in range(inputF):
    for j in range ((inputF-i)-inputW):
        n_floor += ' '
    for k in range ((i*inputW)+inputH):
        n_floor += '*'
    n_floor += ' \n '

print(n_floor)

