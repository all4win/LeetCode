import os
out = open('list.txt','w')

out.write('Medium:\n')
medium = os.listdir('C:\\study\\wordpress\\LeetCode\\Medium')
for name in medium:
    out.write(name[0: -4] + '\n')

out.write('\n')
out.write('Hard:\n')
hard = os.listdir('C:\\study\\wordpress\\LeetCode\\Hard')
for name in hard:
    out.write(name[0: -4] + '\n')

out.close()