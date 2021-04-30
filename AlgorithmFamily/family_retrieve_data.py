import pandas
import os
import math

def handle_nan(inp):
	try:
		if math.isnan(inp):
			return ''
		else:
			return inp
	except:
		return inp

def handle_nan_int(inp):
	try:
		if math.isnan(inp):
			return 0
		else:
			return inp
	except:
		return inp

dataframe = pandas.read_csv('../Data/Algorithms.csv')
algorithm_families = dataframe['Family Name'].dropna().unique()
for family in algorithm_families:
	split_familyname = family.split(' ')
	split_familyname = split_familyname[1:]
	familyname = "_".join(split_familyname)
	print (familyname)
	algorithms = dataframe.loc[dataframe['Family Name'] == family]

	
	#algorithms[['Family for Algorithm']] = algorithms[['Family for Algorithm']].astype(int)
	#Create Directories
	
	#os.makedirs("FamilyPages/"+familyname)
	with open("FamilyPages/"+familyname+"/parsed_text.txt", 'w') as fp: 
		pass
	

	parsed_text = ''
	algorithms = dataframe.loc[dataframe['Family Name'] == family]
	algorithms[['Year']] = algorithms[['Year']].astype(int)
	problem_description = handle_nan(algorithms['Problem Statement'].iloc[0])

	#Problem Description
	parsed_text = parsed_text + '== Problem Description=='
	parsed_text = parsed_text + '\n'
	parsed_text = parsed_text + problem_description

	parsed_text = parsed_text + '\n\n'

	#Bounds Chart
	parsed_text = parsed_text + '== Bounds Chart =='
	parsed_text = parsed_text + '\n'
	parsed_text = parsed_text + '[[File:'+ familyname +'BoundsChart.png|350px]]'

	parsed_text = parsed_text + '\n\n'

	#Step Chart
	parsed_text = parsed_text + '== Step Chart =='
	parsed_text = parsed_text + '\n'
	parsed_text = parsed_text + '[[File:'+ familyname +'StepChart.png|350px]]'

	parsed_text = parsed_text + '\n\n'


	#Table
	parsed_text = parsed_text + '== Improvement Table =='
	parsed_text = parsed_text + '\n'
	parsed_text = parsed_text + '{| class="wikitable" style="text-align:center;" width="100%" \n !width="20%" | Complexity Classes !! width="40%" | Algorithm Paper Links !! width="40%" | Lower Bounds Paper Links\n |-\n'
	check = 0
	count = 0
	temp_text = ""
	for index, row in algorithms.iterrows():
		if int(handle_nan_int(row['Family for Algorithm'])) == 1:
			check = 1
			count = count + 1
			temp_text += '| <nowiki>' + row['Algorithm Name'] +' ('+ str(row['Year']) +')</nowiki>\n|\n|-\n'
	if count==0:
		parsed_text = parsed_text + '| rowspan="'+str(count+1)+'" | Exp/Factorial\n'
	else:
		parsed_text = parsed_text + '| rowspan="'+str(count)+'" | Exp/Factorial\n'
	parsed_text = parsed_text + temp_text
	if check == 0:
		parsed_text = parsed_text + "|\n|\n|-"

	parsed_text = parsed_text + '\n'
	check = 0
	count = 0
	temp_text = ""
	for index, row in algorithms.iterrows():
		if int(handle_nan_int(row['Family for Algorithm'])) == 2:
			check = 1
			count = count + 1
			temp_text += '| <nowiki>' + row['Algorithm Name'] +' ('+ str(row['Year']) +')</nowiki>\n|\n|-\n'
	if count==0:
		parsed_text = parsed_text + '| rowspan="'+str(count+1)+'" | Polynomial > 3\n'
	else:
		parsed_text = parsed_text + '| rowspan="'+str(count)+'" | Polynomial > 3\n'
	parsed_text = parsed_text + temp_text
	if check == 0:
		parsed_text = parsed_text + "|\n|\n|-"

	parsed_text = parsed_text + '\n'
	check = 0
	count = 0
	temp_text = ""
	for index, row in algorithms.iterrows():
		if int(handle_nan_int(row['Family for Algorithm'])) == 3:
			check = 1
			count = count + 1
			temp_text += '| <nowiki>' + row['Algorithm Name'] +' ('+ str(row['Year']) +')</nowiki>\n|\n|-\n'
	if count==0:
		parsed_text = parsed_text + '| rowspan="'+str(count+1)+'" | Cubic\n'
	else:
		parsed_text = parsed_text + '| rowspan="'+str(count)+'" | Cubic\n'
	parsed_text = parsed_text + temp_text
	if check == 0:
		parsed_text = parsed_text + "|\n|\n|-"

	parsed_text = parsed_text + '\n'
	check = 0
	count = 0
	temp_text = ""
	for index, row in algorithms.iterrows():
		if int(handle_nan_int(row['Family for Algorithm'])) == 4:
			check = 1
			count = count + 1
			temp_text += '| <nowiki>' + row['Algorithm Name'] +' ('+ str(row['Year']) +')</nowiki>\n|\n|-\n'
	if count==0:
		parsed_text = parsed_text + '| rowspan="'+str(count+1)+'" | Quadratic\n'
	else:
		parsed_text = parsed_text + '| rowspan="'+str(count)+'" | Quadratic\n'
	parsed_text = parsed_text + temp_text
	if check == 0:
		parsed_text = parsed_text + "|\n|\n|-"

	parsed_text = parsed_text + '\n'
	check = 0
	count = 0
	temp_text = ""
	for index, row in algorithms.iterrows():
		if int(handle_nan_int(row['Family for Algorithm'])) == 5:
			check = 1
			count = count + 1
			temp_text += '| <nowiki>' + row['Algorithm Name'] +' ('+ str(row['Year']) +')</nowiki>\n|\n|-\n'
	if count==0:
		parsed_text = parsed_text + '| rowspan="'+str(count+1)+'" | nlogn\n'
	else:
		parsed_text = parsed_text + '| rowspan="'+str(count)+'" | nlogn\n'
	parsed_text = parsed_text + temp_text
	if check == 0:
		parsed_text = parsed_text + "|\n|\n|-"

	parsed_text = parsed_text + '\n'
	check = 0
	count = 0
	temp_text = ""
	for index, row in algorithms.iterrows():
		if int(handle_nan_int(row['Family for Algorithm'])) == 6:
			check = 1
			count = count + 1
			temp_text += '| <nowiki>' + row['Algorithm Name'] +' ('+ str(row['Year']) +')</nowiki>\n|\n|-\n'
	if count==0:
		parsed_text = parsed_text + '| rowspan="'+str(count+1)+'" | Linear\n'
	else:
		parsed_text = parsed_text + '| rowspan="'+str(count)+'" | Linear\n'
	parsed_text = parsed_text + temp_text
	if check == 0:
		parsed_text = parsed_text + "|\n|\n|-"

	parsed_text = parsed_text + '\n'
	check = 0
	count = 0
	temp_text = ""
	for index, row in algorithms.iterrows():
		if int(handle_nan_int(row['Family for Algorithm'])) == 7:
			check = 1
			count = count + 1
			temp_text += '| <nowiki>' + row['Algorithm Name'] +' ('+ str(row['Year']) +')</nowiki>\n|\n|-\n'
	if count==0:
		parsed_text = parsed_text + '| rowspan="'+str(count+1)+'" | logn\n'
	else:
		parsed_text = parsed_text + '| rowspan="'+str(count)+'" | logn\n'
	parsed_text = parsed_text + temp_text
	if check == 0:
		parsed_text = parsed_text + "|\n|\n|-"

	parsed_text = parsed_text + '|}'

	with open("FamilyPages/"+familyname+"/parsed_text.txt", 'w') as fp: 
		fp.write(parsed_text)
		fp.close()

	print (parsed_text)