import sympy as sp

def trapezio(funcao_fx, intervalo_1, intervalo_2, iteracoes):
    
    # Calculado o valor de h, que é a largura de cada subintervalo do intervalo de integração.
    h = (intervalo_2 - intervalo_1) / iteracoes
    
    # Soma recebe o valor da função funcao_fx nos extremos do intervalo de integração.
    soma = funcao_fx(intervalo_1) + funcao_fx(intervalo_2)
    
    
    # Aqui, é feita a soma dos valores da função funcao_fx nos pontos intermediários do intervalo de integração, ponderados por um fator de 2, 
    # pois esses pontos são contabilizados duas vezes no cálculo da área do trapézio.
    for i in range(1, iteracoes):
        soma += 2 * funcao_fx(intervalo_1 + i * h)
        
    # Área total dos trapézios é calculada multiplicando-se a soma pelo valor de h e dividindo-se por 2, já que cada trapézio tem uma base menor 
    # de h e uma base maior que é a soma das duas avaliações da função em cada ponto intermediário.
    integral = h * soma / 2
    
    return integral


# Lê a função do usuário e transforma em expressão matemática para que possa ser manipulada na função
expr_str = input("Digite a expressão matemática da função: ")
expr = sp.sympify(expr_str)

# Define os intervalos e o número de divisões, lendo pelo input
intervalo_1 = float(input("Determine o primeiro intervalo: "))
intervalo_2 = float(input("Determine o segundo intervalo: "))
iteracoes = int(input("Determine quantas iterações serão feitas: "))

# Define a função a ser integrada a partir da expressão lida, assim o 'x' não será mais uma string
funcao_fx = lambda x: expr.subs('x', x)

# Calcula a aproximação da integral usando a regra do trapézio
integral = trapezio(funcao_fx, intervalo_1, intervalo_2, iteracoes)

# Imprime o resultado
print("\n\nO polinômio lido é:", sp.simplify(expr_str))
print(f"Com intervalos de [{intervalo_1}, {intervalo_2}] com {iteracoes} iterações")
print("Sua aproximação foi de:", sp.simplify(integral))

# Calcula o valor da integral sem usar nenhum método de aproximação
x = sp.Symbol('x')
integral_real = sp.integrate(funcao_fx(x), (x, intervalo_1, intervalo_2))

print("Sua integral real tem valor de:", sp.simplify(integral_real))

erro = integral - integral_real
print("O erro da aproximação foi de:", format(erro, '9f'))
