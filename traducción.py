# Diccionario de codones del ARN a aminoácidos
codon_a_aminoacido = {
    'AUG': 'Metionina', 'UUU': 'Fenilalanina', 'UUC': 'Fenilalanina',
    'UUA': 'Leucina', 'UUG': 'Leucina', 'UCU': 'Serina', 'UCC': 'Serina',
    'UCA': 'Serina', 'UCG': 'Serina', 'UAU': 'Tirosina', 'UAC': 'Tirosina',
    'UGU': 'Cisteína', 'UGC': 'Cisteína', 'UGG': 'Triptofano', 'CUU': 'Leucina',
    'CUC': 'Leucina', 'CUA': 'Leucina', 'CUG': 'Leucina', 'CCU': 'Prolina',
    'CCC': 'Prolina', 'CCA': 'Prolina', 'CCG': 'Prolina', 'CAU': 'Histidina',
    'CAC': 'Histidina', 'CAA': 'Glutamina', 'CAG': 'Glutamina', 'CGU': 'Arginina',
    'CGC': 'Arginina', 'CGA': 'Arginina', 'CGG': 'Arginina', 'AUU': 'Isoleucina',
    'AUC': 'Isoleucina', 'AUA': 'Isoleucina', 'ACU': 'Treonina', 'ACC': 'Treonina',
    'ACA': 'Treonina', 'ACG': 'Treonina', 'AAU': 'Asparagina', 'AAC': 'Asparagina',
    'AAA': 'Lisina', 'AAG': 'Lisina', 'AGU': 'Serina', 'AGC': 'Serina',
    'AGA': 'Arginina', 'AGG': 'Arginina', 'GUU': 'Valina', 'GUC': 'Valina',
    'GUA': 'Valina', 'GUG': 'Valina', 'GCU': 'Alanina', 'GCC': 'Alanina',
    'GCA': 'Alanina', 'GCG': 'Alanina', 'GAU': 'Ácido aspártico', 'GAC': 'Ácido aspártico',
    'GAA': 'Ácido glutámico', 'GAG': 'Ácido glutámico', 'GGU': 'Glicina',
    'GGC': 'Glicina', 'GGA': 'Glicina', 'GGG': 'Glicina', 'UAA': 'Parada',
    'UAG': 'Parada', 'UGA': 'Parada'
}

# Función para traducir ARN a proteína
def traducir_arn_a_proteina(cadena_arn):
    # Validación de caracteres
    if not all(nuc in 'AUCG' for nuc in cadena_arn):
        return "Error: La cadena de ARN contiene caracteres no válidos."
    
    mensaje = ""  # Mensaje informativo

    # Verificar codón de inicio
    if not cadena_arn.startswith('AUG'):
        mensaje += "Advertencia: La cadena de ARN no comienza con el codón de inicio (AUG).\n"
    
    # Verificar codón de parada
    codones_parada = {'UAA', 'UAG', 'UGA'}
    if cadena_arn[-3:] not in codones_parada:
        mensaje += "Advertencia: La cadena de ARN no termina con un codón de parada válido (UAA, UAG, UGA).\n"
    
    # Traducción
    proteina = []
    for i in range(0, len(cadena_arn) - len(cadena_arn) % 3, 3):  # Ignora codones incompletos
        codon = cadena_arn[i:i+3]
        aminoacido = codon_a_aminoacido.get(codon, 'Desconocido')
        if aminoacido == 'Parada':
            break
        proteina.append(aminoacido)
    
    if proteina:
        mensaje += f"La proteína traducida es: {'-'.join(proteina)}"
    else:
        mensaje += "No se puede traducir porque la cadena comeizna con un codón de parada."
    
    return mensaje
