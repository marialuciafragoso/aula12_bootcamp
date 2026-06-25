# Herança e Polimorfismo - Leitura de Arquivos

Projeto da Jornada de Dados pra praticar herança, polimorfismo e classes abstratas em Python, usando um cenário bem comum: ler arquivos de tipos diferentes (csv, json, txt) que chegam em pastas separadas.

## A ideia

Imagina que uma empresa recebe arquivos de clientes, pedidos e produtos em formatos diferentes. Em vez de criar uma função separada e desconectada pra cada tipo de arquivo, a ideia aqui é ter uma estrutura de classes onde:

- Existe um "contrato" comum que toda fonte de dados precisa seguir (`AbstractDataSource`)
- A lógica que é igual pra qualquer arquivo (criar pasta, comparar o que é novo) fica centralizada (`FilesSources`)
- Cada tipo de arquivo só implementa o que é específico dele (`CsvSource`, `JsonSource`, `TxtSource`)

## Estrutura

```
classes/
├── AbstractDataSource.py   # classe abstrata, define o contrato
├── FilesSources.py         # lógica comum (herda de AbstractDataSource)
├── CsvSource.py            # lê arquivos .csv
├── JsonSource.py           # lê arquivos .json
└── TxtSource.py            # lê arquivos .txt

data/
├── csv_files/
│   ├── clientes.csv
│   └── pedidos.csv
└── txt_files/
    └── pedidos.txt

json_files/
├── produto_1.json
└── produto_2.json

teste.py        # script de exemplo, usa as 3 fontes
__main__.py     # versão com agendamento automático (roda a cada 10s)
```

## Como a herança funciona aqui

```
AbstractDataSource (ABC)
        ↓
   FilesSources
   ↓    ↓    ↓
 Csv   Json  Txt
Source Source Source
```

`AbstractDataSource` define 4 métodos abstratos (`start`, `get_data`, `transform_data_to_df`, `save_data`). Nenhuma classe concreta consegue ser instanciada sem implementar todos eles - é o Python garantindo que o "contrato" seja cumprido.

A `FilesSources` já implementa esses 4 métodos de um jeito genérico, então as classes filhas (`CsvSource`, `JsonSource`, `TxtSource`) não precisam reimplementar tudo - elas só sobrescrevem `create_path` e `check_for_new_files`, que são os únicos pontos que mudam de um tipo de arquivo pra outro.

Isso é o polimorfismo na prática: o `__main__.py` chama `.check_for_new_files()` nos três objetos do mesmo jeito, sem se importar com qual classe é qual - cada um sabe se comportar.

## Rodando

```bash
poetry install
poetry run python3 teste.py
```

Resultado esperado:

```
=== CsvSource: clientes ===
New files detected: ['clientes.csv']
   id          name                   email        city
0   1   Maria Lúcia   maria.lucia@email.com  Camaragibe
1   2    Joao Silva    joao.silva@email.com      Recife
2   3     Ana Costa     ana.costa@email.com      Olinda
3   4  Pedro Santos  pedro.santos@email.com    Jaboatao
4   5   Carla Souza   carla.souza@email.com    Paulista
Total de clientes: 5

=== JsonSource: produtos ===
New files detected: ['produto_2.json', 'produto_1.json']
Mouse sem fio Logitech - R$ 45.9 - Estoque: 80
Notebook Dell Inspiron - R$ 3200.0 - Estoque: 15

=== TxtSource: pedidos ===
New TXT files detected: ['pedidos.txt']
    id  cliente_id   produto   valor
0  101           1  Notebook  3200.0
1  102           2     Mouse    45.9
2  103           1   Teclado   150.0
3  104           3   Monitor   890.0
4  105           4    Webcam   210.5
Valor total em pedidos: R$ 4496.40
```

Pra ver o agendamento automático rodando (verificando novos arquivos a cada 10 segundos), roda o `__main__.py` em vez do `teste.py` e vai jogando arquivos novos nas pastas enquanto ele tá de pé.

```bash
poetry run python3 __main__.py
```

## O que eu aprendi de mais importante aqui

- Herança é transitiva: `CsvSource` não precisa herdar direto de `AbstractDataSource` porque já herda isso através de `FilesSources`
- Uma classe abstrata só "libera" a instanciação quando TODOS os métodos abstratos da cadeia foram implementados em algum lugar - não necessariamente na própria classe
- Métodos abstratos não precisam ser sobrescritos de novo em cada classe filha se a classe intermediária já resolveu isso de forma genérica o suficiente

