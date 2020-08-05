# 方法一：使用collections的Counter类
import re
from collections import Counter
filepath = 'text.txt'
def word_count(filepath):
    with open(filepath, encoding='utf-8') as f:
        # print(re.sub(r"\W+", " ", f.read()).split())
        return list(map(lambda c: c[0], Counter(re.sub("\W+", " ", f.read()).split()).most_common(10)))

print(word_count(filepath))


# 方法二：遍历，对比，加减，排序
import re
def word_count2(filepath):
    #统计所有词频，写入字典
    distone = {}
    with open(filepath, encoding='utf-8') as f:
        for line in f:
            # 去除空行，多余空格
            line = re.sub(r'\W+', ' ', line)
            lineone = line.split()
            for keyone in lineone:
                if not distone.get(keyone):
                    distone[keyone] = 1
                else:
                    distone[keyone] += 1
    # print(distone)
    #根据词频字典的 vlue进行排序，选择最大的10个
    num_ten = sorted(distone.items(), key=lambda x:x[1], reverse=True)[:10]
    #取出10个单词的key，生成列表
    num_ten = [x[0] for x in num_ten]
    return num_ten

print(word_count2(filepath))