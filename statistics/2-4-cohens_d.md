# Ex 2.4
'''
Using the variable totalbrthwgt
investigate whether first born babies are lighter or heavier than others. 
Compute Cohen’s d to quantify the difference between the groups.
'''

first_wgt = live[live.birthord ==1].totalwgt_lb
other_wgt = live[live.birthord !=1].totalwgt_lb



# the graph would seem to show that first borns are generally lighter
first_wgt.hist(bins = 12, align = 'left', color = (0.14509803921568629, 0.20392156862745098, 0.58039215686274515, 0.6), label = 'First Borns')
other_wgt.hist(bins = 12, align = 'right', color = (0.11372549019607843, 0.56862745098039214, 0.75294117647058822, 0.6), label = 'Other')
plt.legend()
plt.xlabel('Weight in Lbs')



# HOWEVER...
grp1 = first_wgt.mean()
grp2 = other_wgt.mean()

grp2-grp1 # 0.124lb on average

var1 = first_wgt.var()
var2 = other_wgt.var()

var_pool = (len(first_wgt)*var1 + len(other_wgt)*var2)/(len(first_wgt)+len(other_wgt)) # just 1.98 lb
d_stat = (grp1 - grp2)/np.sqrt(var_pool) # -0.0887
# the diff in means is about 0.0887 pooled standard deviations... seems like nothing?
