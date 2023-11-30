import cmath
from dft import dft

def exponential(N, k):
  return cmath.exp((-2.0 * cmath.pi * 1j * k) / N)

def fft(signal):
  n = len(signal)

  if n == 1:
     return signal
  
  elif n%2:
    return ValueError(f'Number of signal points must be power of 2. ({n})')
  
  elif n <= 32:
    return dft(signal)

  else:
    Feven = fft([signal[i] for i in range(0, n, 2)]) # Calculating for even points
    Fodd = fft([signal[i] for i in range(1, n, 2)]) # Calculating for odd points

    # Combining
    combined = [0 for _ in range(n)]
    for k in range(n // 2):
        exp = exponential(n, k)
        combined[k] = Feven[k] +  exp* Fodd[k]
        combined[k + n // 2] = Feven[k] -  exp* Fodd[k]
    return combined


