from tkinter import *    #Adding the graphics libraries from Tkinter
import os   
import PIL  #Adding the PIL library in the program for editing the images
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
from PIL import ImageTk
import pyqrcode   #Adding the library for QR Code Generation
import png    #Adding png library
import  tkinter.messagebox   #importing the MessageBox
#import tkFileDialog     #importing the tkFilleDialog
from tkinter import filedialog
from tkinter import messagebox
'''from pymongo import MongoClient  #importing the pymongo library for exporting the data to database
client = MongoClient('localhost', 27017)  # Adding the Client in the file database
mydb = client.id #join to the database'''
def add_client(text, id1, ht, start, mn,avatar):  #define a function of adding a data to table
        mydb.forsk_clients.insert(
                {
                "Name" : text,   #For Name
                "ID" : id1,         #For ID number
                "Branch" : ht,      #For Branch
                "Program" : start,  #For Program Type
                "DOB" : mn,     #For setting the Date of Birth
                "Image" : avatar,   #For sending the users image to database
                })
        return "Client added successfully"  #retur a confirmation message

creds = 'tempfile.temp' # This just sets the variable creds to 'tempfile.temp'
def Signup(): # This is the signup definition, 
    global pwordE # These globals just make the variables global to the entire script, meaning any definition can use them
    global nameE
    global roots
 
    roots = Tk() # This creates the window, just a blank one.
    roots.title('Signup') # This renames the title of said window to 'Signup'
    intruction = Label(roots, text='Please Enter new Credidentials\n') # This puts a label, so just a piece of text saying 'please enter blah'
    intruction.grid(row=0, column=0, sticky=E) # This just puts it in the window, on row 0, col 0. If you want to learn more look up a tkinter tutorial :)
 
    nameL = Label(roots, text='New Username: ') # This just does the same as above, instead with the text new username.
    pwordL = Label(roots, text='New Password: ') # This is to send the password
    nameL.grid(row=1, column=0, sticky=W) # Same thing as the instruction var just on different rows. :) Tkinter is like that.
    pwordL.grid(row=2, column=0, sticky=W) # This is just to set the password field to grid
 
    nameE = Entry(roots) # This now puts a text box waiting for input.
    pwordE = Entry(roots, show='*') # Same as above, yet 'show="*"' What this does is replace the text with *, like a password box :D
    nameE.grid(row=1, column=1) # You know what this does now :D
    pwordE.grid(row=2, column=1) # ^^
 
    signupButton = Button(roots, text='Signup', command=FSSignup) # This creates the button with the text 'signup', when you click it, the command 'fssignup' will run. which is the def
    signupButton.grid(columnspan=2, sticky=W)
    roots.geometry('350x350')
    roots.mainloop() # This just makes the window keep open, we will destroy it soon
 
def FSSignup():
    with open(creds, 'w') as f: # Creates a document using the variable we made at the top.
        f.write(nameE.get()) # nameE is the variable we were storing the input to. Tkinter makes us use .get() to get the actual string.
        f.write('\n') # Splits the line so both variables are on different lines.
        f.write(pwordE.get()) # Same as nameE just with pword var
        f.close() # Closes the file
 
    roots.destroy() # This will destroy the signup window. :)
    Login() # This will move us onto the login definition :D



def Login():
    global nameEL
    global pwordEL # More globals
    global rootA
    rootA = Tk() # This now makes a new window.
    rootA.title('ID CARD GENERATOR') # This makes the window title 'login'
 
    intruction = Label(rootA, text='Please Login to Continue...  \n') # More labels to tell us what they do
    intruction.grid(sticky=E) # Blahdy Blah
 
    nameL = Label(rootA, text='Username: ') # More labels
    pwordL = Label(rootA, text='Password: ') # ^
    nameL.grid(row=1, sticky=W)
    pwordL.grid(row=3, sticky=W)
 
    nameEL = Entry(rootA) # The entry input
    pwordEL = Entry(rootA, show='*') #The password entry input
    nameEL.grid(row=1, column=1)  #Adjusting them to grid
    pwordEL.grid(row=3, column=1)
 
    loginB = Button(rootA, text='Login',bg='white',fg='black' ,command=CheckLogin) # This makes the login button, which will go to the CheckLogin def.
    loginB.grid(columnspan=2, row=9,column=1, sticky=W)   #Adjusting them to the Grid
 
    rmuser = Button(rootA, text='Delete User', fg='red',bg='white', command=DelUser) # This makes the deluser button, go to the deluser def.
    rmuser.grid(columnspan=2,row=13,column=1, sticky=W)
    rootA.geometry('400x350')
    rootA.mainloop()   #Binding the root
def logout():   #logout function
        r.destroy()   #This destroys the current session 
        Login()         #Then Login Page is opened again
def logout():   #logout function
        r.destroy()   #This destroys the current session 
        Login()         #Then Login Page is opened again





