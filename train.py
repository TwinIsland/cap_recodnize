import DB, generator, data_generator, beautiful_output
import os
from sklearn.neighbors import KNeighborsClassifier as kNN
from sklearn.externals import joblib
import numpy as np


def execute_program():
    def status(word):
        word = str(word)
        if word.upper() != 'OK':
            beautiful_output.red_normal('--> Status: ' + '[' + "Error because " + str(word) + ']')

            input('Enter to quit...')
            os._exit(0)

        beautiful_output.green_normal('--> Status: ' + '[' + str(word) + ']')


    # Generate the code

    print('Begin to reconstruct...',end='      ')
    try:
        DB.reconstruct()

        # do not use del command become the CLI will be ugly
        os.system('rd /s/q train_data')
        os.system('md train_data')
        status('OK')

    except Exception as e:
        status(e)

    print('\nExecute generating progress...')
    try:
        num = int(input('The number of code you wanna generate: '))

        print('Generating...')
        generator.generate(num)
    except Exception as e:
        num = 0
        status(e)


    # print sample database

    print('\n')
    beautiful_output.underline('DATABASE CHECK:')
    DB.disp_DB()

    print('\nInitialize database...',end='      ')
    status('OK')


    # Clean the DB

    print('Remake the database, it may take a while...')

    try:
        data = data_generator.generate()
    except Exception as e:
        data = []
        status(e)


    # print out the clean data

    beautiful_output.underline('\nData check:')
    try:
        print(list(data.values())[0][0])
        print('\nData Check...', end='      ')

        status('OK')
    except Exception as e:
        status(e)


    # print log

    beautiful_output.underline('\nLog:')
    print('-------------------------------')
    print('train data number:  ' + str(num*4))
    print('train data Pairs :  ' + str(len(list(data.keys()))))
    print('covered data rate:  ' + str(len(list(data.keys()))/26 * 100)[:4] + '%')
    print('data shape       :  ' + str(list(data.values())[0][0].shape))
    print('-------------------------------')


    # data constructor for training

    def construct_data():

        label_total = list(data.keys())

        feature = []
        label = []

        for i in label_total:

            for ii in data[i]:
                # decrease the dimension
                ii = ii.reshape(1, ii.shape[1] * ii.shape[0])[0]
                feature.append(ii)
                label.append(i)

        return [feature,label]


    # train the data

    print('\nReconstruct the feature and label array...')
    try:

        # construct the knn model

        temp = construct_data()
        feature = temp[0]
        label = temp[1]

        beautiful_output.underline('\nCheck the feature:')
        print(feature[0][:10])
        print('\nReconstruct data...',end='      ')
        status('OK')
    except Exception as e:
        label = []
        feature = []
        status(e)


    print('\nTraining...',end='      ')
    try:

        # define cluster
        neighbor_num = len(np.unique(label))
        mode = kNN(n_neighbors = neighbor_num, algorithm = 'auto')
        mode.fit(feature,label)
        status('OK')
    except Exception as e:
        neighbor_num = 0
        mode = None
        status(e)


    # save model

    print('\nSave the model...',end='     ')
    try:
        joblib.dump(mode, './model.m')
        status('OK')
    except Exception as e:
        status(e)


    # validate accuracy

    print('\nValidate model accuracy')
    print('processing...')

    try:
        print('\nReconstruct...')
        DB.reconstruct()
        os.system('rd /s/q train_data')
        os.system('md train_data')


        print('\nGenerating test data...')
        generator.generate(int(num/4))


        print('Clean the data')
        data = data_generator.generate()


        print('Reconstruct the data',end='      ')
        temp = construct_data()
        feature = temp[0]
        label = temp[1]
        predict_label = mode.predict(feature)

        compare = sum(list(map(lambda x,y:x==y,predict_label,label)))

        accuracy = str(compare/len(label)*100)[:4]

        status('OK')

    except Exception as e:
        predict_label = []
        label = []
        accuracy = None
        status(e)

    beautiful_output.underline('\nModel accuracy: ')
    print('---------------------')
    print('Predict: ' + str(predict_label[:10]) + '...')
    print('Actual:  ' + str(label[:10]) + '...')
    print('---------------------')
    print(accuracy + '%')


    # print final summary
    beautiful_output.underline('\nSummary:')
    print('---------------------')
    print('Train data:     ' + str(len(predict_label)))
    print('Test data:      ' + str(int(len(predict_label)*0.2)))
    print('Neighbor:       ' + str(neighbor_num) + '/26')
    print('Model Accuracy: ' + accuracy + '%')
    print('Model Address:  ' + './model.m')
    print('Train method:   ' + 'Knn')
    print('---------------------')

