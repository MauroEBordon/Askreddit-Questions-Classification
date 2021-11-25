import TCA

class FineTuner:
    def __init__(self, df) -> None:
        self.df = df
        self.df = None
        self.textproc = DBParser(None)
       
        
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
