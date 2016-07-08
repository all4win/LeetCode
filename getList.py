import os
out = open('list.txt','w')
readme = open('README.md','w')
readme.write('# LeetCode\n')
readme.write('LeetCode Solution Code by Tiancheng Gong\n')
readme.write('\n')
readme.write('Covered Questions\n')
readme.write('\n')

out.write('Medium:\n')
readme.write('* Medium:\n')
medium = os.listdir('C:\\study\\wordpress\\LeetCode\\Medium')
for name in medium:
    out.write(name[0: -4] + '\n')
    readme.write('	* ' + name[0: -4] + '\n')

out.write('\n')
out.write('Hard:\n')

readme.write('\n')
readme.write('Medium:\n')
readme.write('* Hard:\n')
hard = os.listdir('C:\\study\\wordpress\\LeetCode\\Hard')
for name in hard:
    out.write(name[0: -4] + '\n')
    readme.write('	* ' + name[0: -4] + '\n')

out.close()
readme.close()