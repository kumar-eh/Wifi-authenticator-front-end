#final


##Importing functions
from tkinter import *
from tkinter.messagebox import *
from tkinter.simpledialog import askstring
import time
##========================================================================================================================================
##def stroke_text(x, y, text, textcolor, strokecolor):
    # make stroke text
##    canvas.create_text(x, y, text=text, font=('courier', 16, 'bold'), fill=strokecolor)
    # make regular text
##    canvas.create_text(x, y, text=text, font=('courier', 16), fill=textcolor)

root = Tk()
root.title("Sudo Authenticator");
##global list for connected list and block list 
global val
global block_list #here you define block list in a array or list
block_list = list()
global connected_list #here you have to define connected list in array or list
connected_list = list()
global x#**
x=1 #**
global counter #**
count=5  #**
global y
y=1000
global connected_user   #THIS  LIST IS FOR ALREADY CONNECTED USERS 
global blocked_user
global connected_list1 ##THIS LIST FOR USERS ENTER USING POPUP WINDOW USE IT PROPERLY ELSE OP WILL NOT COME
connected_list1  =list()
global counter  ##For timer
counter = 15
##========================================================================================================================================

#CODE THE DEAUTH FUNCTION HERE
def deauth_func(connected_user):
    global block_list
    global conected_list
    global connected_list1
    print("Deauthenticated")
    try:
        values1 = connected_user.curselection() #**
        index = values1[0]      #**
        block = connected_user.get(index)
        if block in connected_list:
            connected_list.remove(block)   #FOR DEAUTH FUNCTION REMOVE FROM CONNECTED LIST
            block_list.append(block)      #AND ADD TO BLOCK LIST
        else:
            connected_list1.remove(block)
            block_list.append(block)      #AND ADD TO BLOCK LIST       
        for i in block_list:
            print(i)
        for i in connected_list:     #WRITE YOUR CODE HERE
            connected_user.insert(1,i)   #PRINTING THE BLOCKED USERS HERE
        for i in connected_list1:
            connected_user.insert(1,i)
    except IndexError:
        print(showwarning("Alert" , "Please select a User first"))
    except ValueError:
        print(showwarning("Alert" , "Please select a User first"))        

##========================================================================================================================================

#CODE THE UNBLOCK FUNCTION HERE
def Unblock_user(blocked_user):
    global connected_list    
    global block_list
    try:
        print("Unblocked")
        unblock1 = blocked_user.curselection()   #**
        index = unblock1[0]    #**
        unblock = blocked_user.get(index)    #**
        block_list.remove(unblock)     #REMOVING FROM BLOCK LIST AND
        connected_list.append(unblock)   #ADDING TO CONNECTED LIST
    except ValueError:
        print(showwarning("Alert" , "User already unblocked"))  #EXCEPTION ARISES IF USER TRIES TO REMOVE A USER TWO TIMES
    except IndexError:
        print(showwarning("Alert" , "Please select a user first"))
##========================================================================================================================================
def popup(): ##POPUP FUNCTION
    global connected_user
    global blocked_user
    global connected_list #**
    global connected_list1 #**
    global block_list #**
    window = Toplevel()
    window.geometry("380x100")
    label = Label(window )
    label.config(text = "New User named " + str(y) + " has entered , do you want to accept?")  ##IN STR(Y) PLACE ENTER THE USER OR MAC ADDRESS NAME
    label.pack(fill='x')


    def deny():
        print("Denied")
        block_list.append(y)   ##IF DENIED USER WILL DIRECTLY GO TO BLOCK LIST
        window.destroy()
    def accept():
        print("Accept")
        connected_list1.append(y) ##**********IF ACCEPTED USER WILL DIRECTLY GO TO CONNECTED LIST1 LIST NOT CONNECTED LIST PLEASE USE IT ACCORDINGLY********
        window.destroy()

    def counter_label(label):
        def count():
            global counter
            if(counter > 0):
                counter-=1
                label.config(text=str(counter))
                label.after(1000, count)
            else:
                block_list.append(y)
                window.destroy()
        count()

    label = Label(window, fg="green")
    label.pack()
    counter_label(label)

    button_deny = Button(window, text="Deny", command=lambda :deny())
    button_deny.place(relx = 0.6 , rely = 0.4, relheight = 0.2 , relwidth = 0.2)

    button_accept = Button(window  ,text = "Accept" , command = lambda :accept())
    button_accept.place(relx = 0.2 , rely = 0.4, relheight = 0.2 , relwidth = 0.2)
    
