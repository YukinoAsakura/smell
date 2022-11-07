import numpy as np
import pyaudio
import wave
import struct
import time

def test():
    SAMPLE_RATE = 44100
    # 指定ストリーム,指定周波数のサイン波,指定秒数再生
    def play(s: pyaudio.Stream, freq: float, duration: float):
        # 指定周波数のサイン波を指定秒数分生成
        samples = np.sin(np.arange(int(duration * SAMPLE_RATE)) * freq * np.pi * 2 / SAMPLE_RATE)
        # ストリームに渡して再生
        s.write(samples.astype(np.float32).tobytes())

    p = pyaudio.PyAudio()
    # ストリームを開く
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=SAMPLE_RATE,
                    frames_per_buffer=1024,
                    output=True)
# ドレミ...の周波数を定義 --- C,D,E,F,G,A,B,C2 = (261.626, 293.665, 329.628, 349.228, 391.995, 440.000,493.883, 523.251)
    play(stream, 261.626, 0.3)  # note#60 C4 ド 
    play(stream, 329.628, 0.3)  # note#64 E4 ミ
    play(stream, 391.995, 0.3)  # note#67 G4 ソ
    play(stream, 523.251, 0.6)  # note#72 C5 ド

    stream.close()
    # 終了
    p.terminate()


def alert_max():
    SAMPLE_RATE = 44100 #cdと同程度
    # 指定ストリーム,指定周波数のサイン波,指定秒数再生
    def play(s: pyaudio.Stream, freq: float, duration: float):
        # 指定周波数のサイン波を指定秒数分生成
        samples = np.sin(np.arange(int(duration * SAMPLE_RATE)) * freq * np.pi * 2 / SAMPLE_RATE)
        # ストリームに渡して再生
        s.write(samples.astype(np.float32).tobytes())

    p = pyaudio.PyAudio()
    # ストリームを開く
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=SAMPLE_RATE,
                    frames_per_buffer=1024,
                    output=True)

    play(stream, 440.000, 0.1)  # note#60 C4 ド 
    time.sleep(0.1)
    play(stream, 440.000, 0.1)  # note#64 E4 ミ
    time.sleep(0.1)
    play(stream, 440.000, 0.1)  # note#67 G4 ソ
    time.sleep(0.1)
    play(stream, 440.000, 0.1)  # note#72 C5 ド

    stream.close()
    # 終了
    p.terminate()

def alert_min():
    SAMPLE_RATE = 44100 #cdと同程度
    # 指定ストリーム,指定周波数のサイン波,指定秒数再生
    def play(s: pyaudio.Stream, freq: float, duration: float):
        # 指定周波数のサイン波を指定秒数分生成
        samples = np.sin(np.arange(int(duration * SAMPLE_RATE)) * freq * np.pi * 2 / SAMPLE_RATE)
        # ストリームに渡して再生
        s.write(samples.astype(np.float32).tobytes())

    p = pyaudio.PyAudio()
    # ストリームを開く
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=SAMPLE_RATE,
                    frames_per_buffer=1024,
                    output=True)

    play(stream, 261.626, 0.3)  # note#60 C4 ド 
    time.sleep(0.5)
    play(stream, 329.628, 0.3)  # note#64 E4 ミ
    time.sleep(0.5)
    play(stream, 391.995, 0.3)  # note#67 G4 ソ
    time.sleep(0.5)
    play(stream, 523.251, 0.3)  # note#72 C5 ド

    stream.close()
    # 終了
    p.terminate()