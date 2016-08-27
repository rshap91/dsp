[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

>>  Use the NSFG respondent variable to construct the actual distribu- tion for the number of children under 18 in the household. Now compute the biased distribution we would see if we surveyed the chil- dren and asked them how many children under 18 (including themselves) are in their household. Plot the actual and biased distributions, and compute their means.


```
import chap01soln

resp = chap01soln.ReadFemResp()

kids = resp.numkdhh
kids_pmf = thinkstats2.Pmf(kids)
kids_bias = kids_pmf.Copy()
for x in range(6):
	kids_bias.Mult(x, x)
thinkplot.PrePlot(2)
thinkplot.Hists([kids_bias, kids_pmf]) # don't know how to do labels with thinkplot ... shmeh


kids_pmf.Mean() # 1.0242051550438309
kids_bias.Mean() # 2.4618605259714772
diff = kids_pmf.Mean() - kids_bias.Mean() # -1.44
```
