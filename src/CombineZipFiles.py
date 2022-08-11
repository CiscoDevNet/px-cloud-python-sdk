from genericpath import isdir
import zipfile as z
import os
import random
import time

milliseconds = int(round(time.time() * 1000))
print(milliseconds)
randm = random.randint(0,100000)
print(randm)

output_file_name = 'z1_' + str(milliseconds)+'_' + str(randm) + '.zip'
print(output_file_name)

# folder path
dir_path = r'input'

res= [os.path.join('output', output_file_name)]
print(res)


for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        res.append(os.path.join('input', path))
print(res)

#zips = ['output/z1.zip', 'z2.zip', 'z3.zip']
zips = res

print(zips)

"""
Open the first zip file as append and then read all
subsequent zip files and append to the first one
"""
with z.ZipFile(zips[0], 'a') as z1:
    for fname in zips[1:]:
        print(fname)
        zf = z.ZipFile(fname, 'r')
        for n in zf.namelist():
            z1.writestr(n, zf.open(n).read())