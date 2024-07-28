from pydub import AudioSegment
from pydub.playback import play


def OverlayAudio(Carrier, Hidden):
    wav_file = AudioSegment.from_file(file=Carrier,
                                      format="wav")
    wav_file2 = AudioSegment.from_file(file=Hidden,
                                       format="wav")

    new_wav_file = wav_file.overlay(wav_file2)

    return new_wav_file


if __name__ == '__main__':

    File1 = 'Sample.wav'
    File2 = 'Sample.wav'
    # Original = AudioSegment.from_file(file=File2,
    #                                  format="wav")

    new = OverlayAudio(File1, File2, False)
    new_2 = OverlayAudio('Sample.wav', File1,  True)

    # Reconstructed = AudioSegment.from_file(file='recovered.wav',
    #                                       format="wav")

    play(new)
    play(new_2)
