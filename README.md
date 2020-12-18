# Pokemon Battle Analysis
In this project, pokemon.csv dataset with 800 Pokemon features and combats.csv
dataset containing 50 thousand battle results of these Pokemons were used. Pokemon
dataset contains Pokemon names, type 1 and type 2, hp, attack, defense, sp. Attack, sp.
defense, and speed information. And in the light of this information, Pokemons that are
most similar to the selected 2 Pokemons were calculated and a winner was determined
from the results of the battles between these Pokemons. Similarity rates were determined
by the euclidean distance algorithm. The code has also been designed to apply different
distance algorithms.
## Pre-processing:
1) Type 1 and type 2 information, which are among the nominal values, were converted
to numeric values.
2) Data was scaled with the feature scaling process. Normalization and standardization
process was applied. For Euclidian distance, normalized data were used.
3) NaN values in the Type 2 column were changed to ‘NoType’.
4) Combats data was divided into train and test.
## Euclidian Distance:
1) The code has been designed in such a way that different distance calculation
algorithms can be applied.
2) Euclidian calculations were made separately for two Pokemons and ratios were
sorted from large to small, and the most similar Pokemons were found.
3) Similar Pokemons obtained from these 2 similarity results were cross-linked among
each other and the winner was determined by using combat.csv data.
## Testing:
1) Pokemons in the test data were passed through the function and compared with the
result.
2) In the test process using 100 subjects, an accuracy rate of approximately 80% was
obtained.
## Conclusion:
1) The superiority of different types of Pokemons against each other was clearly seen in
the obtained results (weakness of water type pokemon against electrical pokemon,
superiority to fire type pokemon etc.).
2) It is seen that attributes determine the winner in combats between Pokemons of the
same type.
