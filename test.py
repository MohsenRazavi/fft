
from time import time
from regex import match
import numpy as np

from fft import fft
from dft import dft
from test_smaples import *

local_vars = locals()

try:
    sample_pattern = local_vars['TEST_SAMPLE_PATTERN']
    
except KeyError:
    print('The variable TEST_SAMPLE_PATTERN must be defined in test_samples.py.')

else:
    samples = {var:local_vars[var] for var in local_vars.keys() if match(sample_pattern, var)}
    print(f'Running {len(samples)} tests ...\n')

    for sample_key, sample_signal in samples.items():
        print(f'Testing {sample_key}:')
        t1 = time()
        fft_ans = fft(sample_signal)
        print(f'   FFT runtime: {time()-t1} secs')
        t2 = time()
        dft_ans = dft(sample_signal)
        print(f'   DFT runtime: {time()-t2} secs')
        t3 = time()
        np_dft = np.fft.fft(sample_signal)
        print(f'np.FFT runtime: {time()-t3} secs')
        print(f'   FFT answer: {fft_ans[-1]}')
        print(f'np.FFT answer: {np_dft[-1]}')
        print(f'   DFT answer: {dft_ans[-1]}')
        
        print()
        
