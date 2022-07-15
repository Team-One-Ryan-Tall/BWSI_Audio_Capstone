import numpy as np
from IPython.display import Audio
from SongDatabase import add_song
import librosa
import random
from collections import Counter

dict = {} 
class song_database:
   
    def __init__(self):
        
        self.database = {}

    def add_song_fanout(self, fanout_m, song_ID):
        """ take in a peak pair, 
        
        Parameters
        ----------
        ((fm, fn, dt), tm) : 
            Path to text file containing favorite food survey responses.
        fanout_m :

        song_ID :

        Returns
            -------
        Dict[tuple, [(tuple)]]
            Dictionary with the key being peak pair and value being list of song-IDs and times associated.
            """
        self.fanout_m = fanout_m
        self.song_ID = song_ID
        for fm_fn_dt, tm in fanout_m:
            if fm_fn_dt not in self.database:
                self.database[fm_fn_dt] = [(song_ID, tm)]
            else:
                self.database[fm_fn_dt].append((song_ID, tm))

    def add_song(self, fanout_array, song_ID):
        """ take in a peak pair, 
        
        Parameters
        ----------
        ((fm, fn, dt), tm) : 
            Path to text file containing favorite food survey responses.
        fanout_m :
s
        song_ID :

        Returns
            -------
        Dict[tuple, [(tuple)]]
            Dictionary with the key being peak pair and value being list of song-IDs and times associated.
            """
        for i in fanout_array:
            self.add_song_fanout(i, song_ID)

    def find_song(self, fanout_new):
        sample_list = []
        for fm_fn_dt, tm in fanout_new:
            print(fm_fn_dt)
            print(fm_fn_dt in self.database.keys())
            if fm_fn_dt in self.database.keys():
                for i in self.database[fm_fn_dt]:
                    offset = i[1] - tm
                    sample_list.append((i[0], offset))
                
        counter = Counter(sample_list)
        counter_values = list(counter.values())
        if(len(counter_values) > 1):
            if counter_values[0] == counter_values[1]:
                return None
            else: 
                return counter[0]
        return counter[0]