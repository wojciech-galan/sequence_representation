from copy import copy
from typing import Dict
from typing import List
from typing import Iterable
from numbers import Number
from lib.utils import rev_dict
from lib.four_bit_rep import NA_IUPAC_8BIT
from lib.four_bit_rep import REV_NA_IUPAC_8BIT


class SequenceRepresentation(object):
    def __init__(self, seq_string:str, translation:Dict[str, Number], rev_translated:Dict[Number, str]={}):
        self.seq_rep = [translation[c] for c in seq_string]
        self.__translation_dict = translation
        self.__rev_translation_dict = rev_translated or rev_dict(translation)

    @property
    def translation_dict(self):
        return copy(self.translation_dict)

    def __str__(self):
        return ''.join(self.__rev_translation_dict[x] for x in self.seq_rep)

    def __len__(self):
        return len(self.seq_rep)


class SeqCartesianProduct(object):
    def __init__(self, *seqences:Iterable[SequenceRepresentation]):
        assert len(seqences) > 1
        assert all(seqences[0].translation_dict == seq for seq in seqences[1:])


def cartesian_product(lists_of_nums:List[Number]):
    for

if __name__ == '__main__':
    srep = SequenceRepresentation('ARAGA', NA_IUPAC_8BIT, REV_NA_IUPAC_8BIT)
    print(srep)
    import numpy as np
    r = np.array(np.meshgrid([1, 2, 3], [4, 5], [6, 7]))
    rt = r.T
    rtr = rt.reshape(-1, 3)
    print(rt)
    print(np.array(np.meshgrid([1, 2, 3], [4, 5])).T)
    import itertools
    a = [1,2]
    b = [1,2,3]
    for x, y in itertools.product(range(len(a)), range(len(b))):
        print(a[x]*b[y])