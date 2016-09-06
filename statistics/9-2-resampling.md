[Think Stats Chapter 9 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2010.html#toc90) (resampling)

>> 
```
class DiffMeansResample(hypothesis.DiffMeansPermute):
	def RunModel(self):
		"""
		Resample instead of shuffle
		"""
		pooled_dist = pd.Series(self.pool).value_counts()/float(len(self.pool))
		vals= pooled_dist.index.tolist()
		probs = pooled_dist.values
		resamp = np.random.choice(vals, size = self.n,  p = probs), np.random.choice(vals, size = self.m, p = probs) 
		return resamp
```

EXAMPLE CODE USED IN BOOK

```
data = first.prglngth.values, other.prglngth.values
ht = hypothesis.DiffMeansPermute(data)
pv = ht.PValue() # 0.171
```

WITH RESAMPLING
```
ht2 = DiffMeansResample(data)
pv2 = ht2.PValue() #0.174
```
