stream = open('demo.txt')

print(stream.readable()) #can I read it ?

print(stream.read(1)) #read the first character

print(stream.readline()) #read the firsr line

stream.close()

stream = open('output.txt','wt') #write text

stream.write('H') #Write a single string

stream.writelines(['ello',' ', 'world']) #write multiple strings

stream.write('\n') #write a new line

stream.flush() # Write the data to file

stream.close() #close the stream and flush data