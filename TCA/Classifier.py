class Classifier:
    def __init__(self, df) -> None:
        self.df = df
        self.embedder = Embedder(None)
