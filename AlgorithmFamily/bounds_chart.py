import numpy
import matplotlib.pyplot as plt
import pandas

def handle_nan(inp):
	try:
		if math.isnan(inp):
			return ''
		else:
			return inp
	except:
		return inp

x = []
y2 = []
for i in range(1940,2021):
	x.append(i)
	y2.append(1)

dataframe = pandas.read_csv('../Data/Algorithms.csv')
dataframe = dataframe.loc[(dataframe['Quantum?'] == 0) & (dataframe['Parallel?'] == 0) & (dataframe['Exact?'] == 1) & (dataframe['Randomized?'] == 0) & (dataframe['Approximate?'] == 0) & (dataframe['GPU-based?'] == 0) & (dataframe['Time Complexity Improvement?'] == 1)]
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
	years_overall = improvement_algorithms['Year'].tolist()
	
	#Check
	if len(years_overall)==0:
		years_overall = [1940]

	years_of_transition = [min(years_overall)]
	transition_classes = []
	transition_classes.append(int(algorithms['Starting Complexity'].iloc[0]))
	all_transitions = improvement_algorithms[['Year','Transition Class']]

	for index, transition in all_transitions.iterrows():
		#print (transition)
		if transition['Transition Class']!=0 and '->' in transition['Transition Class']:
			#prev_class = transition[0]
			next_class = transition['Transition Class'][3]
			transition_classes.append(int(next_class))
			years_of_transition.append(transition['Year'])

	print (transition_classes)
	for i in range(len(transition_classes)):
		if transition_classes[i] == 1:
			transition_classes[i] = 7
		if transition_classes[i] == 2:
			transition_classes[i] = 6
		if transition_classes[i] == 3:
			transition_classes[i] = 5
		if transition_classes[i] == 4:
			transition_classes[i] = 4
		if transition_classes[i] == 5:
			transition_classes[i] = 3
		if transition_classes[i] == 6:
			transition_classes[i] = 2
		if transition_classes[i] == 7:
			transition_classes[i] = 1
	
	transition_classes.sort()
	transition_classes = transition_classes[::-1]
	years_of_transition.sort()

	transition_classes.append(transition_classes[-1])
	years_of_transition.append(2020)

	print (years_of_transition)
	print (transition_classes)

	lower_bounds = [0]*len(years_of_transition)
	plt.ylim((0,7))
	fig, (ax1) = plt.subplots(1, 1, sharex=True, figsize=(6, 6))
	fig.set_size_inches(15.5, 8.5, forward=True)
	plt.yticks([0,1,2,3,4,5,6,7], ('$O(1)$', '$O(logn)$', '$O(n)$', '$O(nlogn)$', '$O(n^2)$','$O(n^3)$', '$O(n^{>3})$', '$O(n!)/O(c^n)$'))
	ax1.step(years_of_transition, transition_classes, label='Time Complexity',linewidth=8, color='#128EBC',where='mid')
	
	def closest_to(num,series):
		difference=1000
		closest=series[0]
		for i in series:
			if abs(i-num)<difference:
				closest=i
				difference=abs(i-num)
		return series.index(closest)

	ax1.step(years_of_transition, lower_bounds, label='Lower Bounds',linewidth=8, color='#75D4F7',where='mid')
	ax1.scatter([1990],[7],color='white')
	ax1.fill_between(years_of_transition, transition_classes, lower_bounds, color='yellow',step='mid')
	median_year=(max(years_of_transition)-min(years_of_transition))/2+min(years_of_transition)
	index=closest_to(median_year+1,years_of_transition)
	ax1.text(median_year, transition_classes[index]+0.2, 'Upper Bound', fontsize=15, color='#128EBC')
	ax1.text(median_year-(max(years_of_transition)-min(years_of_transition))*0.2, transition_classes[index]/2, 'Optimal algorithm in this range', fontsize=25, color='gray')
	ax1.text(median_year, 0.2, 'Lower Bound', fontsize=15, color='#75D4F7')
	
	


	ax1.annotate('annotate', xy=(2, 1), xytext=(3, 4))
	plt.title(' '.join(split_familyname)+' Best- and Worst-Case Time Complexity Bounds',fontsize=16)
	plt.ylabel("Time Complexity",fontsize=12)
	plt.xticks(fontsize=12)
	fig.tight_layout()
	#plt.show()
	try:
		plt.savefig('FamilyPages/'+familyname + '/' +familyname+'BoundsChart.png')
	except:
		print ("Failed")