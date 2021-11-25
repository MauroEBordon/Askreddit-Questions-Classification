from TCA import *

class Classifier:
    def __init__(self, df=None) -> None:
        self.df = df
        self.embedder = Embedder.Embedder()
