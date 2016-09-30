width = 100
i = open("Xortholian-Architecture_InputForSubmission_1.txt")
l = i.readline()
while width < 200:
    height = 0
    pos = 0
    pattern = l[pos:pos+width]
    flag = True
    while pos < len(l) and flag:
        if l[pos:pos+width] == pattern:
            height += 1
            pos += width
        else:
            if len(l)-width*height<200:
                print(height)
                print(pattern)
            break
    width += 1
