space = 4
width = 5
while width < 14:
    if width < 14:
        print("{:^{space}}".format("",space = space) + "{:*^{width}}".format("*",width = width) + "{:^{space}}".format("",space = space))
        width = width + 2
        space = space - 1
    else:
        exit()