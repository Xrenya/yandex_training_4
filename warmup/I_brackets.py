brackets = input()
mapping = {"(": ")", "{": "}", "[": "]"}
queue = []
output = "yes"
for i in range(len(brackets)):
    if brackets[i] in mapping:
        queue.append(mapping[brackets[i]])
    else:
        if queue and brackets[i] == queue[-1]:
            queue.pop()
        else:
            output = "no"
            break
if output == "yes" and len(queue) == 0:
	print(output)
else:
	print("no")
