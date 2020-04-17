from keras.preprocessing.sequence import pad_sequences

# define sequences
sequences = [
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4],
    [1, 2, 3],
    [1, 2],
    [1]
]

# truncate sequence
truncated = pad_sequences(sequences, maxlen=2)
print(truncated)