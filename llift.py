import sys

CTR = 0
outs = []

def reformat(e):
    e = parse_expr(e)
    e = lift(e)
    return stringify(e)

# e is a term, not a string.
def vars_of(e):
    if type(e) == str:
        assert("(" not in e)
        if e.islower():
            return set()
        else:
            return {e}
    s = set()
    for x in e[1]:
        s = s.union(vars_of(x))
    return s

# converts term to term
def lift(e):
    global CTR

    if type(e) == str:
        return e
    args = [lift(x) for x in e[1]]
    if e[0] != "lam":
        return (e[0], args)

    [var, body] = args

    name = "lifted" + str(CTR)
    vs = vars_of(body) - set(var)
    if vs:
        applied = (name, vs)
    else:
        applied = name

    CTR += 1

    outs.append("cnf(a,axiom, app(" + stringify(applied) + ", " + var + ")  = " + stringify(body) + ").")
    return applied

def stringify(e):
    if type(e) != tuple:
        return e
    op = e[0]
    args = e[1]
    return op + "(" + ", ".join([stringify(x) for x in args]) + ")"

def parse_expr(s):
    s = s.strip()
    pos = 0

    def skip_ws():
        nonlocal pos
        while pos < len(s) and s[pos].isspace():
            pos += 1

    def parse_ident():
        nonlocal pos
        start = pos
        while pos < len(s) and s[pos] not in '(), \t\n\r':
            pos += 1
        if start == pos:
            raise ValueError(f"Expected identifier at {pos}")
        return s[start:pos]

    def parse_expr_inner():
        nonlocal pos
        skip_ws()
        name = parse_ident()
        skip_ws()
        if pos < len(s) and s[pos] == '(':
            pos += 1
            args = []
            skip_ws()
            if pos < len(s) and s[pos] != ')':
                while True:
                    args.append(parse_expr_inner())
                    skip_ws()
                    if pos < len(s) and s[pos] == ',':
                        pos += 1
                        skip_ws()
                        continue
                    break
            if pos >= len(s) or s[pos] != ')':
                raise ValueError(f"Expected ')' at {pos}")
            pos += 1
            return (name, args)
        return name

    result = parse_expr_inner()
    skip_ws()
    if pos != len(s):
        raise ValueError(f"Extra data at end: {s[pos:]}")
    return result

def get_lines(f):
    current = ""
    for line in open(f).readlines():
        i = line.find("%")
        if i != -1:
            line = line[:i]
        current += line.strip()
        if current.endswith("."):
            yield current
            current = ""

s = ""
for line in get_lines(sys.argv[1]):
    assert(line.startswith("cnf(a,axiom,"))
    assert(line.endswith(")."))
    line = line[13:-2]
    if "!=" in line:
        [a, b] = line.split("!=")
        a = reformat(a)
        b = reformat(b)
        g = a + " != " + b
    else:
        [a, b] = line.split("=")
        a = reformat(a)
        b = reformat(b)
        g = a + " = " + b
    outs.append("cnf(a,axiom," + g + ").")

outs.append("cnf(a,axiom, app(F1, bot(F1,F2)) = app(F2, bot(F1,F2)) => F1=F2).")
for x in outs:
    print(x)
