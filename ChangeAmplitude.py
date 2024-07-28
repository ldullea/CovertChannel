from pydub import AudioSegment


def ChangeAmplitude(filename, AmpShift, OutputFile):
    wav_file = AudioSegment.from_file(file=filename,
                                      format="wav")
    loud_wav_file = wav_file + AmpShift
    loud_wav_file.export(out_f=OutputFile,
                         format="wav",
                         bitrate="2000k",)
    return loud_wav_file


if __name__ == '__main__':
    filename = 'pitched_down.wav'
    wav_file = AudioSegment.from_file(file=filename,
                                      format="wav")

    loud_wav_file = wav_file + 10
    loud_wav_file.export(out_f='test.wav',
                         format="wav",
                         bitrate="2000k",)
