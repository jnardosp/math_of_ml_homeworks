import numpy as np
import matplotlib.pyplot as plt

#parameters
num_coins = 1000 #num of coins
num_flips = 10 #num of flips per coin
num_exp = 100000 #num of independent experiments

#variables to store empirical mean
v1 = []
vrand = []
vmin = []

for _ in range(num_exp):
    #0 = Tails
    #1 = Heads
    flips = np.random.randint(0, 2, size=(num_coins, num_flips))

    # Num of heads obtained by each coin
    heads = np.sum(flips, axis=1)

    # Fraction of heads for every coin
    frequencies = heads / num_flips

    # First coin
    v1.append(frequencies[0])

    # Randomly selected coin
    random_index = np.random.randint(num_coins)
    vrand.append(frequencies[random_index])

    # Coin with the minimum fraction of heads
    vmin.append(np.min(frequencies))

v1 = np.array(v1)
vrand = np.array(vrand)
vmin = np.array(vmin)

bins = np.arange(-0.05, 1.15, 0.1)
fig, axes = plt.subplots(1, 3, figsize=(16, 5))

#first coin
axes[0].hist(v1, bins=bins, edgecolor='black')
axes[0].set_title(r'First Coin ($\nu_1$)')
axes[0].set_xlabel('Fraction of Heads')
axes[0].set_ylabel('Frequency')
axes[0].set_xlim(0, 1)

#random coin
axes[1].hist(vrand, bins=bins, edgecolor='black', color='orange')
axes[1].set_title(r'Random Coin ($\nu_{rand}$)')
axes[1].set_xlabel('Fraction of Heads')
axes[1].set_ylabel('Frequency')
axes[1].set_xlim(0, 1)

#minimum coin
axes[2].hist(vmin, bins=bins, edgecolor='black', color='purple')
axes[2].set_title(r'Minimum Coin ($\nu_{min}$)')
axes[2].set_xlabel('Fraction of Heads')
axes[2].set_ylabel('Frequency')
axes[2].set_xlim(0, 1)

plt.tight_layout()
plt.show()

print("Average fraction of heads:")
print(f"First coin   : {np.mean(v1):.4f}")
print(f"Random coin  : {np.mean(vrand):.4f}")
print(f"Minimum coin : {np.mean(vmin):.4f}")

#estimate P(|nu-mu|>=epsilon)
MU = 0.5
epsilons = np.linspace(0, 0.5, 101)

p_v1 = []
p_vrand = []
p_vmin = []

for eps in epsilons:
    p_v1.append(np.mean(np.abs(v1 - MU) >= eps))
    p_vrand.append(np.mean(np.abs(vrand - MU) >= eps))
    p_vmin.append(np.mean(np.abs(vmin - MU) >= eps))

p_v1 = np.array(p_v1)
p_vrand = np.array(p_vrand)
p_vmin = np.array(p_vmin)

#Hoeffding bound
hoeffding = 2 * np.exp(-2 * num_flips * epsilons**2)

#plot Hoeffding comparison
plt.figure(figsize=(8,6))

plt.plot(
    epsilons,
    p_v1,
    linewidth=2,
    label=r"$\nu_1$"
)

plt.plot(
    epsilons,
    p_vrand,
    linewidth=2,
    label=r"$\nu_{rand}$"
)

plt.plot(
    epsilons,
    p_vmin,
    linewidth=2,
    label=r"$\nu_{min}$"
)

plt.plot(
    epsilons,
    hoeffding,
    "k--",
    linewidth=3,
    label="Hoeffding Bound"
)

plt.xlabel(r"$\epsilon$", fontsize=12)
plt.ylabel(r"$P(|\nu-\mu|>\epsilon)$", fontsize=12)
plt.grid(True)
plt.legend()

plt.show()