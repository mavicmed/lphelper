from string import punctuation

runes = ['ᚠ', 'ᚢ', 'ᚦ', 'ᚩ', 'ᚱ', 'ᚳ', 'ᚷ', 'ᚹ', 'ᚻ', 'ᚾ', 'ᛁ', 'ᛄ', 'ᛇ', 'ᛈ', 'ᛉ', 'ᛋ', 'ᛏ', 'ᛒ', 'ᛖ', 'ᛗ', 'ᛚ', 'ᛝ', 'ᛟ', 'ᛞ', 'ᚪ', 'ᚫ', 'ᚣ', 'ᛡ', 'ᛠ']
english = ['F', 'U', 'TH', 'O', 'R', 'C(K)', 'G', 'W', 'H', 'N', 'I', 'J', 'EO', 'P', 'X', 'S', 'T', 'B', 'E', 'M', 'L', '(i)NG', 'OE', 'D', 'A', 'AE', 'Y', 'IA', 'EA']
gematria = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109]
rids = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
low_alphabet = 'abcdefghijklmnopqrstuvwxyz'
numerous = '0123456789'
delimiters = '%\n&$/'
space_and_dots = ['-', '.', ' ']

mgsquare = '3258-3222-3152-3038-3278-3299-3298-2838-3288-3294-3296-2472-4516-1206-708-1820'.split('-')
mgsquare += '434-1311-312-278-966-204-812-934-280-1071-626-620-809-620-626-1071-280-934-812-204-966-278-312-1311-434'.split('-')
mgsquare += '272-138-131-151-18-226-245'.split('-')
base59 = '3N-3p-2l-36-1b-3v-26-33-1W-49-2a-3g-47-04-33-3W-21-3M-0F-0X-1g-2H-0x-1R-1n-3I-2r-0P-2U-16-2L-2D-1t-1s-3H-0d-0s-1K-2D-05-1K-1O-0S-1D-3o-1L-3J-1G-4D-0G-0L-0x-1Q-2p-2a-1K-4E-1w-2Q-19-1k-3G-24-0p-22-4F-0P-3C-3J-1D-2n-1m-2i-1J-3P-2v-1s-2O-0k-1M-2M-0w-3L-3D-2r-0S-1p-15-3V-3e-3I-0n-3u-1O-0u-0Z-3g-2U-1C-0Y-1N-3n-0W-3Q-22-13-0V-3c-0E-34-0W-1t-1D-2N-3H-47-0s-2p-0Z-34-0g-3v-1Q-0s-0D-0K-2h-3D-3L-2x-1Q-20-2n-2L-1C-2p-0A-29-3r-0D-45-0k-2e-2W-25-3U-1W-2r-46-2s-2X-39-3p-0X-0E-1q-0q-4B-49-48-3r-3b-3C-1M-1j-0l-4A-48-40-3m-4E-0s-2s-1v-3T-0I-3t-2B-2k-2t-2O-0e-2l-1L-28-2a-0J-1L-0c-3C-2o-0X-00-2Z-2d-1T-2u-1t-1j-0l-1o-1E-3T-18-3E-1G-27-0L-0v-2t-06-11-1A-2U-4B-1O-2M-3d-2S-0x-0w-0q-0p-2V-18-0q-1D-49-2O-00-1v-2t-1k-3s-3G-21-3w-0W-29-2r-2O-2L-0g-3Y-0M-0u-3i-3C-1r-2c-2q-3o-30-0a-39-1K'.split('-')

additional_data = alphabet+low_alphabet+numerous

def restore_punctuation(st, base_st, res_type=list, sliced=False, puncts='delimiterspacesadd'):
    res = []
    cursor = 0
    skip_counter = 0
    for n, b_s in enumerate(base_st):
        if isinstance(sliced, slice) and cursor == sliced.start:
            res = []
        elif isinstance(sliced, slice) and cursor >= sliced.stop:
            break


        if b_s in space_and_dots:
            if 'spa' in puncts:
                res.append(b_s)
        elif b_s in delimiters:
            if 'del' in puncts:
                res.append(b_s)
        elif b_s in additional_data:
            if 'add' in puncts:
                res.append(b_s)
        else:
            try:
                res.append(st[cursor])
                cursor += 1
                # print(cursor)
            except Exception as e:                
                pass

    if res_type==list:
        return res
    else:
        return ''.join(res)

def spaces_dots_detection(st):
    for n in space_and_dots:
        if n in st:
            return True
        else:
            return False

def clean_spaces_dots(st):
    return [s for s in st if s not in space_and_dots]

def clean_only_runes(st):
    return [s for s in st if s in runes]

def clean_delimiters(st):
    res = ''
    for s in st:
        if s in delimiters:
            continue
        else: res+=s
    return res

def runes_to_english(st):
    res = []
    for s in st:
        try:
            rid = runes.index(s)
            res.append(english[rid])
        except:
            pass
    return res

def runes_to_rids(st):
    res = []
    for s in st:
        try:
            res.append(runes.index(s))
        except:
            pass
    return res

def runes_to_gematria(st):
    res = []
    for s in st:
        try:
            res.append(gematria[runes.index(s)])
        except:
            pass
    return res

def rids_to_runes(st):
    return [runes[s] for s in st]

def rids_to_english(st):
    return [english[s] for s in st]

def rids_to_gematria(st):
    return [gematria[s] for s in st]

def gematria_to_runes(st):
    return [runes[gematria.index(s)] for s in st]

def gematria_to_rids(st):
    return [rids[gematria.index(s)] for s in st]

def gematria_to_english(st):
    return [english[gematria.index(s)] for s in st]

def english_to_rids(st):
    return [rids[english.index(s)] for s in st]

def english_to_runes(st):
    return [runes[english.index(s)] for s in st]

def english_to_gematria(st):
    return [gematria[english.index(s)] for s in st]
