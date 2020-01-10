
def insert(target_string, insert_point, insert_string):
    return target_string[:insert_point] + insert_string + target_string[insert_point:]

N=7

def permutate(n):
    ans=[]
    if n==1:
        ans=["1"]
    else:
        temp=permutate(n-1)

        for t in temp:
            for i in range(len(t)+1):
                tm=insert(t,i,"{}".format(n))
                ans.append(tm)

    return ans

print(permutate(N))
