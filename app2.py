import random

#listas de palavras para o jogo
palavras = ['maçã', 'banana', 'laranja', 'uva', 'morango']

def jogo_da_forca():
    #escolhe uma palavra aleatoria da lista
    palavra = random.choice(palavras)
    #crie uma lista para armazenar as letras corretas
    letras_corretas = ['_'] * len(palavras)
    #crie uma lista para armazenar as letras erradas
    letras_erradas = []
    #define o numero de tentativas
    tentativas = 6

    print("bem vido ao jogo da forca!")
    print("você tem 6 tentativas para adivinha a palvra.")

    while tentativas > 0 and '_' in letras_corretas:
        #mostra a palvra com as letras corretas
        print(' '.join(letras_corretas))
        #pede ao usuario para digitar uma letra
        letra = input("digite uma letra: ").lower()
        #verificar se a letra é correta
        if letra in palavra:
            #subistitui as letras corretas na lista
            for i, l in enumerate(palavra):
                if l == letra:
                    letras_corretas[i] = letra
        else:
            #adiciona a letra errada a lista
            letras_erradas.append(letra)
            #diminui o numero de tentativas
            tentativas -= 1
            print(f"tentativas restantes : {tentativas}")
            print(f"letras erradas: {','.join(letras_erradas)}")   

    #verificar se o usuario ganhou ou perdeu
    if '_' not in letras_corretas:
        print("parabens! você ganhou!")
    else:
        print(f"vecê perdeu! a palavra era {palavra}.")

#inicia o jogo
jogo_da_forca()                                     