import csv
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as mticker    
import scipy.stats as stats
import scipy.integrate as integrate

plt.figure(figsize=(8/2.54, 7/2.54), dpi=80)


randomNumbersFile = open('randomNumbers.csv', 'r')
csvreader = csv.reader(randomNumbersFile)

ranomNumbers = []
for row in csvreader:
    ranomNumbers.append(float(row[0]))


stdDev = 1.0
numBoxes = 60


counts, bins = np.histogram([rnd / stdDev for rnd in ranomNumbers], bins = np.arange(-4,4,0.2))
normalization = integrate.simps(counts,bins[:-1])

plt.stairs([count / normalization for count in counts], bins, fill=True, label='Zufallsgenerator')
plt.plot(bins, stats.norm.pdf(bins, 0, 1), alpha=0.7, label='Normalverteilung', linewidth=2)

#plt.gca().xaxis.set_major_formatter(mticker.FormatStrFormatter('%.0f$\sigma$'))



plt.ylabel('Wahrscheinlichkeitsdichte $p(\zeta)$')
plt.xlabel(r'Amplitude $\zeta$')
plt.tight_layout()
plt.savefig('Figures/_random_numbers_distribution_N_100000_std_1.pdf')
plt.show()


