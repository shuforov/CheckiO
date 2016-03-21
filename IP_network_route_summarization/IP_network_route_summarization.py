# http://www.checkio.org/mission/ip-network-route-summarization/
def checkio(data):
    temp_list = []
    for x in data:
        tempo = []
        for y in x:
            while y != ".":
                tempo.append(y)
        temp_list.append(tempo)
     binary_list = []
     for x in temp_list:
         tempo = []
         for y in x:
             while x.index(y) != x.index(x[-1:]):
                 tempo.append(bin(y))
         binary_list.append(temp)
         new_bin_list = []
         for x in binary_list:
             tempo = []
             for y in x:
                 new_bin_list.append(y [2:])
         print new_bin_list
                        
      
    
print checkio(["172.16.12.0", "172.16.13.0", "172.16.14.0", "172.16.1e5.0"])

#These "asserts" using only for self-checking and not necessary for auto-testing

# (checkio(["172.16.12.0", "172.16.13.0", "172.16.14.0", "172.16.15.0"]) == "172.16.12.0/22"), "First Test"
# (checkio(["172.16.12.0", "172.16.13.0", "172.155.43.9"]) == "172.0.0.0/8"), "Second Test"
# (checkio(["172.16.12.0", "172.16.13.0", "172.155.43.9", "146.11.2.2"]) == "128.0.0.0/2"), "Third Test"