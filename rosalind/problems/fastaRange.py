import sys
import os
if len(sys.argv) != 4:
   print "usage: filename seqpos1 seqpos2"
   sys.exit() #can use 'raise SystemExit' (doesn't need 'import sys')
filename = sys.argv[1]
if os.path.exists(filename):
   handle = open(filename,'r')
else:
   print "usage: filename seqpos1 seqpos2"
   print "filename not found"
   sys.exit()
try:
   i=int(sys.argv[2]) 
   j=int(sys.argv[3])
except ValueError:
   print "usage: filename seqpos1 seqpos2"
   print "integer values for seqpos1 and seqpos2"
   sys.exit()

#Skip any text before the first record (e.g. blank lines, comments)
while True:
    line = handle.readline()
    if not line: #No '>' in file, or just empty?
        print "Records in Fasta files should start with '>' character",
        print "Or file empty"
        sys.exit()
    if line[0] == ">": break #Some comments

while True:
    descr = line[1:].rstrip()
    if len(descr.split()) == 1:
       id = descr.split()[0]
       name = id
       descrip = id
    elif len(descr.split()) == 2:
       id = descr.split()[0]
       name = descr.split()[1]
       descrip = name
    else:
       id = descr.split()[0]
       name = descr.split()[1]
       descrip = ' '.join(descr.split()[2:])
#    print id+'\n', name+'\n', descrip
    lines = []
    line = handle.readline()
    while True:
        if not line : break
        if line[0] == ">": break
        lines.append(line.rstrip())
        line = handle.readline()

    #Remove trailing whitespace, and any internal spaces
    #(and any embedded \r which are possible in mangled files
    #when not opened in universal read lines mode)
    result = "".join(lines).replace(" ", "").replace("\r", "")
#    if i<0 or i>j or j<=i or j>len(result):
#    if not (len(result)>=j >= i>=1):
    if not (1 <= i <= j <= len(result)):
      print "usage: filename seqpos1 seqpos2"
      print "integer values: (1 <= seqpos1 <= seqpos2 <= seq length)"
      sys.exit()
    i=i-1 #Because 1st AA is index 0

    #Return the record and then continue...
    print(">%s(%i-%i:%i)\n%s") % (id, i+1, j, len(result), result[i:j])
    if not line : break #StopIteration
handle.close();
