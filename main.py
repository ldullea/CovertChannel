from shift_pitch import Shift_pitch
from Overlay import OverlayAudio
from ChangeAmplitude import ChangeAmplitude
from filter import high_pass
from pydub import AudioSegment
from pydub.playback import play


def main():
    source_file = 'dog.wav'
    carrier_file = 'rick.wav'
    frequency = 75
    sampling_rate = 88200*8
    amp_shift = 25

    source = AudioSegment.from_file(file=source_file,
                                    format="wav")
    play(source)

    shifted = Shift_pitch(
        source_file, 'pitch_shifted.wav', frequency=frequency)

    play(shifted)
    amp_down = ChangeAmplitude(
        'pitch_shifted.wav', -amp_shift, 'amp_shifted.wav')

    play(amp_down)

    overlay = OverlayAudio(carrier_file, 'amp_shifted.wav', False)

    play(overlay)

    overlay.export(out_f='encoded_overlay.wav',
                   format="wav",
                   bitrate="2000k",)

    high_pass('encoded_overlay.wav', 'filtered.wav')

    filtered = AudioSegment.from_file(file='filtered.wav',
                                      format="wav")
    play(filtered)

    restored = Shift_pitch(
        'filtered.wav', 'pitched_down.wav', frequency=-frequency)

    play(restored)

    amp_up = ChangeAmplitude('pitched_down.wav', amp_shift, 'decoded.wav')

    play(amp_up)

    soundcloud = AudioSegment.from_file(file='soundcloud.wav',
                                        format="wav")
    play(soundcloud)


def encode(carrier_file, source_file, frequency=65, amp_shift=1):

    audio = 1

    source = AudioSegment.from_file(file=source_file,
                                    format="wav")

    shifted = Shift_pitch(
        source_file, 'pitch_shifted.wav', frequency=frequency)

    amp_down = ChangeAmplitude(
        'pitch_shifted.wav', -amp_shift, 'amp_shifted.wav')

    overlay = OverlayAudio(carrier_file, 'amp_shifted.wav')

    overlay.export(out_f='encoded_overlay.wav',
                   format="wav",
                   bitrate="2000k",)

    if audio == 1:
        play(source)
        play(shifted)
        # play(amp_down)
        play(overlay)


def decode(encoded, freq=65, amp=1):
    audio = 1

    high_pass(encoded, 'filtered.wav')

    restored = Shift_pitch(
        'filtered.wav', 'pitched_down.wav', frequency=-freq)

    amp_up = ChangeAmplitude('pitched_down.wav', amp, 'decoded.wav')

    if audio == 1:
        filtered = AudioSegment.from_file(file='filtered.wav',
                                          format="wav")
        play(filtered)

        play(restored)

        # play(amp_up)


if __name__ == '__main__':
    encode(carrier_file='rick.wav',
           source_file='beep-11.wav', )
    decode('encoded_overlay.wav', )

    soundcloud = AudioSegment.from_file(file='soundcloud.wav',
                                        format="wav")

    play(soundcloud)

    soundcloud_decoded = AudioSegment.from_file(file='soundcloud_decoded.wav',
                                                format="wav")
    play(soundcloud_decoded)
