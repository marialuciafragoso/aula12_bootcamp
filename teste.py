from classes.CsvSource import CsvSource
from classes.JsonSource import JsonSource
from classes.TxtSource import TxtSource

print("=== CsvSource: clientes ===")
csv_source = CsvSource()
dados_csv = csv_source.get_data()
for df in dados_csv:
    print(df)
    print(f"Total de clientes: {len(df)}\n")

print("=== JsonSource: produtos ===")
json_source = JsonSource()
dados_json = json_source.get_data()
for produto in dados_json:
    print(f"{produto['nome']} - R$ {produto['preco']} - Estoque: {produto['estoque']}")

print("\n=== TxtSource: pedidos ===")
txt_source = TxtSource()
dados_txt = txt_source.get_data()
for df in dados_txt:
    print(df)
    print(f"Valor total em pedidos: R$ {df['valor'].sum():.2f}")