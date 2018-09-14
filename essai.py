import pandas as pd
A = {'A':[1,2,3,4,5,6]}
df = pd.DataFrame(A)
df.reset_index(inplace=True)
print(df)

def applytest(row):
    print(row.name)
    if int(row['index'])<2:
        return(row['A'])
    else:
        return(8)

df['samere'] = df.apply(applytest,axis=1)
print(df)
