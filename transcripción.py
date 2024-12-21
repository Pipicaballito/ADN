def transcribir_adn_a_arn(cadena_adn):
    # Validación de entrada: solo aceptar caracteres válidos (A, T, C, G)
    for nucleotido in cadena_adn:
        if nucleotido not in 'ATCG':
            return "Error: La cadena contiene caracteres no válidos. Solo se permiten A, T, C, G."
    
    transcripcion = ""
    for nucleotido in cadena_adn:
        if nucleotido == 'A':
            transcripcion += 'U'  # Adenina -> Uracilo
        elif nucleotido == 'T':
            transcripcion += 'A'  # Timina -> Adenina
        elif nucleotido == 'C':
            transcripcion += 'G'  # Citosina -> Guanina
        elif nucleotido == 'G':
            transcripcion += 'C'  # Guanina -> Citosina
    
    return transcripcion
