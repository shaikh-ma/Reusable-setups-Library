#! bin/python2

"""
A Setups Library Framework for easily using the added setups and adding the new ones.

"""

import os
import Tkinter as tk
import tkMessageBox as msg
#import pickle
from time import sleep

global setups_path

version = '0.0.3'
setups_path = [r"",]


##  --------------------- DISABLING ADDITIONAL PATHS FOR NOW ------------------
''''
if os.path.exists('Path_list.txt'):
    pass
else:
    with open('Path_list.txt','wb') as path_lists:
        setups_path = [r"",]
        pickle.dump(setups_path, path_lists)
    #msg.showerror("Not Found!", "Paths to setup file not found!")

    
with open('Path_list.txt','rb') as path_lists:
    contents = path_lists.read()
    setups_path = [r"",]
    for setup_path in setups_path:
        if setup_path not in contents:
            with open('Path_list.txt','wb') as path_lists:
                pickle.dump(setups_path, path_lists)
    #os.startfile('Path_list.txt')

##----------------------------------------------------
'''

def add_new_setup():
    def add_path():
        #go_button.pack_forget()
        #entered_name.pack_forget()
        #intro_label.pack_forget()
        new_setup_name = entered_name.get()
        new_win.withdraw()
        if (new_setup_name != '') and (new_setup_name not in setups_path):
            the_setups_path = setups_path[0]
            new_setup_path = os.path.join(the_setups_path, new_setup_name)
            path_for_additional_files = os.path.join(new_setup_path, 'Additional Files') 
            try:
                os.makedirs(path_for_additional_files )
            except:
                msg.showerror("Error",'Setup already exists')
                entered_name.delete(0,tk.END)
            else:
                os.chdir(new_setup_path)
                with open('Code.txt', 'wb') as new_setup_file:
                    boiler_plate = '''
          -----------------: POINTS TO NOTE FOR THIS SETUP :---------------------
         1. Keep the variable name to be changed in all UPPER CASE
         2. Add the most important things regarding the setup here.
         3. Save all the required js and css file in the folder properly.
         ---------------- Update above points as per the setup requirement. -----------------
        
----------------------- {0} - SETUP STARTS HERE ---------------------------------------------------- 





 ----------------------- {0} - SETUP ENDS  HERE ---------------------------------------------------- 
'''.format(new_setup_name)
                    new_setup_file.write(boiler_plate)
               
                os.startfile(path_for_additional_files)
                sleep(2)
                msg.showinfo("Note", "Save all the js and css files\n related to the setup in this folder")
                os.startfile('Code.txt')
                
            #available_setups.pack_forget()
            #search_setup()
            


##            setups_path.append(new_setup_name)
##        
##        with open('Path_list.txt','rb') as path_lists:
##            contents = path_lists.read()
##            #setups_path = [r"",]
##            for setup_path in setups_path:
##                if setup_path not in contents:
##                    with open('Path_list.txt','wb') as path_lists:
##                        pickle.dump(setups_path, path_lists)
##            
##            print "\nsetups_path: ",setups_path
            #os.startfile('Path_list.txt')
            #msg.showinfo("Important!!!", "Currently this functionality is in development")
            return
            #new_win.destroy()
    
    #new_win = tk.Tk()
    # Get Path to setup  
    new_setup_name = tk.StringVar()
    new_setup_name.set('')
    #print new_setup_name
    new_win = tk.Tk()
    intro_label = tk.Label(new_win, text="Enter descriptive name for the setup: ")
    intro_label.pack()
    entered_name = tk.Entry(new_win, bd=3, textvariable=new_setup_name)
    entered_name.pack()
    
    go_button = tk.Button(new_win, text="Add",command=add_path)
    go_button.pack()    
    new_win.mainloop()



