from xpinyin import Pinyin
rhyme_list = [
    ['a','ba','ca','cha','da','fa','ga','gua','ha','hua','jia','ka','kua','la','lia','ma','na','pa','qia','sa','sha','shua','ta','wa','xia','ya','za','zha','zhua'],
    ['ai','bai','cai','chai','dai','gai','guai','hai','huai','kai','kuai','lai','mai','nai','pai','sai','shai','shuai','tai','wai','zai','zhai'],
    ['an','ban','can','chan','chuan','cuan','dan','duan','fan','gan','guan','han','huan','kan','kuan','lan','luan','man','nan','nuan','pan','ran','ruan','san','shan','shuan','suan','tan','tuan','wan','zan','zhan','zhuan','zuan'],
    ['ang','bang','cang','chang','chuang','dang','fang','gang','guang','hang','huang','jiang','kang','kuang','lang','liang','mang','nang','niang','pang','qiang','rang','sang','shang','shuang','tang','wang','xiang','yang','zang','zhang','zhuang'],
    ['ao','bao','biao','cao','chao','dao','diao','gao','hao','jiao','kao','lao','liao','mao','miao','nao','niao','pao','piao','qiao','rao','sao','shao','tao','tiao','xiao','yao','zao','zhao'],
    ['bei','cui','chui','dei','dui','ei','fei','gei','gui','hei','hui','kui','lei','mei','nei','pei','rui','shui','sui','tui','wei','zei','zhui','zui'],
    ['ben','cen','ceng','chen','cheng','chun','cun','dun','en','fen','gen','gun','hen','heng','hun','jun','ken','keng','kun','lun','men','nen','neng','pen','ren','reng','run','sen','seng','shen','sheng','shun','sun','teng','tun','wen','zen','zeng','zhen','zheng','zhun','zun'],
    ['beng','chong','cong','deng','dong','eng','feng','geng','gong','hong','jiong','kong','leng','long','meng','nong','peng','qiong','rong','song','tong','weng','xiong','yong','zhong','zong'],
    ['bi','di','ji','ju','li','lv','mi','ni','nv','pi','qi','qu','ti','xi','xu','yi','yu'],
    ['bian','dian','jian','juan','lian','mian','nian','pian','qian','quan','tian','xian','xuan','yan','yuan'],
    ['bie','die','jie','jue','lie','lve','mie','nie','nve','pie','qie','que','tie','xie','xue','ye','yue'],
    ['bin','bing','ding','jin','jing','lin','ling','min','ming','nin','ning','pin','ping','qin','qing','qun','ting','xin','xing','xun','yin','ying','yun'],
    ['bo','chou','chou','cou','cuo','diu','dou','duo','fo','fou','gou','guo','hou','huo','jiu','kou','kuo','liu','lou','luo','miu','mo','mou','niu','nou','nuo','o','ou','po','pou','qiu','rou','ruo','shou','shuo','sou','suo','tou','tuo','wo','xiu','you','zhou','zhuo','zou','zuo'],
    ['bu','chu','cu','du','fu','gu','hu','ku','lu','mu','nu','pu','ru','shu','su','tu','wu','zhu','zu'],
    ['ce','che','de','e','er','ge','he','ke','le','me','ne','re','se','she','te','ze','zhe'],
    ['chi','ci','ri','shi','si','zhi','zi']
]
def rhyme(line):
    test = Pinyin()
    b=str(test.get_pinyin(line[-1]))
    number1 = 0
    for rhymes in range(len(rhyme_list)):
        if b in rhyme_list[rhymes]:
            number1 = rhymes + 1
            break
    
    c=str(test.get_pinyin(line[-2]))
    number2 = 0
    for rhymes in range(len(rhyme_list)):
        if c in rhyme_list[rhymes]:
            number2 = rhymes + 1
            break
    
    number = (number1 * (len(rhyme_list) + 1) + number2 ) * 1.0 / (len(rhyme_list) + 2)
    print(number)
    return number









