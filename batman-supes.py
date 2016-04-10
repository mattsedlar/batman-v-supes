import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf

movies = ["Fantastic Four","The Dark Knight Rises","Kick-Ass 2", "Avengers: Age of Ultron", "Iron Man 3", "Captain America: Winter Soldier", "X-Men: First Class", "The Amazing Spider-Man 2", "Thor", "Ant-Man","Guardians of the Galaxy","Captain America: First Avenger","Thor: The Dark World","The Wolverine","TMNT (2014)", "Green Lantern","Marvel's The Avengers","X-Men: Days of Future Past","Green Hornet","Ghost Rider: Spirit of Vengeance","Big Hero 6","Man of Steel","Chronicle","Dredd","Kick-Ass","Jonah Hex","Iron Man 2","X-Men Origins: Wolverine","Watchmen","Push","Jumper","Iron Man","The Incredible Hulk"]

release_year = ["2015","2012","2013","2015","2013","2014","2011","2014","2011","2015","2014","2011","2013","2013","2014","2011","2012","2014","2011","2012","2014","2013","2012","2012","2010","2010","2010","2009","2009","2009","2008","2008","2008"]

first_fri = [11.28,75.8,5.83,84.4,68.9,36.9,21.4,35.2,25.5,22.6,37.8,25.7,31.9,20.7,25.6,21.4,80.8,35.5,11.1,6.9,15.8,44.03,8.65,2.2,7.6,1.9,51.2,34.4,24.5,3.5,6.6,35.2,21.4]

first_sun = [5.83,40.2,3.31,50.3,43,23.4,14,23.3,16.9,15.1,25.5,17.4,21.8,14.3,17.8,15.1,57.1,26,9.8,6.5,16.4,36.3,3.25,1.6,4.9,1.6,31.1,21.3,12.3,2.4,10.6,26,15.5]

opening = [25.6,160.8,13.3,191.2,174.1,95,55.1,91.6,65.7,57.2,94.3,65,85.7,53.1,65.5,53.1,207.4,90.8,33.5,22.1,56.2,116.6,22,6.27,19.8,5.37,128.1,85,55.2,10,27.3,98.6,55.4]

final_gross = [56.1,448.1,28.8,459,409,259.8,146.4,202.9,181,180.2,333.2,176.7,206.4,132.6,191.2,116.6,623.4,233.9,98.8,51.8,222.5,291,64.5,13.4,48,10.5,312,179.8,107.5,31.8,80.1,318.4,134.8]

critics = [.09,.87,.30,.75,.79,.89,.87,.53,.77,.80,.91,.79,.67,.70,.21,.26,.92,.91,.43,.17,.89,.56,.85,.78,.76,.12,.72,.38,.65,.23,.16,.94,.67]

d = { "Release Year" : pd.Series(release_year, index=movies),
      "FirstFridayGross" : pd.Series(first_fri, index=movies),
      "FirstSundayGross" : pd.Series(first_sun, index=movies),
      "OpeningWeekend" : pd.Series(opening, index=movies),
      "FinalGross" : pd.Series(final_gross, index=movies),
      "CriticsScores": pd.Series(critics, index=movies)}

df = pd.DataFrame(d)

# calculating earnings in 2015 dollars
# inflation, 2008 = 10.1%, 2009 = 10.5%, 2010 = 8.7%, 2011 = 5.4%, 2012 = 3.2%, 2013 = 1.7%, 2014 = 0.1%

# 2008
df.ix[df['Release Year'] == '2008','FirstFridayGross'] = df.ix[df['Release Year'] == '2008','FirstFridayGross'] * 1.101
df.ix[df['Release Year'] == '2008','FirstSundayGross'] = df.ix[df['Release Year'] == '2008','FirstSundayGross'] * 1.101
df.ix[df['Release Year'] == '2008','OpeningWeekend'] = df.ix[df['Release Year'] == '2008','OpeningWeekend'] * 1.101
df.ix[df['Release Year'] == '2008','FinalGross'] = df.ix[df['Release Year'] == '2008','FinalGross'] * 1.101

