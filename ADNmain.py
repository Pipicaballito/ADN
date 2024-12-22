import transcripción
import traducción  

def es_arn_valido(cadena_arn):
    return all(nuc in 'AUGC' for nuc in cadena_arn)

def encontrar_superposicion_maxima(str1, str2):
    longitud_maxima = min(len(str1), len(str2))
    for i in range(longitud_maxima, 0, -1):
        if str1.endswith(str2[:i]):
            return str1 + str2[i:]
    return None

def ensamblar_genoma(fragmentos):
    while len(fragmentos) > 1:
        superposicion_maxima = ""
        combinacion = (0, 0)
        for i in range(len(fragmentos)):
            for j in range(len(fragmentos)):
                if i != j:
                    superposicion = encontrar_superposicion_maxima(fragmentos[i], fragmentos[j])
                    if superposicion and len(superposicion) > len(superposicion_maxima):
                        superposicion_maxima = superposicion
                        combinacion = (i, j)
        
        i, j = combinacion
        fragmentos[i] = superposicion_maxima
        fragmentos.pop(j)
    
    return fragmentos[0]

def mainmenu():
    op1 = "1: Transcribir un fragmento "
    op2 = "2: Traducir un fragmento "
    op3 = "3: Dividir en codones el ARN "
    op4 = "4: Mostrar todos los posibles codones con sus aminoácidos correspondientes"
    op5 = "5: Proceso completo(transcribir, traducir y dividir en codones una cadena de ADN)"
    op6 = "6: Ensamblar genoma a partir de fragmentos"
    op7 = "7: Salir"

    print("\n{0} \n{1} \n{2} \n{3} \n{4} \n{5} \n{6}".format(op1, op2, op3, op4, op5, op6, op7))
    
    c = True
    while c:
        o = input("Seleccione una opción: ")
        if o == "1":
            cadena_adn = input("Escribe la cadena de ADN a transcribir: ")
            result = transcripción.transcribir_adn_a_arn(cadena_adn)
            print(f"Secuencia complementaria: {result}")
        elif o == "2":
            cadena_arn = input("Escribe la cadena de ARN a traducir: ")
            proteina = traducción.traducir_arn_a_proteina(cadena_arn)
            print(f"Secuencia de proteína: {proteina}")
        elif o == "3":
            cadena_arn = input("Escribe la secuencia de ARN para dividir en codones: ")
            
            if es_arn_valido(cadena_arn):
                codones = [cadena_arn[i:i+3] for i in range(0, len(cadena_arn), 3)]
                
                if len(codones[-1]) < 3:
                    print(f"Advertencia: El último codón está incompleto: {codones[-1]}")
                    codones = codones[:-1]
                
                print("Codones:", codones)
            else:
                print("La secuencia de ARN contiene caracteres no válidos. Solo se permiten A, U, C, G.")
        elif o == "4":
            print("Codones y sus aminoácidos correspondientes:")
            for codon, aminoacido in traducción.codon_a_aminoacido.items():
                print(f"{codon}: {aminoacido}")
        elif o == "5":
            cadena_adn = input("Escribe la cadena de ADN para el proceso completo: ")
            cadena_arn = transcripción.transcribir_adn_a_arn(cadena_adn)
            print(f"Secuencia de ARN transcrita: {cadena_arn}")
            proteina = traducción.traducir_arn_a_proteina(cadena_arn)
            print(f"Secuencia de proteína: {proteina}")
        elif o == "6":
            fragmentos = []
            while True:
                fragmento = input("Ingrese un fragmento de ADN (o 'done' para finalizar): ")
                if fragmento.lower() == 'done':
                    break
                fragmentos.append(fragmento)
            
            if fragmentos:
                genoma_completo = ensamblar_genoma(fragmentos)
                print(f"Genoma ensamblado: {genoma_completo}")
            else:
                print("No se ingresaron fragmentos.")
        elif o == "7":
            print("Saliendo del programa.")
            c = False
        else:
            print("Opción no válida, por favor seleccione una opción del 1 al 7.")

mainmenu()
