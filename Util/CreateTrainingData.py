import os
import io
import numpy as np
import pickle as pk
import Util.Move as Move
from tensorflow import keras
import random

CATEGORIES = [ 'Black Win', 'Draw', 'White Win' ]

training_data = [ ]


def Convert(g):
    maxlength = 0
    first = 1
    #or game in g:
    #
    #    game=np.asarray(game)       # for 'safety'
    #    if (first):
    #       maxlength = len(game)
    #   if game.shape[0] > 600:
    #       maxlength = len(game)
    gamesTensor = np.zeros((len(g), 1, 8, 8, 400))

    # gamesTensor[tensorIndex (0 - len(g), positionRank (0 - 7), positionFile (0 - 7), positionNumber (0 - len(currentGame))
    tensorIndex = 0
    positionFile = 0
    positionRank = 0
    positionNumber = 0

    increment = 0

    for game in g:
      game = np.asarray(game)       # for 'safety'
      print("games converted : ", tensorIndex)
      positionNumber = 0
      for position in game:
        positionRank = 0
        for rank in position:
          positionFile = 0
          for file in rank:
            #print('tensorIndex = ',tensorIndex,' positionFile = ', positionFile, ' positionRank = ', positionRank, ' positionNumber = ', positionNumber)
            if (game[positionNumber, positionRank, positionFile]<0):
                gamesTensor[tensorIndex,0, positionRank, positionFile, positionNumber] = 1/game[positionNumber, positionRank, positionFile]
            else :
                gamesTensor[tensorIndex, 0, positionRank, positionFile, positionNumber] = game[positionNumber, positionRank, positionFile]
            positionFile += 1
          positionRank += 1
        positionNumber += 1
      tensorIndex += 1

    return gamesTensor

def ConvertLabels(l):
    convertedLabels = np.full((len(l), 8, 8, 400), 1)
    i = 0
    for label in l:
        print('Label: ', int(label))
        convertedLabels[i] = int(label)*convertedLabels[i]
        print('Converted Label: ', convertedLabels[i])
        i += 1
    return convertedLabels

def create_training_data():
    i = 0
    print(
        "Enter the directory path containing the stored games/arrays (has White Win, Black Win, Draw, and Other sub-folders): ")  # Directory containing the games (White Win, Black Win, Draw, and Other sub folders)
    data: str = input()
    for category in CATEGORIES:
        path = os.path.join(data, category)  # path to Black Win, Draw, or White Win directories.
        class_num = (CATEGORIES.index(category))  # used for labeling: -1 = BW, 0 = Draw, 1 = WW
        for gameFile in os.listdir(path):
            try:
                game = np.load(os.path.join(path, gameFile))  # load game from file into ndarray
                training_data.append([ game[1:], class_num ])
                print('Games done so far... ', i)
            except Exception as e:
                print(e)
                exit(0)
            i += 1
            if i>=15000 :
                i=0
                break

def Start():
    create_training_data()
    random.shuffle(training_data)
    print('Games Done: ', len(training_data))

    X = [ ]
    y = [ ]


    for game, label in training_data:
        X.append(game)
        y.append(label)
    X = np.asarray(X)
    y = np.asarray(y)

    X = Convert(X)
    X = np.asarray(X)

    print(X.shape)
    print(y.shape)
    np.save('E:/Chess Games Downloaded/2022 Data/fractions/dataset.npy', X, allow_pickle = True)
    np.save('E:/Chess Games Downloaded/2022 Data/fractions/labels.npy', y, allow_pickle = True)

Start()