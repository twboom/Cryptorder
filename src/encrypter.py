def create_code(lines):
    code = ''
    for line in lines:
        if line == '': continue
        code += (list(line)[-1])
    return code

def encrypt(lines, code):
    encoded = []

    for line in lines:
        encoded.append(str(line).encode())

    return encoded

def run(path):
    file = open(path, 'r')
    lines = file.read().splitlines()
    code = create_code(lines)
    output = encrypt(lines, code)
    print(output)
    return lines