# 2009
df.ix[df['Release Year'] == '2009','FirstFridayGross'] = df.ix[df['Release Year'] == '2009','FirstFridayGross'] * 1.105
df.ix[df['Release Year'] == '2009','FirstSundayGross'] = df.ix[df['Release Year'] == '2009','FirstSundayGross'] * 1.105
df.ix[df['Release Year'] == '2009','OpeningWeekend'] = df.ix[df['Release Year'] == '2009','OpeningWeekend'] * 1.105
df.ix[df['Release Year'] == '2009','FinalGross'] = df.ix[df['Release Year'] == '2009','FinalGross'] * 1.105

# 2010
df.ix[df['Release Year'] == '2010','FirstFridayGross'] = df.ix[df['Release Year'] == '2010','FirstFridayGross'] * 1.087
df.ix[df['Release Year'] == '2010','FirstSundayGross'] = df.ix[df['Release Year'] == '2010','FirstSundayGross'] * 1.087
df.ix[df['Release Year'] == '2010','OpeningWeekend'] = df.ix[df['Release Year'] == '2010','OpeningWeekend'] * 1.087
df.ix[df['Release Year'] == '2010','FinalGross'] = df.ix[df['Release Year'] == '2010','FinalGross'] * 1.087

# 2011
df.ix[df['Release Year'] == '2011','FirstFridayGross'] = df.ix[df['Release Year'] == '2011','FirstFridayGross'] * 1.054
df.ix[df['Release Year'] == '2011','FirstSundayGross'] = df.ix[df['Release Year'] == '2011','FirstSundayGross'] * 1.054
df.ix[df['Release Year'] == '2011','OpeningWeekend'] = df.ix[df['Release Year'] == '2011','OpeningWeekend'] * 1.054
df.ix[df['Release Year'] == '2011','FinalGross'] = df.ix[df['Release Year'] == '2011','FinalGross'] * 1.054

# 2012
df.ix[df['Release Year'] == '2012','FirstFridayGross'] = df.ix[df['Release Year'] == '2012','FirstFridayGross'] * 1.032
df.ix[df['Release Year'] == '2012','FirstSundayGross'] = df.ix[df['Release Year'] == '2012','FirstSundayGross'] * 1.032
df.ix[df['Release Year'] == '2012','OpeningWeekend'] = df.ix[df['Release Year'] == '2012','OpeningWeekend'] * 1.032
df.ix[df['Release Year'] == '2012','FinalGross'] = df.ix[df['Release Year'] == '2012','FinalGross'] * 1.032

# 2013
df.ix[df['Release Year'] == '2013','FirstFridayGross'] = df.ix[df['Release Year'] == '2013','FirstFridayGross'] * 1.017
df.ix[df['Release Year'] == '2013','FirstSundayGross'] = df.ix[df['Release Year'] == '2013','FirstSundayGross'] * 1.017
df.ix[df['Release Year'] == '2013','OpeningWeekend'] = df.ix[df['Release Year'] == '2013','OpeningWeekend'] * 1.017
df.ix[df['Release Year'] == '2013','FinalGross'] = df.ix[df['Release Year'] == '2013','FinalGross'] * 1.017

# 2014
df.ix[df['Release Year'] == '2014','FirstFridayGross'] = df.ix[df['Release Year'] == '2014','FirstFridayGross'] * 1.001
df.ix[df['Release Year'] == '2014','FirstSundayGross'] = df.ix[df['Release Year'] == '2014','FirstSundayGross'] * 1.001
df.ix[df['Release Year'] == '2014','OpeningWeekend'] = df.ix[df['Release Year'] == '2014','OpeningWeekend'] * 1.001
df.ix[df['Release Year'] == '2014','FinalGross'] = df.ix[df['Release Year'] == '2014','FinalGross'] * 1.001

# friday to sunday percentage change
df = df.assign(perc_change= ((df["FirstSundayGross"] - df["FirstFridayGross"])/df["FirstFridayGross"]).round(2))

# OpeningWeekend multiplier
df = df.assign(multiplier=df["FinalGross"]/df["OpeningWeekend"])

