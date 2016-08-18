#!/usr/bin/python3.3
"""Plot # types vs. # tokens for several languages."""

import numpy as np
import matplotlib.pyplot as plot

# Tableau Color Blind 10 palette
cb10 = [(0,107,164), (200,82,0)]
cb10 = [(r/255.,g/255.,b/255.) for r,g,b in cb10]

# Languages
langL = [(206,'Zulu'),
         (102,'Assamese')]

# Read in data
data = list()
for lang in langL:
    file_ = '{}.dat'.format(lang[0])
    data.append(np.loadtxt(file_))

# Set up figure size, font size, and clean axes
plot.figure(figsize=(10.8,7.2))

# Generate the plot
for langX, lang in enumerate(langL):
    plot.plot(data[langX][:,0],data[langX][:,1],color=cb10[langX],
              lw=4,label=lang[1])

ax = plot.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.get_xaxis().tick_bottom()
ax.get_xaxis().set_ticklabels([])
ax.get_yaxis().tick_left()
ax.get_yaxis().set_ticklabels([])
plot.axis([0, 350000, 0, 60000])
plot.legend(loc='best',fontsize=24)

# plot.show()
plot.savefig('../vocGrowthThumb.pdf',bbox_inches='tight')
