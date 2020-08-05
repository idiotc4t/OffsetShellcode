
dict = open('wingding.ttf','rb+').read();
char =0
for i in range(256):
        for p in range(len(dict)):
                if  ord(chr(dict[p])) == ord(chr(i)):
                        char +=1
                        print(char)
                        break

if char == 256:print("this file has full chars table");