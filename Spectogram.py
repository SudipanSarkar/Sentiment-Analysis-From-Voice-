import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy import signal
from playsound import playsound
import numpy as np
import pandas as pd
import os
ravdess_path = r"C:\Users\SUDIPAN SARKAR\OneDrive\Desktop\Final Year Project\RAVDESS DATA SET"
savee_path = r"C:\Users\SUDIPAN SARKAR\OneDrive\Desktop\Final Year Project\SAVEE DATASET\ALL"
ravdess_files = [os.path.join(ravdess_path, f) for f in os.listdir(ravdess_path)]
savee_files = [os.path.join(savee_path, f) for f in os.listdir(savee_path)]
all_files = ravdess_files + savee_files
for audio_path in all_files:
    if audio_path.endswith(".wav"):
        playsound(audio_path)

        # Read audio file
        sr, data = wavfile.read(audio_path)

        # Convert stereo to mono
        if len(data.shape) > 1:
            data = np.mean(data, axis=1)

        # Generate spectrogram
        frequencies, times, Sxx = signal.spectrogram(data, sr)

        # Plot spectrogram
        plt.figure(figsize=(6, 4))
        plt.pcolormesh(times, frequencies, 10 * np.log10(Sxx), shading='auto', cmap="jet")
        plt.xlabel("Time (s)")
        plt.ylabel("Frequency (Hz)")
        plt.title(f"Spectrogram - {audio_path}")
        plt.colorbar(label="Intensity (dB)")
        plt.tight_layout()
        plt.show()

        print("Displayed spectrogram for:", audio_path)
