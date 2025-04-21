# Call the simulation function
S = simulate_path(100,0.05,0.2,1,252,100000)

# Define parameters
K=100; B=150; r=0.05; sigma=0.20; T=1; t=252; dt=T/t; barrier_rebate = 0

# Barrier shift - continuity correction for discrete monitoring
barrier_shift = B*np.exp(0.5826*sigma*np.sqrt(dt))

# Calculate the discounted value of the expeced payoff
C0 = np.exp(-r*T) * np.mean(np.where(np.max(S, axis=0) < barrier_shift, np.maximum(S[-1,:] - K, 0), barrier_rebate))

# Print the values 
print(f"Up-and-Out Barrier Call Option Value is {C0:0.4f}")

figure, axes = plt.subplots(1,3, figsize=(20,6), constrained_layout=True)
title = ['Visualising the Barrier Condition', 'Spot Touched Barrier', 'Spot Below Barrier']

axes[0].plot(S[:,:200])      
for i in range(200):
    axes[1].plot(S[:,i]) if S[:,i].max() > barrier_shift else axes[2].plot(S[:,i])

for i in range(3):
    axes[i].set_title(title[i])
    axes[i].hlines(barrier_shift, 0, 252, colors='k', linestyles='dashed')

figure.supxlabel('time steps')
figure.supylabel('index levels')

plt.show()