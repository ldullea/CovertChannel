from __future__ import print_function, division, unicode_literals
import wave
import numpy as np

# Band pass filter derived from https://stackoverflow.com/questions/12093594/how-to-implement-band-pass-butterworth-filter-with-scipy-signal-butter


def high_pass(filename, output_file):
    wr = wave.open(filename, 'r')
    par = list(wr.getparams())  # Get the parameters from the input.
    par[3] = 0  # Number of samples

    # Open the output file
    ww = wave.open(output_file, 'w')
    ww.setparams(tuple(par))  # Use the same parameters as input file.

    lowpass = 40000  # Remove lower frequencies.
    highpass = 70000  # Remove higher frequencies.

    sz = wr.getframerate()
    c = int(wr.getnframes()/sz)
    for num in range(c):
        print('Processing {}/{} s'.format(num+1, c))
        da = np.fromstring(wr.readframes(sz), dtype=np.int32)
        left, right = da[0::2], da[1::2]  # left and right channel
        lf, rf = np.fft.rfft(left), np.fft.rfft(right)
        lf[:lowpass], rf[:lowpass] = 0, 0  # low pass filter
        lf[55:66], rf[55:66] = 0, 0  # line noise
        lf[highpass:], rf[highpass:] = 0, 0  # high pass filter
        nl, nr = np.fft.irfft(lf), np.fft.irfft(rf)
        ns = np.column_stack((nl, nr)).ravel().astype(np.int32)
        ww.writeframes(ns.tobytes())
    # Close the files
    wr.close()
    ww.close()
