# Implementação da Regra do Trapézio

## Introdução

Esse código tem como objetivo aproximar o valor de uma integral definida, utilizando a regra do trapézio. A regra do trapézio é um método de integração numérica que se baseia em aproximar a área abaixo de uma curva pela área de trapézios que têm a mesma base e altura da curva em um intervalo de integração.

A fórmula utilizada para calcular a integral utilizando a regra do trapézio é:

$$ \int_a^b f(x) ,dx \approx \frac{b-a}{2n} [f(a) + 2f(a+h) + 2f(a+2h) + \cdots + 2f(a+(n-1)h) + f(b)] $$

onde $n$ é o número de subintervalos do intervalo de integração, $h = \frac{b-a}{n}$ e $f(x)$ é a função a ser integrada.

## Função

A função principal do programa é a `trapezio`, que recebe quatro parâmetros: a função a ser integrada `funcao_fx`, os limites do intervalo de integração `intervalo_1` e `intervalo_2` e o número de subintervalos `iteracoes`. A função utiliza a regra do trapézio para calcular a integral definida da função dentro do intervalo fornecido.

```python
def trapezio(funcao_fx, intervalo_1, intervalo_2, iteracoes):
```

## Entrada de dados

O programa inicia solicitando ao usuário a expressão matemática da função que deseja integrar, que deve ser digitada em uma única linha e ser compatível com a biblioteca sympy. A expressão é lida como uma string e, em seguida, convertida em uma expressão matemática manipulável pela biblioteca `sympy`. Em seguida, o programa solicita ao usuário os limites do intervalo de integração, onde o primeiro intervalo deve ser digitado antes do segundo intervalo, e o número de subintervalos desejado para calcular a integral aproximada usando a regra do trapézio.

## Saída de dados

O programa imprime o valor aproximado da integral definida da função utilizando a regra do trapézio. Além disso, o programa também calcula o valor real da integral e o erro cometido na aproximação.

## Execução

Para rodar o aplicativo em Python, basta executar o código em qualquer ambiente que suporte a linguagem Python 3. 

```bash
python3 regra_do_trapezio.py
```

O código utiliza as bibliotecas `sympy` e `numpy`, portanto, é necessário ter essas bibliotecas instaladas no ambiente em que o código será executado.
