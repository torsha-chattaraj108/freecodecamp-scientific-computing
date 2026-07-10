NUMBER_OF_DISKS=5
A=list(range(NUMBER_OF_DISKS,0,-1))
B=[]
C=[]
def move(n,source,auxiliary,target):
    if n<=0:
        return
    move(n-1,source,target,auxiliary)#move n-1 disks from source to auxiliary so they are out of the way
    target.append(source.pop())#now move the nth disk that we left in source to target
    print(f"source: {source} | auxiliary: {auxiliary} | target: {target}")#print our progress
    move(n-1,auxiliary,source,target)#move the n-1 disks from auxiliary to target
move(NUMBER_OF_DISKS,A,B,C)#initiate call from source A to target C with auxiliary C
