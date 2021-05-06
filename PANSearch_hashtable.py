'''
PYTHON PROGRAMMING LANGUAGE
CODING PLATFORM CAN BE USED- JUPYTER NOTEBOOK /SPYDER/ PYCHARM
 
'''
import os
import sys
import csv
#Class definition

def upload():
        from tkinter import Tk 
        from tkinter.filedialog import askopenfilename    
        Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
        filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
        #print(filename)
        return(filename)
    
def get_file_type(filename):
    return filename.split('.')[1] 

class HashTable:
    #Initialisation
    def __init__(self,key,value):       
        self.ROW=10
        self.COL=10
        self.key=key
        self.value=value
        #create 2D array (10*100)
        self.arr=[[[-1,-1] for i in range(self.COL)]for j in range(self.ROW)]        
        #print(f'Step 1- 2D Array Created: {self.arr}')
        
    #-------Defining Hash Function------------------
    def get_hash(self,key,N):
        self.N=N
        hash=0
        for char in key:
            hash += ord(char)
        return hash % self.N        
    
    #------Defining _setitem_ function to store PAN,Name Place in Hash Table-----
    def __setitem__(self,key,value):
        #print(f'------------For PAN= {key}---------------------')
        assesse=key[3]
        #print(f'ROW inside setitem={self.ROW}')
        h1=self.get_hash(assesse,self.ROW)
        #print(f'Hash 1 Generated={h1}')
        h2=self.get_hash(key,self.COL)
        #print(f'Hash 2 Generated={h2}')
        t=-1
        #print(f'self.arr[h1]={self.arr[h1]}')

        #-----------Without Collision-----------------
        #print(f'self.arr[h1][h2]={self.arr[h1][h2]}')
        if self.arr[h1][h2][0]==-1:
            self.arr[h1][h2]=value
            #print(f'No collision')
            #found=True
            #print(f'Final Hash Table= {self.arr}')
            
                    
        #------Collision solution-using Quadratic probing-----    
        else:
            found=False;count=1
            #print(f'collision occured')
            
            while not found:                                                 
                #print(f'Quadratic probing ,finding new index')
                t=(h2+count*count)% self.COL
                #print(f't={t}')
                #print(f'self.arr[h1][t]={self.arr[h1][t]}')                                                  
                if self.arr[h1][t][0]==-1:
                    #print(f'New Index found ,resolving Collision,index= {t} inside arr.index= {h1}')
                    found=True                           
                    break      
                else:
                    count+=1
            if found:
                self.arr[h1][t]=value 
                #print(f'Final Hash Table= {self.arr}')  

  #---------------GET FUNCTION:FOR GETTNG THE SEARCH RESULT-------------------------------------------
    def __getitem__(self,key):
        #print(f'------------Searching PAN= {key}---------------------')
        if len(key)==1:
            result_arr=[]
            h1=self.get_hash(key,self.ROW)
            for items in self.arr[h1]:
                
                if items[0] != -1:
                    result_arr.append(items[0]+" "+items[1])
            return result_arr    
        else:
            assesse=key[3]
            h1=self.get_hash(assesse,self.ROW)           
            h2=self.get_hash(key,self.COL)            
            if self.arr[h1][h2][0]==key:
                text="The entry "+key+" does exist –"+ self.arr[h1][h2][1]
                return(text) 
            elif self.arr[h1][h2][0]!=key:
                count=1;found=False;t=-1
                
                while not found:
                    t=(h2+count*count)% self.COL
                    count+=1
                    #print(f't= {t}')
                    if self.arr[h1][t][0]==key:
                        #print(f'key found at new index= {t}')
                        found=True
                        text="The entry "+key+" does exist –"+ self.arr[h1][t][1]
                        return(text)
                                        
            else:
                text="The entry "+key+" does not exist" 
                return(text)
        

    
        
#---------Main Function--Starting Block-------------------
if __name__=="__main__":      
    #Upload File from Local Space
    print('*******SELECT FILE FROM OPENED WINDOW*******')
    filename=upload()     
    file_type=get_file_type(filename)
    
    #Create Class Object
    key,value="",""
    obj=HashTable(key,value)   
    
    if file_type== 'csv':
        with open(filename, 'r') as csvfile:
            csvreader = csv.reader(csvfile)  
      
            #Read each row of csv file 
            for rows in csvreader:
                key=rows[0]
                #print('***************csv file*************************')
                #print(f'key={key}')
                value=[key,rows[1]+' '+rows[2]]
                #print(f'value={value}')
                obj[key]=value #call setitem
        csvfile.close() 
    else:
        with open(filename,'r') as txtfile:
            txt_reader = txtfile.readlines()            
            #print(f'text_reader ={txt_reader}')
            for rows in txt_reader:
                rows=rows.split(' ')
                key=rows[0]
                #print('****************text file************************')
                #print(f'rows={rows}')
                #print(f'key={key}')
                value=[key,' '.join(map(str,rows[1 :]))]
                #print(f'value={value}')
                obj[key]=value #call setitem
        txtfile.close()       
    #--------------------------------------------------------------------------    
    
    #Input the Pan Number as text
    while True:
        pan_num=input("Enter PAN Number to Search or type 'exit' to close- ")
        if pan_num =='exit':
            break
        if len(pan_num)>3 and pan_num[3] in 'CPHFATBLJG':
            result=obj[pan_num]  #call getitem
            print(result)
        elif len(pan_num)==1 and pan_num in 'CPHFATBLJG':
            result=obj[pan_num]  #call getitem
            for entry in result:
                print(entry)
        else:
            print('Entered Pan does not have valid Assesse ') 