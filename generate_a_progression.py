def generation_function(n):
    '''return a list that is going to be written in the txt file'''
    rlist = [0]
    for i in range(n):
        rlist.append(1*test[-1] + i**2)
    return(rlist)

with open('GeneratedProgression.txt', 'w') as f:
    for item in generation_function(1000):
        f.write(item)
