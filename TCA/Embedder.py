
import TCA


class Embedder:
  def __init__(self, df=None) -> None:
        self.df = df
        self.embeddings = None