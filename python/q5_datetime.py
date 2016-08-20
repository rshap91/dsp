# Hint:  use Google to find python function
import pandas as pd
####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'   
date_start = pd.to_datetime(date_start)
date_stop = pd.to_datetime(date_stop)
td = date_stop - date_start # 937 days

####b)  

date_start = '12312013'  
date_stop = '05282015'  
date_start = pd.to_datetime(date_start, format = '%m%d%Y')
date_stop = pd.to_datetime(date_stop, format = '%m%d%Y')
td = date_stop - date_start # 513 days

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  
date_start = pd.to_datetime(date_start, format = '%d-%b-%Y')
date_stop = pd.to_datetime(date_stop, format = '%d-%b-%Y')
td = date_stop - date_start # 7850 days