##========================================================================================================================================
#CONNECTED FRAME DISPLAY CODE
def connected(connected_frame):
    global connected_user
    global blocked_user
    print("hello")
    global connected_list
    global connected_list1
    global x
    connected_user = Listbox(connected_frame , bg = "#ffcc66")  #**
    connected_user.place(relx = 0 ,rely = 0, relheight = 1 , relwidth = 0.7)  #**
   
    scrollbar1 = Scrollbar(connected_user , bg = "#66fcf1")  #**
    scrollbar1.pack(side=RIGHT, fill=Y)   #**
    connected_user.config(yscrollcommand = scrollbar1.set)    #**
    scrollbar1.config(command = connected_user.yview)  #**
    if(x<2):            ##STORE THE USERS IN THE ARRAY AND PRINT THEM
        for i in range(145):
            connected_list.append(i)   #WRITE THE CODE HERE TO PRINT THE CONNECTED USERS HERE  (ALREADY CONNECTED USERS)
        for i in connected_list:
            connected_user.insert(1,i) #**
        for i in connected_list1:      ##********FOR USERS WHO CAME THROUGH POPUP USE IT ACCORDINGLY*********
            connected_user.insert(1,i)
        x+=1
    else:
        for i in connected_list:
            connected_user.insert(1,i)  #WRITE THE CODE HERE TO PRINT THE CONNECTED USERS HERE AGAIN
        for i in connected_list1:
            connected_user.insert(1,i)
 


##========================================================================================================================================

    try:
        deauth = Button(connected_frame , text = "BLOCK" , command = lambda:deauth_func(connected_user) ,bg = "#ffcc66")  #**
        deauth.place(relx= 0.73 , rely =0.35 , relwidth = 0.25 , relheight = 0.1)  #**
    except IndexError:
        print(showwarning("Alert" , "Please select a User first"))
    connected_frame.lift()
    

##========================================================================================================================================
#CODE OF BLOCKED USER HERE
def blocked(blocked_frame):
    global connected_user
    global blocked_user
    global block_list
    
    print("hello") 
    blocked_user = Listbox(blocked_frame , bg = "#ffcc66") #**
    blocked_user.place(relx = 0 ,rely = 0, relheight = 1 , relwidth = 0.7)  #**

    scrollbar2 = Scrollbar(blocked_user , bg = "#66fcf1")  #**
    scrollbar2.pack(side=RIGHT, fill=Y)  #** 
    blocked_user.config(yscrollcommand = scrollbar2.set)  #**
    scrollbar2.config(command = blocked_user.yview) #**

    unblock = Button(blocked_frame , text = "UNBLOCK", command = lambda : Unblock_user(blocked_user))   #**
    unblock.place(relx = 0.73 , rely = 0.3 , relwidth = 0.25 , relheight = 0.1)  #**
    print(block_list)
    for i in block_list:
        blocked_user.insert(1,i) ##CODE THE FUNCTION OF PRINTING BLOCKED USERS HERE 
    blocked_frame.lift()
##========================================================================================================================================
#DISPLAYING THE LIST OF NETWORKS FUNCTION
def getSelection(network_list):
    global val
    global connected_list
    connected_list = list()
    try:
        values = network_list.curselection() #**
        index = values[0]   #** 
        val = network_list.get(index) #**

    except IndexError:
        print(showwarning("ALert" , "Please select a network"))

    print(val)
    changing_frame3 = Frame( height = 500 , width= 700 , bg = "#FF0000" ) #**
    changing_frame3.place(relx = 0 , rely = 0.2 , relheight = 0.8 , relwidth = 1)  #**

    monitoring = Label(changing_frame3 , bg= "#ffcc66" ,  font = ("Helvetica" , "16" ,"bold")) #**
    monitoring.place(relx = 0 , rely = 0 , relheight = 0.15 , relwidth = 1) #**
    monitoring.config(text = "Monitoring network  " + str(val)) #**

