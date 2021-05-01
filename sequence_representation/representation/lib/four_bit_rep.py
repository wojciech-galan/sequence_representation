import numpy as np
from typing import Dict
from typing import List
from typing import Tuple
from numbers import Number
from .utils import count_numeric_representation_for_degenerate_bases
from .utils import rev_dict

na_iupac_4bit_certain = {'A': 1, 'C': 2, 'G':4, 'T':8}
NA_IUPAC_8BIT = count_numeric_representation_for_degenerate_bases(na_iupac_4bit_certain)
REV_NA_IUPAC_8BIT = rev_dict(NA_IUPAC_8BIT)





if __name__ == '__main__':
    import json
    print(json.dumps(count_numeric_representation_for_degenerate_bases(na_iupac_4bit_certain), indent=4))