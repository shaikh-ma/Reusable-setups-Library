
"""
A Setups Library Framework for easily using the added setups and adding the new ones.

"""

import os
from sys import version_info
from time import sleep
import shelve, random

    
if version_info.major == 2:
    import Tkinter as tk
    import tkMessageBox as msg
    import tkFileDialog as dialog
    
elif version_info.major == 3:
    import tkinter as tk
    from tkinter import messagebox as msg
    from tkinter import filedialog as dialog



setups_path = []
setup_text_file_name = 'code.txt'
setup_additional_file_name = 'Additional Files'
root_setup_folder = 'Setups Folder'
theme_color = random.choice(['blue','red','green'])

try:
    paths = shelve.open('.setups_paths')
    setups_path = paths['setups_paths']
    setups_path = [str(the_path) for the_path in setups_path if the_path not in ('', None)]
    #print(setups_path)
    paths.close()
except:
    if not(any(setups_path)):
        msg.showinfo("Not found","No directory found!!\n Please select a directory.")
        sleep(1)
        new_path = dialog.askdirectory()
        if new_path is not None:
            if not(os.path.exists(root_setup_folder)):
                os.mkdir(root_setup_folder)
                
            new_path = os.path.join(new_path,root_setup_folder)
            setups_path.append(new_path)
            paths = shelve.open('.setups_paths')
            paths['setups_paths'] = setups_path
            paths.close()





'''
#---------------- TAKS TO BE DONE -------

1. Add functionality to change exisiting setup path.
2. Add checkbox button to exclude additional files in not there.

#----------------------------------------
'''



'''
##  --------------------- DISABLING ADDITIONAL PATHS FOR NOW ------------------

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

##--------------------------------------------------------------------------------
'''


def add_new_setup():
    def add_path():
        new_setup_name = entered_name.get()
        new_win.withdraw()
        if (new_setup_name != '') and (new_setup_name not in setups_path):
            
            the_setups_path = os.path.join(setups_path[0])# , root_setup_folder)
            new_setup_path = os.path.join(the_setups_path, new_setup_name)
            path_for_additional_files = os.path.join(new_setup_path, setup_additional_file_name)
            print(new_setup_name)
            print(path_for_additional_files)
            try:
                os.makedirs( path_for_additional_files )
            except:
                msg.showerror("Error",'Setup already exists')
                entered_name.delete(0,tk.END)
            else:
                os.chdir(new_setup_path)
                with open(setup_text_file_name, 'w') as new_setup_file:
                    boiler_plate = '''
----------------------- {0} - SETUP STARTS HERE ---------------------------------------------------- 











----------------------- {0} - SETUP ENDS  HERE ---------------------------------------------------- 

'''.format(new_setup_name)
                    new_setup_file.write(boiler_plate)
               
                
                
                if msg.askyesno("Additinal Files", "Does this setup has additional files?"):
                    os.startfile(path_for_additional_files)

                os.startfile(setup_text_file_name)                
            return 0


##    def save_function(event):
##        add_path()
##        



    new_setup_name = tk.StringVar()
    new_setup_name.set('')
    new_win = tk.Toplevel(root) #tk.Tk()
    intro_label = tk.Label(new_win, text="Enter descriptive name for the setup: ")
    intro_label.pack()
    entered_name = tk.Entry(new_win, bd=3, textvariable=new_setup_name)
    entered_name.pack()    
    go_button = tk.Button(new_win, text="Add",command=add_path, bg=theme_color, fg='white')
    #go_button.bind('<Return>',save_function)
    go_button.pack()
    new_win.mainloop()



