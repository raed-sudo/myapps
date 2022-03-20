# WRITING TO A FILE

stream = open('output_file.txt','wt')
stream.write('Lorem ipsum dolar')
stream.close() #THIS IS REALLY IMPORTANT ! 

# Re-writing with a try/finally

try: 
    stream = open ('output_file_1.txt','wt')
    stream.write('Lorem ipsum dolar')
except Exception as e:
    print('Error')
finally:
    stream.close() # THIS I S REALLY IMPORTANT !

# Simplifying with with : 

with open('output_file_2','wt') as stream:
    stream.write('Lorem ipsum dolar')