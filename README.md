Language : English | [简体中文](./README.cn.md)
# Tong-Music by using LSTM and GPT2 from Morizeyao/GPT2-Chinese
## Countless sleepless nights, yearning, it's so sweet, so warm. Every accidental thought of you, tears streaming down my face, memories flood over my heart like a tidal wave.

## Description

- Chinese GPT-2 training code (Thanks to [Morizeyao]( https://github.com/Morizeyao "Morizeyao")'s contribute, the model can be used to train universal language models).
- Thanks to [hughqiu](https://github.com/hughqiu "hughqiu")'s Prose model.
- Chinese LSTM rhyming processor with Markov chain to generate text autonomously.
- Label the dataset with the LDA model.
- finetune prose model combining tags with new data.
- This program is mainly used for the generation of lyrics and rap lyrics.

## Status

Project restart 

### 2020.2.15 new

- rhyme_searching2.py can find double rhyme, is the updated version of rhyme_searching.py.
- chinese_rappers2.rap stores the new model parameters.
- demo2.py is demo to show that the model learn double rhyme well.
- modify rhyme_searching.py to learn triple rhyme, This also gave me the idea to use lstm not only to learn sentence rhyme but also to continue to further the technical training, which also needs continuous learning and trying.

### 2020.3.12 new

- Retrieve data.
- Re-clean the data.
- Classify and label the data using the LDA model.
- By labeling data finetune prose model.
- Model parameters are too large, you can add my wechat (qtdsjyq).

### 2020.4.16 new

- use django to build the website AIonemusic to achieve speech synthesis and independent song generation, hoping to have a good lyric alignment and speech-to-singing big guy to add a wechat exchange!
- Free commercial services!
- If someone knows LAVA NAT or various ways to improve the generation speed? (the generation is too unfriendly to the cpu).

## Demo: "I can't forget"


"I can't forget her,
Can't forget the love she had for me,
She took root in my heart,
And blossomed into a beautiful flower.
I think,
It's not really like me,
There's no bridge between us to communicate our hearts,
That beautiful legend is truly unforgettable.

I can't forget her existence,
Can't forget the days when she was here,
From then on, my heart became heavy,
I can't accept this reality.
I'm somewhat helpless,
I just hope that in such days there could be someone to confide in,
To let you know how oppressive my existence is,
Perhaps my efforts have been enough."

## Quick start

### LSTM section
- Modify chinese_lyrics.txt for retraining.**chinese_lyrics.txt is a txt file with lyrics divided by '\n'.
- To retrain, clear demo.txt and chinese_rappers.rap files.
-Chinese_lyrics_flow. py change train_mode in line 19 of the program to True during training and False during generation. You can run it directly.
- Then open flow_finding.py to automatically match the rhyme pattern —— or set the length —— and copy the ans result from print.
### GPT-2 part
- You may refer to - https://github.com/Morizeyao/GPT2-Chinese configure, model used here is online training good prose, can bring about a more poetic lyrics.
- Due to the large file size, it is necessary to download the model parameters at the bottom of the link, create the final_model folder in the Create model folder of the root directory, and copy the downloaded config.json and pytorch_model.bin to final_model.vocab.txt has been imported to cache.
- There's no need to retrain here.
- Modify the style of line 10 of generate_with_flow.py according to the result of copying print out ans.**style refers to the way the text rhymes next.
- You can also modify the style according to your favorite style.
- Modified -prefix is run directly for the theme you want to start with, and can generate its own text.
### Machine singing part
- Change the beat you want to beat.mp3.
- Modify the lyrics you want to demo.txt.
- Open start.py and run it directly.

## notice


## model download links
|  Name |   Description|   Sharer|  Link1 |  Link2 |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| Prose Model  | Trained with 130MB of famous prose, emotional prose, and prose poetry.  |  [hughqiu](https://github.com/hughqiu "hughqiu") | [Baidu netdisk【fpyu】](https://pan.baidu.com/s/1nbrW5iw34GRhoTin8uU2tQ)   | [GDrive](https://drive.google.com/drive/folders/1rJC4niJKMVwixUQkuL9k5teLRnEYTmUf?usp=sharing "GDrive") |

|  Name |   Description|   Sharer|  Link1 | 
| ------------ | ------------ | ------------ | ------------ |
| Lyrics Model  |  Using Chinese lyrics to train. |  [jianyq](https://github.com/jianyq "jianyq") | [百度网盘【3x89】](https://pan.baidu.com/s/112qp2TomjHJ3w_g5DC_ZvA)  

## Contact me

Wechat：qtdsjyq

Email：yuqingj2@illinois.edu