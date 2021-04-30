import numpy
import matplotlib.pyplot as plt

x = [1940,
1941,
1942,
1943,
1944,
1945,
1946,
1947,
1948,
1949,
1950,
1951,
1952,
1953,
1954,
1955,
1956,
1957,
1958,
1959,
1960,
1961,
1962,
1963,
1964,
1965,
1966,
1967,
1968,
1969,
1970,
1971,
1972,
1973,
1974,
1975,
1976,
1977,
1978,
1979,
1980,
1981,
1982,
1983,
1984,
1985,
1986,
1987,
1988,
1989,
1990,
1991,
1992,
1993,
1994,
1995,
1996,
1997,
1998,
1999,
2000,
2001,
2002,
2003,
2004,
2005,
2006,
2007,
2008,
2009,
2010,
2011,
2012,
2013,
2014,
2015,
2016,
2017,
2018,
2019,
2020
]
y = [0,0,0,0,0,0,0,19.9,19.9,19.9,19.9,19.9,19.9,19.9,19.9,19.9,19.9,19.9,31.3,31.3,31.3,31.3,31.3,31.3,31.3,31.3,31.3,31.3,31.3,31.3,36.6,36.6,36.6,36.6,36.6,36.6,36.6,36.6,36.6,36.6,36.6,36.6,36.6,36.6,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37]
y2 = []
y3 = []
for i in y:
	if i!=0:
		y2.append(i+15)
		y3.append(i+28)
	else:
		y2.append(0)
		y3.append(0)
print (len(x),len(y2))

x = numpy.array(x)
y = numpy.array(y)

'''
plt.step(x, y, label='Time Complexity')
plt.step(x, y2, label='Lower Bounds')
plt.yticks([0,1,2,3,4,5,6,7], ('$O(1)$', '$O(logn)$', '$O(n)$', '$O(nlogn)$', '$O(n^2)$','$O(n^3)$', '>$O(n^3)$', '$O(e^x)$'))
ax = plt.plot()
ax.fill_between(x, y)
#plt.plot(x, y + 2, 'o--', color='grey', alpha=0.3)

#plt.step(x, y + 1, where='mid', label='mid')
#plt.plot(x, y + 1, 'o--', color='grey', alpha=0.3)

#plt.step(x, y, where='post', label='post')
#plt.plot(x, y, 'o--', color='grey', alpha=0.3)

plt.grid(axis='x', color='0.95')
plt.legend(title='Parameter where:')
plt.title('Sample Family Bounds Chart')
plt.show()
'''

xan = [1947,1958,1970,1983]
yan = [19.9+28,31.3+28,36.6+28,37+28]
zan = ['Algo1','Algo2','Algo3','Algo4']



fig, (ax1) = plt.subplots(1, 1, sharex=True, figsize=(6, 6))
ax1.step(x, y3, label='1 billion',linewidth=3)
ax1.step(x, y2, label='1 million',linewidth=3)
ax1.step(x, y, label='1 thousand',linewidth=3)
ax1.grid(axis='y', color='0.65')

ax1.set_xlabel('Year')
ax1.set_ylabel('Performance Improvement')

for x,y,z in zip(xan,yan,zan):

    label = z

    ax1.annotate(label, # this is the text
                 (x,y), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center


ax1.legend()
plt.title('Sample Step Chart for Improvements')

fig.tight_layout()
plt.show()