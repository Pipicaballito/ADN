import heapq

def encontrar_superposicion_maxima(str1, str2):
    longitud_maxima = min(len(str1), len(str2))
    for i in range(longitud_maxima, 0, -1):
        if str1.endswith(str2[:i]):
            return str1 + str2[i:]
    return None

def ensamblar_genoma(fragmentos):
    if not fragmentos:
        return ""

    while len(fragmentos) > 1:
        max_superposicion = ""
        best_pair = (0, 0)

        # Crear una cola de prioridad para almacenar las mejores superposiciones
        heap = []
        for i in range(len(fragmentos)):
            for j in range(i + 1, len(fragmentos)):
                superposicion = encontrar_superposicion_maxima(fragmentos[i], fragmentos[j])
                if superposicion:
                    heapq.heappush(heap, (-len(superposicion), (i, j), superposicion))

        while heap:
            _, (i, j), superposicion = heapq.heappop(heap)
            if fragmentos[i] and fragmentos[j]:
                fragmentos[i] = superposicion
                fragmentos[j] = ""
                break

        # Filtrar los fragmentos vacíos resultantes de la combinación
        fragmentos = [frag for frag in fragmentos if frag]

    return fragmentos[0]

