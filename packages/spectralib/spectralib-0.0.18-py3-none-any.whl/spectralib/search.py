import numpy as np
from scipy.special import fresnel
from scipy.fft import rfft, irfft
import matplotlib.pyplot as plt

# PRESTO (Scott Ransom)
def presto_correlator_response(z, numbetween):
    if z == 0:
        return np.ones(numbetween)
    u = np.linspace(-0.5, 0.5, numbetween, endpoint=False)
    C, S = fresnel(np.sqrt(np.abs(z) * np.pi * u))
    response = (S - 1j * C) / np.sqrt(np.abs(z))
    return response

def generate_acceleration_response(roffset, numbetween, z, numkern):
    t = np.arange(0, 1, 1.0 / (numbetween * numkern))
    t_scaled = (t - roffset) * np.sqrt(2 * np.abs(z))
    C, S = fresnel(t_scaled)
    
    if z > 0:
        response = (C + 1j * S) / np.sqrt(np.abs(z))
    else:
        response = (S - 1j * C) / np.sqrt(np.abs(z))
    
    return response[:numkern]

def fdas(x, z_trials, numbetween):
    n = len(x)
    
    # Compute the FFT of the input signal x
    x_fft = rfft(x)
    
    # Calculate the correlator response for each z value
    responses = []
    for z in z_trials:
        response = presto_correlator_response(z, numbetween)
        responses.append(response)

    # Compute the FFT and conjugate of each response, only taking the real part
    response_fft_conj = []
    for response in responses:
        response_fft = rfft(np.real(response), n)
        response_fft_conj.append(np.conj(response_fft))

    # Multiply the x_fft with each response_fft_conj and compute the inverse FFT,
    # then truncate the result to the first half of the array
    power_spectra = []
    for response_fft_conj_z in response_fft_conj:
        product = x_fft * response_fft_conj_z
        power_spectrum = irfft(product, n)[:n // 2]
        power_spectra.append(power_spectrum)

    return power_spectra


# Create a synthetic time series
def synthetic_signal_with_acceleration(t, f0, z, amp=1):
    phase = 2 * np.pi * (f0 * t + 0.5 * z * t ** 2)
    return amp * np.sin(phase)

# Parameters
n = 2048
f0 = 50
z_true = 10
amp = 1
t = np.arange(n) / n
signal = synthetic_signal_with_acceleration(t, f0, z_true, amp)

# Add noise
noise_level = 0.5
noisy_signal = signal + noise_level * np.random.randn(n)

# Perform FDAS
numbetween = 64
z_trials = np.linspace(0, 20, 200)
power_spectra = fdas(noisy_signal, z_trials, numbetween)

# Find the maximum power and its corresponding z value
max_power = [np.max(power_spectrum) for power_spectrum in power_spectra]
best_z_index = np.argmax(max_power)
best_z = z_trials[best_z_index]

print(f"True z: {z_true}, Estimated z: {best_z}")

# Plot the results
plt.figure(figsize=(10, 6))

# Plot the original power spectrum
plt.subplot(2, 1, 1)
plt.plot(np.abs(original_power_spectrum))
plt.xlabel("Fourier Bin")
plt.ylabel("Power")
plt.title("Original Power Spectrum")

# Plot the FDAS processed power spectra
plt.subplot(2, 1, 2)
for idx, trial in enumerate(z_trials):
    plt.plot(np.abs(power_spectra[idx]), label=f"z = {trial}", linestyle='-', alpha=0.7)
plt.xlabel("Fourier Bin")
plt.ylabel("Power")
plt.title("FDAS Processed Power Spectra")
plt.legend()

plt.tight_layout()
plt.show()

