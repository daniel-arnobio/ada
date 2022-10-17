import sys

def imprimeInverso(*numeros):
   n = [int(i) for i in numeros[1:]]

   print(n[::-1])
if __name__ == '__main__':
      imprimeInverso(*sys.argv)