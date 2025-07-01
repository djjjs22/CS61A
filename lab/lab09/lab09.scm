(define (over-or-under num1 num2) 
    'YOUR-CODE-HERE
    (cond 
         ((< num1 num2) -1)
         ((= num1 num2) 0)
         (else 1))
    )

(define (make-adder num)
  (lambda (inc) (+ inc num))
)
(define (make-adder num)
  (lambda (inc) (+ inc num))
)
(define (repeat f n)
; note: this relies on `composed` being implemented correctly
  (if (< n 1)
    (lambda (x) x)
    (composed f (repeat f (- n 1)))))
    
(define (max a b) (if (> a b) a b))
(define (min a b) (if (> a b) b a))
(define (gcd a b)
  (cond ((zero? a) b)
        ((zero? b) a)
        ((= (modulo (max a b) (min a b)) 0) (min a b))
        (else (gcd (min a b) (modulo (max a b) (min a b))))))
; (define (line) (fd 50))

; (define (repeat k fn)
;   (if (> k 1) (repeat (- k 1) fn) (fn)))

; (define (tri fn)
;   (repeat 3 (lambda () (fn) (lt 120))))

; (define (sier d k)
;   (tri (lambda () (if (= d 1) (fd k) (leg d k)))))


; (define (leg d k)
;   (sier (- d 1) (/ k 2))
;   (pendown) (fd k) (penup))

; (fd 0)
; (load 'ex.scm)
; (rt 90)
; (speed 0)
; (sier 3 100)