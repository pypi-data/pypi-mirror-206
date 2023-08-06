from sklearn.metrics import classification_report
from sklearn.svm import SVC
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

# Tensorflow warning silencer
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'



def sv_model(X_train, X_test, y_train, y_test, verbose):

    pipeline_sv = Pipeline([
        # strings to token integer counts
        ('bow', CountVectorizer(analyzer=pt.process_text)),
        # integer counts to weighted TF-IDF scores
        ('tfidf', TfidfTransformer()),
        # train w/ Support Vectors classifier
        ('classifier', SVC(C=1.0, kernel='linear', gamma='auto', probability=True)),
    ])

    pipeline_sv.fit(X_train, y_train)
    predictions_SVM = pipeline_sv.predict(X_test)

    print('SVM - test')
    print(classification_report(predictions_SVM, y_test))


    while True:
        user_input = input('New model was trained, would you like to save it? (Y/N): ')

        if user_input.lower() == 'y':
            os.makedirs('saved_models', exist_ok=True)
            filename = 'model_svm.pk'
            # save model when training on new dataset
            with open('saved_models/' + filename, 'wb') as file:
                pickle.dump(pipeline_sv, file)
            break
        elif user_input.lower() == 'n':
            break
        else:
            print('Invalid option, please, type yes or no.')

    if verbose:
        cm = confusion_matrix(y_test, predictions_SVM)
        class_label = [0, 1]
        df_cm = pd.DataFrame(cm, index=class_label, columns=class_label)
        sns.heatmap(df_cm, annot=True, fmt='d', cmap="crest")
        plt.title("Confusion Matrix - Support vectors")
        plt.xlabel("Predicted Label")
        plt.ylabel("True Label")
        plt.savefig('figures/svm' +
                    str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + '.png')

