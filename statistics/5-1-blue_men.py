[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

>>


# Ex 5.1 ---------------------------------------------------------------------------------

'''
In order to join Blue Man Group, you have to be male between 5’10” and 6’1”
What percentage of the U.S. male population is in this range? 
'''
import brfss
import scipy
df = brfss.ReadBrfss()


# i got 47.3% cuz i used the actual data from df...
# they got 34% cuz they just used a normal distribution

# MY WAY:

# 1 is men
# 2 is women

men = df[df.sex = 1]
avg = men.htm3.mean() # 178
sd = men.htm3.std() #7.7

def inches_to_cm(inches):
	return inches*2.54


# 5,10 = 12*5 +10 = 70 inches
# 6,1 = 12*6 + 1 = 73 inches

low = inches_to_cm(70) #177.8
high = inches_to_cm(73) # 185.4

num_men = len(men) # 155703
num_blue_men = len(men[(men.htm3 > 177.8) & (men.htm3 < 185.4)]) # 73697
num_blue_men/float(num_men) # 47%...


p_low = len(men[men.htm3<177.8])/float(num_men) #40%
p_high = len(men[men.htm3<185.4])/float(num_men) # 87%
p_high - p_low # 47%


# THEIR WAY:
avg = 178
sd = 7.7

norm_dis = scipy.stats.norm(loc = avg, scale = sd)
plow = norm_dis.cdf(low) # 49%
phigh = norm_dis.cdf(high) # 83%
perc = phigh-plow # 34%

# The Point of all this is that you can find the probability of people within a range 
	# by subtracting the high cdf from the low cdf
# This is mainly for continous random variables



