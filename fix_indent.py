import re

def fix_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    fixed = []
    for i, line in enumerate(lines, 1):
        # Se for linha 43, corrigir
        if i == 43 and filename == 'app/schemas/cliente_schema.py':
            line = line.lstrip()
        elif i == 23 and filename == 'app/schemas/usuario_schema.py':
            line = line.lstrip()
        elif i == 38 and filename == 'app/schemas/funcionario_schema.py':
            line = line.lstrip()
        fixed.append(line)
    
    with open(filename, 'w') as f:
        f.writelines(fixed)
    print(f"✅ Corrigido: {filename}")

fix_file('app/schemas/cliente_schema.py')
fix_file('app/schemas/usuario_schema.py')
fix_file('app/schemas/funcionario_schema.py')
