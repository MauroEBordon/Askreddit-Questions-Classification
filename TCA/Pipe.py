import pandas as pd



class Pipe:
    def __init__(self) -> None:

        self.df = None
        self.db_processor = DBCleaner(None)
        self.clusterer = Clusterizer(None)

        self.classifier = Classifier(None)

    def create_db(self) -> None:
        pass
    def process_db(self) -> None:
        pass
    def get_clusters(self) -> None:
        pass
    def train_classifier(self) -> None:
        pass
    def reply(self, text) -> Answear:
        pass

class Answear:
    pass




