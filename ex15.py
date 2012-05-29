from sys import argv

script, filename = argv

txt = open(filename)#sets txt to filename

print "Here's your file %r" % filename
print txt.read()#prints text in file
txt.close#closes file

print "type filename again:"
file_again = raw_input("> ")#sets file_again to users input

txt_again = open(file_again)#opens file_again as txt_again

print txt_again.read()#prints txt_again contents
txt_again.close#closes file

