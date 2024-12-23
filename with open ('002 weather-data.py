# with open ('002 weather-data.csv') as data_file:
#     data=data_file.readlines()# readlines takes item into list instead of read
#     print(data)#******the output is not clean*********
    
    
# import csv #it makes all cleaning that we need it 
# with open ('002 weather-data.csv') as data_file:
#     data=csv.reader(data_file)
#     temp=[]
#     for row in data:
#         print(row[1])#kolan csv mikoni bayad az row va column estfde koni bad miad micharkhe tu item haei k hast 
        
        
# import csv 
# with open ('002 weather-data.csv') as data_file:
#     data=csv.reader(data_file)
#     temp=[]
#     for row in data:
#         if row[1]!='temp':#if the row is not the header
#             temp.append(int(row[1]))#add the temperature to the list
#     print(temp) #print moheme k koja mizarish  age zire append bud tike tike hey hame ro nshun midad


# import pandas
# data=pandas.read_csv('002 weather-data.csv')
# print(data['temp'])

# #pandas has two part series and data frame
# #series is  column  in data in sheet format
#every sheet consider of data drame like google sheet
# pandas change to everything like dict and...
#U CAN CHANGE DATAFRAME INTO EVERY TYPE OF FILE


# import pandas as pd
# data=pd.read_csv('002 weather-data.csv')
# data_dict=data.to_dict()
# print(data_dict)



# import pandas as pd
# data=pd.read_csv('002 weather-data.csv')
# data_dict=data.to_dict()
# print(data_dict['temp'])


# import pandas as pd
# data=pd.read_csv('002 weather-data.csv')

# print(data['temp'].to_list()) #
# #we cant change data in pandas to list

# import pandas as pd
# data=pd.read_csv('002 weather-data.csv')
# print(data['temp'].mean())
# Pandas می‌توانید یک ستون از DataFrame را به لیست تبدیل کنید. \
    
    
    

# import pandas as pd
# data=pd.read_csv('002 weather-data.csv')
# print(data['temp'].max())
# print(data.condition)
# # Pandas می‌توانید یک ستون از DataFrame را به لیست تبدیل کنید. 




# ???how to get data in row in dataframe???


# محاسبه بزرگ‌ترین مقدار ستون temp
# max_temp = data['temp'].max()

# فیلتر کردن ردیف‌هایی که temp برابر با بیشینه است
# max_temp_rows = data[data['temp'] == max_temp]






# import pandas as pd

# # خواندن داده‌ها
# data = pd.read_csv('002 weather-data.csv')

# # فیلتر کردن ردیف‌هایی که temp برابر با بیشینه است
# max_temp_rows = data[data.temp == data.temp.max()]

# print(max_temp_rows)
