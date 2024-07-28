import numpy as np
import numpy as np
from scipy.fft import *
from scipy.io import wavfile
import sounddevice as sd
import soundfile as sf


def freq(file):

    # Open the file and convert to mono
    sr, data = wavfile.read(file)
    if data.ndim > 1:
        data = data[:, 0]
    else:
        pass

    signal = np.array([-2, 8, 6, 4, 1, 0, 3, 5], dtype=float)
    fourier = np.fft.fft(data)
    n = data.size
    timestep = 0.1
    freq = np.fft.fftfreq(n, d=timestep)
    x = freq[:int(n/2 - 1)]
    y = freq[int(n/2):]
    return x, y, freq[0], freq, sr, data


x, y, zero, frequencies, sr, data = freq('dog.wav')

q = data + 5000

# q[0] = np.array(0)

print(q)

# s = np.fft.ifft(q)

sf.write('new_file.wav', [q.real,
                          q.imag], sr)


x, y, zero, frequencies, sr, data = freq('new_file.wav')

q = data

# q[0] = np.array(0)

print(q)

sf.write('new_file2.wav', q.imag, sr)


# np.cos(2*np.pi*audiofrequency) * np.cos(2*np.pi*100000) = 0.5 * (np.cos(2 * np.pi*(100000 + audiofrequency))) + (np.cos(2 * np.pi*(100000 - audiofrequency)))
