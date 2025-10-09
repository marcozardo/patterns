import pandas as pd

in_csv1 = snakemake.input[0]
in_csv2 = snakemake.input[1]
out_csv= snakemake.output[0]

df3 = pd.read_csv(in_csv2)

data = {
    "N° paper": 10,
    "attempt": 1,
    "first simulation (ratio)": True,
    "second simulation (ratio)":True,
    "third simulation (ratio)":True,
    "N° Boundary sp.(query/original)":round(df3.iloc[0, 0], 2),
    "N° Floating sp.(query/original)":round(df3.iloc[0, 1], 2),
    "N° Reactions(query/original)":round(df3.iloc[0, 2], 2),
    "N° Compartments(query/original)":round(df3.iloc[0, 3], 2),
    "N° Glob.Parameters(query/original)":"TBD",
}

df = pd.DataFrame(data, index=[input()])


df2 = pd.read_csv(in_csv1)

first_column = pd.Series(df2["first Simulation"])

first_column = pd.Series.to_list(first_column)
second_column = pd.Series(df2["second Simulation"])
second_column = pd.Series.to_list(second_column)

third_column = pd.Series(df2["third Simulation"])
third_column = pd.Series.to_list(third_column)

total = len(first_column)
first_success = first_column.count(0)
second_total = len(second_column) 
third_total = len(third_column)
second_success= second_column.count(0)
third_success = third_column.count(0)

ratio_1 = (first_success/total) 
ratio_2 = (second_success/total)
ratio_3=  (third_success/total)


df["first simulation (ratio)"] = ratio_1
df["second simulation (ratio)"] = ratio_2
df["third simulation (ratio)"] = ratio_3

print(df)



df.to_csv(out_csv)
