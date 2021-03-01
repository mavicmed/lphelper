# Runeglish object

### Importing the package. "Runeglish" is the main object for working with runes and their representations.


```python
from lphelper.core import Runeglish
```

### There are two ways to get a rune object. The first way is to use a string containing runes.


```python
page5 = "ᛋᚩᛗᛖᚹᛁᛋᛞᚩᛗ.ᚦᛖ-ᛈᚱᛁᛗᛖᛋ-ᚪᚱᛖ-ᛋᚪᚳ/\nᚱᛖᛞ.ᚦᛖ-ᛏᚩᛏᛁᛖᚾᛏ-ᚠᚢᚾᚳᛏᛡᚾ-ᛁᛋ-ᛋᚪ/\nᚳᚱᛖᛞ"
runic_object1 = Runeglish(page5)
runic_object1
```

### The second way is to use the built-in function to load pages.
This function returns a Runeglish object containing the specified page number. 

The page numbers are the numbers of their images from the iddqd repository.
https://github.com/rtkd/iddqd/tree/master/liber-primus__images--full




```python
from lphelper.page_loader import get_page
page_number = 5
page5 = get_page(page_number)
page5
```

**Page numbers missing runes or other valuable data have been omitted. If you try to call such a page, you will get an exception.**

Below are all the pages that can be obtained using this function.


