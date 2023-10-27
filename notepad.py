from tkinter import *;
from tkinter.messagebox import showinfo;
from tkinter.filedialog import askopenfilename, asksaveasfilename;
import os;

def newFileMethod():
    global file;
    file = None;
    root.title('Untitled - Notepad');
    textArea.delete(1.0, END);

def openFileMethod():   
    global file; 
    file = askopenfilename(defaultextension="*.txt", filetypes=[("All Files", "*.*"), ("Text Document", "*.txt")]);
    if(file == ""):
        file = None;
    else:
        root.title(os.path.basename(file));
        textArea.delete(1.0, END);
        f = open(file, "r");
        textArea.insert(1.0, f.read());
        f.close();

def saveMethod():
    global file;    
    if(file != None):
        f = open(file, "w");        
        f.write(textArea.get(1.0, END));
        f.close();
    else:
        file = asksaveasfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Document", "*.txt")]);  
        if(file == ""):
            file = None;
        else:
            f = open(file, "w");
            f.write(textArea.get(1.0, END));
            f.close();
            root.title(os.path.basename(file));   
    

def exitMethod():
    root.destroy();

def cutMethod():
    textArea.event_generate('<<Cut>>');

def copyMethod():
    textArea.event_generate('<<Copy>>');

def pasteMethod():
    textArea.event_generate('<<Paste>>');

def aboutMethod():
    showinfo('About', 'Version: 1.0.0');


if __name__ == '__main__':

    root = Tk();
    root.geometry('500x600');
    root.title('Untitled - Notepad');

    file = None;

    #Creating MenuBar
    menuBar = Menu(root);

    #Creating FileMenu
    fileMenu = Menu(menuBar, tearoff=0);
    fileMenu.add_command(label='New File', command=newFileMethod);
    fileMenu.add_command(label='Open', command=openFileMethod);
    fileMenu.add_command(label='Save', command=saveMethod);
    fileMenu.add_command(label='Exit', command=exitMethod);

    #Creating EditMenu
    editMenu = Menu(menuBar, tearoff=0);
    editMenu.add_command(label='Cut', command=cutMethod);
    editMenu.add_command(label='Copy', command=copyMethod);
    editMenu.add_command(label='Paste', command=pasteMethod);    

    #Creating Help Menu
    aboutMenu = Menu(menuBar, tearoff=0);
    aboutMenu.add_command(label='About', command=aboutMethod);
    
    #Adding Menus in MenuBar
    menuBar.add_cascade(label='File', menu=fileMenu);
    menuBar.add_cascade(label='Edit', menu=editMenu);
    menuBar.add_cascade(label='About', menu=aboutMenu);

    #Adding MenuBar in root
    root.config(menu=menuBar);

    #Creating Text Area
    textArea = Text(root);

    #Adding Text Area into root
    textArea.pack(expand=True, fill='both');

    #Creating and addind scrollbar
    scrollBar = Scrollbar(textArea);
    scrollBar.config(command=textArea.yview);
    textArea.config(yscrollcommand=scrollBar.set);
    scrollBar.pack(side='right', fill='y');

    root.mainloop();