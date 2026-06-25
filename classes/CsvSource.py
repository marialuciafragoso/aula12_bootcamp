import os
import pandas as pd
from classes.FilesSources import FilesSources

class CsvSource(FilesSources):
    """Fonte de dados especializada em arquivos .csv."""

    def create_path(self):
        """Sobrescreve: usa a pasta 'csv_files' em vez da genérica."""
        current_directory = os.getcwd()
        self.folder_path = os.path.join(current_directory, 'data', 'csv_files')
        if not os.path.exists(self.folder_path):
            os.makedirs(self.folder_path)

    def check_for_new_files(self):
        """Sobrescreve: filtra só arquivos que terminam com .csv."""
        current_files = os.listdir(self.folder_path)
        new_files = [file for file in current_files if file not in self.previous_files and file.endswith('.csv')]

        if new_files:
            print("New files detected:", new_files)
            self.previous_files = current_files
            self.get_data()
        else:
            print("No new CSV files detected.")

    def get_data(self):
        """Lê todos os arquivos csv já vistos e transforma cada um em DataFrame."""
        data_frames = []
        for file_path in self.previous_files:
            try:
                path = f'{self.folder_path}/{file_path}'
                data = pd.read_csv(path)
                data_frames.append(data)
            except Exception as e:
                print(f"Erro ao ler {file_path}: {e}")
        return data_frames