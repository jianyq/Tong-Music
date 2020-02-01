# Tong-Music by using LSTM and GPT2 from Morizeyao/GPT2-Chinese

## Description

- 中文的GPT-2训练代码（感谢[Morizeyao]（ https://github.com/Morizeyao ）的贡献，可以写诗，新闻，小说，或是训练通用语言模型）。
- 十分感谢[hughqiu](https://github.com/hughqiu "hughqiu")的散文模型。
- 中文的LSTM押韵处理器，其中配有马尔科夫链可自主生成文本。
- 本程序主用于歌词和说唱歌词的生成。

## 项目状态

- 本人第一次使用github，此项目也为高中时期练手所用，难免会有很多暴力（朴素）的地方，请谅解。
- 一年内会持续更新填坑。

## 使用方法

### LSTM部分

- 若使用自己的歌曲库可修改chinese_lyrics.txt。**chinese_lyrics.txt是个txt文件，歌词一句一行以'\n'为分割。
- 若使用自己的歌曲库需清空demo.txt和chinese_rappers.rap两个文件。
- Chinese_lyrics_flow.py训练时要将程序第19行train_mode改为True，生成时要改为False，直接运行即可。
- 然后打开flow.py可自动匹配出押韵方式————也可自己设置长度————然后复制print出的ans结果。

### GPT-2部分

- 可参照 https://github.com/Morizeyao/GPT2-Chinese 自行配置，这里使用的是网友训练好的散文模型，可使课词更富有诗情画意。
- 这里已经不需要再重新训练。
- 根据复制的print出ans的结果修改generate_with_flow.py第10行style **style是指接下来的文本押韵方式。
- 也可以根据自己喜欢的风格修改style。
- 修改--prefix为自己想以之为开头的主题直接运行，即可自行生成文本。

## 文件结构

- __pycache__ 文件夹为马尔科夫链生成的模型参数。
- cache 文件夹为GPT-2语料库。
- config 文件夹中贮存GPT-2模型基本参数。
- scripts, tokenizations文件为GPT-2配套文件。
- chinese_lyrics.txt为中文说唱曲库。
- Chinese_lyrics_flow.py为使用keras搭建的LSTM的中文说唱押韵模型，也可以直接生成说唱，只不过前后文内容衔接效果欠佳。
- chinese_rappers.rap储存LSTM参数
- demo.txt为Chinese_lyrics_flow.py的说唱曲目
- demo_我忘不了.txt为使用generate_with_flow.py生成的说唱歌曲这里使用了调押和单押的方式，将几个生成文件合并之后的展示文件。
- eval.py为GPT-2配套文件
- flow.py用于使demo文件生成对应的押韵style
- generate.py为原先GPT-2生成文件
- generate_texts.py也为原先GPT-2生成文件
- generate_with_flow.py为正式的修改后的生成文件
- markov_speaking.py为马尔科夫链生成文本文件
- train.json为GPT-2训练文本的样式
- train.py用于训练GPT-2
- train_single.py也用于训练GPT-2

## 注意

- Chinese_lyrics_flow.py训练时时间可能较长，若时间紧迫可修改其中epoch和长度参数减少训练和生成时间。
- 若要自己尝试训练GPT-2数据量较少时可以考虑自己建立语料库建立方法即点击cache里的py文件即可。
- style长度建议不长于12。
- generate_with_flow.py生成可能会较慢，这是因为电脑词穷了，可以通过更改topk参数来改变随机性，改变生成的速度。
- 若自己准备歌曲数据转换为chinese_lyrics.txt时注意每一行最后一个字后除了'\n'不要有任何字符。

## model文件下载地址
|  模型名称 |   模型介绍|   分享者|  链接地址1 |  链接地址2 |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| 散文模型  | 使用130MB的名家散文、情感散文和散文诗歌训练所得 。  |  [hughqiu](https://github.com/hughqiu "hughqiu") | [百度网盘【fpyu】](https://pan.baidu.com/s/1nbrW5iw34GRhoTin8uU2tQ)   | [GDrive](https://drive.google.com/drive/folders/1rJC4niJKMVwixUQkuL9k5teLRnEYTmUf?usp=sharing "GDrive") |

## 联系作者

微信：158109871775
邮箱：jianyq2003@sina.com
