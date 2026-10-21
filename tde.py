# Implementação das funções pedidas no documento lista_dominio_condicional.docx,
# disponibilisado no AVA do Curso de Raciocínio Matemático para Computação.

import math

VERMELHO = "\033[31m"
VERDE = "\033[32m"
CIANO = "\033[36m"
RESET = "\033[0m"

# Questão A -> √(2x-8)
questao_a = lambda x: math.sqrt(2*x - 8)
dominio_a = lambda x: x >= 4

# Questão B -> √(x²-2x-8)
questao_b = lambda x: math.sqrt(x**2 - 2*x - 8)
dominio_b = lambda x: (x <= -2 or x >= 4)

# Questão C -> (2x-1)/(x²-5x+6)
questao_c = lambda x: (2*x - 1)/(x**2 - 5*x + 6)
dominio_c = lambda x: (x != 2 and x != 3)

# Questão D -> Ln(4-2x)
questao_d = lambda x: math.log(4 - 2*x)
dominio_d = lambda x: x < 2

# def para cast int na resposta
def cast_int(resp):
    try:
        return int(resp)
    except:
        print(f"{VERMELHO}O valor inserido não era um Número! Valor:{RESET} {resp}\n")
        return None

# função genérica que recebe valor de x, espressão a calcular e domínio da função.
def avaliar_funcao(resp, caulculo_funcao, condicao_dominio):
    x = cast_int(resp)
    try:
        # cast falhou
        if x is None:
            return False
        # cast funcionou e x dentro do dominio
        if condicao_dominio(x):
            return caulculo_funcao(x)
        # valor de x fora do dominio
        else:
            print(f"{VERMELHO}O valor de x não está no domínio da função F(x)!{RESET}\n")
            return False
                   
    except NameError:
        print(NameError)

def main():
    questoes = [
        (f"{CIANO}Digite um valor de X para a expressão √( 2x - 8 ): {RESET}", questao_a, dominio_a),
        (f"{CIANO}Digite um valor de X para a expressão √( x² - 2x - 8 ): {RESET}", questao_b, dominio_b),
        (f"{CIANO}Digite um valor de X para a expressão ( 2x + 1 ) / ( x² - 5x + 6 ): {RESET}", questao_c, dominio_c),
        (f"{CIANO}Digite um valor de X para a expressão ln( 4 - 2x ): {RESET}", questao_d, dominio_d)
    ]
    
    # itera sobre a lista de tuplas que contem as msg que aparecem no terminal, as espressoes a serem calculadas e os dominios das espressoes
    for msg_input, funcao_calc, funcao_dom in questoes:
        while True:
            var = input(msg_input)
            resp = avaliar_funcao(var, funcao_calc, funcao_dom)
            
            # resp false repete o loop
            if resp is False:
                continue
            
            # break faz o codigo voltar ao for, oque inicia a proxima questao
            print(f"{VERDE}Resultado: {resp}{RESET}\n")
            break
        
if __name__ == "__main__":
    main()
    
    
