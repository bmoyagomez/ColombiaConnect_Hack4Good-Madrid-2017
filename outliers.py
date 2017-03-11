inputFile = ""
outFile = ""

idCode = "cod_mpio"
weekDay = "dayOfWeek"
dateCode = "date_dt"

sep = ","

outValue = 1.5

#-----
import pandas as pd

inputData = pd.read_csv(inputFile, header = 0)

def findOut(data, multi):
    q1 = data.quantile(0.25)
    q3 = data.quantile(0.75)
    iqr = q3 - q1
    return [q1 - multi * iqr, q3 + 1.5 * iqr]

#print inputData.groupby(idCode).describe()
#print inputData.columns

a = inputData.groupby(idCode).agg("mean")
print a

#print inputData.groupby(idCode).agg(lambda x: findOut(x, outValue))

#outThreshold = inputData.groupby([idCode, weekDay]).agg(lambda x: findOut(x, outValue))

#print outThreshold

print list(a.index)

print a.loc[2,'dwells']

                
        
        
            
            
        
