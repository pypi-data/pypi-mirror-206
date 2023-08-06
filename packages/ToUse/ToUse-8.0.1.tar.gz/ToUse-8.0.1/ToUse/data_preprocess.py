import re
import jieba


class DataProcessor:
    def __init__(self, stopwords_path):
        self.stopwords = [line.strip() for line in open(stopwords_path, 'r', encoding='utf-8').readlines()]
        self.special_regex = re.compile(r"[a-zA-Z0-9\s]+")
        self.en_regex = re.compile(r"[.…{|}#$%&\'()*+,!-_/:~^;<=>?@★●，。]+")
        self.zn_regex = re.compile(r"[《》！、，“”；：（）【】]+")

    def process_data(self, sentence):
        '''

        :param sentence: 1、数据过滤；2、去除中文停用词；3、数据分词
        :return:
        '''
        sentence = self.special_regex.sub(r"", sentence)
        sentence = self.en_regex.sub(r"", sentence)
        sentence = self.zn_regex.sub(r"", sentence)
        seg_list = jieba.cut(sentence)
        words = [word for word in seg_list if word not in self.stopwords]
        return words
