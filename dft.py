from cmath import pi, exp

def exponential(N, k):
  return exp((-2.0 * pi * 1j * k) / N)


def dft(signal):
    N = len(signal)
    ans = [0 for _ in range(N)]
    for n in range(N):
      temp = 0
      for k in range(N):
        temp += signal[k] * exponential(N, k*n)
      ans[n] = temp

    return ans
