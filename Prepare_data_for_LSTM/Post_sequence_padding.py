from keras.preprocessing.sequence import pad_sequences

# define sequences
sequences = [
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4],
    [1, 2, 3],
    [1, 2],
    [1]
]

# pad sequence
padded = pad_sequences(sequences, padding='post')
print(padded)