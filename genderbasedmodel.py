import csv as csv
import numpy as np

csv_file_object = csv.reader(open('C:/Priya UT Dallas/Titanic/excel/train.csv','rb'))
header = csv_file_object.next()
data= []
for row in csv_file_object:
    data.append(row)
data = np.array(data)


women_only = data[0::,4] == "female"
men_only =  data[0::,4] != "female"

women_aboard = np.size(data[women_only,1].astype(np.float))
women_survived = np.sum(data[women_only,1].astype(np.float))

men_aboard = np.size(data[men_only,1].astype(np.float))
men_survived = np.sum(data[men_only,1].astype(np.float))
ratio_women_survived = women_survived/women_aboard
ratio_men_survived = men_survived/men_aboard

print 'Proportion of women who survived is %s' % ratio_women_survived
print 'Proportion of men who survived is %s' % ratio_men_survived


test_file = open('C:/Priya UT Dallas/Titanic/excel/test.csv','rb+')
test_reader = csv.reader(test_file)
header = test_reader.next()

prediction_file = open ('C:/Priya UT Dallas/Titanic/excel/genderbasedmodel.csv','wb')
pred_obj = csv.writer(prediction_file)

pred_obj.writerow(["PassengerId","Survived"])
for row in test_reader:
    if row[3] == "female":
        pred_obj.writerow([row[0],"1"])
    else:
        pred_obj.writerow([row[0],"0"])

test_file.close()
prediction_file.close()









