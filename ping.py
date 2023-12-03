import pyaudio
import numpy as np
import time

def play_tone(frequency, duration):
    sampling_rate = 44100  # Sample rate (samples per second)
    time_points = np.linspace(0, duration, int(sampling_rate * duration), False)

    # Generate sine wave
    tone = np.sin(frequency * 2 * np.pi * time_points)

    # Apply a fade-out effect to the tone
    fade_out_duration = int(0.5 * sampling_rate)  # Fade-out duration: 0.1 seconds
    fade_out_samples = np.linspace(1, 0, fade_out_duration)
    tone[-fade_out_duration:] *= fade_out_samples

    # Initialize PyAudio
    audio = pyaudio.PyAudio()

    # Open stream
    stream = audio.open(format=pyaudio.paFloat32,
                        channels=2,
                        rate=sampling_rate,
                        output=True)

    # Play tone
    stream.write(tone.astype(np.float32).tobytes())

    # Stop stream
    stream.stop_stream()
    stream.close()

    # Close PyAudio
    audio.terminate()

def send_pings(interval, num_pings):
    for _ in range (num_pings):
        # Play a ping (2000 Hz tone for 0.5 seconds)
        play_tone(2000, 0.5)
        time.sleep(interval)

# Send pings every 2 seconds for testing (10 times)
ping_interval = 1  # seconds
num_pings = 1

send_pings(ping_interval, num_pings)
