
#inputは文字列として取得
input=input()
#splitする必要がある
input=input.split(" ")

sum=0
for i in range(len(input)):
    print("args[{}]:".format(i)+input[i])
    sum+=int(input[i])

print("sum:",sum)