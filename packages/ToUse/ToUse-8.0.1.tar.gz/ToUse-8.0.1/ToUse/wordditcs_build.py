from collections import Counter
import numpy as np

class BuildDicts:
    def __int__(self, words, normal_dict_path):
        self.words=words
        self.ditcs_path=normal_dict_path

    def calculate_tfidf(self,corpus):

        # 使用Counter获取每个单词在文本中的出现次数
        word_count = Counter (self.words)
        # 获取语料库中的单词数量
        num_words = len ( self.words )
        # 创建vocabulary：按单词出现次数排序，忽略低频单词
        vocab = { word : count for word , count in word_count.items ( ) if count > 1 }
        vocab = sorted ( vocab.items ( ) , key = lambda x : x [ 1 ] , reverse = True )
        vocab = { pair [ 0 ] : idx for idx , pair in enumerate ( vocab ) }

        # 计算每个文本的tf和idf向量
        tfidf_vectors = [ ]
        for doc in corpus :
            word_freq = Counter ( doc.split ( ) )
            max_freq = max ( word_freq.values ( ) )

            tf_vector = np.zeros ( len ( vocab ) )
            idf_vector = np.zeros ( len ( vocab ) )
            tfidf_vector = np.zeros ( len ( vocab ) )

            for word , freq in word_freq.items ( ) :
                if word in vocab :
                    tf = 0.5 + 0.5 * (freq / max_freq)
                    idf = np.log ( num_words / (1 + word_count [ word ]) )
                    tfidf = tf