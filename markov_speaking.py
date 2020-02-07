#coding=utf8

# last edit date: 2016/10/19
# author: Forec
# LICENSE
# Copyright (c) 2015-2017, Forec <forec@bupt.edu.cn>

# Permission to use, copy, modify, and/or distribute this code for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.

# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
import jieba
import codecs
import random
import re

class Markov:
	def __init__(self, filepath = None, mode = 0, coding="utf8"):
		self.dictLen = 0
		self.Cap = []
		self.mode = mode
		self.coding = coding
		self.dic = {}
		if filepath is not None:
			self.train(filepath, mode, coding)
	def train(self, filepath = '', mode = 0, coding="utf8"):
		self.dic = {}
		self.Cap = []
		self.mode = mode
		self.coding = coding
		if filepath is None or filepath == '':
			return
		eg_puncmark = re.compile('[\,\.\!\;\?\~\`\#\$\%\@\^&\*\(\)\]\[]')
		zh_puncmark = re.compile('[，。！；]')
		with codecs.open(filepath, "r", coding) as f:
			for line in f.readlines():
				words = []
				line = re.sub('[\r\n]', "", line)
				if mode == 0:
					sentences = eg_puncmark.split(line)
					sentences_words = []
					for sentence in sentences:
						sentences_words.append(filter(lambda x:x != '',sentence.split(" ")))
					for words in sentences_words:
						for i in range(len(words)-2):
							keypair = words[i] + " " + words[i+1]
							if keypair[0].isupper():
								self.Cap.append(keypair)
							if self.dic.get(keypair) is None:
								self.dic[keypair] = [words[i+2]]
							else:
								self.dic[keypair].append(words[i+2])
				else:
					sentences = zh_puncmark.split(line)
					for sentence in sentences:
						jwords = jieba.cut(sentence, cut_all=False)
						for word in jwords:
							if len(word) >= 2:
								words.append(word)
						if len(words) > 2:
							self.Cap.append(words[0] + " " + words[1])
							#print(words)
							#words = filter(lambda x:x != '', words)
							
							for i in range(len(words)-2):
								keypair = words[i] + " " + words[i+1]
								if self.dic.get(keypair) is None:
									self.dic[keypair] = [words[i+2]]
								else:
									self.dic[keypair].append(words[i+2])
			self.dictLen = len(self.dic)
	def getDic(self):
		return self.dic
	def say(self, length = 10):
		if self.dictLen <= 2:
			print("I feel tired and I need food to say something.")
		else:
			keypair = self.Cap[random.randint(0, len(self.Cap)-1)]
			fst, snd = keypair.split(" ")[0], keypair.split(" ")[1]
			pairlen = len(self.dic[keypair])
			if self.mode == 0:
				sentence = fst + " " + snd
			else:
				sentence = fst + snd
			while length > 0 and pairlen > 0:
				temp = self.dic[keypair][random.randint(0, pairlen-1)]
				fst = snd
				snd = temp
				if self.mode == 0:
					sentence = sentence + " " + snd
				else:
					sentence = sentence + snd
				keypair = fst + " " + snd
				if self.dic.get(keypair) is not None:
					pairlen = len(self.dic[keypair])
				else:
					break
				length -= 1
			if self.mode == 0:
				print(sentence + ".")
			else:
							#sentence + "。".encode("utf8")
								#print(sentence + "。".decode("utf8"))
				print(sentence)
		return sentence
	
