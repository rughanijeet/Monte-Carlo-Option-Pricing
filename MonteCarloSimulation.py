# Importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set max row to 300
pd.set_option('display.max_rows', 300)

# Generate path
def simulate_path(spot, mu, sigma, horizon, timesteps, nsims):
    
    # set the seed
    np.random.seed(2025)

    # define dt
    dt = horizon/timesteps
    
    # simulate path
    S = np.zeros((timesteps,nsims))
    S[0] = spot
    
    for i in range(0, timesteps-1):
        w = np.random.standard_normal(nsims)
        S[i+1] = S[i] * (1+ mu*dt + sigma*np.sqrt(dt)*w)
    
    return S


# Assign simulated price path to dataframe for analysis and plotting
price_path = pd.DataFrame(simulate_path(100,0.05,0.2,1,252,100000))

# Verify the generated price paths
price_path.head()


# Plot the histogram of the simulated price path at maturity
price_path.iloc[-1].hist(bins=100);

# Plot initial 100 simulated path using matplotlib
plt.plot(price_path.iloc[:,:100])
plt.xlabel('time steps')
plt.xlim(0,252)
plt.ylabel('index levels')
plt.title('Monte Carlo Simulated Asset Prices');