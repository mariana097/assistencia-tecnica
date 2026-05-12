import requests
import json

base_url = "http://localhost:8000"

relatorios = [
    ("dashboard/resumo", "Dashboard Resumo"),
    ("usuarios", "Relatório de Usuários"),
    ("clientes", "Relatório de Clientes"),
    ("funcionarios", "Relatório de Funcionários"),
    ("completo", "Relatório Completo")
]

print("=" * 60)
print("ANÁLISE DOS RELATÓRIOS DO SISTEMA")
print("=" * 60)

for endpoint, nome in relatorios:
    try:
        response = requests.get(f"{base_url}/relatorios/{endpoint}")
        if response.status_code == 200:
            data = response.json()
            print(f"\n✅ {nome}:")
            print(f"   Status: Sucesso")
            if "resumo" in data:
                print(f"   Resumo: {json.dumps(data['resumo'], indent=4)}")
            elif "total" in data:
                print(f"   Total registros: {data['total']}")
                if data['total'] > 0 and 'usuarios' in data:
                    print(f"   Primeiro usuário: {data['usuarios'][0]['nome']}")
                elif data['total'] > 0 and 'clientes' in data:
                    print(f"   Primeiro cliente: {data['clientes'][0]['nome']}")
        else:
            print(f"\n❌ {nome}: Erro {response.status_code}")
    except Exception as e:
        print(f"\n❌ {nome}: Erro de conexão - {e}")

print("\n" + "=" * 60)
print("ANÁLISE CONCLUÍDA")
print("=" * 60)