```python
#pages 0 and 2 omitted
from lphelper.page_loader import iddqd_pages
iddqd_pages.keys()
```




    dict_keys(['delimiters', '1', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74'])



The **delimiters** page contains information about the various additional characters used to digitize the pages.


```python
print(iddqd_pages['delimiters'])
```

    Delimiters
    Word     : -
    Clause   : .
    Paragraph: &
    Segment  : $
    Chapter  : §
    Line     : /
    Page     : %
    
    


### Working with rune representations. 
Each rune can be represented as an image of a rune, an English letter or the ordinal number of the rune in Gematria Primus. 
Through the Runeglish object, you can access all representations at once.


```python
for r, e, i in zip(page5.runes[:5], page5.rids[:5], page5.eng[:5]):
    print(f'{r:2}  {e:3}  {i:4}')
```

    ᛋ    15  S   
    ᚩ     3  O   
    ᛗ    19  M   
    ᛖ    18  E   
    ᚹ     7  W   


If the object was originally created from a string containing additional characters, then you can restore the string along with them.


```python
page5.as_runes_with_delimiters
```




    'ᛋᚩᛗᛖ-ᚹᛁᛋᛞᚩᛗ.ᚦᛖ-ᛈᚱᛁᛗᛖᛋ-ᚪᚱᛖ-ᛋᚪᚳ/\nᚱᛖᛞ.ᚦᛖ-ᛏᚩᛏᛁᛖᚾᛏ-ᚠᚢᚾᚳᛏᛡᚾ-ᛁᛋ-ᛋᚪ/\nᚳᚱᛖᛞ.ᚪᛚᛚ-ᚦᛝᛋ-ᛋᚻᚩᚢᛚᛞ-ᛒᛖ-ᛖᚾᚳᚱᚣ/\nᛈᛏᛖᛞ./\n&\nᚳᚾᚩᚹ-ᚦᛁᛋ./\n272-138-ᛋᚻᚪᛞᚩᚹᛋ-131-151/\nᚫᚦᛖᚱᛠᛚ-ᛒᚢᚠᚠᛖᚱᛋ-ᚢᚩᛁᛞ-ᚳᚪᚱᚾᚪᛚ-18/\n226-ᚩᛒᛋᚳᚢᚱᚪ-ᚠᚩᚱᛗ-245-ᛗᚩᛒᛁᚢᛋ/\n18-ᚪᚾᚪᛚᚩᚷ-ᚢᚩᛁᛞ-ᛗᚩᚢᚱᚾᚠᚢᛚ-ᚫᚦᛖᚱᛠᛚ/\n151-131-ᚳᚪᛒᚪᛚ-138-272/\n&\n$\n'




```python
page5.as_english_with_spaces
```




    'SOME-WISDOM.THE-PRIMES-ARE-SAC(K)RED.THE-TOTIENT-FUNC(K)TIAN-IS-SAC(K)RED.ALL-TH(i)NGS-SHOULD-BE-ENC(K)RYPTED.C(K)NOW-THIS.--SHADOWS--AETHEREAL-BUFFERS-UOID-C(K)ARNAL--OBSC(K)URA-FORM--MOBIUS-ANALOG-UOID-MOURNFUL-AETHEREAL--C(K)ABAL--'



### Slices
Using python notation for slices, you can get parts of an object. When using slices, rune indices are indicated in a line containing only runes. But the slice is still able to display the content along with additional characters.


```python
part_of_page5 = page5[10:30]
part_of_page5.as_runes_string
```




    'ᚦᛖᛈᚱᛁᛗᛖᛋᚪᚱᛖᛋᚪᚳᚱᛖᛞᚦᛖᛏ'




```python
part_of_page5.as_english_with_spaces
```




    'THE-PRIMES-ARE-SAC(K)RED.THE-T'



### Functions for decryption
Inside Runeglish there are functions for decrypting already resolved pages. To use these functions, it is enough to specify the key, the list of missing runes (if any) and the type of cipher.


```python
from lphelper.page_loader import list_of_pages
from lphelper.converters.core import runes_to_rids
page = list_of_pages([3,4])
page.as_english_with_spaces
```




    'UEA(i)NGSEOFC(K).REOUGPEAEA-FWXTC(K)LEA-YM-EAEO-TC(K)NAE-(i)NGMIAIAMMW-AEPD(i)NGIAR-OEA-IAMI-FF-EU(i)NG-EOUAE.YP-RAE-IPAE-C(K)AE-AENW-BXMD-RIAI-FPC(K)-EOEOAEC(K)-RTHP-FJMO-EOC(K)WIA-BAEW-BEALS-RY-JAE-R-MC(K)THEOAETC(K)PW-MGEO.C(K)(i)NGPU-EOC(K)-REW-IAPI-BYBX-FLIR-RM-C(K)GB-YR-C(K)FU-THPIAJWTFEA-JGB-AETHFFEAPTH-PFAX-JMEP(i)NGSOSM-WEOJL-WXUTHAEWMTH-DYJC(K)-SIAXO(i)NGRMBW-RMI-DYJC(K)-XHUYPL.J(i)NGYMFJPEOUIA-WEOJ-DWXU-ALASMIAEOX-AEM-IAMI-PY-AEMUF.MY-YEO-AEXRJSE-EWN-DJUSXYTETM-EORY-DS-NEAEDIA-PBUNEA(i)NGJIAAE-JGB-PTHX-PNWWILMAE.LPBUOEAIA-RIAEAF-RREOJM-RMI-DYJ-HLFU-JUIALTHEA-EOJOEORRM.UMSC(K)-EAEO-LIAEAEC(K)L-WI-LT-PEUP-EAIAPTHTB-TME-ULOLE-EOJP-UEA-LC(K)G-EAGSIATM.BMRTHFP.WRJ-RXC(K)-(i)NG-JEAOE-JEYM-DYJC(K)AEIAUF.PFA-C(K)C(K)EA-R-UJR-AMBP-GPBUNEA(i)NGF.NXE-YGIEA(i)NGUMTC(K)GEAEA-JAE-BPWD.FYX-AEUF-EOJP-XLTHEAA-LTH-C(K)YUIA.C(K)E-LAEEOIXTHSAEHAE-THYFLC(K)ER-PFAX-RBE-AEC(K)BF.'



When using the list_of_pages function, the pages are concatenated with a "%" separator inserted between them.


```python
key = runes_to_rids('ᛞᛁᚢᛁᚾᛁᛏᚣ')
missing_f = [48, 74, 84, 132, 159, 160, 250, 421, 443, 465, 514]
page.decription(key, missing_f, cipher_type='vigenere')
page.as_english_with_spaces
```




    'WELC(K)OME.WELC(K)OME-PILGRIM-TO-THE-GREAT-JOURNEY-TOWARD-THE-END-OF-ALL-TH(i)NGS.IT-IS-NOT-AN-EASY-TRIP-BUT-FOR-THOSE-WHO-FIND-THEIR-WAY-HERE-IT-IS-A-NEC(K)ESSARY-ONE.ALO(i)NG-THE-WAY-YOU-WILL-FIND-AN-END-TO-ALL-STRUGGLE-AND-SUFFER(i)NG-YOUR-INNOC(K)ENC(K)E-YOUR-ILLUSIANS-YOUR-C(K)ERTAINTY-AND-YOUR-REALITY.ULTIMATELY-YOU-WILL-DISC(K)OUER-AN-END-TO-SELF.IT-IS-THROUGH-THIS-PILGRIMAGE-THAT-WE-SHAPE-OURSELUES-AND-OUR-REALITIES.JOURNEY-DEEP-WITHIN-AND-YOU-WILL-ARRIUE-OUTSIDE.LIC(K)E-THE-INSTAR-IT-IS-ONLY-THROUGH-GO(i)NG-WITHIN-THAT-WE-MAY-EMERGE.WIDSOM.YOU-ARE-A-BE(i)NG-UNTO-YOURSELF.YOU-ARE-A-LAW-UNTO-YOURSELF.EAC(K)H-INTELLIGENC(K)E-IS-HOLY.FOR-ALL-THAT-LIUES-IS-HOLY.AN-INSTRUC(K)TIAN-C(K)OMMAND-YOUR-OWN-SELF.'



### Calculation of statistics. 
More stats will be added later.


```python
page = list_of_pages([3,4])
page.stats_base
```




    {'ioc': 13.199507389162559, 'runes_entropy': 4.669365170554235}




```python
page.decription(key, missing_f, cipher_type='vigenere')
page.stats_base
```




    {'ioc': 19.36945812807882, 'runes_entropy': 4.235364993277167}




```python
page.stats_full
```




    {'_runes_frequency': {'ᚠ': 0.021359223300970873,
      'ᚢ': 0.06019417475728155,
      'ᚦ': 0.02912621359223301,
      'ᚩ': 0.0854368932038835,
      'ᚱ': 0.06990291262135923,
      'ᚳ': 0.02330097087378641,
      'ᚷ': 0.021359223300970873,
      'ᚹ': 0.031067961165048542,
      'ᚻ': 0.015533980582524271,
      'ᚾ': 0.06796116504854369,
      'ᛁ': 0.08349514563106795,
      'ᛄ': 0.003883495145631068,
      'ᛇ': 0.0,
      'ᛈ': 0.009708737864077669,
      'ᛉ': 0.0,
      'ᛋ': 0.05825242718446602,
      'ᛏ': 0.05631067961165048,
      'ᛒ': 0.003883495145631068,
      'ᛖ': 0.1029126213592233,
      'ᛗ': 0.019417475728155338,
      'ᛚ': 0.07184466019417475,
      'ᛝ': 0.009708737864077669,
      'ᛟ': 0.0,
      'ᛞ': 0.02912621359223301,
      'ᚪ': 0.06407766990291262,
      'ᚫ': 0.0,
      'ᚣ': 0.04854368932038835,
      'ᛡ': 0.003883495145631068,
      'ᛠ': 0.009708737864077669},
     'ioc': 19.36945812807882,
     'runes_entropy': 4.235364993277167}



### An End

This is still more a prototype than a full-fledged package. Although the functions described here should work well, there may be bugs in the code. I tried to make the code more understandable in terms of the algorithms that are used in it and tried to ignore the DRY principle. This was done so that new solvers could understand how to work with runes and their representations by looking at the code. It seems to me that it turned out worse than I wanted, so the code is waiting for refactoring. Nevertheless, I recommend that you look into the code, as it contains useful functions that were not described here.
