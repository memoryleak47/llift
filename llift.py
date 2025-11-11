import sys

def reformat(e):
    ee = parse_expr(e)
    return stringify(ee)

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

s = ""
for line in open(sys.argv[1]).readlines():
    i = line.find("%")
    if i != -1:
        line = line[:i]
    line = line.strip()
    if line != "":
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
        print("cnf(a,axiom," + g + ").")

print("cnf(a,axiom, ifeq(X, X, T) = T).")
print("cnf(a,axiom, ifeq(app(F1, bot), app(F2, bot), F1) = ifeq(app(F1, bot), app(F2, bot), F2)).")
