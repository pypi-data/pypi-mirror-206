import dill as pickle
import FakeNewsClassifier.scraper as scraper
from lime.lime_text import LimeTextExplainer
from keras.models import load_model
import numpy as np
import re
from sklearn.preprocessing import FunctionTransformer

# PREROBIŤ toto je grcka
# Tensorflow warning silencer
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

saved_model_dir = os.path.join(os.path.dirname(__file__), 'saved_models/')

def pad_features(X,max_features):
    n_samples = X.shape[0]
    n_features = X.shape[1]
    if n_features < max_features:
        padding = np.zeros((n_samples, max_features - n_features))
        return np.hstack((X.toarray(), padding))
    else:
        return X.toarray()

def saved_model(model, url, verbose):

    url_regex = re.compile(
        "^((http|https)://)[-a-zA-Z0-9@:%._\\+~#?&//=]{2,256}\\.[a-z]{2,6}\\b([-a-zA-Z0-9@:%._\\+~#?&//=]*)$")

    if model == 'NB':
        filename = os.path.join(saved_model_dir, 'model_nb.pk')

    elif model == 'DT':
        filename = os.path.join(saved_model_dir, 'model_dt.pk')

    elif model == 'SVM':
        filename = os.path.join(saved_model_dir, 'model_svm.pk')

    elif model == 'SNN':
        filename = os.path.join(saved_model_dir, 'model_snn.pk')
        modelname = os.path.join(saved_model_dir, 'model_snn.hdf5')

    else:
        print('Wrong parameter! Available : --SNN --NB --SV --DT')
        exit(-1)

    try:
        with open(filename, 'rb') as f:
            loaded_pipeline = pickle.load(f)
    except FileNotFoundError:
        print('Model does not exist! Use --s to save new model or no second parameter.')
        exit(-1)

    if (re.search(url_regex, url)):  # ide o url

        try:
            online_article = scraper.parse_article(url)
        except:
            print('Unexpected error parsing url.')
            exit(-1)

        if model == 'SNN':

            snn_model = load_model(modelname)

            loaded_pipeline.steps.append(('padding', FunctionTransformer(lambda x: pad_features(x,snn_model.layers[0].input_shape[1]))))
            loaded_pipeline.steps.append(('clf', snn_model))

                
            prediction = loaded_pipeline.predict(online_article)

        else:
            prediction = loaded_pipeline.predict_proba(online_article)

        # Lime explanation
            if verbose:
                explainer = LimeTextExplainer(
                    class_names=['False', 'True'], bow=True)
                explanation = explainer.explain_instance(online_article[0],
                                                         loaded_pipeline.predict_proba,
                                                         num_features=20
                                                         )
                explanation.save_to_file('html/article_lime_explanation.html')

    # nie je to url, je to string
    else:
        while True:
            user_input = input(
                'URL not detected, do you want to parse given text? (Y/N): ')

            if user_input.lower() == 'y':
                prediction = loaded_pipeline.predict_proba(url)
                break
            elif user_input.lower() == 'n':
                exit(0)
            else:
                print('Invalid option, please, type yes or no.')

    for i in range(0, len(prediction), 2):

        print('\033[91m' + 'Fake: ' + '\033[0m' + "%.2f" % (prediction.item(i)*100.0) + ' % -- ' +
              '\033[92m' + 'Real: ' + '\033[0m' + "%.2f" % (prediction.item(i+1)*100.0) + ' %')
        print('------------------------------')
