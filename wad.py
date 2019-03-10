import caption
import os.path

n = open("temp_img/num.txt", "r")
s = int(n.readline())
print(s)
n.close()

n = open("temp_img/num.txt", "w")
n.write(str(s + 1))
n.close()
