import sys

def calculadora(*operacao):
    op_numeros = operacao[1:]
    print(op_numeros[0], op_numeros[1], op_numeros[2])
    if  op_numeros[0] == 'SOMA':
        soma = int(op_numeros[1]) + int(op_numeros[2])
        return print(f'SOMA: {soma}')
    elif  op_numeros[0] == 'SUB':
        sub = int(op_numeros[1]) - int(op_numeros[2])
        return print(f'SUB: {sub}')
    elif  op_numeros[0] == 'MULT':
       mult = int(op_numeros[1]) * int(op_numeros[2])
       return print(f'MULT: {mult}')
    elif  op_numeros[0] == 'DIV':
        div = int(op_numeros[1]) / int(op_numeros[2])
        return print(f'DIV: {div}')

if __name__ == '__main__':
    calculadora(*sys.argv)
    