def CheckLogin():   #Checker Function to confirm password and username
    global username
    global id_no   #More Globals
    global branch
    global program
    global year
    global month
    global day
    global r
    global filename
    global c
    with open(creds) as f:
        data = f.readlines() # This takes the entire document we put the info into and puts it into the data variable
        uname = data[0].rstrip() # Data[0], 0 is the first line, 1 is the second and so on.
        pword = data[1].rstrip() # Using .rstrip() will remove the \n (new line) word from before when we input it
        c='white'
    if nameEL.get() == uname and pwordEL.get() == pword: # Checks to see if you entered the correct data.
        rootA.destroy()    #Destroys the Login window
        r = Tk() # Opens new window
        r.title('ID CARD GENERATOR')
        r.geometry('500x500') # Makes the window a certain size
        r.configure(bg=c)
        username = Label(r, text='\n NAME ',bg=c).grid(row=2, sticky=W)
        username=StringVar(r)
        text = Entry(r,textvariable=username).grid(row=2, column=2, sticky=W)#Labels defined for Various details of user

        id1l = Label(r, text='\n  ID',bg=c).grid(row=4, sticky=W)
        id_no=StringVar(r)
        id1 = Entry(r,textvariable=id_no).grid(row=4, column=2, sticky=W)

        htl = Label(r, text='\n BRANCH',bg=c).grid(row=6, sticky=W)
        branch = StringVar(r) #Making a ComboBox for Stream
        branch.set("CSE") # initial value
        option = OptionMenu(r, branch, "CSE", "ECE")  #Giving Options for stream
        option.grid(row=6, column=2, sticky=W)#ht = Entry(r)

        startl = Label(r, text='\nPROGRAM',bg=c).grid(row=8, sticky=W)
        program= StringVar(r)  #Making a ComboBox for Program
        program.set("B.tech")
        startoption = OptionMenu(r ,program, "B.tech", "M.Tech")  #Giving Options for Program
        startoption.grid(row=8, column=2, sticky=W)

        
        mnl = Label(r, text='\n DOB',bg=c).grid(row=10, sticky=W)
        day = StringVar(r)  #Making a ComboBox for Date
        day.set("01")
        op=OptionMenu(r ,day, "01", "02","03","04", "05","06","07", "08","09","10", "11","12","13", "14","15","16", "17","18","19", "20","21","22", "23","24","25", "26","27","28", "29","30","31")
        op.grid(row=10, column=2, sticky=W)

        month = StringVar(r)  #Making a ComboBox for Month
        month.set("01")
        op1=OptionMenu(r ,month, "01", "02","03","04", "05","06","07", "08","09","10", "11","12")
        op1.grid(row=10, column=3, sticky=W)

        year = StringVar(r)   #Making a ComboBox for Years
        year.set("1995")
        op2=OptionMenu(r ,year, "1995", "1996","1997","1998", "1999","2000","2001", "2002","2003","2004", "2005","2006","2007", "2008")
        op2.grid(row=10, column=4, sticky=W)
        
        
        photo=Label(r,text='\n PHOTO',bg=c).grid(row=12, sticky=W)
        photo =Button(r, text='browse',bg='white',fg='black' ,command=browse_file).grid(row=12, column=2, sticky=W) # This makes the login button, which will go to the CheckLogin def
        submit = Button(r, text='SUBMIT DETAILS',fg='black' ,command=generate).grid(row=24, sticky=W)#,command=generate) # This makes the login button, which will go to the CheckLogin def.
        logou = Button(r, text='logout', fg='red',bg='white', command=logout).grid(row=1,column=10,sticky=W) # This makes the deluser button. blah go to the deluser def.
        r.mainloop()
    else:
        r = Tk()       #Showing the Error Message Box For Invalid Login
        r.title('D:')
        r.geometry('150x50')
        rlbl = Label(r, text='\nInvalid Login',by=cyan)
        rlbl.pack()
        r.configure(background='cyan')
        r.mainloop()





def browse_file():   #This is the Function defined for Searching the user Pics
        global fname
        fname = filedialog.askopenfilename(parent=r, initialdir= "/", title='Please select a directory')
        img = ImageTk.PhotoImage(Image.open(fname).resize((100,100), Image.ANTIALIAS))#Displaying it
        imglabel = Label(r, image=img)
        imglabel.grid(row=30, column=7,sticky=W)
        print (fname)
        

        




