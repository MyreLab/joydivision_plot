
import pandas as pd
import matplotlib.pyplot as plt

#setting the size of the frame
vertical_margin = 20
horizontal_margin = 20
x_size = 30
y_size = 30

#line width
linewidth = 4

#source dataset
src = 'https://gist.githubusercontent.com/borgar/31c1e476b8e92a11d7e9/raw/0fae97dab6830ecee185a63c1cee0008f6778ff6/pulsar.csv'

#plot name
joydiv='joydiv_plot.png'

#use grayscale theme
df = pd.read_csv(src, header=None)
plt.style.use('grayscale')

#add subplot with no frame
fig, ax = plt.subplots(figsize=(x_size,y_size),frameon=False)

n_lines = df.shape[0]
x = range(df.shape[1])

#plotting the lines
for row in df.iterrows():
    line = row[1].values/3 + (n_lines - row[0])
    ax.plot(x, line, lw=linewidth, c='black', alpha=1, zorder=row[0]/n_lines)
    ax.fill_between(x, -5,line,  facecolor='white', zorder=row[0]/n_lines)

#no ticks
ax.set_yticks([])
ax.set_xticks([])

#set x and y limits
ax.set_xlim(min(x)-horizontal_margin, max(x)+horizontal_margin)
ax.set_ylim(-vertical_margin, df.shape[0] + vertical_margin)

#save plot
plt.savefig(joydiv)