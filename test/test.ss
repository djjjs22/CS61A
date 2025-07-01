(define (line) (fd 50))

(define (repeat k fn) 
    (fn)
    (if (> k 1) (repeat (- k 1) fn)))

(define (tri fn)
    (repeat 3 (lambda () (fn) (lt 120))))

(define (sier d k)
  (tri (lambda () (if (= d 1) (fd k) (leg d k)))))

(define (leg d k)
  (sier (- d 1) (/ k 2))
  (pendown) (fd k) (penup))

(sier 3 100)