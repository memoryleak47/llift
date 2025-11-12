%%% ARITHMETIC %%%
cnf(a,axiom, mul(X, Y) = mul(Y, X)).
cnf(a,axiom, plus(X, Y) = plus(Y, X)).

cnf(a,axiom, mul(zero, X) = zero).
cnf(a,axiom, mul(one, X) = X).
cnf(a,axiom, plus(zero, X) = X).

% RULES WITH NOTABLE BLOW-UP

% cnf(a,axiom, mul(plus(A, B), C) = plus(mul(A, C), mul(B, C))).
% cnf(a,axiom, mul(X, mul(Y, Z)) = mul(mul(X, Y), Z)).
% cnf(a,axiom, plus(X, plus(Y, Z)) = plus(plus(X, Y), Z)).

%%% VECTORS %%%
% every vector and matrix is of size 'size'.
% It is encoded as a function that we call with numbers '0..size'.

cnf(a,axiom, dot(A, B) = sum(lam(X, mul(app(A, X), app(B, X))))).

cnf(a,axiom, memset(C) = lam(X, C)).
cnf(a,axiom, sum(memset(C)) = mul(C, size)).

cnf(a,axiom, transpose(A) = lam(X, lam(Y, app(app(A, Y), X)))).

% should this be transpose(A)?
cnf(a,axiom, mv(A, B) = lam(X, dot(app(A, X), B))).

% do these indices make sense?
cnf(a,axiom, mm(A, B) = lam(X, mv(A, app(B, X)))).


% Things we are able to prove:
%cnf(a,axiom, dot(x,y) != dot(y,x)).
%cnf(a,axiom, zero != app(mv(memset(memset(bar)), memset(zero)), any)).
%cnf(a,axiom, zero != app(mv(memset(memset(zero)), memset(foo)), any)).
%cnf(a,axiom, size != app(mv(memset(memset(one)), memset(one)), any)).
%cnf(a,axiom, transpose(transpose(aa)) != aa).
