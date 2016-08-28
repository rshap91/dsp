[Think Stats Chapter 6 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2007.html#toc60) (household income)

>> Compute the median, mean, skewness and Pearson’s skewness of the re- sulting sample.  What fraction of households reports a taxable income below the mean? How do the results depend on the assumed upper bound?

I am so confused... this doesn't make any sense

```
df = hinc.ReadData()
samp = hinc2.InterpolateSample(df)
len(samp) # 122,458
samp.mean() # 4.658
np.median(samp) # 4.709
Skewness(samp) # -0.641
Pearson_Skew(samp) # -0.338

plt.hist(samp) # looks pretty un-skewed to me
samp[samp<samp.mean()]
# percent of housolds in samp that are below the mean income
len(samp[samp<samp.mean()])/float(len(samp)) # 45%
``` 
<img src = "https://github.com/rshap91/dsp/blob/master/statistics/ch6_232_samp_hist.png" width = 500px>

```
means = []
medians = []
skews = []
pearson_skews = []
for u in range(3,7):
	samp = hinc2.InterpolateSample(df, log_upper = u)
	print len(samp)
	means.append(samp.mean())
	medians.append(np.median(samp))
	skews.append(Skewness(samp))
	pearson_skews.append(Pearson_Skew(samp))

plt.figure(figsize = (12,8))

plt.subplot(2,2,1)
plt.plot(range(3,7), means)
plt.title('Means')

plt.subplot(2,2,2)
plt.plot(range(3,7), medians)
plt.title('Medians')

plt.subplot(2,2,3)
plt.plot(range(3,7), skews)
plt.title('Skew')

plt.subplot(2,2,4)
plt.plot(range(3,7), pearson_skews)
plt.title('Pearson Skews')
```
means rise exactly linearly as log_upper increases
medians increase from 3-5 but then plateau
skews goes toward zero as log_upper goes to 6
pearson_skews goes toward zero as log_upper goes to 6

<img src = 'https://github.com/rshap91/dsp/blob/master/statistics/ch6_269_means_medians_skews_of_samp.png' width = 500px>

Might be interesting to look at the histograms for each samp varying log_upper

```
plt.figure(figsize = (12,8))
for u in range(3,7):
	samp = hinc2.InterpolateSample(df, log_upper = u)
	plt.subplot(2,2,u-2)
	plt.hist(samp)
	plt.title('Log_Upper = %s' %u, y = 1.07)
	tx = plt.gca().axis()[1]*0.66
	ty = plt.gca().axis()[3]*1.03
	plt.text(tx,ty, 'Skew = %s' %np.round(Skewness(samp),3), style = 'italic', size = 11)

plt.subplots_adjust(hspace = 0.34, wspace = 0.44)
```

<img src = 'https://github.com/rshap91/dsp/blob/master/statistics/ch6_289_multi_samp_hists.png' width = 600px>

I feel like i must be doing this wrong because apparently the skew decreases (goes to 0) once you get to log_upper = 6
