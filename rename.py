import sys, getopt, os, re

opts, args = getopt.getopt(sys.argv[1:], "hd:p:r:t") 

path, pattern, replacePattern, isTest = "", "", "", False

for opt, arg in opts:
    if opt == "-d":
        path = arg
    if opt == "-p":
        pattern = arg
    if opt == "-r":
        replacePattern = arg
    if opt == "-t":
        isTest = True
    if opt == "-h": 
        print(u"-d:  目录")
        print(u"-p:  正则表达式，()代表group")
        print(u"-r:  替换表达式，group(n)")
        print(u"-t:  是否测试")
        print(u"-h:  帮助")
        print(r"例:  python rename.pyw -d d:\test\ -p .+(\d{4}).*?(.txt) -r Test{1}{2}")
        exit()

dirs = os.listdir(path)
print(dirs)

for dir in dirs:
    replaceText = replacePattern
    match = re.match(pattern, dir)
    if match:
        groupIndexs = re.findall(r'\{(\d)\}', replacePattern)
        if groupIndexs:
            for index in groupIndexs:
                replaceText = replaceText.replace("{" + index + "}", match.group(int(index)))

        if isTest:
            print(replaceText)
        else:
            print("rename " + dir + "...")
            os.rename(path + dir, path + replaceText)

print("Done!")
