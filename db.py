import pandas as pd
import pickle
from keywords import extract_keywords
from heapq import nlargest

class db_matcher():
    def __init__(self):
        self.db = pd.read_csv('db.csv')
        with open('kw_list.pkl','rb') as f:
            self.db_kw_list = pickle.load(f)

    def match(self, user_input, n_cats):
        self.n_cats = n_cats
        self.user_kws = extract_keywords(user_input)
        self.result_dict = {}
        for book_ix in range(len(self.db)):
            self.result_dict[book_ix] = len(set(self.db_kw_list[book_ix])\
                                       & set(self.user_kws))
        self.top_n_list = nlargest(self.n_cats, self.result_dict, key = \
                                   self.result_dict.get)

    def get_result(self):
        print('Top {} results from the current database: '.format(\
            len(self.top_n_list)))
        for nr, result_ix in zip(range(1, len(self.top_n_list)+1,1), self.top_n_list):
            print('Result nr.{}: '.format(nr)+self.db.iloc[result_ix]['title'])
            
    def get_detail(self, choice):
        print('Description for recommendation nr.{}: '.format(choice))
        print(self.db.iloc[self.top_n_list[choice-1]]['description'])
