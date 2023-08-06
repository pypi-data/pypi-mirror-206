from sklearn.metrics import classification_report
from sklearn.tree import DecisionTreeClassifier
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import FakeNewsClassifier.process_text as pt
from sklearn.metrics import confusion_matrix
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import dill as pickle
from datetime import datetime
from sklearn.tree import plot_tree
import os


def dt_model(X_train, X_test, y_train, y_test, verbose):

    pipeline_dt = Pipeline([
        # strings to token integer counts
        ('bow', CountVectorizer(analyzer=pt.process_text)),
        # integer counts to weighted TF-IDF scores
        ('tfidf', TfidfTransformer()),
        # train on TF-IDF vectors w/ Decision Tree classifier
        ('classifier', DecisionTreeClassifier(min_samples_leaf=10)),
    ])

    pipeline_dt.fit(X_train, y_train)
    predictions_DT = pipeline_dt.predict(X_test)

    print('DT - test')
    print(classification_report(predictions_DT, y_test))

    while True:
        user_input = input('New model was trained, would you like to save it? (Y/N): ')

        if user_input.lower() == 'y':
            os.makedirs('saved_models', exist_ok=True)
            filename = 'model_dt.pk'
            # save model when training on new dataset
            with open('saved_models/' + filename, 'wb') as file:
                pickle.dump(pipeline_dt, file)
            break
        elif user_input.lower() == 'n':
            break
        else:
            print('Invalid option, please, type yes or no.')

    if verbose:

        # tree plotting
        plt.figure()
        plot_tree(pipeline_dt['classifier'], class_names=['False', 'True'])
        plt.savefig('figures/tree.png'+
                str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + '.png', bbox_inches="tight")

        cm = confusion_matrix(y_test, predictions_DT)
        class_label = [0, 1]

        plt.figure()
        df_cm = pd.DataFrame(cm, index=class_label, columns=class_label)
        sns.heatmap(df_cm, annot=True, fmt='d', cmap="crest")
        plt.title("Confusion Matrix - Decision Tree")
        plt.xlabel("Predicted Label")
        plt.ylabel("True Label")
        plt.savefig('figures/dt_' +
                    str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + '.png')
