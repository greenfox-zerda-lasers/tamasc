ag = [3, 4, 5, 6, 7]
# please double all the elements of the list

# i=0
# for x in ag:
#     ag[i] = x * 2
#     i+=1

# for i, val in enumerate(ag):
#     ag[i] = ag[i] * 2
# print(ag)

for i in range(len(ag)):
    ag[i] = ag[i] * 2
print(ag)
