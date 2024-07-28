
import librosa
import soundfile
from pydub import AudioSegment


def Shift_pitch(filename, output_file, frequency):
    sampling_rate = 88200*8
    y, sr = librosa.load(filename, sr=sampling_rate)
    steps = frequency
    new_y = librosa.effects.pitch_shift(
        y, sr=sr, n_steps=steps, bins_per_octave=12, res_type='soxr_vhq')

    soundfile.write(output_file, new_y, sampling_rate, subtype='FLOAT')
    export = AudioSegment.from_file(file=output_file, format="wav")
    return export


if __name__ == '__main__':
    # todo create main test function
    print('todo')
