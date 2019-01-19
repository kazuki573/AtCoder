n, m = [int(x) for x in input().split()]
pi_yi_list = [[] for i in range(n)]
input_list = []
iddict = {}
for i in range(m):
    pi, yi = [int(x) for x in input().split()]
    pi_yi_list[pi - 1].append(yi)
    input_list.append(str(pi) + str(yi))
    iddict[str(pi) + str(yi)] = -1
pi_yi_list_sorted = [sorted(x) for x in pi_yi_list]
for pi, pilist in enumerate(pi_yi_list_sorted):
    for j, yi in enumerate(pilist):
        iddict[str(pi + 1) + str(yi)] = '{:0=6}'.format(pi+1) + '{:0=6}'.format(j+1)

for input in input_list:
    print(iddict[input])
