for i in range(1, 10):
    output = ""
    for j in range(1, 10):
        output = output + "%d x %d = %2d%s" % (i, j, i * j, j == 9 and "" or ", ")
    print (output)
