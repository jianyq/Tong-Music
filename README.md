# Tong-Music by using LSTM and GPT2 from Morizeyao/GPT2-Chinese
## 多少个深夜无法入眠，思念，是那么的甜，那么的温暖。想你的每一次偶然，泪流满面，思念如潮水漫过心田。
## Description

- 中文的GPT-2训练代码（感谢[Morizeyao]( https://github.com/Morizeyao "Morizeyao")的贡献，可以写诗，新闻，小说，或是训练通用语言模型）。
- 十分感谢[hughqiu](https://github.com/hughqiu "hughqiu")的散文模型。
- 中文的LSTM押韵处理器，其中配有马尔科夫链可自主生成文本。
- 结合LDA模型对数据打标签。
- 结合标签与新数据finetune散文模型。
- 本程序主用于歌词和说唱歌词的生成。

## 项目状态

- 本人第一次使用github，此项目也为高中时期练手所用，难免会有很多暴力（朴素）的地方，请谅解。
- 一年内会持续更新填坑。


### 2020.2.15新增

- rhyme_searching2.py为双押查找函数rhyme_searching.py的进化版。
- chinese_rappers2.rap储存押韵模型通过再次训练学会的双押。
- demo2.py为机器学会调押+双押的示范。
- 可以通过修改rhyme_searching.py完成三押四押等多押的训练，这也使我有了去使用lstm不仅学会句子押韵而且继续往技巧性训练更进一步的想法，还需要不断的学习和尝试。

### 2020.3.12新增

- 重新获取数据。
- 重新清洗数据。
- 使用LDA模型对数据进行主题分类并打标签。
- 通过打标签数据finetune散文模型。
- 模型参数过大，可以加本人微信qtdsjyq分享。

### 2020.4.16新增

- django搭建网站AIonemusic，实现语音合成和自主歌曲生成，希望有擅长歌词对齐还有speech-to-singing的大佬加一下微信交流一下！
- 无偿提供商业服务！
- 有无大佬了解LAVA NAT或者各种提高生成速度的办法，本蒟蒻跪求大佬请教(泪奔，生成对cpu太不友好了)

## demo：《我忘不了》

我忘不了她，
忘不了她对我的爱，
她在我的心里生根发芽，
开出一朵美丽的花来。
我想，
我真的不是这样，
我们之间没有什么可以沟通彼此心的桥梁，
那美丽的传说真是令人难忘。

我忘不了她的存在，
忘不了她在的日子里，
我的心里从此刻沉重起来，
我不能接受这个现实。
我是有点无奈的，
我只是希望这样的日子能有个可以倾诉的角色，
让你知道我的存在是多么有压抑的选择，
也许我的努力就够了。

## 使用方法

### LSTM部分

- 若重新训练需修改chinese_lyrics.txt。**chinese_lyrics.txt是个txt文件，歌词一句一行以'\n'为分割。
- 若重新训练需清空demo.txt和chinese_rappers.rap两个文件。
- Chinese_lyrics_flow.py训练时要将程序第19行train_mode改为True，生成时要改为False，直接运行即可。
- 然后打开flow_finding.py可自动匹配出押韵方式————也可自己设置长度————然后复制print出的ans结果。

### GPT-2部分

- 可参照 https://github.com/Morizeyao/GPT2-Chinese 自行配置，这里使用的是网友训练好的散文模型，可使歌词更富有诗情画意。
- 因文件较大需自行下载模型参数在最下方链接，在根目录建立model文件夹中建立final_model文件夹并将下载下来的config.json与pytorch_model.bin拷贝至final_model中即可，vocab.txt已经导入cache。
- 这里已经不需要再重新训练。
- 根据复制的print出ans的结果修改generate_with_flow.py第10行style。 **style是指接下来的文本押韵方式。
- 也可以根据自己喜欢的风格修改style。
- 修改--prefix为自己想以之为开头的主题直接运行，即可自行生成文本。

### 机器演唱部分

- 修改自己想要的beat为beat.mp3。
- 修改自己想要的歌词为demo.txt。
- 打开start.py直接运行即可。

## 文件结构

- pycache文件夹为马尔科夫链生成的模型参数。
- cache文件夹为GPT-2语料库。
- config文件夹中贮存GPT-2模型基本参数。
- scripts, tokenizations文件为GPT-2配套文件。
- chinese_lyrics.txt为中文说唱曲库。
- Chinese_lyrics_flow.py为使用keras搭建的LSTM的中文说唱押韵模型，也可以直接生成说唱，只不过前后文内容衔接效果欠佳。
- chinese_rappers.rap储存LSTM参数。
- demo.txt为Chinese_lyrics_flow.py的说唱曲目。
- demo_我忘不了.txt为使用generate_with_flow.py生成的说唱歌曲这里使用了调押和单押的方式，将几个生成文件合并之后的展示文件。
- eval.py为GPT-2配套文件。
- flow_finding.py.py用于使demo文件生成对应的押韵style。
- generate.py为原先GPT-2生成文件。
- generate_texts.py也为原先GPT-2生成文件。
- generate_with_flow.py为正式的修改后的生成文件。
- markov_speaking.py为马尔科夫链生成文本文件。
- train.json为GPT-2训练文本的样式。
- train.py用于训练GPT-2。
- train_single.py也用于训练GPT-2。
- rhyme_searching.py中有自己写的函数rhyme供查找押韵所用。
- demo_0.txt为在epoch为20的训练结果下计算机学会单双押的示范。
- start.py用于机器演唱。
- beat.mp3为想播放的beat文件。

## 注意

- 环境配置问题请自行百度或挂梯子解决。
- Chinese_lyrics_flow.py训练时时间可能较长，若时间紧迫可修改其中epoch和长度参数减少训练和生成时间。
- 若要自己尝试训练GPT-2数据量较少时可以考虑自己建立语料库建立方法即点击cache里的py文件即可。
- style长度建议不长于12。
- generate_with_flow.py生成可能会较慢，这是因为电脑词穷了，可以通过更改topk参数来改变随机性，改变生成的速度。
- 若自己准备歌曲数据转换为chinese_lyrics.txt时注意每一行最后一个字后除了'\n'不要有任何字符。
- 非windows用户可能在播放时会出点小问题（也许）。修改start.py中打开beat的函数参数即可。

## model文件下载地址
|  模型名称 |   模型介绍|   分享者|  链接地址1 |  链接地址2 |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| 散文模型  | 使用130MB的名家散文、情感散文和散文诗歌训练所得 。  |  [hughqiu](https://github.com/hughqiu "hughqiu") | [百度网盘【fpyu】](https://pan.baidu.com/s/1nbrW5iw34GRhoTin8uU2tQ)   | [GDrive](https://drive.google.com/drive/folders/1rJC4niJKMVwixUQkuL9k5teLRnEYTmUf?usp=sharing "GDrive") |

|  模型名称 |   模型介绍|   分享者|  链接地址1 |
| ------------ | ------------ | ------------ | ------------ |
| 歌词模型  | 使用中文歌词训练所得 。  |  [jianyq](https://github.com/jianyq "jianyq") | [百度网盘【3x89】](https://pan.baidu.com/s/112qp2TomjHJ3w_g5DC_ZvA)   |
## 联系作者

微信：qtdsjyq
邮箱：jianyq2003@sina.com
