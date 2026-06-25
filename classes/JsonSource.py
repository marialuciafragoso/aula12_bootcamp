import json
import os
from classes.FilesSources import FilesSources

class JsonSource(FilesSources):
    """Fonte de dados especializada em arquivos .json."""

    def create_path(self):
        """Sobrescreve: usa a pasta 'json_files'."""
        current_directory = os.getcwd()
        self.folder_path = os.path.join(current_directory, 'json_files')
        if not os.path.exists(self.folder_path):
            os.makedirs(self.folder_path)

    def check_for_new_files(self):
        """Sobrescreve: filtra só arquivos que terminam com .json."""
        current_files = os.listdir(self.folder_path)
        new_files = [file for file in current_files if file not in self.previous_files and file.endswith('.json')]

        if new_files:
            print("New files detected:", new_files)
            self.previous_files = current_files
            self.get_data()
        else:
            print("No new JSON files detected.")

    def get_data(self):
        """Lê cada arquivo json novo e devolve seu conteúdo."""
        results = []
        for file in self.previous_files:
            full_path = os.path.join(self.folder_path, file)
            results.append(self.read_json_file(full_path))
        return results

    def read_json_file(self, file_path):
        """Abre e carrega o conteúdo de um arquivo json específico."""
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
            return data
        except Exception as e:
            print("Erro ao acessar o JSON")
            return None