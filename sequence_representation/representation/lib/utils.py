from typing import Dict
from numbers import Number

NA_IUPAC = {'A':('A',), 'C':('C',), 'G':('G',), 'T':('T',),
            'R':('A','G'), 'Y':('C','T'), 'M':('A','C'), 'K':('G','T'),
            'S':('C','G'), 'W':('A','T'), 'B':('C','G','T'), 'D':('A','G','T'),
            'H':('A','C','T'), 'V':('A','C','G'), 'N':('A','C','G','T')}


def count_numeric_representation_for_degenerate_bases(num_rep_for_certain_bases:Dict[str, Number]) -> Dict[str, Number]:
    out_dict = {}
    for certain, degenerate in NA_IUPAC.items():
        out_dict[certain] = sum(num_rep_for_certain_bases[x] for x in degenerate)
    return out_dict


def rev_dict(translation_dict:Dict[str, Number]) -> Dict[Number, str]:
    out = {}
    for k, v in translation_dict.items():
        if v in out:
            raise RuntimeError("key to value mapping must be unambiguous to revert dictionary")
        out[v] = k
    return out