<h1>NLP-Persian-Poets</h1>

This code uses some train sets to learn the n-grams (n=1, 2). These train sets each include the poems from a specific poet. Then the code uses these n-grams in a back-off model to predict the poets of each poem. It also provides accuracy for the model.

## Data
The training dataset contains poems from 3 great Persian poets: Ferdowsi, Hafez, Molavi. The training dataset can be found [here](https://github.com/mahvash-siavashpour/ngram-persian-poem-classification/tree/master/train_set).<br>
Sample poems:
<br>
<img src="https://github.com/mahvash-siavashpour/mahvash-siavashpour.github.io/blob/main/assets/img/poems.png?raw=true" alt="img"/>
<br>

## Building the Model
In order to perform calculations, it was necessary to build unigram and bigram models for each of the poets according to their training data. In Unigram, words with a frequency of less than 2 were removed to make calculations more accurate. Then, with the backoff model calculations were done for each stanza. The model (poet) that produced the highest probability is considered as the label of this stanza.
Calculations of probabiliry: <br>
```
probability[poet] *= (frqBi * landa[2] + frqUni * landa[1] + landa[0] * e)
```

## Parameter Tuning
Parameter tuning was done on the coefficients of the backoff model. According to that the best values for Landa and e coefficients was tobtained. The results show that the highest coefficient value should be given to the bigram model and the value of e should be small. Also the bigram and unigram coefficients should be chosen close to each other. In explanation, it can be stated that bigram and unigram models are both powerful, but bigram is more accurate because it takes into account 2 tokens. Therefore, assigning a higher coefficient to it will make our answer more accurate. The coefficients for the unigram are smaller because the goal is to use the unigram if the combination is not available in the bigram. e is also important when our word is not in any of the models. So this value should be close to the lowest probability of occurrence of each word, so a small number should be chosen.<br>

<h3>How to use</h3>
1. place your test file in /test_set (include persian poems in persian and their known poets as numbers) <br>
(1: ferdowsi, 2: hafez, 3: molavi) <br>
3. run main.py <br>

<h3>How it works</h3>
This code uses some train sets to learn the n-grams (n=1, 2). These train sets each include the poems from a specific poet. Then the code uses these n-grams in a back-off model to predict the poets of each poem. It also provides some accuracy for the model. 

<h3>Results and Conclusion</h3>
The code managed to predict 85% of the poets correctly. <br>
You can see an example here:<br>
<br>3	تا خدایش باز صاف و خوش کند
<br>3	آنکه تیره کرد هم صافش کند
<br>
=> molavi<br>

