import os
from classes.AbstractDataSource import AbstractDataSource

class FilesSources(AbstractDataSource):
    """Implementa a lógica comum a qualquer tipo de arquivo (csv, json, txt)."""

    def __init__(self):
        self.previous_files = []
        self.start()  # chama start() já na criação do objeto

    def start(self):
        """Implementação do método abstrato: prepara a pasta e faz a checagem inicial."""
        self.create_path()
        self.check_for_new_files()

    def create_path(self):
        """Cria (se não existir) a pasta onde os arquivos dessa fonte ficam salvos."""
        current_directory = os.getcwd()
        self.folder_path = os.path.join(current_directory, 'data', 'extension_files')
        if not os.path.exists(self.folder_path):
            os.makedirs(self.folder_path)

    def check_for_new_files(self):
        """Compara os arquivos da pasta agora com os já vistos antes, pra achar novidades."""
        current_files = os.listdir(self.folder_path)
        new_files = [file for file in current_files if file not in self.previous_files]

        if new_files:
            print("New files detected:", new_files)
            self.previous_files = current_files
        else:
            print("No new files detected.")

    def get_data(self):
        """Será sobrescrito pelas classes filhas (cada tipo de arquivo lê do seu jeito)."""
        pass

    def transform_data_to_df(self):
        """Será sobrescrito pelas classes filhas, se precisar de tratamento específico."""
        pass

    def save_data(self):
        """Implementação genérica: por enquanto só avisa que salvaria os dados.
        Pode ser sobrescrita pelas filhas se precisar de lógica específica."""
        print("Dados prontos para serem salvos (implementar destino: banco, S3, etc).")