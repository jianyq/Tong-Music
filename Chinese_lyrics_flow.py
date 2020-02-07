import markov_speaking
import re
import random
import numpy as np
import os
import keras
from rhyme_searching import *
from keras.models import Sequential
from keras.layers import LSTM
from keras.layers.core import Dense

# training depth
depth = 4 

train_mode = False
artist = "chinese_rappers" 
rap_file = "demo.txt"

def create_network(depth):
	model = Sequential()
	model.add(LSTM(4, input_shape=(2, 2), return_sequences=True))
	for i in range(depth):
		model.add(LSTM(8, return_sequences=True))
	model.add(LSTM(2, return_sequences=True))
	model.summary()
	model.compile(optimizer='rmsprop',
               loss='mse')
	if artist + ".rap" in os.listdir(".") and train_mode == False:
		model.load_weights(str(artist + ".rap"))
		print("loading saved network: " + str(artist) + ".rap")
	return model

# split the text
def split_lyrics_file(text_file):
	text = open(text_file, encoding='UTF8', errors='ignore').read()
	text = text.replace(" ","").split("\n")
	while "" in text:
		text.remove("")
	return text

# build the dataset for training
def build_dataset(lines):
	print("Start biulding,you have to wait")
	# print(lines)
	dataset = []
	line_list = []
	j = 0
	for line in lines:
		line_list = [line, len(line), rhyme(line)]
		dataset.append(line_list)
		j += 1
		print(j)
	x_data = []
	y_data = []
	for i in range(len(dataset) - 3):
		print(i)
		line1 = dataset[i][1:]
		line2 = dataset[i + 1][1:]
		line3 = dataset[i + 2][1:]
		line4 = dataset[i + 3][1:]
		x = [line1[0], line1[1], line2[0], line2[1]]
		x = np.array(x)
		x = x.reshape(2, 2)
		x_data.append(x)
		y = [line3[0], line3[1], line4[0], line4[1]]
		y = np.array(y)
		y = y.reshape(2, 2)
		y_data.append(y)
	x_data = np.array(x_data)
	y_data = np.array(y_data)
	print("Finished building the dataset")
	return x_data, y_data

# use for predicting the next bar
def compose_rap(lines, lyrics_file, model):
	rap_vectors = []
	human_lyrics = split_lyrics_file(lyrics_file)

	initial_index = random.choice(range(len(human_lyrics) - 1))
	initial_lines = human_lyrics[initial_index:initial_index + 2]

	starting_input = []
	for line in initial_lines:
		starting_input.append([len(line), rhyme(line)])

	starting_vectors = model.predict(
		np.array([starting_input]).flatten().reshape(1, 2, 2))
	rap_vectors.append(starting_vectors)

	for i in range(100):
		rap_vectors.append(model.predict(
			np.array([rap_vectors[-1]]).flatten().reshape(1, 2, 2)))

	return rap_vectors

# use the vectors to make songs
def vectors_into_song(vectors, generated_lyrics):
	print("\n\n")
	print("About to write rap (this could take a moment)...")
	print("\n\n")


	def calculate_score(vector_half, syllables, rhyme):
		desired_syllables = vector_half[0]
		desired_rhyme = vector_half[1]
		desired_rhyme = desired_rhyme * len(rhyme_list)

		score = 1.0 - (abs((float(desired_syllables) - float(syllables))) +
		               abs((float(desired_rhyme) - float(rhyme))))
		return score
	dataset = []
	for line in generated_lyrics:
		line_list = [line, len(line), rhyme(line)]
		dataset.append(line_list)
	rap = []
	vector_halves = []
	for vector in vectors:
		vector_halves.append(list(vector[0][0]))
		vector_halves.append(list(vector[0][1]))
	for vector in vector_halves:
		scorelist = []
		for item in dataset:
			line = item[0]
			total_score = calculate_score(vector, item[1], item[2])
			score_entry = [line, total_score]
			scorelist.append(score_entry)
		fixed_score_list = []
		for score in scorelist:
			fixed_score_list.append(float(score[1]))
		if len(fixed_score_list) == 0:
			return rap
		max_score = max(fixed_score_list)
		for item in scorelist:
			if item[1] == max_score:
				rap.append(item[0])
				print(str(item[0]))

				for i in dataset:
					if item[0] == i[0]:
						dataset.remove(i)
						break
				break
	return rap

# start training
def train(x_data, y_data, model):
	model.fit(np.array(x_data), np.array(y_data),
           batch_size=2,
           epochs=5,
           verbose=1)
	model.save_weights(artist + ".rap")
	print("Finished training")

# the main function
def main(depth, train_mode):
	# create the network
	model = create_network(depth)
	text_file = "chinese_lyrics.txt"
	if train_mode == True:
		bars = split_lyrics_file(text_file)
	if train_mode == False:
		p = markov_speaking.Markov(text_file, 1)
		bars = []
		for _ in range(10000):
			bars.append(p.say())
	if train_mode == True:
		x_data, y_data = build_dataset(bars)
		train(x_data, y_data, model)
	if train_mode == False:
		vectors = compose_rap(bars,text_file, model)
		rap = vectors_into_song(vectors, bars)
		f = open(rap_file, "w",encoding="UTF8")
		for bar in rap:
			f.write(bar)
			f.write("\n")
main(depth, train_mode)
