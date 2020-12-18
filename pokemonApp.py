import pandas as pd 
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder, MinMaxScaler
from scipy import spatial
from sklearn.model_selection import train_test_split
from scipy.spatial import distance

pokemons = pd.read_csv('pokemon.csv')
pokename = pokemons.values
combats = pd.read_csv('combats.csv')
sc = StandardScaler()
mms = MinMaxScaler()

#TRAIN TEST SPLIT:
combats, test = train_test_split(combats, test_size=0.01)
test = test.values
#PREPROCESSING DONE HERE:
      #FEATURE SCALING: 
pokemons['Type 2'] = pokemons['Type 2'].fillna('NoType')
standardPokemon = pd.DataFrame(sc.fit_transform(pokemons.iloc[:,4:10]), index = range(800), columns=['HP','Attack','Defense','Sp.Atk','Sp.Def','Speed'] )
normalizedPokemon = pd.DataFrame(mms.fit_transform(pokemons.iloc[:,4:10]))

pokemonType1 = pokemons.iloc[:,2:3]
ohe = OneHotEncoder(categories='auto')

type1Encoded = pd.DataFrame(ohe.fit_transform(pokemonType1).toarray() , index = range(800), columns=['Bug','Dark','Dragon','Electric',
                                                                                                     'Fairy','Fighting','Fire','Flying','Ghost',
                                                                                                     'Grass','Ground','Ice','Normal','Poison',
                                                                                                     'Psyshic','Rock','Steel','Water'])
pokemonType2 = pokemons.iloc[:,3:4]
type2Encoded = pd.DataFrame(ohe.fit_transform(pokemonType2).toarray(), columns = ['Bug2','Dark2','Dragon2','Electric2','Fairy2','Fighting2',
                                                                                  'Fire2','Flying2','Ghost2','Grass2','Ground2','Ice2',
                                                                                  'NoType2','Normal2','Poison2','Psychic2','Rock2','Steel2','Water2'])
preProcessed = pd.concat([type1Encoded,type2Encoded, normalizedPokemon] , axis=1)

def pokeFight(fighter1 , fighter2, similarityRange):
  
  #THE EUCLIDIAN DISTANCE ALGORITHM DONE HERE: 
  similarities1 = []
  similarities2 = []
  for i in range(0,len(preProcessed)):
    result = 1 - distance.euclidean(preProcessed.iloc[fighter1,:], preProcessed.iloc[i,:])
    similarities1.insert(i,result)
  similarities1 = pd.DataFrame(similarities1, columns=['Sim'])
  similarities1['index'] = range(0, len(similarities1))
  similarities1 = similarities1.sort_values(by=['Sim'],ascending=False).values
  for i in range(0,len(preProcessed)):
    result = 1 - distance.euclidean(preProcessed.iloc[fighter2,:], preProcessed.iloc[i,:])
    similarities2.append(result)
  similarities2 = pd.DataFrame(similarities2, columns=['Sim'])
  similarities2['index'] = range(0, len(similarities2))
  similarities2 = similarities2.sort_values(by=['Sim'],ascending=False).values
  
  firstWin = 0
  secondWin = 0
  
  #CROSS CALCULATION
  for i in range(1, similarityRange):
    for j in range(1, similarityRange):
      fight1 = combats.loc[(combats['First_pokemon'] == similarities1[i,1]) & (combats['Second_pokemon'] == similarities2[j,1])]
      fight2 = combats.loc[(combats['First_pokemon'] == similarities2[i,1]) & (combats['Second_pokemon'] == similarities1[j,1])]
      if(len(fight1) > 0):
        if(int(fight1.iloc[0,0:1]) == int(fight1.iloc[0,2:3])):
          secondWin += 1
        else:
          firstWin += 1 

  #RESULTS RETURN:
  if(firstWin > secondWin):
    return fighter1 
  elif(secondWin > firstWin):
    return fighter2  



#PICKING POKEMONS: 
POKEMON1 = 11
POKEMON2 = 9


print('Pokemon 1: ', pokename[POKEMON1, 1],' VS Pokemon 2: ' , pokename[POKEMON2, 1])
print(pokename[pokeFight(POKEMON1,POKEMON2,5), 1], ' wins!')


#TESTING:
wrong = 0
correct = 0
for i in range(0, 100):
  result = pokeFight(test[i,0], test[i,1], 5)
  if(result == test[i,2]):
    wrong += 1
  else:
    correct += 1
print('Correct Results: ', correct , ' Wrong Results: ', wrong)
