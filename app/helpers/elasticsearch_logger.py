import logging

from elasticsearch import Elasticsearch


class ElasticsearchLogger(logging.Handler):
    """Classe que irá salvar os logs de todas as requisições que fizer nos endpoints,
    retornando o status code, tempo de resposta e o body da requisição"""

    def __init__(self, index):
        super().__init__(index)
        self.es = Elasticsearch('http://localhost:9200/')
        self.setLevel(logging.INFO)
        self.index = index
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s',
                                      datefmt='%d-%b-%y %H:%M:%S')
        handler = logging.StreamHandler()  # Enviar os logs para o console
        handler.setFormatter(formatter)  # Setar o formato do log
        self.addHandler(handler)  # Adicionar o handler no logger

    def emit(self, record):
        """Método que irá salvar os logs no elastic search"""
        try:
            self.es.index(index=self.index, body=record.__dict__)
        except Exception as e:
            print(e)

    def log(self, level, message):
        document = {
            'level': level,
            'message': message,
            'logger': self.index
        }

        self.es.index(index=self.index, body=document)  # Inserir o log no elastic search

        """Métodos para salvar os logs no elastic search"""

        def info(self, message):
            self.log(logging.INFO, message)

        def warning(self, message):
            self.log(logging.WARNING, message)

        def error(self, message):
            self.log(logging.ERROR, message)

        def debug(self, message):
            self.log(logging.DEBUG, message)
