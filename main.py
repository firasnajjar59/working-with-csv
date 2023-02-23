import pandas
day_list=[]
dic={"Fur color":[],"Count":[]}
tempertures=[]
data=pandas.read_csv("Data.csv")
for color in data["Primary Fur Color"].to_list():
    if not color in dic["Fur color"] and not str(color)=="nan":
        dic["Fur color"].append(color)
        count=0
        for num in data["Primary Fur Color"].to_list():
            if color==num:
                count+=1
        dic["Count"].append(count)
data_from_dic=pandas.DataFrame(dic)
data_from_dic.to_csv("squirrel_count.csv")
        