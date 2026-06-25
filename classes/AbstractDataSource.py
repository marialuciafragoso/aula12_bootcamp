from abc import ABC, abstractmethod

class AbstractDataSource(ABC):
    """Define o contrato que toda fonte de dados precisa seguir."""

    def __init__(self):
        pass

    @abstractmethod
    def start(self):
        """Inicia o processo da fonte de dados (ex: cria pasta e faz a primeira checagem)."""
        raise NotImplementedError("Método não implementado")

    @abstractmethod
    def get_data(self):
        """Lê e retorna os dados encontrados nos arquivos novos."""
        raise NotImplementedError("Método não implementado")

    @abstractmethod
    def transform_data_to_df(self):
        """Transforma os dados lidos em um DataFrame do pandas."""
        raise NotImplementedError("Método não implementado")

    @abstractmethod
    def save_data(self):
        """Salva/persiste os dados já transformados (ex: banco, S3, etc)."""
        raise NotImplementedError("Método não implementado")

    def hello_world(self):
        """Método de teste simples, não faz parte do contrato (não é abstrato)."""
        print('Hello World')