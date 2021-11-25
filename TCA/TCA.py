import pandas as pd


class TCA:
    def __init__(self) -> None:import pandas as pd


class TCA:
    def __init__(self) -> None:
        self.df = None
        self.textproc = TextProcessor(None)
       
        
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


class TextProcessor:
    def __init__(self) -> None:
        self.df = None
        

    def run_proc1(self) -> None:
        pass
    
    def run_proc2(self) -> None:
        pass
    
    def run_proc3(self) -> None:
        pass

    def get_df(self) -> pd.DataFrame:
        return self.df.copy()


class Embedder:
  def __init__(self, df) -> None:
        self.df = df
        self.embeddings = None

class Clusterizer:
    def __init__(self, df) -> None:
        self.df = df
        self.embedder = Embedder(None)
    
    def get_knn(self) -> None:
        pass

    def get_knn(self) -> None:
        pass

class Classifier:
    def __init__(self, df) -> None:
        self.df = df
        self.embedder = Embedder(None)


class FineTuner:
    def __init__(self, df) -> None:
        self.df = df
        self.df = None
        self.textproc = TextProcessor(None)
       
        
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


class TextProcessor:
    def __init__(self) -> None:
        self.df = None
        

    def run_proc1(self) -> None:
        pass
    
    def run_proc2(self) -> None:
        pass
    
    def run_proc3(self) -> None:
        pass

    def get_df(self) -> pd.DataFrame:
        return self.df.copy()


class Embedder:
  def __init__(self, df) -> None:
        self.df = df
        self.embeddings = None

class Clusterizer:
    def __init__(self, df) -> None:
        self.df = df
        self.embedder = Embedder(None)
    
    def get_knn(self) -> None:
        pass

    def get_knn(self) -> None:
        pass

class Classifier:
    def __init__(self, df) -> None:
        self.df = df
        self.embedder = Embedder(None)


class FineTuner:
    def __init__(self, df) -> None:
        self.df = df