##========================================================================================================================================
#BLOCKED FRAME GUI CODE
    blocked_frame = Frame(changing_frame3 , bg = "#ffcc66")  #**
    blocked_frame.place(relx = 0 , rely = 0.3 , relheight = 0.7 , relwidth = 1) #**
  
    blocked_users = Button(changing_frame3 , text = "Blocked users" , command = lambda : blocked(blocked_frame)) #**
    blocked_users.place(relx = 0.5 , rely = 0.15 , relheight = 0.15 , relwidth = 0.5) #**

    select_label = Label(changing_frame3 , bg = "#ffcc66" , text = "*Select any one tab*"  ,font = ("Helvetcia" , "14" , "bold")) #**
    select_label.configure(underline = 1)
    select_label.place(relx = 0.3 , rely = 0.1, relwidth = 0.4 , relheight = 0.05)  #**

    
##========================================================================================================================================
#CONNECTED USERS FRAME GUI CODE
    connected_frame = Frame(changing_frame3 , bg = "#ffcc66") #**
    connected_frame.place(relx=0,rely=0.3 , relheight = 0.7 , relwidth = 1)  #**
    
    connected_users = Button(changing_frame3, text = "Connected users" , command = lambda : connected(connected_frame)) #**
    connected_users.place(relx = 0 , rely = 0.15 , relheight= 0.15 , relwidth = 0.5)  #**
    
##========================================================================================================================================
##SECOND PAGE GUI
def changing_frame2():
    a=clicked.get()
    if(a=="--Select--"):
        print(showwarning("Alert" , "Select a valid Interface"))
    
    else:
        print(a)
        changing_frame2 = Frame(first_page ,bg="#111111")
        changing_frame2.place(relx = 0 , rely = 0.2 , relheight = 0.8 , relwidth = 1)
##GRADIENT FRAMES CODE
        gradient_frame6 = Frame(changing_frame2 , bg = "#ffb31a")#ffb31a
        gradient_frame6.place(relx= 0,rely = 0 , relwidth = 1 , relheight = 0.2)

        gradient_frame7 = Frame(changing_frame2 , bg = "#ffbb33")#ffbb33
        gradient_frame7.place(relx= 0,rely = 0.2 , relwidth = 1 , relheight = 0.2)

        gradient_frame8 = Frame(changing_frame2 , bg = "#ffc34d")
        gradient_frame8.place(relx= 0,rely = 0.4 , relwidth = 1 , relheight = 0.2)

        gradient_frame9 = Frame(changing_frame2 , bg = "#ffcc66")#ffcc66
        gradient_frame9.place(relx= 0,rely = 0.6 , relwidth = 1 , relheight = 0.2)

        gradient_frame10 = Frame(changing_frame2 , bg = "#ffd480")#ffd480
        gradient_frame10.place(relx= 0,rely = 0.8 , relwidth = 1 , relheight = 0.2)
        
        available_networks_label = Label(changing_frame2 , text = "Available networks" , bg = "#ffbb33" ,  font = ("Helvetica" , "16" ,"bold"))
        available_networks_label.place(relx = 0.27 , rely = 0.3 , relwidth= 0.4 , relheight = 0.1)

        network_list = Listbox(changing_frame2,  bg = "#ffd480")
        network_list.place(relx = 0.27 , rely = 0.4 , relwidth = 0.4 , relheight = 0.4)
    
        scrollbar = Scrollbar(network_list , bg = "#000428") #**
        scrollbar.pack(side=RIGHT, fill=Y) #**
        network_list.config(yscrollcommand = scrollbar.set) #**
        scrollbar.config(command = network_list.yview) #**

        for i in range(145):
            network_list.insert(1,i)

        
        try:
            scan_network = Button(changing_frame2 , text = "Scan this network" , command = lambda: getSelection(network_list))
            scan_network.place(relx=0.4 , rely = 0.85 , relheight = 0.1 , relwidth = 0.2)
        except:
            print(showwarning("ALert" , "Please select a network")) 
