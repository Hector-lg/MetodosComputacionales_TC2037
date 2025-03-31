def lexetAritmetico(texto):
    # Diccionario para clasificar los caracteres
    dic = {
        'd': '0123456789', 
        'l': 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', 
        'suma': '+', 
        'resta': '-', 
        'mult': '*', 
        'div': '/', 
        'pot': '^',
        'igual': '=',
        'pa': '(', 
        'pc': ')', 
        'punto': '.',
        'guion': '_',
        'b': ' \t\n'
    }
    
    # Tabla de transiciones: estados x tipos de entrada
    # Estados:
    # 0 = inicio
    # 1 = entero
    # 2 = punto decimal
    # 3 = real
    # 4 = variable
    # 5 = exponente
    # 6 = signo exponente
    # 7 = valor exponente
    # 8-14 = operadores y simbolos
    # 15 = posible comentario
    # 16 = comentario
    # 99 = error
    
    tabla = {
        0: {'d': 1, 'l': 4, 'suma': 8, 'resta': 9, 'mult': 10, 'div': 15, 
            'pot': 11, 'pa': 12, 'pc': 13, 'igual': 14, 'punto': 2, 'b': 0},
        1: {'d': 1, 'punto': 2, 'l': 99, 'b': 0, 'suma': 8, 'resta': 9, 
            'mult': 10, 'div': 15, 'pot': 11, 'pa': 12, 'pc': 13, 'igual': 14, 'e': 5, 'E': 5},
        2: {'d': 3, 'l': 99, 'suma': 99, 'resta': 99, 'mult': 99, 
            'div': 99, 'pot': 99, 'pa': 99, 'pc': 99, 'igual': 99},
        3: {'d': 3, 'l': 99, 'b': 0, 'suma': 8, 'resta': 9, 'mult': 10, 
            'div': 15, 'pot': 11, 'pa': 12, 'pc': 13, 'igual': 14, 'e': 5, 'E': 5},
        4: {'d': 4, 'l': 4, 'guion': 4, 'b': 0, 'suma': 8, 'resta': 9, 
            'mult': 10, 'div': 15, 'pot': 11, 'pa': 12, 'pc': 13, 'igual': 14},
        5: {'d': 7, 'suma': 6, 'resta': 6},
        6: {'d': 7},
        7: {'d': 7, 'b': 0, 'suma': 8, 'resta': 9, 'mult': 10, 
            'div': 15, 'pot': 11, 'pa': 12, 'pc': 13, 'igual': 14},
        8: {'b': 0, 'd': 1, 'l': 4, 'punto': 2},
        9: {'b': 0, 'd': 1, 'l': 4, 'punto': 2},
        10: {'b': 0, 'd': 1, 'l': 4, 'punto': 2},
        11: {'b': 0, 'd': 1, 'l': 4, 'punto': 2},
        12: {'b': 0, 'd': 1, 'l': 4, 'punto': 2, 'resta': 9},
        13: {'b': 0, 'suma': 8, 'resta': 9, 'mult': 10, 'div': 15, 
             'pot': 11, 'pa': 12, 'pc': 13, 'igual': 14},
        14: {'b': 0, 'd': 1, 'l': 4, 'punto': 2, 'resta': 9},
        15: {'div': 16, 'b': 0, 'd': 1, 'l': 4, 'punto': 2, 'resta': 9},
        16: {c: 16 for c in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+-*/^()=_. \t'},
    }
    
    # Mapeo de estados finales a tipos de token
    tipos_token = {
        1: "Entero",
        3: "Real",
        4: "Variable",
        7: "Real",
        8: "Suma",
        9: "Resta",
        10: "Multiplicacion",
        11: "Potencia",
        12: "Parentesis que abre",
        13: "Parentesis que cierra",
        14: "Asignacion",
        15: "Division",
        16: "Comentario"
    }
    
    estado = 0
    lexema = ""
    tokens = []
    i = 0
    
    while i < len(texto):
        caracter = texto[i]
        
        # Determinar tipo de entrada
        tipo_entrada = None
        for tipo, chars in dic.items():
            if caracter in chars:
                tipo_entrada = tipo
                break
        
        # Si no esta en el diccionario usar el mismo caracter para E y e
        if tipo_entrada is None:
            tipo_entrada = caracter
        
        # Verificar si la transicion puede er valida
        if estado in tabla and tipo_entrada in tabla[estado]:
            nuevo_estado = tabla[estado][tipo_entrada]
            
            # Si pasamos a otro estado y el actual es un estado final, procesar el token
            if nuevo_estado != estado and estado in tipos_token:
                if estado == 16:  # Para comentarios, incluir // y el contenido
                    tokens.append((lexema, tipos_token[estado]))
                    lexema = ""
                elif estado != 0:  # No procesar tokens desde el estado inicial
                    tokens.append((lexema, tipos_token[estado]))
                    lexema = ""
            
            # Actualizar estado
            estado = nuevo_estado
            
            # Solo agregar al lexema si no es un espacio en blanco (excepto en comentarios)
            if not (tipo_entrada == 'b' and estado != 16) or (estado == 16 and caracter == '\n'):
                if not (tipo_entrada == 'b' and estado == 0):
                    lexema += caracter
            
            # Caso especial: fin de comentario en nueva linea
            if estado == 16 and caracter == '\n':
                tokens.append((lexema, tipos_token[estado]))
                lexema = ""
                estado = 0
                
        else:
            # Error: transicion no definida
            print(f"Error: caracter '{caracter}' inesperado en estado {estado}")
            if lexema:
                print(f"Lexema parcial: '{lexema}'")
            estado = 0
            lexema = ""
            
        i += 1
    
    # Procesar el ultimo token si queda alguno
    if lexema and estado in tipos_token:
        tokens.append((lexema, tipos_token[estado]))    
    return tokens

# Ejemplo de uso
if __name__ == "__main__":
    # Este codigo se ejecutara solo si el archivo se ejecuta directamente
    texto_ejemplo = "b=7\na = 32.4 *(-8.6 - b)/       6.1E-8\nd = a ^ b // Esto es un comentario"
    print("\nEjemplo:")
    tokens = lexetAritmetico(texto_ejemplo)
    print("\nToken\t\tTipo")
    print("-" * 30)
    for token, tipo in tokens:
        print(f"{token}\t\t{tipo}")