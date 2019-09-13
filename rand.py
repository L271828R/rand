#!/usr/bin/env python

import sys
import hashlib
import time
import os
from datetime import datetime as dt
from uuid import getnode as get_mac
from collections import Counter
from scipy import stats
import pandas as pd
import numpy as np

class rand:
    def __init__(self, seed=None):
        self.seed = str(seed)

    def srand(self, seed):
        self.seed = seed

    def _create_entropy(self):
        labels = [0, 0, 1, 1]
        data = pd.Series(labels)
        return stats.entropy(data.value_counts())

    def _hash(self, entropy):
        if self.seed is None:
            self.seed = get_mac()

        hash = hashlib.sha256((self.seed + str(entropy))
            .encode('utf-8')).hexdigest()
        self.seed = hash
        return hash

    def create_random(self):
        while True:
            entropy = self._create_entropy()
            hash = self._hash(entropy)
            sys.stdout.write(hash)

if __name__ == '__main__':
    try:
        r = rand(dt.now())
        r.create_random()
    except KeyboardInterrupt:
        exit()
