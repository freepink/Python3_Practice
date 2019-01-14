import csv

# with open('lostAndFound.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter = '-')
#     with open('new_lostAndFound.csv', 'w') as new_file:
#         csv_writer = csv.writer( new_file, delimiter ='/')


#         for line in csv_reader:
#             csv_writer.writerow(line)
#             #print(line)

with open('lostAndFound.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter =',')

    for line in csv_reader:
            print(line['Date'])

# class IO:
#     def __init__(self,year,month):
#         self.year = year
#         self.month = month

#     def get_last_month(self):
#             if self.month == 1:
#                 year = self.year-1
#                 month = 12
#             else:
#                 year = self.year
#                 month = self.month-1
#             return (year,month)

#     def save(self):
#         i = input("input: ")
#         if i == '1':
#             year,month = IO.get_last_month(self)
#             print(year,month)
#         else:
#             print(year,month)
# ad1 = IO(2018,12)
# ad1.save()
