import os
import pandas as pd
from classes.FilesSources import FilesSources

class TxtSource(FilesSources):
    """Fonte de dados especializada em arquivos .txt."""

    def create_path(self):
        """Sobrescreve: usa a pasta 'txt_files'."""
        current_directory = os.getcwd()
        self.folder_path = os.path.join(current_directory, 'data', 'txt_files')
        if not os.path.exists(self.folder_path):
            os.makedirs(self.folder_path)

    def check_for_new_files(self):
        """Sobrescreve: filtra só arquivos que terminam com .txt."""
        current_files = os.listdir(self.folder_path)
        new_files = [file for file in current_files if file not in self.previous_files and file.endswith('.txt')]

        if new_files:
            print("New TXT files detected:", new_files)
            self.previous_files = current_files
            self.get_data()
        else:
            print("No new TXT files detected.")

    def get_data(self):
        """Lê cada txt novo (assumindo formato tipo csv, com vírgula) e gera um DataFrame."""
        data_frames = []
        for file_path in self.previous_files:
            try:
                path = f'{self.folder_path}/{file_path}'
                data = pd.read_csv(path)  # mesmo formato do csv, só que extensão .txt
                data_frames.append(data)
            except Exception as e:
                print(f"Erro ao ler {file_path}: {e}")
        return data_frames