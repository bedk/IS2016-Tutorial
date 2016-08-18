#!/usr/bin/python3.3
"""Plot # types vs. # tokens for several languages."""

import numpy as np
import matplotlib.pyplot as plot

# Tableau Color Blind 10 palette
cb10 = [(0,107,164), (255,128,14), (171,171,171), (89,89,89),
        (95,158,209), (200,82,0), (137,137,137), (162,200,236),
        (255,188,121), (207,207,207)]
cb10 = [(r/255.,g/255.,b/255.) for r,g,b in cb10]

# Languages
langL = [(206,'Zulu'),
         (307,'Amharic'),
         (404,'Georgian'),
         (305,'Guaraní'),
         (401,'Mongolian'),
         (102,'Assamese'),
         (403,'Dholuo'),
         (306,'Igbo'),
         (201,'Haitian Creole'),
         (207,'Tok Pisin'),]

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
ax.get_yaxis().tick_left()
plot.axis([0, 350000, 0, 60000])
plot.xticks(fontsize=12)
plot.yticks(fontsize=12)
plot.xlabel('# observed tokens',fontsize=14)
plot.ylabel('# observed types',fontsize=14)
# plot.title('Vocabulary Growth for Babel Languages',fontsize=16)
plot.legend(loc='best')

# plot.show()
plot.savefig('../vocGrowth.pdf',bbox_inches='tight')
