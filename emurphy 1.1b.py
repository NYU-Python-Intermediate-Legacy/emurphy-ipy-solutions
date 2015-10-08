import sys

def max_price(lst):
   return max(lst)

def min_price(lst):
   return min(lst)

def avg_price(lst,days):
   return sum(lst)/days

def sort_lst(lst):
   lst.sort()
   return lst

def median(lst):
   sort_lst = sorted(lst)	
   
   mid = len(sort_lst)/2
   
   if len(sort_lst)%2 == 0:
      return (sort_lst[mid-1] + sort_lst[mid]) / 2
   else:
      return sort_lst[mid]

def center_avg(lst):
   
   uni_set=set()
   
   for elem in lst:
      uni_set.add(elem)       
   
   uni_set.remove(max_price(lst))   
   uni_set.remove(min_price(lst))
   return median(uni_set)
   

ticker = str(sys.argv[1])

try:
   fh = open('%s.csv' % ticker)
except IOError:
   print 'Error: Stock ticker %s could not be found' % ticker
   print 'Usage: python [Ticker] [number of days to retrieve]'
   print 'Script exiting...'
   exit()

fh.readline()

days = int(sys.argv[2])

if days > 251:
   print 'Error: You have exceeded the amount of days in the file.'
   print 'Usage: You must choose a value between 1 and 251.'
   print 'Script exiting...'
   exit()

stock_prices=[]
i = 1
   
while i <= days:
  file_line = fh.readline()
  linez = file_line.split(",")
  stock_prices.append(float(linez[4]))
  i = i + 1

fh.close

print 'The max price of %s is: %s' % (ticker,max_price(stock_prices))
print 'The min price of %s is: %s' % (ticker,min_price(stock_prices))
print 'The average price for %s over the past %s days is %s' % (ticker,days, avg_price(stock_prices,days))
print sort_lst(stock_prices)
print 'The median of the stock prices is %s' % median(stock_prices)
print 'The center average of the stock prices is %s with the min: %s and the max %s removed.' % (center_avg(stock_prices), min(stock_prices), max(stock_prices))
