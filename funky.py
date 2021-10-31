#define a function say funkynumeral 
def funkynumeral():
  #use serial number n
  n = 1
  #store the string as value for numerals as key
  d = {0:'*', 1:'**', 2:'***', 3:'****'}
  #three digit numeral , all possible combinations can be formed using three loop range 0,1,2 and 3
  for a in range(4):
    for b in range(4):
      for c in range(4):
        #print the serial number n, followed by numeral followed by dictionary value string of star to be printed 
        print(n, a,d[a],b,d[b],c,d[c])
        #increase the counter
        n += 1

#main function 
if __name__ == '__main__':
  #calling funkynumeral()
  funkynumeral()


     
