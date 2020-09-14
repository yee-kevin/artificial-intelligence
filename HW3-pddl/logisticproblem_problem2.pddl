(define (problem logisticproblem2)
  (:domain logisticproblem)
  (:objects truck package1 package2 tampinese changi bedok)
  (:init (truck truck)
    (package package1)
    (package package2)
    (location tampinese)
    (location changi)    
    (location bedok)
    (at-truck truck tampinese)
    (at-package package1 bedok)
    (at-package package2 changi)
    (road tampinese changi)
    (road changi tampinese)
    (road changi bedok)
    (road bedok changi)
    (road tampinese bedok)
    (road bedok tampinese))

  (:goal (and (at-package package1 changi) (at-package package2 bedok))))