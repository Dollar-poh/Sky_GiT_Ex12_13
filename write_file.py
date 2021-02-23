append = open("pelican.txt", "a")
output = open("pelican.txt", "w")

num = append.write("A wonderful bird is the pelican,\n")
print(num)

num = append.write("His bill holds more than his belican.\n")
print(num)

f = "A wonderful bird is the pelican,"
print(len(f))

lines =["He can take in his beak,\n", "Enough food for a week,\n", "But I’m damned if I see how the helican.\n"]
output.writelines(lines)