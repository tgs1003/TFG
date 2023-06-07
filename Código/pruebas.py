#algoritmo que busca la secuencia más larga de caracteres iguales entre 2 cadenas
#ejemplo: "abcde" y "abccde" -> "abc"

def secuencia_mas_larga(cadena1, cadena2):
    secuencia = ""
    for i in range(len(cadena1)):
        for j in range(len(cadena2)):
            if cadena1[i] == cadena2[j]:
                secuencia += cadena1[i]
                i += 1
                j += 1
            else:
                break
    return secuencia
print(secuencia_mas_larga("abcde", "abccde"))

