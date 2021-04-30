import pandas
import os
import math
import matplotlib.pyplot as plt

fig, (ax1) = plt.subplots(1, 1, sharex=True, figsize=(6, 6))
initial = 0
increment = 0.002
x = []
for i in range(1940,2020):
	x.append(i)
dataframe = pandas.read_csv('../Data/Algorithms.csv')
dataframe.loc[dataframe.Year < 1940, 'Year'] = 1940
algorithm_domains = dataframe['Domains'].dropna().unique()
for domain in algorithm_domains:
	print (domain)
	algorithm_families = dataframe.loc[dataframe['Domains'] == domain]
	curr_algorithm_families = algorithm_families['Family Name'].dropna().unique()
	total_average = [1]*(2020-1940)
	total_average_final = [1]*(2021-2010)
	inf_average = [0]*(2020-1940)

	req_count = 0
	for family in curr_algorithm_families:
		#print (family)
		algorithms = algorithm_families.loc[algorithm_families['Family Name'] == family]
		algorithms = algorithms.sort_values('Year')
		algorithms = algorithms.loc[(algorithms['Quantum?'] == 0) &  (dataframe['Exact Problem Statement?'] == 1) & (algorithms['Parallel?'] == 0) & (algorithms['Exact?'] == 1) & (algorithms['Randomized?'] == 0) & (algorithms['Approximate?'] == 0) & (algorithms['GPU-based?'] == 0) & (algorithms['Time Complexity Improvement?'] == 1)]
		algo_improvement_levels = [1]*(2020-1940)
		c = 0
		for index, row in algorithms.iterrows():
			if row['Year']>2010:
				print (row['Algorithm Name'],row['n = 10^6 scale'],row['Year'])

			algo_improvement_levels[int(row['Year'])-1940] = max(algo_improvement_levels[int(row['Year'])-1940],row['n = 10^6 scale'])
			if row['n = 10^6 scale'] == float('inf') and c==0:
				inf_average[int(row['Year'])-1940] = inf_average[int(row['Year'])-1940] + 1
				c = 1
		start_val = algo_improvement_levels[0]
		#print (start_val)
		for i in range(len(algo_improvement_levels)):
			if algo_improvement_levels[i]>start_val:
				start_val = algo_improvement_levels[i]
			else:
				algo_improvement_levels[i] = start_val


		final_sub = algo_improvement_levels[2010-1940:]
		#print ("check")
		#print (final_sub)
		temp_first = final_sub[0]
		
		if float('inf') not in algo_improvement_levels:
			for i in range(len(final_sub)):
				final_sub[i] = final_sub[i]/(temp_first*1.0)
				total_average_final[i] = total_average_final[i] * final_sub[i]

		#print ("check2")
		#print (final_sub)
		

		#print (algo_improvement_levels)
		if float('inf') not in algo_improvement_levels:
			req_count = req_count + 1
			for i in range(len(total_average)):
				#total_average[i] = algo_improvement_levels[i] * total_average[i]
				total_average[i] = algo_improvement_levels[i] + total_average[i]


	

	for i in range(len(total_average_final)):
		#total_average_final[i] = total_average_final[i]/(req_count*1.0)
		total_average_final[i] = math.pow(total_average_final[i],(1/(req_count*1.0)))

	print ("Total Average Final")
	print (total_average_final)


	for i in range(len(total_average)):
		#total_average[i] = math.pow(total_average[i],(1/(req_count*1.0)))
		
		total_average[i] = total_average[i]/(req_count*1.0)


	#print ("Family Count")
	#print (str(req_count))

	start_inf = inf_average[0]
	for i in range(1,len(inf_average)):
		start_inf = start_inf + inf_average[i]
		inf_average[i] = start_inf
	
	#print (total_average)
	
	subset_average = total_average[-11:]

	first_val = subset_average[0]
	for i in range(len(subset_average)):
		subset_average[i] = subset_average[i]/first_val
		#print (subset_average[i])
	#print (subset_average)


	for i in range(len(inf_average)):
		inf_average[i] = inf_average[i]/len(curr_algorithm_families)*1.0
	
	subset_inf_average = inf_average[-11:]
	first_val = subset_inf_average[0]
	for i in range(len(subset_inf_average)):
		subset_inf_average[i] = subset_inf_average[i]-first_val
		#print (subset_inf_average[i])

	if sum(inf_average)==0:
		inf_average = [initial]*(2020-1940)
		initial = initial + increment

	ax1.step(x, inf_average, label=domain,linewidth=3)

	#print (curr_algorithm_families)
	print ()
plt.legend()
plt.yticks([0,0.05,0.10,0.15,0.20], ['0%','5%','10%','15%','20%'])
plt.title('Share of algorithms with exponential speed-ups')
plt.show()