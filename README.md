######
Scenario:
This covert channel is for sending secure information to an inside oporative under the guise of standard friendly communiation.
Communication is done through obfuscated sound files and can contain text or audio reccording within a sound file format.

Capabilities:
Can send megabytes worth of information in a single transmission. This makes it very capable for breif but data-heavy conversation
or file transferrs

#####
How to use:

install dependencies for Librosa, Pydub, scipy, numpy, matplotlib, soundfile, wave

pip3 install <library_name>
repeat this for each dependency

To use run main.py and audio will play for each step of the encoding and decoding process. To change signals being encoded or decoded you can change the source and carrier file within the encode() function call. 
  Please note that changing the input files may end in worse results. The band pass filter has been calibrated for the current directory and needs to be adjusted for other files. 
To observe any spectrograms specify the desired file in spectrogram.py and run the file. 
Other flags are available in each function call for any desired audio changes.

To encode the files we utilize Librosa and Pydub to perform fourier transforms and to overlay the audio respectively. To decode we use a band pass filter and fourier transforms again. 
