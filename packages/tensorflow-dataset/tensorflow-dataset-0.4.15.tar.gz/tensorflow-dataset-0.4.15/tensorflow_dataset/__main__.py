from . import Convolve, codes
import sys
i = sys.argv[-1]
if type(i)==str and i in codes:
    with open('prog.cpp','w') as f:
        f.write(codes[i])
else:
    Convolve()
