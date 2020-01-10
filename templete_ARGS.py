import sys

args = sys.argv

##argsは文字列として取得
sum=0
for i in range(1,len(args)):
    print("args[{}]:".format(i)+args[i])
    sum+=int(args[i])

print("sum:",sum)
