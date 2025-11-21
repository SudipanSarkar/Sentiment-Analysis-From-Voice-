import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy import signal
import numpy as np


audio_path = r"C:\Users\SUDIPAN SARKAR\OneDrive\Desktop\Final Year Project\archive\ALL\DC_a03.wav"

sr, data = wavfile.read(audio_path)


if len(data.shape) > 1:
    data = np.mean(data, axis=1)


frequencies, times, Sxx = signal.spectrogram(data, sr)


# different types of colormaps  : 'inferno', 'magma', 'plasma', 'viridis', 'cividis', 'jet'
cmap = "jet"

plt.figure(figsize=(6, 4))
plt.pcolormesh(times, frequencies, 10 * np.log10(Sxx), shading='auto', cmap=cmap)
plt.xlabel("Time (s)")
plt.ylabel("Frequency (Hz)")
plt.title(f"Spectrogram ({cmap})")
plt.colorbar(label="Intensity (dB)")
plt.tight_layout()
plt.show()
