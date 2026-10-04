
import hashlib
import os


def calculatechecksum(filename):   #4567 
    fobj = open(filename,"rb")
    
    hobj = hashlib.md5()
    
    buffer = fobj.read(1048576)
    
    while(len(buffer)> 0):
        hobj.update(buffer)
        buffer = fobj.read(1048576)
        
    fobj.close()
    
    return hobj.hexdigest()  
  
def findduplicate(directoryname = "Marvellous"):
    
    ret = False  
    ret = os.path.exists(directoryname)
    
    if(ret == False):
        print("there is no such directory")
        return
    
    ret = os.path.isdir(directoryname) 
    if(ret == False):
        print("there is not directory")
          
    duplicate ={}
    for foldername,subfoldername,filename in os.walk(directoryname):
        for fname in filename:
            fname = os.path.join(foldername,fname)
            checksum = calculatechecksum(fname)
            
            if checksum in duplicate :
                duplicate [checksum].append(fname)
            else:
                duplicate[checksum] = [fname]
                   
    return duplicate 

            

    
       
def deleteduplicate(path = "Marvellous"):
    Mydict = findduplicate(path)
    
    result = list(filter(lambda x : len(x) > 1,Mydict.values()))
    
    count = 0
    cnt = 0
    
    for value in result:
        for subvalue in value:
            count += 1
            if count == 1:
                print("deleted file :",subvalue)
                os.remove(subvalue)
                cnt += 1
                
        count = 0
        
    print("total file deleted : ",cnt)            
    
    
            
            
             

def main():
    
    
    
    deleteduplicate()
    
    
    
    
    
if __name__== "__main__":
    main()    