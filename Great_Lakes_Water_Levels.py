<<<<<<< HEAD
""""
To use this notebook for your in-class assignment, you will need these 
files, which you shoujld have downloaded:
* mhu.csv -- Lake Michigan and Lake Huron
* sup.csv -- Lake Superior
* eri.csv -- Lake Erie
* ont.csv -- Lake Ontario

As instructed in the in-class activity notebook for today, you are 
only expected to complete one PART below. Do not worry if your group 
is not big enough to finish all parts below, but if you have extra 
time, you're welcome to do so.
""""


=======
>>>>>>> 4459d1e9c70d560df6b4a3997b5451ee2198bdbf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# -

# PART 1
# Using the Michigan/Huron Dataset, plot the Water Level, the second 
# column, as a function of time years

<<<<<<< HEAD
# +
mhu = pd.read_csv("mhu.csv")
mhu.head()

plt.plot(mhu["time"], mhu["lake average"])
# -
=======
mhu = pd.read_csv("mhu.csv")
plt.plot(mhu["time"], mhu["lake average"])
>>>>>>> 4459d1e9c70d560df6b4a3997b5451ee2198bdbf

# PART 2
# Using the Superior Dataset, plot the Water Level, the second column, 
# as a function of time years

<<<<<<< HEAD
# +
sup = pd.read_csv("sup.csv")
sup.head()

plt.plot(sup["year"], sup["lake levels"])
# -
=======
sup = pd.read_csv("sup.csv")
year = sup["year"]
lake_levels = sup["lake levels"]
plt.plot(year, lake_levels, label= "Water level")
plt.title("Lake Levels Over Time")
plt.legend()
>>>>>>> 4459d1e9c70d560df6b4a3997b5451ee2198bdbf

# PART 3
# Using the Erie Dataset, plot the Water Level, the second column, 
# as a function of time years

# +
eri = pd.read_csv("eri.csv")
eri.head()

plt.plot(eri["time"], eri["water level"])
# -

# PART 4
# Using the Ontario Dataset, plot the Water Level, the second column, 
# as a function of time years

# +
ont = pd.read_csv("ont.csv")
ont.head()

plt.plot(ont["year"], ont["Lake Ontario annual averages"])
# -

# PART 5
# Using the Michigan/Huron and Superior Datasets, plot the 
# Michigan/Hurion Water Level vs Superior Water Level to see if there 
# is any correlation between the water levels.

plt.plot(mhu)

# PART 6
# Using the Michigan/Hurion and Erie Datasets, plot the 
# Michigan/Huron Water Level vs Erie Water Level to see if there is 
# any correlation between the water levels.



# PART 7
# Using the Superior and Ontario Datasets, plot the Superior Water 
# Level vs Ontario Water Level to see if there is any correlation 
# between the water levels.


