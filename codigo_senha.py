"""
Módulo Validador de Senhas Forte.

Este script verifica se uma senha atende aos requisitos mínimos de segurança
definidos para autenticação de usuários.
"""

from typing import Tuple


def validar_senha(senha: str) -> Tuple[bool, str]:
    """
    Valida a força de uma senha com base em critérios pré-definidos.

    Parâmetros:
        senha (str): A string contendo a senha a ser avaliada.

    Retorna:
        Tuple[bool, str]: Uma tupla contendo o status da validação (True/False)
                          e uma mensagem explicativa.
    """
    if len(senha) < 8:
        return False, "A senha deve conter pelo menos 8 caracteres."

    tem_maiuscula = False
    tem_minuscula = False
    tem_numero = False

    for caractere in senha:
        if caractere.isupper():
            tem_maiuscula = True
        elif caractere.islower():
            tem_minuscula = True
        elif caractere.isdigit():
            tem_numero = True

    if not tem_maiuscula:
        return False, "A senha deve conter pelo menos uma letra maiúscula."
    if not tem_minuscula:
        return False, "A senha deve conter pelo menos uma letra minúscula."
    if not tem_numero:
        return False, "A senha deve conter pelo menos um número."

    return True, "Senha forte e válida!"


if __name__ == "__main__":
    print("--- Testador de Senha Forte ---")
    entrada_usuario = input("Digite uma senha para testar: ")
    eh_valida, mensagem = validar_senha(entrada_usuario)

    if eh_valida:
        print(f"[SUCESSO] {mensagem}")
    else:
        print(f"[ERRO] {mensagem}")