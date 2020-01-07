#!/usr/bin/env python
# coding: utf-8

# In[ ]:


teldict =  {"jonathan": 1567, "Fammy": 2415123,"Michael": 8990}
telmail = {"jonathan": "john@email.com", "Fammy": "fammy@gmail.com", "Michael": "Mic@hotmail"}

def feedback():
   print("Thank you its updated.")

def del_ctc():   #Option 5 - Remove contact
   del_ctc = input("Please enter contact to delete:\n")
   for ctc in teldict:
      while ctc == del_ctc:
         del teldict[ctc]
         del telmail[del_ctc]
         print( "The contact ("+str(ctc)+") is removed.")
         start_()
   print("This contact is not in the dictionary, please try again.")
   start_()

def edit_ctc(): # Option 4 - Edit Contact
   edit_ctc = input("Please enter the contact to edit:\n")
   for ctc in teldict:
     while ctc == edit_ctc:
       edit_tel = input("Please enter the tel to edit:\n")
       teldict[edit_ctc] = edit_tel      
       if edit_tel == "":
          feedback()
          start_()
       else:
        edit_mail = input("Please enter the mail to edit:\n")
        telmail[edit_ctc] = edit_mail 
        feedback()
        start_()
   print("The contact you wish to edit ("+str(edit_ctc)+") is not in the current dictionary.")
   start_()
   
            
def add_ctc():  # Option 3 - Add Contact
   add_ctc = input("Please enter the new contact:\n")
   add_tel =  input("Please enter the new tel:\n")
   add_mail  = input("Please enter the new email:\n")
   teldict[add_ctc] = add_tel
   telmail[add_ctc] = add_mail
   print("The new values are added into the dictionary.")
   start_()
   
   
def search_ctc():  # Option 2 - Search Contact
   search_name = input("Please enter the search name:\n")
   for name in teldict:
     while name == search_name:
       print("Telno:"+str(teldict[search_name])+"     Email:"+str(telmail[search_name]))
       start_()
   print("The name you enter us not in the dictionary, try again.")
   start_()
   
   
def extract_(): # Option 1 - Get dictionary
   print(60*"-")
   for tel in telmail:
      char_count = len(tel)
      space_ctc = 12 - len(tel)
      space_tel = 12 - len(str(teldict[tel]))
      print (str(tel)+space_ctc*" "+"Telno:"+str(teldict[tel])+space_tel*" "+"Email:"+str(telmail[tel]))
   start_()
   
def start_():  # Request user selection options
   print("-----WELCOME TO THE ADDRESS----")
   print("Enter 1 to display all contacts")
   print("Enter 2 to search for contact")
   print("Enter 3 to add contact")
   print("Enter 4 to edit contact")
   print("Enter 5 to delete contact")
   print("Enter -1 to get out the program")
   
   entry = input("Enter your choice:\n")
   if entry == "1":
      extract_()
   elif entry == "2":
      search_ctc()
   elif entry == "3":
      add_ctc()
   elif entry == "4":
      edit_ctc()
   elif entry == "5":
      del_ctc()
   elif entry == "-1":
      print("You have end the operation and have a goood day.")
   else: 
      print("Please enter again")
      start_()
start_()

dict = {"jack":{44555:"jacko@gmail.com"},"Michelle":{33669:"mich@hotmail.com"},"Fabian":{774484:"Fab@ymail.com"}}

def extract():
   for key in dict:
      value = key
      print(value)
   for key in dict:
      for key1 in dict[key]:
        value1 = key1
   for key in dict:
      for key1 in dict[key]:
        value2 = dict[key][key1]
        print(value, value1, value2)

extract()


# In[ ]:




