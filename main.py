import pandas as pd
df = pd.read_csv("car.data", header=None)
buying, maintenance, doors, people, boot_size, safety = [],[],[],[],[],[]

pd.options.display.max_rows = 9999
# print(df)
for i in range(0,len(df)):
    # print(str(i))
    counter = 0
    for item in df.loc[i]:
        if counter==0:
            buying+=[item]
            counter+=1
        elif counter==1:
            maintenance+=[item]
            counter+=1
        elif counter==2:
            doors+=[item]
            counter+=1
        elif counter==3:
            people+=[item]
            counter+=1
        elif counter==4:
            boot_size+=[item]
            counter+=1
        elif counter==5:
            safety+=[item]
print(str(buying))