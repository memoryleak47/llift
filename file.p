cnf(a,axiom, f = lam(X, lam(Y, plus(X,Y)))).
cnf(a,axiom, double(X) = plus(X,X)).
cnf(a,axiom, app(app(f, b), b) != double(b)).

%cnf(a,axiom, f = lam(X, X)).
%cnf(a,axiom, app(f, a) != a).

%cnf(a,axiom, cst(X) = lam(Y, X)).
%cnf(a,axiom, app(cst(a), b) != a).
