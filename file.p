%%% ARITHMETIC %%%
cnf(a,axiom, mul(X, Y) = mul(Y, X)).
cnf(a,axiom, plus(X, Y) = plus(Y, X)).
cnf(a,axiom, mul(X, mul(Y, Z)) = mul(mul(X, Y), Z)).
cnf(a,axiom, plus(X, plus(Y, Z)) = plus(plus(X, Y), Z)).

cnf(a,axiom, mul(zero, X) = zero).
cnf(a,axiom, mul(one, X) = X).
cnf(a,axiom, plus(zero, X) = X).

cnf(a,axiom, mul(plus(A, B), C) = plus(mul(A, C), mul(B, C))).

%%% VECTORS %%%
% every vector and matrix is of size 'size'.
% It is encoded as a function that we call with numbers '0..size'.

cnf(a,axiom, dot(A, B) = sum(lam(X, mul(app(A, X), app(B, X))))).

cnf(a,axiom, memset(C) = lam(X, C)).
cnf(a,axiom, sum(memset(C)) = mul(C, size)).

cnf(a,axiom, lhs = dot(memset(n20), memset(n21))).
cnf(a,axiom, rhs = dot(memset(n21), memset(n20))).

cnf(a,axiom, lhs != rhs).
