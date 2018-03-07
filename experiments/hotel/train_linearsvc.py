from os.path import dirname, join
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from load_data import load_dataset
from model import TfidfModel

data_train = join(dirname(dirname(dirname(__file__))), "data", "vlsp2018", "corpus", "train", "hotel.xlsx")
data_test = join(dirname(dirname(dirname(__file__))), "data", "vlsp2018", "corpus", "test", "hotel.xlsx")

X_train, y_train = load_dataset(data_train)
X_test, y_test = load_dataset(data_test)

models = [
    TfidfModel("Tfidf Bigram", TfidfVectorizer(ngram_range=(1, 2))),
    # TfidfModel("Tfidf Trigram", TfidfVectorizer(ngram_range=(1, 3))),
    # TfidfModel("Count Bigram", CountVectorizer(ngram_range=(1, 2))),
    # TfidfModel("Count Trigram", CountVectorizer(ngram_range=(1, 3)))
]

# for n in [2000, 5000, 10000, 15000, 20000]:
#     model = TfidfModel(
#         "Count Max Feature {}".format(n),
#         CountVectorizer(max_features=n)
#     )
#     models.append(model)

# for n in [2000, 5000, 10000, 15000, 20000]:
#     model = TfidfModel(
#         "Count Max Feature {}".format(n),
#         TfidfVectorizer(max_features=n)
#     )
#     models.append(model)

# for n in [500, 700, 800, 900, 1000]:
#     for ngram in [('Bigram', (1, 2)), ("Trigram", (1, 3))]:
#         model = TfidfModel(
#             "Count {0} + Max Feature {1}".format(ngram[0], n),
#             CountVectorizer(ngram_range=ngram[1], max_features=n)
#         )
#         models.append(model)

# for n in [500, 700, 800, 900, 1000]:
#     for ngram in [('Bigram', (1, 2)), ("Trigram", (1, 3))]:
#         model = TfidfModel(
#             "Count {0} + Max Feature {1}".format(ngram[0], n),
#             TfidfVectorizer(ngram_range=ngram[1], max_features=n)
#         )
#         models.append(model)

for model in models:
    model.load_data(X_train, y_train)
    model.fit_transform()
    model.train()
    model.evaluate(X_test, y_test)