##========================================================================================================================================
clicked = StringVar()
clicked.set("--Select--")
##STARTING PAGE GUI
first_page = Canvas(root, height = 500 , width = 700)
first_page.pack()

Title_frame = Frame(first_page, bg= "#000428")
Title_frame.place(relx=0,rely=0,relwidth=1,relheight=0.2)
#LOGO 
p= PhotoImage(file="LOGO.png" , width = 140 , height = 85)
bglabel=Label(Title_frame, image=p , padx = 0 ,pady =0)
bglabel.place(relx = 0.02 , rely = 0.04 )
#TITLE FRAME
p1= PhotoImage(file="title.png" , width = 540 , height = 25)
Title_label=Label(Title_frame, image=p1 ,bg = "#000428" ,padx = 0 ,pady =0)
Title_label.place(relx= 0.29 , rely = 0.2 , relheight = 0.7 , relwidth = 0.73 )
##Title_label = Label(Title_frame )##, text = "Sudo wifi authenticator" , bg = "#000428" , fg = "#80ffff" , font=("Rockwell",23))
##Title_label.place(relx= 0.33 , rely = 0.2 , relheight = 0.5 , relwidth = 0.4)

##canvas = Canvas(Title_label, bg='#000428')
##canvas.pack()
##stroke_text(105, 30, "Sudo Wi-Fi authenticator", '#80ffff', 'red')


#FIRST PAGE FRAME
changing_frame1 = Frame(first_page, bg= "#d1d1e0")
changing_frame1.place(relx = 0 , rely = 0.2 , relheight = 0.8 , relwidth = 1)
#GRADIENT FRAMES
gradient_frame1 = Frame(changing_frame1 , bg="#ffd480")
gradient_frame1.place(relx=0 , rely = 0 , relheight = 0.2 , relwidth = 1)

gradient_frame2 = Frame(changing_frame1 , bg="#ffcc66")
gradient_frame2.place(relx=0 , rely = 0.2 , relheight = 0.2 , relwidth = 1)

gradient_frame3 = Frame(changing_frame1 , bg="#ffc34d")
gradient_frame3.place(relx=0 , rely = 0.4 , relheight = 0.2 , relwidth = 1)

gradient_frame4 = Frame(changing_frame1 , bg="#ffbb33")
gradient_frame4.place(relx=0 , rely = 0.6 , relheight = 0.2 , relwidth = 1)

gradient_frame5 = Frame(changing_frame1 , bg="#ffb31a")
gradient_frame5.place(relx=0 , rely = 0.8 , relheight = 0.2 , relwidth = 1)

team_name = Label(gradient_frame5 ,text = "Team : Code Sploit" , bg= "#ffb31a" , font = ("Helvetica" , "16" ,"bold"))
team_name.place(relx = 0.15 , rely = 0.1 , relheight = 0.8 , relwidth = 0.7)

select_interface_frame = Frame(changing_frame1 , bg="#ffc34d")
select_interface_frame.place(relx=0.33 , rely= 0.3 , relheight = 0.1 , relwidth =  0.34)

select_interface = OptionMenu(select_interface_frame , clicked , "Tplink121214","2","3")
select_interface.place(relx = 0.03 , rely = 0.08 , relheight = 0.8 , relwidth = 0.6)

interface_label = Label(select_interface_frame , text = "Interface" )
interface_label.place(relx = 0.67 , rely = 0.065 , relheight = 0.8 , relwidth = 0.3)
#SCAN WIFI BUTTON FIRST PAGE
scan_wifibutton = Button(changing_frame1, text = "Scan Wifi" , command = lambda: changing_frame2() , activebackground="#05386B",activeforeground="#80ffff", relief = "raise" )
scan_wifibutton.place(relx  = 0.42 , rely = 0.48 , relwidth = 0.15 , relheight = 0.07)

##Write YOUR CONDITION HERE WHEN THE POPUP SHOULD APPEAR
if(y==1000):
    popup()

root.mainloop()
