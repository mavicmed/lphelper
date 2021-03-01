from .converters.core import *
from .statistics import core as statcore

class Runeglish:
    def __init__(self, st='', input_type=None):
        self.available_types = ['runes',
        'runes_with_delimiters_and_spaces',
        'runes_with_delimiters',
        'runes_with_spaces',
        'runes_as_english',
        'runes_as_rids',
        'runes_as_gematria',
        'unknown',]

        self.input_data = st
        self.input_type = input_type

        if self.input_type == None or self.input_type not in available_types:
            self.detect_input_type()
        if self.input_type == 'uncnown':
            print('Cannot continue with current input')

        if self.input_type in self.available_types[:3]:
            self.runes = clean_only_runes(self.input_data)
            self.runes_with_delimiters = self.input_data
            self.gematria = runes_to_gematria(self.runes)
            self.rids = runes_to_rids(self.runes)
            self.eng = runes_to_english(self.runes)

        elif self.input_type == 'runes_as_rids':
            self.runes = rids_to_runes(self.input_data)
            self.runes_with_delimiters = self.runes
            self.gematria = runes_to_gematria(self.runes)
            self.rids = runes_to_rids(self.runes)
            self.eng = runes_to_english(self.runes)

        elif self.input_type == 'runes_as_gematria':
            self.runes = gematria_to_runes(self.input_data)
            self.runes_with_delimiters = self.runes
            self.gematria = runes_to_gematria(self.runes)
            self.rids = runes_to_rids(self.runes)
            self.eng = runes_to_english(self.runes)

        elif self.input_type == 'runes_as_english':
            self.runes = english_to_runes(self.input_data)
            self.runes_with_delimiters = self.runes
            self.gematria = runes_to_gematria(self.runes)
            self.rids = runes_to_rids(self.runes)
            self.eng = runes_to_english(self.runes)

        else:
            # print('Uncnown input type')
            self.runes = []
            self.runes_with_delimiters = ''
            self.gematria = []
            self.rids = []
            self.eng = []

    def __repr__(self,):
        return self.as_english_with_spaces[:50].lstrip('.- ')

    def __getitem__(self, arg):
        if isinstance(arg, slice):
            return Runeglish(restore_punctuation(self.runes,
                                                self.runes_with_delimiters,
                                                res_type=str,
                                                sliced=arg, ))

        elif isinstance(arg, (list, tuple)):
            return [x for n, x in enumerate(self.runes) if n in arg]

        elif isinstance(arg, int):
            return self.runes[arg]

    def detect_input_type(self,):
        st = self.input_data
        if type(st) == str:
            st_set = st.replace(' ', '-')
        st_set = set(st)

        mgsquare_number = len(set(mgsquare).intersection(st_set))
        base59_number = len(set(base59).intersection(st_set))

        if base59_number > 0:
            print('Base59 was found in the input. \
            Base59 will be excluded from the data.')
            # st_set = set(clean_additional_data(st))
        if mgsquare_number > 0:
            print('Numbers from MagicSquare was found in the input. \
            Numbers from MagicSquare will be excluded from the data.')
            # st_set = set(clean_additional_data(st))

        runes_number = len(set(runes).intersection(st_set))
        rids_number = len(set(rids).intersection(st_set))
        gematria_number = len(set(gematria[10:]).intersection(st_set))
        eng_number = len(set(english).intersection(st_set))
        delimiters_number = len(set(delimiters).intersection(st_set))
        space_and_dots_number = len(set(space_and_dots).intersection(st_set))

        if runes_number > 0 and delimiters_number > 0 and space_and_dots_number > 0:
            self.input_type = 'runes_with_delimiters_and_spaces'
        elif runes_number > 0 and delimiters_number > 0:
            self.input_type = 'runes_with_delimiters'
        elif runes_number > 0:
            self.input_type = 'runes'
        elif runes_number > 0 and space_and_dots_number > 0:
            self.input_type = 'runes_with_spaces'
        elif eng_number > 0:
            self.input_type = 'runes_as_english'
        elif rids_number > 0:
            self.input_type = 'runes_as_rids'
        elif gematria_number > 0:
            self.input_type = 'runes_as_gematria'
        else:
            self.input_type = 'unknown'

    @property
    def as_runes_list(self,):
        return self.runes

    @property
    def as_runes_string(self,):
        return ''.join(self.runes).rstrip('-')

    @property
    def as_english_with_spaces(self,):
        return restore_punctuation(self.eng,
                                    self.runes_with_delimiters,
                                    str,
                                    puncts='spaces')

    @property
    def as_runes_with_delimiters(self,):
        return restore_punctuation(self.runes,
                                    self.runes_with_delimiters,
                                    str,
                                    )

    @property
    def as_english_list(self,):
        return self.eng

    @property
    def as_rids_list(self,):
        return self.rids

    def decription(self, key, missing_f=[], cipher_type='sequence'):
        res = []
        key_cursor = 0
        if cipher_type == 'sequence':
            for n, rid in enumerate(self.rids):
                if n not in missing_f:
                    res.append((rid-key[key_cursor])%29)
                    key_cursor+=1
                else:
                    res.append(rid)
        elif cipher_type == 'atbash':
            for n, rid in enumerate(self.rids):
                if n not in missing_f:
                    res.append((28-rid+key)%29)
                    key_cursor+=1
                else:
                    res.append(rid)
        elif cipher_type == 'vigenere':
            for n, rid in enumerate(self.rids):
                if n not in missing_f:
                    # print(f'{rid} - {key[key_cursor]} = {rid-key[key_cursor]}')
                    res.append((rid-key[key_cursor])%29)
                    key_cursor+=1
                    if key_cursor >= len(key):
                        key_cursor = 0
                else:
                    res.append(rid)

        self.rids = res
        self.runes = rids_to_runes(self.rids)
        self.gematria = runes_to_gematria(self.runes)
        self.eng = runes_to_english(self.runes)

    def concat(self, page):
        if len(self.runes_with_delimiters) > 0:
            self.runes_with_delimiters += '%'
        self.runes_with_delimiters += page.runes_with_delimiters

        self.runes = clean_only_runes(self.runes_with_delimiters)
        self.gematria = runes_to_gematria(self.runes)
        self.rids = runes_to_rids(self.runes)
        self.eng = runes_to_english(self.runes)

    @property
    def stats_base(self,):
        return statcore.base(self.runes)

    @property
    def stats_full(self,):
        return statcore.full(self.runes)
