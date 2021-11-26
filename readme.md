![](https://i.imgur.com/MW2UiDZ.png)

# Tweet classification for specializing an automated-reply model


## 👷 🚧 Under Construction 🚧

---

<center>Training Pipeline</center>  
  
![](https://i.imgur.com/jqXrqS3.png)

<center>Objective</center>  

![](https://i.imgur.com/3qBSEVD.png)

---
## __Roadmap__

-- Tier 1 --
* Dataset building
* Text processing module overhaul
* Clustering module overhaul:
    * get optimal cluster number
    * try the next embeddings: Doc2Vec, FastText, WordNet
    * try diferent strategies of feature-extraction
* Classification module overhaul  
    * choose a metric to determing the best algorithm

-- Tier 2 --
* Creation of the reply module
* Creation of a test dataset manually  

--  Tier 3 --
* Modularize using OOP to get a nice library with easy to use functions
* Write Readme
* Posible:   
    - Make final presentation Video

---

## Projected use case (extremly temporal)

```python
from tca import TCA

#Create the model with a database and some configuration
model = TCA(db_path="database.csv"], clusterer_params = ["..."], classifier_params = ["..."] )

#Text processing
model.process_db(options = ["..."])

#Clusterization and labeling
model.get_clusters(embedder_params = ["..."])

#Classification training 
model.trian_classifier(embedder_params = ["..."])

#Check some metric
model.report()
>>> "the model is excelent!", 0.123, 0.567

#Train the Response Component
model.train_repliers(???)

#Use the model to classify and answer a Text Document.
ans = model.get_ans("Every person who is vaccinated must be a spawn of satan")

ans.text
>>> "They shoud burn in hell!"

ans.cluster
>>> 6

ans.precition
>>> 0.654

``` 

[URL del corpus](https://www.kaggle.com/mauroebordon/askreddit-qa)

## Other: 
* [Old presentation video](https://www.youtube.com/watch?v=YM8J4S4PLTI)

## Bibliografy
* [Sentence Embedding Techniques 
](http://www.stat.cmu.edu/~rnugent/PCMI2016/papers/DocClusterComparison.pdf)
* [Applying Sentiment Analysis on Spanish Tweets Using BETO](http://ceur-ws.org/Vol-2943/emoeval_paper9.pdf)
* [Fine-tuning with custom datasets (mt5)](https://huggingface.co/transformers/custom_datasets.html)
* Incomplete!!!
