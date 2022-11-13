from pyhanlp import *


def load_dictionary():
    dic = set()
    for line in open("CoreNatureDictionary.mini.txt", "r",encoding="UTF-8"):
        dic.add(line[0:line.find('	')])
    return dic


dic = load_dictionary()

# 不显示词性
HanLP.Config.ShowTermNature = False

# 可传入自定义字典 [dir1, dir2]
segment = DoubleArrayTrieSegment(dic)
# 激活数字和英文识别
segment.enablePartOfSpeechTagging(True)

print(segment.seg("江西鄱阳湖干枯，中国最大淡水湖变成大草原"))
print(segment.seg("上海市虹口区大连西路550号SISU"))
print(segment.seg('项目的研究'))
print(segment.seg('吴记：明天下午10只，10斤肾'))
