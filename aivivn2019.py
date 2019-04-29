from tempfile import mkdtemp

from languageflow.data import CategorizedCorpus
from languageflow.data_fetcher import DataFetcher, NLPData
from languageflow.models.text_classifier import TextClassifier, TEXT_CLASSIFIER_ESTIMATOR
from languageflow.trainers.model_trainer import ModelTrainer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import f1_score
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC


corpus: CategorizedCorpus = DataFetcher.load_corpus(NLPData.AIVIVN2019_SA)
pipeline = Pipeline(
    steps=[('features', CountVectorizer(ngram_range=(1, 2), max_features=4000)),
           ('estimator', SVC(kernel='linear', C=0.3))]
)
classifier = TextClassifier(estimator=TEXT_CLASSIFIER_ESTIMATOR.PIPELINE, pipeline=pipeline)
model_trainer = ModelTrainer(classifier, corpus)
tmp_model_folder = mkdtemp()


def negative_f1_score(y_true, y_pred):
    score_class_0, score_class_1 = f1_score(y_true, y_pred, average=None)
    return score_class_1


def macro_f1_score(y_true, y_pred):
    return f1_score(y_true, y_pred, average='macro')


score = model_trainer.train(tmp_model_folder, scoring=negative_f1_score)
print(score)
