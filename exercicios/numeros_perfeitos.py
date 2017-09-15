'''
num: um número inteiro
Essa função retorna True se num for um número perfeito e False caso contrário.

Um número perfeito é um número inteiro para o qual a soma de todos os seus divisores positivos (excluindo o próprio número) é igual a ele.
Exemplo: 28 é um número perfeito, pois seus divisores são 1, 2, 4, 7, 14. 1 + 2 + 4 + 7 + 14 = 28, portanto, 28 é um número perfeito!
Desenvolva a função numero_perfeito que receberá como entrada um número e retornará True se ele for perfeito e False caso contrário.
'''

def numero_perfeito(num):
    soma=0
    for numero in range(1,num):
        #print("Numero:",numero)
        if num %numero==0:
            soma+=numero
            #print(numero)
    if num==soma:
        print("True") 
        return True
    else:
        print("False") 
        return False

numero_perfeito(28)
        
