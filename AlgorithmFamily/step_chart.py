import numpy
import matplotlib.pyplot as plt
import pandas
import copy
import math

x = []
for i in range(1940,2021):
	x.append(i)

dataframe = pandas.read_csv('../Data/Algorithms.csv')
dataframe = dataframe.loc[(dataframe['Quantum?'] == 0) & (dataframe['Parallel?'] == 0) & (dataframe['Exact?'] == 1) & (dataframe['Randomized?'] == 0) & (dataframe['Approximate?'] == 0) & (dataframe['GPU-based?'] == 0) & (dataframe['Time Complexity Improvement?'] == 1)]
algorithm_families = dataframe['Family Name'].dropna().unique()
algorithm_families = dataframe['Family Name'].dropna().unique()
for family in algorithm_families:
	split_familyname = family.split(' ')
	split_familyname = split_familyname[1:]
	familyname = "_".join(split_familyname)
	print (familyname)
	algorithms = dataframe.loc[dataframe['Family Name'] == family]
	algorithms.loc[algorithms.Year < 1940, 'Year'] = 1940
	algorithms[['Year']] = algorithms[['Year']].astype(int)
	improvement_algorithms = algorithms.loc[algorithms['Time Complexity Improvement?']==1]
	improvement_algorithms = algorithms[['Algorithm Name','Year','n = 1000 scale','n = 10^6 scale','n = 10^9 scale']].dropna()
	x = improvement_algorithms['Year'].tolist()
	names = improvement_algorithms['Algorithm Name'].tolist()
	y = improvement_algorithms['n = 1000 scale'].tolist()
	y2 = improvement_algorithms['n = 10^6 scale'].tolist()
	y3 = improvement_algorithms['n = 10^9 scale'].tolist()

	for i in range(len(y)):
		y[i] = math.log(y[i],10)
		y2[i] = math.log(y2[i],10)
		y3[i] = math.log(y3[i],10)

	x.sort()
	y.sort()
	y2.sort()
	y3.sort()

	print (x)
	print (y)
	print (y2)
	print (y3)
	xan = copy.copy(x)
	yan = copy.copy(y3)
	if len(y)>0:
		y.append(y[-1])
		y2.append(y2[-1])
		y3.append(y3[-1])
		x.append(2020)

	fig, (ax1) = plt.subplots(1, 1, sharex=True, figsize=(6, 6))
	fig.set_size_inches(15.5, 8.5, forward=True)

	ax1.step(x, y3, label='1 billion',linewidth=3,color="#127499")
	ax1.step(x, y2, label='1 million',linewidth=3,color="#3B9FC3")
	ax1.step(x, y, label='1 thousand',linewidth=3,color="#75D4F7")
	ax1.grid(axis='y', color='0.65')


	
	zan = copy.copy(names)

	print (xan,yan,zan)
	print (len(xan),len(yan),len(zan))

	#ax1.set_xlabel('Year')
	#ax1.set_ylabel('Performance Improvement')

	for i in range(len(xan)):
		if i==0:
			ax1.annotate(zan[i], # this is the text
		                 (xan[i],yan[i]), # this is the point to label
		                 textcoords="offset points", # how to position the text
		                 xytext=(0,-10), # distance from text to points (x,y)
		                 ha='left',fontsize=12) # horizontal alignment can be left, right or center

		elif i==len(xan)-1:
			ax1.annotate(zan[i], # this is the text
		                 (xan[i],yan[i]), # this is the point to label
		                 textcoords="offset points", # how to position the text
		                 xytext=(-10,5), # distance from text to points (x,y)
		                 ha='left',fontsize=12) # horizontal alignment can be left, right or center

		else:
			if yan[i] - yan[i-1] < 1:
				ax1.annotate(zan[i], # this is the text
			                 (xan[i],yan[i]), # this is the point to label
			                 textcoords="offset points", # how to position the text
			                 xytext=(-10,10), # distance from text to points (x,y)
			                 ha='right',fontsize=12) # horizontal alignment can be left, right or center
			else:
				ax1.annotate(zan[i], # this is the text
			                 (xan[i],yan[i]), # this is the point to label
			                 textcoords="offset points", # how to position the text
			                 xytext=(-10,5), # distance from text to points (x,y)
			                 ha='right',fontsize=12) # horizontal alignment can be left, right or center

	ax1.legend()
	plt_y = []
	j = 0
	for i in range(9):
		plt_y.append("$10^{" + str(j)+"}$")
		j = j+5
	plt.yticks([0,2,4,6,8,10,12], plt_y, fontsize=12)
	plt.xticks(fontsize=12)
	plt.ylabel("Improvement Scale",fontsize=12)
	plt.title(familyname+': Step Chart for Improvements',fontsize=16)

	fig.tight_layout()
	#plt.show()
	try:
		plt.savefig('FamilyPages/'+familyname + '/' +familyname+'StepChart.png')
	except:
		print ("Failed")
