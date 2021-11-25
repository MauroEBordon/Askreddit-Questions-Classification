from TCA import *

class Embedder:
  def __init__(self, df=None) -> None:
        self.df = df
        self.embeddings = None