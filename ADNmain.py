import transcripción
import traducción  

def es_arn_valido(cadena_arn):
    # Verifica que la cadena de ARN contenga solo los caracteres válidos: A, U, C, G
    return all(nuc in 'AUGC' for nuc in cadena_arn)

def mainmenu():
    op1 = "1: Transcribir un fragmento "
    op2 = "2: Traducir un fragmento "
    op3 = "3: Dividir en codones el ARN "
    op4 = "4: Mostrar todos los posibles codones con sus aminoácidos correspondientes"
    op5 = "5: Proceso completo(transcribir, traducir y dividir en codones una cadena de ADN)"
    op6 = "6: Salir"

    print("\n{0} \n{1} \n{2} \n{3} \n{4} \n{5}".format(op1, op2, op3, op4, op5, op6))
    
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
            
            # Validar que la cadena de ARN sea válida
            if es_arn_valido(cadena_arn):
                # Dividir la cadena en codones
                codones = [cadena_arn[i:i+3] for i in range(0, len(cadena_arn), 3)]
                
                # Verificar si el último codón es incompleto
                if len(codones[-1]) < 3:
                    print(f"Advertencia: El último codón está incompleto: {codones[-1]}")
                    codones = codones[:-1]  # Eliminar el último codón incompleto
                
                print("Codones:", codones)
            else:
                print("La secuencia de ARN contiene caracteres no válidos. Solo se permiten A, U, C, G.")
        elif o == "4":
            print("Codones y sus aminoácidos correspondientes:")
            for codon, aminoacido in traducción.codon_a_aminoacido.items():
                print(f"{codon}: {aminoacido}")
        elif o == "5":
            cadena_adn = input("Escribe la cadena de ADN para el proceso completo: ")
            # Primero transcribimos la cadena de ADN a ARN
            cadena_arn = transcripción.transcribir_adn_a_arn(cadena_adn)
            print(f"Secuencia de ARN transcrita: {cadena_arn}")
            # Luego traducimos el ARN a proteína
            proteina= traducción.traducir_arn_a_proteina(cadena_arn)
            print(f"Secuencia de proteína: {proteina}")
        elif o == "6":
            print("Saliendo del programa.")
            c = False
        else:
            print("Opción no válida, por favor seleccione una opción del 1 al 6.")

mainmenu()