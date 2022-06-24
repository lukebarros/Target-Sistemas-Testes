#Solução Recursiva da implementação de Fibonacci
def fib(ntermos):
    if ntermos <= 1:
        return ntermos
    else:
        return (fib(ntermos-1) + fib(ntermos-2)) #adiciona 2 numeros anteriores para encontrar o próximo

#Função para verificar se o termo pertence a sequencia de Fibonacci
def verificafib(ntermos):
    pertence = [fib(i) for i in range(ntermos)] #list comprehension
    if ntermos not in pertence:
        print(f'O termo "{ntermos}" não pertence a sequencia de Fibonacci')
    else:
        print(f'O termo "{ntermos}" pertence a sequencia de Fibonacci')

ntermos = int(input('Digite o número de termos da sequencia de Fibonacci: '))

for i in range(ntermos):
    print(fib(i))
verificafib(ntermos)