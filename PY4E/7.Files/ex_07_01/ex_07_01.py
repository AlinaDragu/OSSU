#Write a progrm to read through a file and print the contents of the file (line by line) all in upper case.
#Run with terminal

fh = open('mbox-short.txt')

for lx in fh:
    ly = lx.rstrip()
    print(ly.upper())