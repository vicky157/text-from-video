#in this code we will store the text in a sepereate text file.

l_chunks=[diz['chunk{}'.format(i+1)] for i in range(len(diz))]
text='\n'.join(l_chunks)

with open('recognized.txt',mode ='w') as file: 
   file.write("Recognized Speech:") 
   file.write("\n") 
   file.write(text) 
   print("Finally ready!")