def generate():#Making the Generating Function to make the Final ID Card
    global username
    global c
    username=username.get()
    global id_no
    id_no=id_no.get()    #Input the ID
    global branch
    branch=branch.get()   #Input the Branch
    global program
    program=program.get()  #Input the Stream
    global day
    day=day.get()  #Input the Date
    global month
    month=month.get()
    global year
    year=year.get()
    l = []
    l.append(day)  #Appending the day,month and year to one single string
    l.append('-')
    l.append(month)
    l.append('-')
    l.append(year)               
    mn = ''.join(l)
    #Joining them with '-' sign
    global fname
    global r
    messagebox.askyesno("YOUR INFO","\nNAME\t" +username+ "\nID\t"+id_no+"\nBRANCH\t"+branch+"\nprogram\t"+program+"\nDOB\t"+mn)  #Asking the user for confirmation of details
    if messagebox.askyesno()==True:
            bg = Image.open('bg.jpg')   #Taking the background Image from our folder
            #font1 = ImageFont.truetype("C:\Windows\Fonts\Comic Sans MS\comic.ttf", 36)  #Setting the font for Headings
            #font = ImageFont.truetype("", 30)   #Setting the font for Text Fields
            user=Image.open(fname) #Open the browsed image
            user = user.resize((300,400), Image.ANTIALIAS)   #Resize the image before Applying
            user_w,user_h=user.size  #Setting the size of images
            bg_w,bg_h=bg.size
            offset=(450,210)
            bg.paste(user,offset)
            draw = ImageDraw.Draw(bg)   #Drawing the Image on Our Background
            draw.text((380,120), "ABC INSTITUTE OF  TECHNOLOGY", fill=(0,0,0))  #Appending the strings to the id card image
            draw = ImageDraw.Draw(bg)
            draw.text((1100,205), username, fill=(0,0,0))  #Setting Username
            draw = ImageDraw.Draw(bg)
            draw.text((1050,270), id_no, fill=(0,0,0))   #Setting ID
            draw = ImageDraw.Draw(bg)
            draw.text((1100,332), branch, fill=(0,0,0))       #Setting the program
            draw = ImageDraw.Draw(bg)
            draw.text((1150,407),program, fill=(0,0,0))     #Setting Stream
            draw = ImageDraw.Draw(bg)
            draw.text((1100,468),mn, fill=(0,0,0))  #Setting the DOB
            draw = ImageDraw.Draw(bg)   #Setting the Users Image over our Background
            import pyqrcode    #Importing the Library For a Qr Code Generation
            url = pyqrcode.create('ID CARD GENERATOR\n'+username+'\n'+id_no+'\n'+branch+'\n'+program+'\n'+'\nDEVLOPED BY UTKARSH AND AYUSH')     #Iserting the Encoded Details in the QR COde
            url.png('code.png')  #Generating the QR Code Image
            qr=Image.open('code.png')  
            qr = qr.resize((200,200), Image.ANTIALIAS) #Resizing the QR Code To fit In the ID Card
            offset1=(1000,520)
            bg.paste(qr,offset1)
            draw = ImageDraw.Draw(bg)  #Appending the QR code to ID Card
            bg.save(username+'.png')  #And saving the Generated ID Card as PNG Format with users name
            pdf()      # Saving the users data in PDF Format 
    else:
            r.destroy()  #Destroying the Windoow
            Login()  #Calling Login Widnow Again
            from gridfs import GridFS  #Inserting the data to Mongo Db database
            fs = GridFS(mydb)
            data=open('user2.jpg',"rb") #Sending the Image as an Object to MONGODB
            thedata=data.read()
            avatar_id = fs.put(thedata, filename="inmongoimage")

           # print add_client(username,id_no,branch,program,mn,photo)  #Calling the ADD Client Function to send data to Monogo DB
           
        



def pdf():  #This is the PDF generation Function
    r.destroy()
    global p
    global c
    p= Tk()
    p.title('PDF GENERATOR')  #Now the image will be converted to a PDF Format
    p.geometry('1000x400')
    p.configure(bg=c)
    pl = Label(p, text='\nDO YOU LIKE TO PRINT ITS PDF ALSO\n',bg=c)  #Setting the Label for user to confirm printing the PDF
    pl.grid(row=1,  column=2, sticky=W)
    submit= Button(p, text='YES',command=generatepdf) # This makes the login button, which will go to the CheckLogin def.
    submit.grid(row=7, sticky=W)
    print (username)
    img = ImageTk.PhotoImage(Image.open(username+".png").resize((500,200), Image.ANTIALIAS))#Displaying it
    imglabel = Label(p, image=img).grid(row=30, column=8)
    p.mainloop()
def generatepdf():  #Generation of PDF Function
    p.destroy()
    im = PIL.Image.open(username+".png") #Opening the id Card Image
    #newfilename = 'r.pdf'
    PIL.Image.Image.save(im, username+".pdf", "PDF", resoultion=100.0) #Converting it to PDF
    tkinter.messagebox.showinfo("PDF GENERATE","YOUR ID CARD IN PDF FORMAT IS SUCCESSFULLY GENERATED BY YOUR "+username+".pdf")
    print ("THANK YOU FOR USING OUR SERVICES")
    #tkMessageBox.showinfo("DISCLAIMER","\nTHIS ID CARD IS ONLY FOR DEMO PURPOSE THIS HAS NO AUTHENTICATION WITH ANY OF THE INSTITUTE SO PLEASE DO NOT USE IT ANYWHERE\n")









def DelUser():
    os.remove(creds) # Removes the file
    rootA.destroy() # Destroys the login window
    Signup() # And goes back to the start!





if os.path.isfile(creds):
    Login()
else:     # This if else statement checks to see if the file exists. If it does it will go to Login, if not it will go to Signup :)
    Signup()
