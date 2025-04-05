from dataset import read_files
path = "Capaccreceipts.csv"
df = read_files(path)
#print(df.head())
import train as t
obj = t.Train()
print(obj.split)
obj = t.Train(0.30)
print(obj.split)

obj = t.Hyperparameter()
obj.train_meter()