def search_setup():
    #search_setup_button.pack_forget()   
    def done():
        setup_name = available_setups.selection_get()
        print setup_name
        #setup_name = entered_name.get().strip()
        #if 'setup' not in setup_name.lower(): setup_name = setup_name + ' Setup'

        #check if setup exists
        found_setup_path = ''
        #found_setup_folder = ''
        #setups_path = setups_path + '\\' + setup_name 
        print "setups_path:", setups_path, "setups_name:", setup_name
                #print  found_setup_path
        path_exists = False
        if setup_name != '':
            for the_path in setups_path:
                #found_setup_folder = os.path.join(the_path, setup_name)
                found_setup_path = os.path.join(the_path, setup_name)
                if  os.path.exists(found_setup_path):
                    path_exists = True
                #elif os.path.exists(found_setup_folder):
                #    found_setup_path = found_setup_folder
                #    path_exists = True
                    break

        if path_exists:
            print "found_setup_path: ",found_setup_path
            contents = tk.StringVar()
            content = ''
            try:
                with open(found_setup_path + r'\Code.txt', 'rU') as setup_file:
                    content = setup_file.read().strip() 
                    #contents.set(setup_file.read().strip())
                    #contents.replace('\n\n','\n')
            except:
                msg.showerror("Not Found!","No Text Files found!!")
           
            additional_files_path = found_setup_path.replace('Code.txt','Additional Files')

            def open_additional_files():
                try:
                    os.startfile(additional_files_path + r'\Additional Files')
                except:
                    msg.showerror("Not Found!","No Additional Files found!!")
  
            #print additional_files_path
            if  os.path.exists(additional_files_path):
               #msg.showinfo("passed","Passed")
                open_additional_files()

            else:
                msg.showerror("Not Found!","No files found!")
                
            def close_code_win():
                code_win.destroy()
                root.deiconify()
                #search_setup()
                #root.mainloop()
            #entered_name.delete(0,tk.END)
            if len(content) > 0:
                code_win = tk.Tk()
                code_win.minsize(350,350)
                #code_win.maxsize(650,650)
                #code_win.attributes('-fullscreen', True)
                info_name = tk.Label(code_win, text=setup_name)
                info_name.pack()
              
                code = tk.Text(code_win, state=tk.NORMAL, padx=2, pady=2, exportselection=1,selectbackground="Blue", wrap=tk.WORD) 
                code.insert(tk.INSERT,content)
                code_win.clipboard_clear()
                code_win.clipboard_append(content)
                #code.tag_add('sel', '1.0', 'end')
                #code.bind("<Control-Key-a>", select_all)
                #code.bind("<Control-Key-A>", select_all)
                code.pack(side=tk.TOP, pady=5, fill=tk.X )
                def copy_text():
                    code_win.clipboard_clear()
                    code_win.clipboard_append(content)

                additional_file = tk.Button(code_win, text="Open additional files(css and js files)", command=open_additional_files)
                additional_file.pack(side=tk.LEFT, padx=4)
                close_window = tk.Button(code_win, text="Back to Setups Library", command=close_code_win)
                close_window.pack(side=tk.LEFT, padx=4)
                copy_text = tk.Button(code_win, text="Copy text", command=copy_text)
                copy_text.pack(side=tk.LEFT, padx=4)
                info = tk.Label(code_win, text="Code Copied! You can directly paste the code")
                info.pack(pady=10)
                
                #msg.showinfo("DONE", "Code Copied! You can directly paste the code")
                root.withdraw()
                code_win.mainloop()
                
    
        else:
            msg.showerror("Not Found!","The entered setup does not exists!")

    
        #go_button.pack_forget()
        #entered_name.pack_forget()
        #intro_label.pack_forget()
        #available_setups.pack_forget()
        #search_setup_button.pack()
        


        #new_win.destroy()
 
    # open new window
    #new_win = tk.Tk()
    
    # Get Setup Name   
    setup_name = tk.StringVar()
    setup_name.set('')
    #print "setup_name: ", setup_name
    intro_label = tk.Label(root, text="Select the setup from below list and Hit ENTER: ")
    intro_label.config(bg="white")
    intro_label.pack(pady=10)
    #entered_name = tk.Entry(root, bd=3, textvariable=setup_name)
    #entered_name.pack()
    #go_button = tk.Button(root, text="Search", command=done)
    #go_button.pack()

    def call_done_function(event):
        done()
        #entered_name.unbind('<Return>')

    ##entered_name.bind('<Return>', call_done_function)
    
    present_setups = []
    
    for ind in range(len(setups_path)):
        try:
            os.listdir(setups_path[ind])
        except WindowsError, e:
            continue
        else:
            present_setups.append(os.listdir(setups_path[ind]))

    #present_setups = '\n'.join('\n'.join(present_setups))
    present_setups.sort()
    setups_list = ''
    for setups in present_setups:
        for setup in setups:
            setups_list += setup + '\n' 
        
    #print "setups_list: ", setups_list
    ##    available_setups = tk.Text(root, state=tk.NORMAL, wrap=tk.CHAR)
    ##    available_setups.insert(tk.INSERT,setups_list)
    ##    available_setups.pack( fill=tk.BOTH)

    available_setups = tk.Listbox(root, ) #height=40, )
    
    setups_list = setups_list.split('\n')
    for ind,setup in enumerate(setups_list):
        #print "setup:" , setup
        available_setups.insert(ind, setup)
    available_setups.pack(fill=tk.BOTH)
    available_setups.bind('<Return>',call_done_function)
    available_setups.bind('<Double-1>',call_done_function)
    #search_setup_button.pack()
    #print present_setups
     
    
    #setup_name = (entered_name.get())
    #print setup_name   

    #new_win.mainloop()

    # Show list of all available setups found
    
    # Show Button to add additional files
    # for adding files open folder to upload files
    # Move selected files to setup folder
    #pass


##----------------------------------------------------
root = tk.Tk()
root.config(bg="white")
root.minsize(width=100, height=100)
root.minsize(width=300, height=300)
#root.attributes('-fullscreen', True)
root.title('Setups Library - ' + version)


search_setup()
add_setup_button = tk.Button(root,text="Add a new setup", padx=1, pady=5, command=add_new_setup)
add_setup_button.pack()
root.mainloop()

#root.bell()
#a = root.clipboard_get()
#search_setup_button = tk.Button(root,text="Search Setup", padx=1, pady=5, command=search_setup)
#search_setup_button.pack()




'''

available_setups = []
print available_setups

#path_exists = False
for the_path in setups_path:
    found_setup_path = os.path.join(the_path, 'Bipolar Grid Setup' ,'Code.txt')
    if  os.path.exists(found_setup_path):
        available_setups.append(setup_file)
        #path_exists = True
        #break

cnt = 1
avail = tk.Listbox(root)
for setup in available_setups:
    avail.insert(cnt,setup)
    cnt += 1
avail.pack()
'''

