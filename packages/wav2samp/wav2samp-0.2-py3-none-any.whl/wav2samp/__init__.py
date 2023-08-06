from scipy.io.wavfile import write
from scipy.io.wavfile import read
import numpy as np
import sys


def txt2mono_wav(txt_file, sample_rate, wav_file):
    """This function is used to convert text file with audio samples in to mono wav file"""
    # open the text file which has audio samples
    file1 = open(txt_file, 'r')
    # Read the opened text file
    data = file1.read()
    print("Reading TXT file: " + txt_file)
    # Close the opened text file
    file1.close()

    # Convert into a list
    data2 = data.split('\n')
    # Reading the length of the data2 (number of rows in the txt file)
    length1 = len(data2)
    print("Number of Samples: " + str(length1))

    # Convert into a numpy ndarray of data type int16
    data3 = np.asarray(data2[0:length1-1], dtype=np.int16)

    # Write the numpy ndarray into a .wav file with a sample rate given
    write(wav_file, sample_rate, data3)
    print("Writing to WAV file " + wav_file + " " + "with the sample rate of " + str(sample_rate) + "Hz " + "DONE")


def mono_wav2txt(file_name, txt_file):
    """This function is used to convert mono wav file in to a text file with audio samples"""
    # Read the .wav file (Get the Sampling rate and the data)
    fs, data = read(file_name)
    print("Reading WAV file: " + file_name)

    # Print the Sampling rate in Hz
    print("Sampling Rate: {} Hz".format(fs))

    if len(data.shape) == 2:
        print("Stereo detected!")
        print("Error. You cannot use this function to convert stereo .wav files.")
        print("Please use stereo_wav2txt() function")
    elif len(data.shape) == 1:
        print("Mono detected!")
        # set the numpy ndarray to maximum size without truncations
        np.set_printoptions(threshold=sys.maxsize)

        # Convert the objects inside the numpy ndarray in to strings
        new_list2 = data.astype(str)

        # Open a text file with Write enable
        text_file = open(txt_file, 'w')
        print("Creating a TXT file: " + txt_file)

        # Write the audio samples into a column of the text file
        print("Writing to TXT file: " + txt_file)
        for item in new_list2:
            text_file.writelines("%s\n" % item)
            # Note that when writing in to a text file it creates a empty space after the last sample.
            # Therefore when converting back to a .wav file it is essential to give the right number of samples.

        # Close the text file
        text_file.close()
        print("Writing to " + txt_file + " DONE")


def stereo_wav2txt(file_name, txt_left, txt_right):
    """This function is used to convert stereo wav file in to two text file with left and right audio samples"""
    # Read the .wav file (Get the Sampling rate and the data)
    fs, data = read(file_name)
    print("Reading WAV file: " + file_name)

    # Print the Sampling rate in Hz
    print("Sampling Rate: {} Hz".format(fs))

    # Check the shape of the audio data which is Stereo or Mono
    if len(data.shape) == 2:
        print("Stereo detected!")
        data_left_ch = data[:, 0]
        data_right_ch = data[:, 1]

        # Convert the objects inside the numpy ndarray in to strings
        new_list_l = data_left_ch.astype(str)
        new_list_r = data_right_ch.astype(str)

        # Write in to two txt files
        print("Creating and Writing to TXT files: " + txt_left + " " + txt_right)
        np.savetxt(txt_left, new_list_l, fmt=['%s'])
        np.savetxt(txt_right, new_list_r, fmt=['%s'])
        print("Writing to " + txt_left + " and " + txt_right + " DONE")
    elif len(data.shape) == 1:
        print("Mono detected!")
        print("Error. You cannot use this function to convert mono .wav files.")
        print("Please use mono_wav2txt() function")


def txt2stereo_wav(txt_left, txt_right, sample_rate, wav_file):
    """This function is used to convert two text files with left and right audio samples in to stereo wav file"""
    # open the text file which has audio samples
    file1 = open(txt_left, 'r')
    file2 = open(txt_right, 'r')
    # Read the opened text file
    data_left = file1.read()
    print("Reading TXT file: " + txt_left)
    data_right = file2.read()
    print("Reading TXT file: " + txt_right)
    # Close the opened text file
    file1.close()
    file2.close()
    # Convert into a list
    data_l = data_left.split('\n')
    data_r = data_right.split('\n')
    # Combine the two lists to two columns in an array
    data = np.column_stack([data_l, data_r])
    # Reading the length of the data2 (number of rows in the txt file)
    length1 = len(data)
    print("Number of Samples: " + str(length1))
    # Convert into a numpy ndarray of data type int16
    data2 = np.asarray(data[0:length1 - 1], dtype=np.int16)
    # Write the numpy ndarray into a .wav file with a sample rate given
    write(wav_file, sample_rate, data2)
    print("Writing to WAV file " + wav_file + " " + "with the sample rate of " + str(sample_rate) + "Hz " + "DONE")

