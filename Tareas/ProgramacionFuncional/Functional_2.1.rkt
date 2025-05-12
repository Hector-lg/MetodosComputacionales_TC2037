;1. La funci ́on fahrenheit-to-celsius toma como entrada una temperatura f en grados Fahrenheit y la
;convierte a su equivalente en grados Celsius usando la siguiente f ́ormula:
;C = 5(F − 32) / 9
;9
;Ejemplos:
;(fahrenheit-to-celsius 212.0)
;⇒ 100.0
;(fahrenheit-to-celsius 32.0)
;⇒ 0.0
;(fahrenheit-to-celsius -40.0)
;⇒ -40.0

(define (fahrenheit-to-celsius f)
  (* 5 (/ (- f 32) 9)))

(fahrenheit-to-celsius 212.0) ; ⇒ 100.0

;2. La funcion sign recibe como entrada un valor entero n. Devuelve -1 si n es negativo, 1 si n es positivo mayor
;que cero, o 0 si n es cero.
;Ejemplos:
;(sign -5)
;⇒ -1
;(sign 10)
;⇒ 1
;(sign 0)
;⇒ 0
(define (sign n)
  (cond
    ((< n 0) -1)
    ((> n 0) 1)
    (else 0)))

(sign -5) ; ⇒ -1

;3. La funcion root devuelve la raiz de una ecuacion cuadratica de la forma ax^2 + bx + c = 0. Recibe como
;entrada los coeficientes a, b y c. La funcion devuelve una lista con las dos raices de la ecuacion.
; x = (-b ± √(b^2 - 4ac)) / 2a

;Ejemplos:
;(root 2 4 2)
;=> -1

(define (root a b c)
    (define discriminant (- (* b b) (* 4 a c)))
  (if (< discriminant 0)
      '()
      (let ((sqrt-discriminant (sqrt discriminant)))
        (list (/ (+ (- b) sqrt-discriminant) (* 2 a))
              (/ (- (- b) sqrt-discriminant) (* 2 a))))))

(root 2 4 2) ; => -1


;4. El indicie de masa corporal (IMC) se calcula como el peso en kilogramos dividido por la altura en metros al cuadrado.
; se calcula usando la siguiente formula:
;IMC = peso / (altura * altura)
; Donde w es el peso en kilogramos y h es la altura en metros.
; Tabla de IMC:
; IMC < 20: Bajo peso
; 20 <= IMC < 25: Peso normal
; 25 <= IMC < 30: Sobrepeso 
; 30 <= IMC < 40: Obesidad 2
; IMC >= 40: Obesidad 3

; deve devolver un simplo que represente la descripcion de BMI correspondiente.
;Ejemplos:

;(bmi 45 1.7)
;=> "Bajo peso"

(define (bmi w h)
    (define imc (/ w (* h h)))
    (cond
        ((< imc 20) "Bajo peso")
        ((< imc 25) "Peso normal")
        ((< imc 30) "Sobrepeso")
        ((< imc 40) "Obesidad 2")
        (else "Obesidad 3")))

(bmi 45 1.7) ; => "Bajo peso"


;5. La funci on factorial toma un entero positivo n como su entrada y devuelve el factorial correspondiente, que
;matem aticamente se define as ́ı:
;n! =
;{
;1 Si n = 0
;n · (n − 1)! Si n > 0
;Ejemplos:
;(factorial 0)
;⇒ 1
;(factorial 5)
;⇒ 120

(define (factorial n)
(if (= n 0)
1
(* n (factorial (- n 1)))))

(factorial 0) ; ⇒ 1
(factorial 5) ; ⇒ 120


;6 la funcion duplicate toma una lista lst como entrada
; y devuelve una nueva lista donde cada elemento de lst esta duplicado.

;Ejemplos:
; (duplicate '())
; => '()
; (duplicate '(1 2 3))
; => '(1 1 2 2 3 3)
(define (duplicate lst)
  (if (null? lst)
      '()
      (cons (car lst) (cons (car lst) (duplicate (cdr lst))))))

(duplicate '()) ; => '()
(duplicate '(1 2 3)) ; => '(1 1 2 2 3 3)


; La funcion pow toma dos enteros a y b como entrada y devuelve a elevado a la potencia b.
;Ejemplos:
; (pow 2 3)
; => 8
; (pow 5 0)
; => 1

(define (pow a b)
(   if (= b 0)
        1 
    (* a (pow a (- b 1)))))

(pow 2 3) ; => 8
(pow 5 0) ; => 1