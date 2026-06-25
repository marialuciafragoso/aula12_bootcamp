import schedule
import time
from classes.CsvSource import CsvSource
from classes.JsonSource import JsonSource
from classes.TxtSource import TxtSource

# Cria as instâncias (cada __init__ já chama start(), criando pasta e checando arquivos)
csv_source = CsvSource()
txt_source = TxtSource()
json_source = JsonSource()

def check_for_new_files():
    """Roda a checagem de novos arquivos nas 3 fontes (polimorfismo: mesmo método, comportamentos diferentes)."""
    csv_source.check_for_new_files()
    txt_source.check_for_new_files()
    json_source.check_for_new_files()

# Agenda a checagem pra rodar a cada 10 segundos
schedule.every(10).seconds.do(check_for_new_files)

while True:
    schedule.run_pending()
    time.sleep(1)