#Generate two sets – first for all singers and second for all dancers of the class using set comprehension. Perform set operations to generate the following sets 
#of all artists of the class
#allrounders of the class
#dancers but not singers
#singers but not dancers
#dancers but not singers cum singers but not dancers
singers={"Kavya","Harshit","Rishika"}
dancers={"Rishika","Ananya","Arnav"}
artists=singers|dancers
allrounders=singers&dancers
dancersnotsingers=dancers-singers
singersNotDancers=singers-dancers
dancersCumSingers=dancersnotsingers|singersNotDancers
print(artists)
print(allrounders)
print(dancersnotsingers)
print(singersNotDancers)
print(dancersCumSingers)
