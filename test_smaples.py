import numpy as np

TEST_SAMPLE_PATTERN = "sample_\d+"

sample_1 = [2.0]

# Simple sample
sample_2 = [1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0]


# Sin wave
n = np.linspace(0, 2*np.pi, 2**4)
sample_3 = np.sin(n)


# Cos wave
n = np.linspace(0, 2*np.pi, 2**5)
sample_4 = np.cos(n)


# Sin wave
n = np.linspace(0, 2*np.pi, 2**7)
sample_5 = np.sin(n)


# Cos wave
n = np.linspace(0, 2*np.pi, 2**10)
sample_6 = np.cos(n)


# Sin wave
n = np.linspace(0, 2*np.pi, 2**15)
sample_7 = np.sin(n)


# Two Sin waves, 40 Hz + 90 Hz
n = np.linspace(0, 0.5, 2**20)
sample_8 = np.sin(40 * 2 * np.pi * n) + 0.5 * np.sin(90 * 2 * np.pi * n)
