#Author:Bing Liu
import wave
import struct
import numpy as np


if __name__ == '__main__':
    data_size = 40000
    fname = "auido.wav"
    frate = 11025.0
    wav_file = wave.open(fname, 'r')
    params = wav_file.getparams()
    ''' _nchannels -- the number of audio channels
              available through the getnchannels() method
    _nframes -- the number of audio frames
              available through the getnframes() method
    _sampwidth -- the number of bytes per audio sample
              available through the getsampwidth() method
    _framerate -- the sampling frequency'''
    print(params)
    # sampwidth, framerate, nframes =params[:4]

    data = wav_file.readframes(data_size)
    wav_file.close()
    data = struct.unpack('{n}h'.format(n=data_size), data)
    data = np.array(data)
    w = np.fft.fft(data)
    freqs = np.fft.fftfreq(len(w))
    # '''频率最小值 频率最大值'''
    print(freqs.min(), freqs.max())
    # # (-0.5, 0.499975)
    print(freqs.view())
    # # Find the peak in the coefficients
    idx = np.argmax(np.abs(w))
    freq = freqs[idx]
    freq_in_hertz = abs(freq * frate)
    print(freq_in_hertz)
    # # 439.8975