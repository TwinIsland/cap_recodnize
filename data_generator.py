import crack_cap.DB as DB
import crack_cap.clean as clean
import os


def generate():
    # initialize file path
    file = os.listdir('train_data/')
    file = list(map(lambda x:'./train_data/' + x,file))

    # data's index
    index = (list(map(chr,range(97,123))))

    # dataLib
    data = {}

    # merge the data lib and index to a constructor
    for i in index:
        data[i.upper()] = []

    # letter data lib
    letter = []

    # word lib
    word = []

    # gain the letter data
    for i in file:
        letters = clean.clean_photo(i)
        for le in letters:
            letter.append(le)


    # loop the original word lib
    for i in file:
        wo = DB.getWord(i)
        for i in range(len(wo)):
            word.append(wo[i])



    for i in range(len(word)):
        data[word[i]].append(letter[i])


    i = 0
    while i < len(data):
        keys = list(data.keys())
        if data[keys[i]] == []:
            data.pop(keys[i])
            continue
        i += 1

    return data

