 import csv
from mimetypes import init
import urllib.request
from math import sqrt
from mybase import state
import mybase

from gensim.models import fasttext
import numpy as np
from numpy import dot
from numpy.linalg import norm
from gensim.utils import tokenize
import re

  def MovieSearch(self, userid, searchstr: str):
        s_t = [j for j in tokenize(searchstr) if re.compile(self._english_test)]
        l = dict()
        for title in self._moviedb.GetTitle.keys():
            i_t = [j for j in tokenize(title) if re.compile(self._english_test)]
            l[title] = self._cossim(self.ListToVec(s_t), self.ListToVec(i_t))

        return l
