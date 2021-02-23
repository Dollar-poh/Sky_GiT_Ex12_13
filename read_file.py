# infile = open("pelican.txt", "r")
# line = infile.read()
# print(line)
# print(type(line))

# linelist = open("pelican.txt").readlines()
#
# print(linelist)
# print(type(linelist))


for line in open("pelican.txt"):
    print(line,end="")

print(type(line))