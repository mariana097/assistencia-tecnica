#!/usr/bin/env python3
import os
import sys
import compileall

print("=== DIAGNÓSTICO DE COMPILAÇÃO ===\n")

# 1. Verificar estrutura
print("📁 Estrutura do projeto:")
for root, dirs, files in os.walk("app"):
    level = root.count(os.sep) - 1
    indent = "  " * level
    print(f"{indent}📂 {os.path.basename(root)}/")
    subindent = "  " * (level + 1)
    for file in files[:3]:  # Mostrar apenas 3 arquivos por pasta
        if file.endswith('.py'):
            print(f"{subindent}📄 {file}")

# 2. Compilar todos os arquivos
print("\n🔧 Compilando todos os arquivos...")
success = compileall.compile_dir('app', force=True, quiet=1)
if success:
    print("✅ Todos os arquivos compilados com sucesso!")
else:
    print("❌ Erros de compilação encontrados")

# 3. Testar importações críticas
print("\n📦 Testando importações:")
try:
    from app.config import *
    print("  ✅ config.py")
except Exception as e:
    print(f"  ❌ config.py: {e}")

try:
    from app.database import *
    print("  ✅ database.py")
except Exception as e:
    print(f"  ❌ database.py: {e}")

try:
    from app.main import app
    print("  ✅ main.py")
except Exception as e:
    print(f"  ❌ main.py: {e}")

print("\n🎉 Testes concluídos!")
