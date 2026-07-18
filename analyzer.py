import json
import numpy as np
import soundfile as sf

# Load config
with open("config.json", "r") as f:
    cfg = json.load(f)

BASS_MIN, BASS_MAX = cfg["bass_range_hz"]
CLIP_THRESHOLD = cfg["clipping_threshold_db"]

def analyze_bass(file_path):
    print(f"Analyzing: {file_path}")

    # Load audio
    audio, sr = sf.read(file_path)
    audio = audio.astype(float)

    # Calculate RMS
    rms = np.sqrt(np.mean(audio**2))
    rms_db = 20 * np.log10(rms + 1e-9)

    # Peak detection
    peak = np.max(np.abs(audio))
    peak_db = 20 * np.log10(peak + 1e-9)

    # Clipping check
    clipping = peak_db >= CLIP_THRESHOLD

    print(f"Sample rate: {sr} Hz")
    print(f"RMS: {rms_db:.2f} dB")
    print(f"Peak: {peak_db:.2f} dB")
    print(f"Clipping detected: {clipping}")

    return {
        "rms_db": rms_db,
        "peak_db": peak_db,
        "clipping": clipping
    }

if __name__ == "__main__":
    print("Clean Bass Analyzer ready.")
