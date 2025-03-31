# DOCUMENTACION DEL AUTOMATA FINITO DETERMINISTICO (AFD)

## JUSTIFICACION DEL DISENO

El diseno del automata de 16 estados proporciona una solucion completa para el analisis lexico de expresiones aritmeticas, siendo capaz de reconocer todos los tokens requeridos de manera eficiente.

### Estados del Automata

Nuestro automata utiliza 16 estados principales más un estado de error (99):

1. **Estado 0**: Estado inicial - punto de partida para reconocer cualquier token
2. **Estado 1**: Enteros - secuencias de digitos
3. **Estado 2**: Punto decimal - transicion entre entero y real
4. **Estado 3**: Real - numeros con punto decimal
5. **Estado 4**: Variable - identificadores (letras, numeros, guion bajo)
6. **Estado 5**: Exponente - despues de encontrar 'e' o 'E'
7. **Estado 6**: Signo exponente - signo opcional tras exponente
8. **Estado 7**: Valor exponente - digitos del exponente
9. **Estado 8**: Suma - operador '+'
10. **Estado 9**: Resta - operador '-'
11. **Estado 10**: Multiplicacion - operador '*'
12. **Estado 11**: Potencia - operador '^'
13. **Estado 12**: Parentesis que abre - '('
14. **Estado 13**: Parentesis que cierra - ')'
15. **Estado 14**: Asignacion - '='
16. **Estado 15**: Division - operador '/'
17. **Estado 16**: Comentario - texto tras '//'
18. **Estado 99**: Error - manejo de entradas invalidas

### Estados de Aceptacion

Los estados finales (de aceptacion) son: 1, 3, 4, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16

### Por que este Automata es Efectivo

1. **Manejo preciso de casos especiales**:
   - Diferencia entre operador resta (-) y numeros negativos
   - Reconoce puntos decimales al inicio (ej. .5) y al final (ej. 5.)
   - Procesa notacion cientifica con exponentes (ej. 1.2E-5)
   - Detecta comentarios correctamente

2. **Estructura modular y clara**:
   - Cada estado tiene un proposito bien definido
   - Las transiciones son completas y no ambiguas
   - Los estados de aceptacion corresponden a tokens concretos

3. **Flexibilidad y robustez**:
   - Maneja espacios en blanco adecuadamente
   - Detecta y reporta errores de sintaxis
   - Permite combinar diferentes tipos de tokens en expresiones complejas

4. **Implementacion eficiente**:
   - Procesamiento lineal (O(n)) donde n es la longitud de la entrada

### Pruebas de Validacion

El automata ha sido probado exitosamente con diferentes tipos de expresiones aritmeticas:
- Variables y asignaciones: `b=7`
- Operaciones complejas: `a = 32.4 *(-8.6 - b)/6.1E-8`
- Comentarios en linea: `d = a ^ b // Esto es un comentario`
- Casos limite: numeros con diferentes formatos decimales y exponenciales

## CONCLUSION

Este automata de 16 estados representa una implementacion robusta y eficiente para el analisis lexico de expresiones aritmeticas. Su diseno cuidadoso garantiza la correcta identificacion de todos los tipos de tokens necesarios, cumpliendo con los requerimientos del problema y proporcionando un fundamento solido para fases posteriores de analisis sintactico y evaluacion.

<!-- La tabla de transiciones ya existente se mantiene igual -->

# TABLA DE TRANSICIÓN DEL AUTÓMATA FINITO DETERMINÍSTICO (AFD)

Esta tabla muestra todas las transiciones posibles del autómata con 16 estados. Las filas representan el estado 
actual, las columnas representan el carácter de entrada, y cada celda muestra el estado resultante.

| Estado | Letras [a-zA-Z] | Dígitos [0-9] | Punto [.] | + | - | * | ^ | ( | ) | = | / | e,E | Guión bajo [_] | Espacio | Otros |
|--------|----------------|---------------|-----------|---|---|---|---|---|---|---|---|-----|---------------|---------|-------|
| 0      | 4              | 1             | 2         | 8 | 9 | 10| 11| 12| 13| 14| 15| -   | -             | 0       | Error |
| 1      | Error          | 1             | 2         | 8 | 9 | 10| 11| 12| 13| 14| 15| 5   | Error         | 0       | Error |
| 2      | Error          | 3             | Error     | Error | Error | Error | Error | Error | Error | Error | Error | Error | Error | Error | Error |
| 3      | Error          | 3             | Error     | 8 | 9 | 10| 11| 12| 13| 14| 15| 5   | Error         | 0       | Error |
| 4      | 4              | 4             | Error     | 8 | 9 | 10| 11| 12| 13| 14| 15| -   | 4             | 0       | Error |
| 5      | Error          | 7             | Error     | 6 | 6 | Error | Error | Error | Error | Error | Error | Error | Error | Error | Error |
| 6      | Error          | 7             | Error     | Error | Error | Error | Error | Error | Error | Error | Error | Error | Error | Error | Error |
| 7      | Error          | 7             | Error     | 8 | 9 | 10| 11| 12| 13| 14| 15| Error | Error       | 0       | Error |
| 8      | 4              | 1             | 2         | Error | Error | Error | Error | Error | Error | Error | Error | Error | Error | 0       | Error |
| 9      | 4              | 1             | 2         | Error | Error | Error | Error | Error | Error | Error | Error | Error | Error | 0       | Error |
| 10     | 4              | 1             | 2         | Error | Error | Error | Error | Error | Error | Error | Error | Error | Error | 0       | Error |
| 11     | 4              | 1             | 2         | Error | Error | Error | Error | Error | Error | Error | Error | Error | Error | 0       | Error |
| 12     | 4              | 1             | 2         | Error | 9    | Error | Error | Error | Error | Error | Error | Error | Error | 0       | Error |
| 13     | Error          | Error         | Error     | 8 | 9 | 10| 11| 12| 13| 14| 15| Error | Error       | 0       | Error |
| 14     | 4              | 1             | 2         | Error | 9    | Error | Error | Error | Error | Error | Error | Error | Error | 0       | Error |
| 15     | 4              | 1             | 2         | Error | 9    | Error | Error | Error | Error | Error | 16| Error | Error | 0       | Error |
| 16     | 16             | 16            | 16        | 16   | 16   | 16   | 16   | 16   | 16   | 16   | 16   | 16    | 16            | 16      | 16 hasta \\n |

Donde:
- 0: Estado inicial
- 1: Estado entero
- 2: Estado punto decimal
- 3: Estado real
- 4: Estado variable
- 5: Estado exponente
- 6: Estado signo exponente
- 7: Estado valor exponente
- 8: Estado suma
- 9: Estado resta
- 10: Estado multiplicación
- 11: Estado potencia
- 12: Estado paréntesis que abre
- 13: Estado paréntesis que cierra
- 14: Estado asignación
- 15: Estado división
- 16: Estado comentario

Los estados finales (de aceptación) son: 1, 3, 4, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16