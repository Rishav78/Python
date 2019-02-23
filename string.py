import sys
print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', *sys.argv[-1:0:-1])