import math

def Bhaskara(a, b, c):

    delta = (b ** 2) - (4 * a * c)

    if ( delta < 0 ):
        return None # Raiz Negativa
  
    x = math.sqrt(delta)

    x1 = (-b + x) / (2 * a)
    x2 = (-b - x) / (2 * a)

    return x1, x2

def main():
    
    
    a = int(input('Digite um valor para A '))
    b = int(input('Digite um valor para B '))
    c = int(input('Digute um valor para C '))

    x = Bhaskara(a, b, c)


    if  x == None:
        print("Delta negativo. Nenhuma raiz real")

    elif x[0] == x[1]:
        print('Delta = 0. Somente um resultado.\nx = {}'.format(x[0]))

    else:
        print('X1 = {}'.format(x[0]))
        print('X2 = {}'.format(x[1]))

if __name__ == '__main__':
    main()
    
    