# correlation coefficients
print("correlation between final gross and percentage change")
print(np.corrcoef(df["FinalGross"], df["perc_change"]))

print("correlation between final gross and multiplier")
print(np.corrcoef(df["FinalGross"], df["multiplier"]))

print("correlation between final gross and critics scores")
print(np.corrcoef(df["FinalGross"], df["CriticsScores"]))

print("correlation between critics scores and percentage change")
print(np.corrcoef(df["perc_change"], df["CriticsScores"]))


# linear model
fit = smf.ols(formula="FinalGross ~ CriticsScores + perc_change",data=df).fit()
print(fit.summary())

# PLOTS
ax = df.plot.scatter(x="multiplier",y="FinalGross",title="Short- and Long-Run Peformance of Superhero Films, 2010-2015",s=50,edgecolor="none",alpha=0.75)
ax.set_xlabel("Opening Weekend Multiplier")
ax.set_ylabel("Final Domestic Gross (Millions)")
ax.set_title(ax.get_title(), fontsize=15, ha='left')
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.get_xaxis().tick_bottom()
ax.get_yaxis().tick_left()
ax.title.set_position((-0.05,1.05))
ax.tick_params('x',labelsize=8)
ax.tick_params('y',labelsize=8)
ax.set_ylim(0,700)
fig = ax.get_figure()
fig.savefig("batman-supes-fig-1.png")

ax2 = df.plot.scatter(x="perc_change",y="FinalGross",title="Short- and Long-Run Peformance of Superhero Films, 2010-2015",s=50,edgecolor="none",alpha=0.75)
ax2.set_xlabel("Friday to Sunday Earnings Percentage Change on Opening Weekend")
ax2.set_ylabel("Final Domestic Gross (Millions)")
ax2.set_title(ax2.get_title(), fontsize=15, ha='left')
ax2.title.set_position((-0.05,1.05))
ax2.spines["top"].set_visible(False)
ax2.spines["right"].set_visible(False)
ax2.get_xaxis().tick_bottom()
ax2.get_yaxis().tick_left()
ax2.tick_params('x',labelsize=8)
ax2.tick_params('y',labelsize=8)
ax2.set_ylim(0,700)
fig = ax2.get_figure()
fig.savefig("batman-supes-fig-2.png")

ax3 = df.plot.scatter(x="perc_change",y="FinalGross",c="CriticsScores",cmap=plt.cm.BuPu,s=50,title="Short- and Long-Run Peformance of Superhero Films, 2010-2015",edgecolor="none",alpha=0.75)
ax3.set_xlabel("Friday to Sunday Earnings Percentage Change on Opening Weekend")
ax3.set_ylabel("Final Domestic Gross (Millions)")
ax3.set_title(ax3.get_title(), fontsize=15, ha='left')
ax3.title.set_position((-0.05,1.05))
ax3.spines["top"].set_visible(False)
ax3.spines["right"].set_visible(False)
ax3.get_xaxis().tick_bottom()
ax3.get_yaxis().tick_left()
ax3.tick_params('x',labelsize=8)
ax3.tick_params('y',labelsize=8)
ax3.set_ylim(0,700)
fig = ax3.get_figure()
fig.savefig("batman-supes-fig-3.png")

ax4 = df.plot.scatter(x="CriticsScores",y="FinalGross",title="Critics' Scores and Domestic Gross of Superhero Films, 2010-2015",s=50,edgecolor="none",alpha=0.75)
ax4.set_xlabel("Rotten Tomatoes Score")
ax4.set_ylabel("Final Domestic Gross (Millions)")
ax4.set_title(ax4.get_title(), fontsize=15, ha='left')
ax4.title.set_position((-0.05,1.05))
ax4.spines["top"].set_visible(False)
ax4.spines["right"].set_visible(False)
ax4.get_xaxis().tick_bottom()
ax4.get_yaxis().tick_left()
ax4.tick_params('x',labelsize=8)
ax4.tick_params('y',labelsize=8)
ax4.set_ylim(0,700)
fig = ax4.get_figure()
fig.savefig("batman-supes-fig-4.png")