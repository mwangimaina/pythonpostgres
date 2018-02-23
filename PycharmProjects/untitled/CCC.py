import pandas
#
# print(dir(pandas))
#
# names = ['Bob','Jessica','Mary','John','Mel']
# births = [968, 155, 77, 578, 973]
#
# BabyDataSet = list(zip(names,births))
#
# print(BabyDataSet)
#
# df = pandas.DataFrame(data = BabyDataSet, columns=['Names', 'Births'])


# df.to_csv('births1880.csv',index=False,header=False)
#

Location = 'movies.xls'

movies = pandas.read_excel(Location,sheet_name=0, index_col=0)

sorted_by_gross = movies.sort_values(['Gross Earnings'], ascending=False)


print(sorted_by_gross["Gross Earnings"].head(10))

print (movies["Gross Earnings"].mean())

print(movies.describe())











