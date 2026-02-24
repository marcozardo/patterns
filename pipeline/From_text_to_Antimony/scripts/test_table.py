import pandas as pd
#from datetime import datetime

## Snakemake ##

in_csv1 = snakemake.input[0]
in_csv2 = snakemake.input[1]
out_csv= snakemake.output[0]

#current_dateTime = datetime.now()

df3 = pd.read_csv(in_csv2)

data = {
    "N° paper": 10,
    "Day:time-slot": True,
    "First simulation (ratio)": True,
    "Second simulation (ratio)":True,
    "Third simulation (ratio)":True,
    "AAFE evaluation (N°correct/N°paper)":True,
    "Total Hamming ratio":True,
    "N° Species B&F(query/original)":round(df3.iloc[0, 0], 2),
    "N° Reactions(query/original)":round(df3.iloc[0, 1], 2),
    "N° Compartments(query/original)":round(df3.iloc[0, 2], 2),
    "N° Glob.Parameters(query/original)":round(df3.iloc[0, 3], 2)
}

#"N° Floating sp.(query/original)":round(df3.iloc[0, 1], 2),
#"Date":current_dateTime,

print("which LLM model you are using:")
df = pd.DataFrame(data, index=[input()])


df2 = pd.read_csv(in_csv1)

first_column = pd.Series(df2["first Simulation"])

first_column = pd.Series.to_list(first_column)
second_column = pd.Series(df2["second Simulation"])
second_column = pd.Series.to_list(second_column)

third_column = pd.Series(df2["third Simulation"])
third_column = pd.Series.to_list(third_column)

fourth_column = pd.Series(df2["AAFE evaluation"])
fourth_column = pd.Series.to_list(fourth_column)

fifth_column = pd.Series(df2["HAMMING evaluation"])

total = len(first_column)
first_success = first_column.count(0)
second_total = len(second_column) 
third_total = len(third_column)
second_success= second_column.count(0)
third_success = third_column.count(0)
fourth_success = fourth_column.count(0)

ratio_1 = (first_success/total) 
ratio_2 = (second_success/total)
ratio_3 =  (third_success/total)
ratio_4 = (fourth_success/total)
ratio_5 = fifth_column.mean()

print("day and time slot in which you have been used this LLM model:")
df["Day:time-slot"] = input()
print("number of tested papers:")
df["N° paper"] = input()
df["First simulation (ratio)"] = ratio_1
df["Second simulation (ratio)"] = ratio_2
df["Third simulation (ratio)"] = ratio_3
df["AAFE evaluation (N°correct/N°paper)"] = ratio_4
df["Total Hamming ratio"] = ratio_5

df.to_csv(out_csv)
