from TCA import *

class Answer:
    pass

class Pipe:
    def __init__(self, df: pd.DataFrame) -> None:

        self.df = df

        self.clusterer = Clusterizer.Clusterizer()

        self.classifier = Classifier.Classifier()


    def train_classifier(self) -> None:
        pass

    def reply(self, text: str) -> Answer:
        pass






