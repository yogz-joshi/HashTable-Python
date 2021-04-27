# HashTable-Python
DESIGN SPECIFICATION :
Data Structure used:
 arr[ROW][COL]= A two dimensional list to store the input file content. ROW is the total number of Assesse and COL= Max number of PAN Record for that Assesse. 
 
Function Definitions:
1-Main:
  Var used:- filename= Location of the file in local directory,file_type= type of inout file,key= PAN,value= Name+Place(Space sepereated),obj=Object of class HashTable
  
  Assumption: A) Input must be txt or csv file to be uploaded with 3 columns (PAN ,Name,Place) 
              B) The PAN Associated with same Assesse type in input file  must not be more than 100.
              C) PAN Number to be searched in Input text box should not be blank.
              D) To close the Program press "exit" in the input box
              E) File should be saved in the format like "abc.txt/abc.csv"
  
2- Class HashTable:
   HashTable expects two parameters key,value.
   Funtion __init__:
    Var used:- ROW=10 (Total assesse), COL=100(Maximum PAN with same assesse code),arr= 2D array[COL*ROW]
    
   Function get_hash(key,N):
    Var Used:- key= input to hash function,N= Integer for modulo function (here ROW or COL)
    
   Function __setitem__:
    Var Used:-
      key= PAN Number,value= Name+Place ,assesse= 4th char of PAN,h1= Hash value od Assesse,h2=Hash value of the PAN 
      
   Function __getitem__:
    Var Used:- Key = Input search PAN or Assesse,result_arr= empty list,text= text to be returned as output
  
3-Function upload():
    Package used: tkinter
    Var used: filename= File Directry name to be returned by function.
    
4-Function get_file_type(filename):
    Var used :- filename= File directory name.
    
    
    
              
   
