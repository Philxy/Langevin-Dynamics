import csv
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as mticker    
import scipy.stats as stats

randomNumbersFile = open('randomNumbers.csv', 'r')
csvreader = csv.reader(randomNumbersFile)

ranomNumbers = []
for row in csvreader:
    ranomNumbers.append(float(row[0]))


stdDev = 100.0
numBoxes = 100


counts, bins = np.histogram([rnd / stdDev for rnd in ranomNumbers], bins = np.arange(-4,4,0.15))
normalization = max(counts)

plt.stairs([count / normalization for count in counts], bins, linewidth=1.5)
plt.plot(bins, stats.norm.pdf(bins, 0, 1)/0.4, alpha=0.8)

plt.gca().xaxis.set_major_formatter(mticker.FormatStrFormatter('%.0f$\sigma$'))

plt.ylabel('$N/N_\mathrm{max}$')

plt.show()


