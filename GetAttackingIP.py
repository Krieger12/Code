ipaddr = []
with open("attack_download.log") as openfile:
    for line in openfile:
        for part in line.split():
            if "src=" in part:
                ipaddr.append(part[4:])
    attack = (list(set([i for i in ipaddr if ipaddr.count(i) > 1])))
    line=0
    print ("Sorted list of attacking ip addresses:")
    for x in sorted(attack):
        print (x)
    print ()
    print ("Input to putty:")
    line=0
    while line < len(attack):
        if attack[line] != "192.168.0.1":
            print ("set",attack[line])
        line = line+1
    
    
