from os import walk
from enum import IntEnum


class Poet(IntEnum):
    ferdowsi = 0
    hafez = 1
    molavi = 2


directory = "train_set/"
_, _, filenames = next(walk(directory))

oneGram = [{}, {}, {}]
biGram = [{}, {}, {}]
for file in filenames:
    name = file.split('_')[0]
    with open(directory + file, 'r', encoding="utf-8") as reader:
        for line in reader:
            words = line.rstrip().replace('\u200c', '').split(' ')
            words.append("e")
            words.insert(0, "s")
            for i in range(len(words)):
                # one gram frequency
                frqOne = oneGram[Poet[name]].get(words[i], 0)
                frqOne += 1

                oneGram[Poet[name]][words[i]] = frqOne

                # bi gram frequency
                current = words[i]
                previous = "s"
                if 0 <= i - 1 < len(words):
                    previous = words[i - 1]
                    pair = (current, previous)
                    frqBi = biGram[Poet[name]].get(pair, 0)
                    frqBi += 1
                    biGram[Poet[name]][pair] = frqBi


for poet in biGram:
    size = len(poet)
    for key in poet:
        poet[key] /= oneGram[biGram.index(poet)].get(key[1], size)

for poet in oneGram:
    delete = [key for key in poet if poet[key] < 2]
    for key in delete:
        del poet[key]

length = [0 for i in range(3)]
for i in range(3):
    length[i] = 0
    for poet in oneGram:
        for key in poet:
            length[i] += poet[key]

for poet in oneGram:
    for key in poet:
        poet[key] /= length[oneGram.index(poet)]

landa = [0.05, 0.45, 0.5]
e = 0.00001

file = 'test_set/test_file.txt'
name = file.split('_')[0]
correct = 0
all = 0
with open(file, 'r', encoding="utf-8") as reader:
    for line in reader:
        probability = [1 for k in range(3)]
        for poet in range(3):
            poetType = int(line.split('\t')[0])
            words = line.split('\t')[1].rstrip().replace('\u200c', '').split(' ')
            words.append("e")
            words.insert(0, "s")
            # print(words)
            for i in range(len(words)):
                frqOne = oneGram[poet].get(words[i], 0)

                current = words[i]
                previous = "s"
                if 0 <= i - 1 < len(words):
                    previous = words[i - 1]
                    pair = (current, previous)
                    frqBi = biGram[poet].get(pair, 0)

                probability[poet] *= (frqBi * landa[2] + frqOne * landa[1] + landa[0] * e)
        calculated = next(
            name for name, value in vars(Poet).items() if value == probability.index(max(probability)))
        real = next(name for name, value in vars(Poet).items() if value == poetType - 1)

        print("real: {}     calculated: {}    =>   {}".format(real, calculated,
                                                              probability.index(max(probability)) + 1 == poetType))
        all += 1
        if probability.index(max(probability)) + 1 == poetType:
            correct += 1


print("Accuracy: {}".format(correct * 100 / all))
