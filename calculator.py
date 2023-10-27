from tkinter import *;

def updateSrcVal(event):
    # print(event.widget.cget('text'));
    text = event.widget.cget('text');
    if(text == '='):
        try:
            if(scVar.get().isdigit()):
                scVar.set(int(scVar.get()));
                entryScreen.update();
            else:
                scVar.set(eval(scVar.get()));
                entryScreen.update(); 
        except Exception as e:
            scVar.set("Error");
            entryScreen.update();   
    elif(text == 'C'):
        scVar.set("");
        entryScreen.update();
    else:
        scVar.set(scVar.get()+text);
        entryScreen.update();

if __name__ == '__main__':

    root = Tk();
    root.geometry('400x600');
    root.title('Calculator');

    scVar = StringVar();

    entryFrame = Frame(root, padx=20, pady=10);
    entryScreen = Entry(entryFrame, textvariable=scVar, width=100, font=('Arial', 18));
    entryScreen.pack();
    entryFrame.pack();

    f1 = Frame(root);
    b1 = Button(f1, text="9", padx=15, pady=15);
    b1.bind("<Button-1>", updateSrcVal);
    b1.pack(side='left', padx=15, pady=15);
    b2 = Button(f1, text="8", padx=15, pady=15);
    b2.bind("<Button-1>", updateSrcVal);
    b2.pack(side='left', padx=15, pady=15);
    b3 = Button(f1, text="7", padx=15, pady=15);
    b3.bind("<Button-1>", updateSrcVal);
    b3.pack(side='left', padx=15, pady=15);
    f1.pack();

    f1 = Frame(root);
    b1 = Button(f1, text="6", padx=15, pady=15);
    b1.bind("<Button-1>", updateSrcVal);
    b1.pack(side='left', padx=15, pady=15);
    b2 = Button(f1, text="5", padx=15, pady=15);
    b2.bind("<Button-1>", updateSrcVal);
    b2.pack(side='left', padx=15, pady=15);
    b3 = Button(f1, text="4", padx=15, pady=15);
    b3.bind("<Button-1>", updateSrcVal);
    b3.pack(side='left', padx=15, pady=15);
    f1.pack();

    f1 = Frame(root);
    b1 = Button(f1, text="3", padx=15, pady=15);
    b1.bind("<Button-1>", updateSrcVal);
    b1.pack(side='left', padx=15, pady=15);
    b2 = Button(f1, text="2", padx=15, pady=15);
    b2.bind("<Button-1>", updateSrcVal);
    b2.pack(side='left', padx=15, pady=15);
    b3 = Button(f1, text="1", padx=15, pady=15);
    b3.bind("<Button-1>", updateSrcVal);
    b3.pack(side='left', padx=15, pady=15);
    f1.pack();

    f1 = Frame(root);
    b1 = Button(f1, text="0", padx=15, pady=15);
    b1.bind("<Button-1>", updateSrcVal);
    b1.pack(side='left', padx=15, pady=15);
    b2 = Button(f1, text="+", padx=15, pady=15);
    b2.bind("<Button-1>", updateSrcVal);
    b2.pack(side='left', padx=15, pady=15);
    b3 = Button(f1, text="-", padx=15, pady=15);
    b3.bind("<Button-1>", updateSrcVal);
    b3.pack(side='left', padx=15, pady=15);
    f1.pack();

    f1 = Frame(root);
    b1 = Button(f1, text="*", padx=15, pady=15);
    b1.bind("<Button-1>", updateSrcVal);
    b1.pack(side='left', padx=15, pady=15);
    b2 = Button(f1, text="/", padx=15, pady=15);
    b2.bind("<Button-1>", updateSrcVal);
    b2.pack(side='left', padx=15, pady=15);
    b3 = Button(f1, text="%", padx=15, pady=15);
    b3.bind("<Button-1>", updateSrcVal);
    b3.pack(side='left', padx=15, pady=15);
    f1.pack();

    f1 = Frame(root);
    b1 = Button(f1, text="C", padx=15, pady=15);
    b1.bind("<Button-1>", updateSrcVal);
    b1.pack(side='left', padx=15, pady=15);
    b2 = Button(f1, text="=", padx=15, pady=15);
    b2.bind("<Button-1>", updateSrcVal);
    b2.pack(side='left', padx=15, pady=15);    
    f1.pack();

    root.mainloop();