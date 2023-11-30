import cmath
from dft import dft

def exponential(N, k):
  return cmath.exp((-2.0 * cmath.pi * 1j * k) / N)

def fft(signal):
  N = len(signal)

  if N == 1:
     return signal
  
  elif N%2:
    return ValueError(f'Number of signal points must be power of 2. ({N})')
  
  elif N <= 32:
    return dft(signal)

  else:
    Feven = fft([signal[i] for i in range(0, N, 2)]) # Calculating for even points
    Fodd = fft([signal[i] for i in range(1, N, 2)]) # Calculating for odd points

    # Combining
    combined = [0 for _ in range(N)]
    for k in range(N // 2):
        exp = exponential(N, k)
        combined[k] = Feven[k] +  exp* Fodd[k]
        combined[k + N // 2] = Feven[k] -  exp* Fodd[k]
    return combined


