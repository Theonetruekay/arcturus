embedding_size = 50
lstm_units = 100

user_input = Input(shape=(1,))
user_embedding = Embedding(input_dim=len(user_mapping), output_dim=embedding_size)(user_input)

skill_input = Input(shape=(1,))
skill_embedding = Embedding(input_dim=len(skill_mapping), output_dim=embedding_size)(skill_input)

time_input = Input(shape=(1,))
time_dense = Dense(embedding_size, activation='linear')(time_input)

concatenated = Concatenate()([user_embedding, skill_embedding, time_dense])
lstm_out = LSTM(lstm_units, activation='tanh', dropout=0.2, recurrent_dropout=0.2)(concatenated)

output = Dense(data['level'].nunique(), activation='softmax')(lstm_out)

model = Model(inputs=[user_input, skill_input, time_input], outputs=output)
model.compile(loss='categorical_crossentropy', optimizer=Adam(learning_rate=0.001), metrics=['accuracy'])
 