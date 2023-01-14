
def Tower(n,source ,destination, auxiliary):
    if n==1:
        print("Move disk 1 from source ",source,"to destination",destination)
        return
    Tower(n-1,source, auxiliary, destination)
    print("Move disk",n,"from source ",source,"to destinat",destination)
    Tower(n-1, auxiliary, destination, source)

n=4
Tower(n,'A','B','C')



''''
def Tower(n,source , auxiliary, destination):
    if n==1:
        print("Move disk 1 from rod {} to rod {}".format(source,destination))
        return
    Tower(n-1,source, destination, auxiliary)
    print("Move disk {} from rod {} to rod {}".format(n,source,destination))
    Tower(n-1, auxiliary, source, destination)

n=3     # disk
Tower(n,'A','B','C')

'''
