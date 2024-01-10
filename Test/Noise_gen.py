import numpy as np
import scipy.io.wavfile as wav
import scipy.fft as fft
import simpleaudio as sa

# Load the audio samples
violin_rate, violin_data = wav.read('violin_sample.wav')
flute_rate, flute_data = wav.read('flute_sample.wav')

# Apply Fourier transform to each sample
violin_spectrum = np.abs(fft(violin_data))
flute_spectrum = np.abs(fft(flute_data))

# Identify frequencies with highest amplitudes
violin_freqs = np.argsort(violin_spectrum)[-5:]
flute_freqs = np.argsort(flute_spectrum)[-5:]

# Generate sine waves with identified frequencies and amplitudes
violin_sines = [np.sin(2 * np.pi * f / violin_rate * np.arange(len(violin_data))) * violin_spectrum[f] for f in violin_freqs]
flute_sines = [np.sin(2 * np.pi * f / flute_rate * np.arange(len(flute_data))) * flute_spectrum[f] for f in flute_freqs]

# Combine sine waves to create reconstructed signals
violin_reconstructed = np.sum(violin_sines, axis=0)
flute_reconstructed = np.sum(flute_sines, axis=0)

# Play original and reconstructed signals
violin_original = sa.play_buffer(violin_data, 1, 2, violin_rate)
violin_original.wait_done()
violin_reconstructed = sa.play_buffer(violin_reconstructed.astype(np.int16), 1, 2, violin_rate)
violin_reconstructed.wait_done()

flute_original = sa.play_buffer(flute_data, 1, 2, flute_rate)
flute_original.wait_done()
flute_reconstructed = sa.play_buffer(flute_reconstructed.astype(np.int16), 1, 2, flute_rate)
flute_reconstructed.wait_done()
import numpy as np
import scipy.io.wavfile as wav
import scipy.fft as fft
import simpleaudio as sa

def pitch_shift_sound(sound_file_path, pitch_changes, sample_rate):
    # Load the audio samples
    rate, data = wav.read(sound_file_path)

    # Apply Fourier transform to the sample
    spectrum = np.abs(fft(data))

    # Identify frequencies with highest amplitudes
    freqs = np.argsort(spectrum)[-5:]

    # Generate sine waves with identified frequencies and amplitudes
    sines = [np.sin(2 * np.pi * f / rate * np.arange(len(data))) * spectrum[f] for f in freqs]

    # Combine sine waves to create reconstructed signal
    reconstructed = np.sum(sines, axis=0)

    # Apply pitch changes to reconstructed signal
    for pitch_change in pitch_changes:
        reconstructed = librosa.effects.pitch_shift(reconstructed, sr=rate, n_steps=pitch_change)

    # Play original and reconstructed signals together
    original = sa.play_buffer(data, 1, 2, rate)
    reconstructed = sa.play_buffer(reconstructed.astype(np.int16), 1, 2, rate)
    sa.play_buffer(np.concatenate((data, reconstructed)), 1, 2, rate).wait_done()

    return reconstructed
