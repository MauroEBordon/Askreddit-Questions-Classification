from TCA import *

class Answer:
    pass

class Model:
    def __init__(self ,path:str) -> None:

        self.df = None

        self.db_processor = DBCleaner.DBCleaner()

        self.clusterer = Clusterizer.Clusterizer()

        self.classifier = Classifier.Classifier()

    def create_db(self) -> None:
        pass
    def process_db(self) -> None:
        pass
    def get_clusters(self) -> None:
        pass
    def train_classifier(self) -> None:
        pass
    def reply(self, text: str) -> Answer:
        pass






