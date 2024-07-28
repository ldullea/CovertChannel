import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft
from scipy.io import wavfile


def spectrogram(filename):

    sr, data = wavfile.read(filename)
    # print(data.shape, sr)
    signal = data[:sr]
    Signal = fft(signal)
    fig, (axt, axf) = plt.subplots(2, 1,
                                   constrained_layout=1,
                                   figsize=(11.8, 3),)
    axt.plot(signal, lw=1)
    axt.grid(1)
    axf.plot(np.abs(Signal[:sr//2]), lw=1)
    axf.grid(1)
    axf.set_xlabel('Frequency (Hz)')
    axt.set_xlabel('Time (Sample #)')
    axf.set_ylabel('Amplitude')
    axt.set_ylabel('Amplitude')
    plt.show()
    sr, data = wavfile.read(filename)


if __name__ == '__main__':
    spectrogram('decoded.wav')
