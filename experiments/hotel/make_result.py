from os.path import join, dirname
import pandas as pd
import re
from exported.svc import sentiment
from exported.svc_full import sentiment as sentiment_full
import pandas as pd
import json

data = join(dirname(dirname(dirname(__file__))), "data", "vlsp2018", "corpus", "hotel", "test.xlsx")
X_test = list(pd.read_excel(data)["text"])

y = sentiment(X_test)
y_full = sentiment_full(X_test)


def save_result(X_test, y, file):
    content = {
        "text": X_test,
        "labels": y
    }

    with open(file, "w") as f:
        json.dump(content, f)


save_result(X_test, y, "results/svc.json")
save_result(X_test, y_full, "results/svc_full.json")


def generate_labels(y):
    labels = []
    for item in y:
        matched = re.match("^(?P<attribute>.*)#(?P<sentiment>POSITIVE|NEGATIVE|NEUTRAL)$", item)
        attribute = matched.group("attribute")
        sentiment = matched.group("sentiment")
        label = "{}, {}".format(attribute, sentiment.lower())
        label = "{" + label + "}"
        labels.append(label)
    labels = ", ".join(labels)
    return labels


content = ""
for i in range(len(X_test)):
    content += "#{}\n".format(i + 1)
    content += "{}\n".format(X_test[i])
    content += "{}\n\n".format(generate_labels(y[i]))

content_full = ""
for i in range(len(X_test)):
    content += "#{}\n".format(i + 1)
    content += "{}\n".format(X_test[i])
    content += "{}\n\n".format(generate_labels(y_full[i]))

open("results/svc_result.txt", "w").write(content)
open("results/svc_full_result.txt", "w").write(content_full)
