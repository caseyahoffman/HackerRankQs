import fileinput # read in data
data = []
for line in fileinput.input():
    data.append(line.rstrip())

Q = int(data.pop(0)) # extract number of actions
data = [tuple(data[i].split()) for i in range(0,Q)]
s = ""
actions = [s]
# create actions saved for potential undoing
for i in range(0,Q):
    if data[i][0] == '1':
        s+=data[i][1]
        actions.append(s)
    elif data[i][0] == '2':
        to_remove = int(data[i][1])
        s = (s[0:(len(s)-to_remove)])
        actions.append(s)
    elif data[i][0] == '3':
        to_print = int(data[i][1])-1
        print(s[to_print])
    elif data[i][0] == '4':
        actions.pop()
        s = actions[-1]