def search_setup():

    def done():
        setup_name = available_setups.selection_get()
        found_setup_path = ''
        path_exists = False
        if setup_name != '':
            for the_path in setups_path:
                found_setup_path = os.path.join(the_path, setup_name)
                if  os.path.exists(found_setup_path):
                    path_exists = True
                    break
        else:
            return 0

        if path_exists:
            contents = tk.StringVar()
            content = ''
            try:
                with open(os.path.join(found_setup_path , setup_text_file_name), 'r') as setup_file:
                    content = setup_file.read().strip()
                    content.encode('utf-8')
            except:
                msg.showerror("Not Found!","No Text Files found!!")
           
            additional_files_path = found_setup_path.replace(setup_text_file_name,setup_additional_file_name)

            def open_additional_files():
                try:
                    os.startfile(additional_files_path + r'\Additional Files')
                except:
                    msg.showerror("Not Found!","No Additional Files found!!")
  
            if  os.path.exists(additional_files_path):
                pass
                #sleep(3)
                #open_additional_files()
            else:
                msg.showerror("Not Found!","No files found!")
                
            def close_code_win():
                code_win.destroy()
                root.deiconify()

            if len(content) > 0:
                code_win = tk.Toplevel(root)
                code_win.minsize(350,350)
                info_name = tk.Label(code_win, text=setup_name)
                info_name.pack()
              
                code = tk.Text(code_win, state=tk.NORMAL, padx=2, pady=2, exportselection=1,selectbackground="Blue", wrap=tk.WORD) 
                code.insert(tk.INSERT,content)
                code_win.clipboard_clear()
                code_win.clipboard_append(content)
                code.pack(side=tk.TOP, pady=5, fill=tk.X )
                def copy_text():
                    code_win.clipboard_clear()
                    code_win.clipboard_append(content)

                additional_file = tk.Button(code_win, text="Open additional files(css and js files)", command=open_additional_files, bg=theme_color, fg='white')
                additional_file.pack(side=tk.LEFT, padx=4)
                close_window = tk.Button(code_win, text="Back to Setups Library", command=close_code_win, bg=theme_color, fg='white')
                close_window.pack(side=tk.LEFT, padx=4)
                copy_text = tk.Button(code_win, text="Copy text", command=copy_text, bg=theme_color, fg='white')
                copy_text.pack(side=tk.LEFT, padx=4)
                info = tk.Label(code_win, text="Code Copied! You can directly paste the code")
                info.pack(pady=10)
                root.withdraw()
                code_win.mainloop()
                
                    
        else:
            msg.showerror("Not Found!","The entered setup does not exists!")

    
    setup_name = tk.StringVar()
    setup_name.set('')
    instructions = "\n Select the setup from below list and Hit ENTER:  \n"
    intro_label = tk.Label(root, text=instructions)
    intro_label.config(bg="white")
    intro_label.pack(pady=10)

    def call_done_function(event):
        done()  


    present_setups = []
            

    for ind in range(len(setups_path)):
        try:
            os.listdir(setups_path[ind])
        except WindowsError as e:
            continue
        else:
            present_setups += os.listdir(setups_path[ind])

    present_setups.sort()
    
    setups_list = [setup for setup in present_setups if not(setup.startswith('.'))]
    
    setups_list = '\n'.join(setups_list)
        
    available_setups = tk.Listbox(all_setups_list, )   #root, ) 
    all_setups_list.pack(fill=tk.BOTH)
    setups_list = setups_list.split('\n')

    _currdir = os.path.join(os.getcwd(),root_setup_folder)
    

    for ind,setup in enumerate(setups_list):
        curr_setup_path = os.path.join(_currdir, setup)
        text_file = os.path.exists(os.path.join(curr_setup_path,setup_text_file_name))
        additional_file = os.path.exists(os.path.join(curr_setup_path,setup_additional_file_name))
        if text_file or ( additional_file and os.path.isdir(additional_file) ):
            available_setups.insert(ind, setup)


    available_setups.pack(fill=tk.BOTH)
    available_setups.bind('<Return>',call_done_function)
    available_setups.bind('<Double-1>',call_done_function)
    add_setup_button = tk.Button(all_setups_list,text="Add a new setup and files", padx=1, pady=5, command=add_new_setup , bg=theme_color, fg='white')
    add_setup_button.pack()






##----------------------------------------------------
    
root = tk.Tk()
root.config(bg="white")
root.minsize(width=300, height=300)
root.maxsize(width=300, height=300)
root.title('  Setups Library  ')


all_setups_list = tk.Frame(root, height=25)
search_setup()


root.mainloop()
