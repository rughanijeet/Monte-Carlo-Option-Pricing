import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set max row to 300
pd.set_option('display.max_rows', 300)

# Generate path
def simulate_path(spot, mu, sigma, horizon, timesteps, nsims):
    np.random.seed(2025)
    dt = horizon/timesteps
    S = np.zeros((timesteps, nsims))
    S[0] = spot
    
    for i in range(timesteps-1):
        w = np.random.standard_normal(nsims)
        S[i+1] = S[i] * (1 + mu*dt + sigma*np.sqrt(dt)*w)
    
    return S

# Simulate price paths
price_path = pd.DataFrame(simulate_path(100, 0.05, 0.2, 1, 252, 100000))

# Create figure with 2 subplots side by side
plt.figure(figsize=(14, 5))

# --- Plot 1: First 100 Paths ---
plt.subplot(1, 2, 1)  # 1 row, 2 columns, position 1
plt.plot(price_path.iloc[:, :100])
plt.xlabel('Time Steps (Trading Days)')
plt.xlim(0, 252)
plt.ylabel('Asset Price')
plt.title('First 100 Simulated Price Paths')

# --- Plot 2: Histogram of Terminal Prices ---
plt.subplot(1, 2, 2)  # 1 row, 2 columns, position 2
price_path.iloc[-1].hist(bins=100, edgecolor='k', alpha=0.7)
plt.xlabel('Terminal Price at Maturity (T=1 Year)')
plt.ylabel('Frequency')
plt.title('Distribution of Simulated Terminal Prices')

plt.tight_layout()  # Prevent overlapping
plt.show()

# Option pricing (unchanged)
S = simulate_path(100, 0.05, 0.2, 1, 252, 100000)
K = 100; r = 0.05; T = 1
C0 = np.exp(-r*T) * np.mean(np.maximum(0, S[-1] - K))
P0 = np.exp(-r*T) * np.mean(np.maximum(0, K - S[-1]))

print(f"European Call Option Value: {C0:0.4f}")
print(f"European Put Option Value: {P0:0.4f}")