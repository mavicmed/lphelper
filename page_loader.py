import os
import json

import importlib.resources as pkg_resources


from .core import Runeglish
from .converters.core import *
from .nbr import get_prime_list
from . import static

f = pkg_resources.read_text(static, 'pages_dump.json')
# f = open(stream, 'r').read()
iddqd_pages = json.loads(f)
solved_pages = {}


def get_page(n):
    return Runeglish(iddqd_pages[str(n)])

def list_of_pages(lst):
    page = Runeglish()
    for pn in lst:
        page.concat(get_page(pn))
    return page

def solve_a_warning(pages=[1,]):
    for pn in pages:
        page = get_page(pn)
        page.decription(0, cipher_type='atbash')
        solved_pages[str(pn)] = page.as_runes_with_delimiters

def solve_welcome(pages=[3,4]):
    page = list_of_pages(pages)
    missing_f = [48, 74, 84, 132, 159, 160, 250, 421, 443, 465, 514]
    key = runes_to_rids('ᛞᛁᚢᛁᚾᛁᛏᚣ')
    page.decription(key, missing_f, cipher_type='vigenere')
    solved_page = str(page.as_runes_with_delimiters).split('%')
    for n, pn in enumerate(pages):
        solved_pages[str(pn)] = solved_page[n]

def solve_some_wisdom(pages=[5,]):
    for pn in pages:
        page = get_page(pn)
        solved_pages[str(pn)] = page.as_runes_with_delimiters

def solve_koan_1(pages=[6,7,8,9]):
    page = list_of_pages(pages)
    page.decription(3, cipher_type='atbash')
    solved_page = str(page.as_runes_with_delimiters).split('%')
    for n, pn in enumerate(pages):
        solved_pages[str(pn)] = solved_page[n]

def solve_loss_of_divinity(pages=[10,11,12,13]):
    page = list_of_pages(pages)
    solved_page = str(page.as_runes_with_delimiters).split('%')
    for n, pn in enumerate(pages):
        solved_pages[str(pn)] = solved_page[n]

def solve_koan_2(pages=[14,15]):
    page = list_of_pages(pages)
    missing_f = [49, 58]
    _key = runes_to_rids('ᚠᛁᚱᚠᚢᛗᚠᛖᚱᛖᚾᚠᛖ')
    page.decription(_key, missing_f, cipher_type='vigenere')
    solved_page = str(page.as_runes_with_delimiters).split('%')
    for n, pn in enumerate(pages):
        solved_pages[str(pn)] = solved_page[n]

def solve_an_instruction(pages=[16,]):
    page = list_of_pages(pages)
    solved_page = str(page.as_runes_with_delimiters).split('%')
    for n, pn in enumerate(pages):
        solved_pages[str(pn)] = solved_page[n]

def solve_parable(pages=[74]):
    page = list_of_pages(pages)
    solved_page = str(page.as_runes_with_delimiters).split('%')
    for n, pn in enumerate(pages):
        solved_pages[str(pn)] = solved_page[n]

def solve_an_end(pages=[73,]):
    primes = get_prime_list(0, 1000)
    page = list_of_pages(pages)
    key = [primes[x]-1 for x in range(len(page.rids))]
    missing_f = [56,]
    page.decription(key, missing_f, cipher_type='sequence')
    solved_page = str(page.as_runes_with_delimiters).split('%')
    for n, pn in enumerate(pages):
        solved_pages[str(pn)] = solved_page[n]

def get_solved_page(n):
    if len(solved_pages) == 0:
        solve_a_warning()
        solve_welcome()
        solve_some_wisdom()
        solve_koan_1()
        solve_loss_of_divinity()
        solve_koan_2()
        solve_an_instruction()
        solve_parable()
        solve_an_end()
    # print(solved_pages)
    return Runeglish(solved_pages[str(n)])
