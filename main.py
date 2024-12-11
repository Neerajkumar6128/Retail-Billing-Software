from tkinter import *
from tkinter import messagebox
import random,os,tempfile
#function part
def clear():
    bathsoapEntry.delete(0,END)
    facecreamEntry.delete(0,END)
    facewashEntry.delete(0,END)
    hairserumEntry.delete(0,END)
    bodylotionEntry.delete(0,END)

    riceEntry.delete(0,END)
    oilEntry.delete(0,END)
    daalEntry.delete(0,END)
    sugarEntry.delete(0,END)
    teaEntry.delete(0,END)

    mangoEntry.delete(0,END)
    kiwiEntry.delete(0,END)
    bananaEntry.delete(0,END)
    pineappleEntry.delete(0,END)
    orangeEntry.delete(0,END)

    bathsoapEntry.insert(0,0)
    facecreamEntry.insert(0,0)
    facewashEntry.insert(0,0)
    hairserumEntry.insert(0,0)
    bodylotionEntry.insert(0,0)

    riceEntry.insert(0,0)
    oilEntry.insert(0,0)
    daalEntry.insert(0,0)
    sugarEntry.insert(0,0)
    teaEntry.insert(0,0)

    mangoEntry.insert(0,0)
    kiwiEntry.insert(0,0)
    bananaEntry.insert(0,0)
    pineappleEntry.insert(0,0)
    orangeEntry.insert(0,0)
    #######
    cosmeticspriceEntry.delete(0,END)
    grocerypriceEntry.delete(0,END)
    fruitspriceEntry.delete(0,END)

    cosmeticstaxEntry.delete(0,END)
    grocerytaxEntry.delete(0,END)
    fruitsTaxEntry.delete(0,END)

    nameEntry.delete(0,END)
    phoneEntry.delete(0,END)
    billnumberEntry.delete(0,END)
    textarea.delete(1.0,END)

def print_bill():
    if textarea.get(1.0,END)=='\n':
        messagebox.showerror('Error','Bill is Empty')
    else:
        file=tempfile.mktemp('.txt')
        open(file,'w').write(textarea.get(1.0,END))
        os.startfile(file,'print')

def search_bill():
    for i in os.listdir('bills/'):
        if i.split('.')[0]==billnumberEntry.get():
            f=open(f'bills/{i}','r')
            textarea.delete(1.0,END)
            for data in f:
                textarea.insert(END,data)
            f.close()
            break
    else:
        messagebox.showerror('Error','Invalid Bill Number')        
def total():
    global soapprice,facecreamprice,facewashprice,hairserumprice,bodaylotionprice
    global riceprice,oilprice,daalprice,sugarprice,teaprice
    global mangoprice,kiwiprice,bananaprice,pineappleprice,orangeprice
    global totalbill
    soapprice=int(bathsoapEntry.get())*45
    facecreamprice=int(facecreamEntry.get())*80
    facewashprice=int(facewashEntry.get())*100
    hairserumprice=int(hairserumEntry.get())*145
    bodaylotionprice=int(bodylotionEntry.get())*290
    totalcoemeticsprice=soapprice+facecreamprice+facewashprice+hairserumprice+bodaylotionprice
    cosmeticspriceEntry.delete(0,END)
    cosmeticspriceEntry.insert(0,f'{totalcoemeticsprice}Rs')
    cosmeticstax=totalcoemeticsprice* 0.20
    cosmeticstaxEntry.delete(0,END)
    cosmeticstaxEntry.insert(0,f'{cosmeticstax}Rs')
    ####
    riceprice=int(riceEntry.get())*50
    oilprice=int(oilEntry.get())*170
    daalprice=int(daalEntry.get())*120
    sugarprice=int(sugarEntry.get())*55
    teaprice=int(teaEntry.get())*65
    totalgroceryprice=riceprice+oilprice+daalprice+sugarprice+teaprice
    grocerypriceEntry.delete(0,END)
    grocerypriceEntry.insert(0,f'{totalgroceryprice}Rs')
    grocerytax=totalgroceryprice*0.11
    grocerytaxEntry.delete(0,END)
    grocerytaxEntry.insert(0,str(grocerytax)+'Rs')
    #####
    mangoprice=int(mangoEntry.get())*80
    kiwiprice=int(kiwiEntry.get())*100
    bananaprice=int(bananaEntry.get())*60
    pineappleprice=int(pineappleEntry.get())*125
    orangeprice=int(orangeEntry.get())*75
    totalfruitsprice=mangoprice+kiwiprice+pineappleprice+orangeprice+bananaprice
    fruitspriceEntry.delete(0,END)
    fruitspriceEntry.insert(0,f'{totalfruitsprice}Rs')
    fruitstax=totalfruitsprice* 0.12
    fruitsTaxEntry.delete(0,END)
    fruitsTaxEntry.insert(0,f'{fruitstax}Rs')
    totalbill=totalcoemeticsprice+totalgroceryprice+totalfruitsprice+cosmeticstax+grocerytax+fruitstax
########
if not os.path.exists('bills'):
    os.mkdir('bills')
def save_bill():
    global billnumber
    result=messagebox.askyesno('Confirm','Do you want to save the bill?')
    if result:
        bill_content=textarea.get(1.0,END)
        file=open(f'bills/{billnumber}.txt','w')
        file.write(bill_content)
        file.close()
        messagebox.showinfo('Success',f'Bill Number {billnumber} is saved Successfully')
        billnumber=random.randint(500,1000)
billnumber=random.randint(500,1000)
def bill_area():
    textarea.delete(1.0,END)
    if nameEntry.get()=='' or phoneEntry.get()=='':
        messagebox.showerror('Error','Customer Details Are Required')
    elif cosmeticspriceEntry.get()=='' and grocerypriceEntry.get()=='' and fruitspriceEntry.get()=='':
        messagebox.showerror('Error','No Products Are Selected')   
    elif cosmeticspriceEntry.get()=='0Rs' and grocerypriceEntry.get()=='0Rs' and fruitspriceEntry.get()=='0Rs':
        messagebox.showerror('Error','No Products Are Selected')
    else:
        textarea.insert(END,'\t\t**WELLCOME CUSTOMER**')
        textarea.insert(END,f'\nBill Number:{billnumber}')
        textarea.insert(END,f'\nCustomer Name:{nameEntry.get()}')
        textarea.insert(END,f'\nCustomer Phone Number:{phoneEntry.get()}')
        textarea.insert(END,'\n===========================================================================')
        textarea.insert(END,'\nProduct\t\t\tQuantity\t\t\tPrices')
        textarea.insert(END,'\n===========================================================================')
        if bathsoapEntry.get()!='0':
            textarea.insert(END,f'\nBathSoap \t\t\t{bathsoapEntry.get()}\t\t\t{soapprice}Rs')
        if facecreamEntry.get()!='0':    
            textarea.insert(END,f'\nFaceCream \t\t\t{facecreamEntry.get()}\t\t\t{facecreamprice}Rs')
        if facewashEntry.get()!='0':
            textarea.insert(END,f'\nFaceWash \t\t\t{facewashEntry.get()}\t\t\t{facewashprice}Rs')
        if hairserumEntry.get()!='0':
            textarea.insert(END,f'\nHairSerum \t\t\t{hairserumEntry.get()}\t\t\t{hairserumprice}Rs')
        if bodylotionEntry.get()!='0':    
            textarea.insert(END,f'\nBodyLotion \t\t\t{bodylotionEntry.get()}\t\t\t{bodaylotionprice}Rs')
        if riceEntry.get()!='0':    
            textarea.insert(END,f'\nRice \t\t\t{riceEntry.get()}\t\t\t{riceprice}Rs')
        if oilEntry.get()!='0':    
            textarea.insert(END,f'\nOil \t\t\t{oilEntry.get()}\t\t\t{oilprice}Rs')
        if daalEntry.get()!='0':    
            textarea.insert(END,f'\nDaal \t\t\t{daalEntry.get()}\t\t\t{daalprice}Rs')
        if sugarEntry.get()!='0':    
            textarea.insert(END,f'\nSugar \t\t\t{sugarEntry.get()}\t\t\t{sugarprice}Rs') 
        if teaEntry.get()!='0':    
            textarea.insert(END,f'\nTea \t\t\t{teaEntry.get()}\t\t\t{teaprice}Rs')
        if mangoEntry.get()!='0':    
            textarea.insert(END,f'\nMango \t\t\t{mangoEntry.get()}\t\t\t{mangoprice}Rs')
        if kiwiEntry.get()!='0':    
            textarea.insert(END,f'\nKiwi \t\t\t{kiwiEntry.get()}\t\t\t{kiwiprice}Rs')    
        if bananaEntry.get()!='0':    
            textarea.insert(END,f'\nBanana \t\t\t{bananaEntry.get()}\t\t\t{bananaprice}Rs')
        if pineappleEntry.get()!='0':    
            textarea.insert(END,f'\nPineapple \t\t\t{pineappleEntry.get()}\t\t\t{pineappleprice}Rs')   
        if orangeEntry.get()!='0':    
            textarea.insert(END,f'\nOrange \t\t\t{orangeEntry.get()}\t\t\t{orangeprice}Rs')
        textarea.insert(END,'\n---------------------------------------------------------------------------')
        if cosmeticstaxEntry.get()!='0.0Rs':
            textarea.insert(END,f'\nCosmetic Tax\t\t\t\t{cosmeticstaxEntry.get()}')
        if grocerytaxEntry.get()!='0.0Rs':
            textarea.insert(END,f'\nGrocery Tax\t\t\t\t{grocerytaxEntry.get()}')
        if fruitsTaxEntry.get()!='0.0Rs':
            textarea.insert(END,f'\nFruits Tax\t\t\t\t{fruitsTaxEntry.get()}')
        textarea.insert(END,f'\n\nTotal Bill\t\t\t\t{totalbill}')   
        textarea.insert(END,'\n---------------------------------------------------------------------------') 
        save_bill()
#GUI Based
root=Tk()
root.title('Retail Billing Software')
root.geometry('1270x685')
root.iconbitmap('icon.ico')
headingLabel=Label(root,text='Retail Billing Software',font=('times new roman ',30,'bold'),bg='lightblue1',fg='black',bd=12,relief=GROOVE)
headingLabel.pack(fill=X,pady=10)
##########
customer_details_frame=LabelFrame(root,text='Customer Details ',font=('times new roman ',15,'bold'),bg='lightblue',fg='black',bd=8,relief=GROOVE)
customer_details_frame.pack(fill=X)
################
nameLabel=Label(customer_details_frame,text='Name',font=('times new roman ',15,'bold'),bg='lightblue',fg='black')
nameLabel.grid(row=0,column=0,padx=20,pady=2)
nameEntry=Entry(customer_details_frame,font=('arial',15) ,bd=7,width=18)
nameEntry.grid(row=0,column=1,padx=8)
###########
phoneLabel=Label(customer_details_frame,text='Phone Number',font=('times new roman ',15,'bold'),bg='lightblue',fg='black')
phoneLabel.grid(row=0,column=2,padx=20,pady=2)
phoneEntry=Entry(customer_details_frame,font=('arial',15) ,bd=7,width=18)
phoneEntry.grid(row=0,column=3,padx=8)
##########
billnumberLabel=Label(customer_details_frame,text='BillNumber',font=('times new roman ',15,'bold'),bg='lightblue',fg='black')
billnumberLabel.grid(row=0,column=4,padx=20,pady=2)
billnumberEntry=Entry(customer_details_frame,font=('arial',15) ,bd=7,width=18)
billnumberEntry.grid(row=0,column=5,padx=8)
#########
searchButton=Button(customer_details_frame,text='SEARCH',font=('arial',12,'bold'),bd=7,width=10,command=search_bill)
searchButton.grid(row=0,column=6,padx=10,pady=8)
#########
productFrame=Frame(root)
productFrame.pack(pady=10,fill=X)
cosmeticsFrame=LabelFrame(productFrame,text='Cosmetics ',font=('times new roman ',15,'bold'),bg='lightblue',fg='black',bd=8,relief=GROOVE)
cosmeticsFrame.grid(row=0,column=0)
######
bathsoapLabel=Label(cosmeticsFrame,text='BathSoap',font=('times new roman ',15,'bold'),bg='lightblue',fg='black')
bathsoapLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')
bathsoapEntry=Entry(cosmeticsFrame,font=('times new roman ',15,'bold'),width=10,bd=5)
bathsoapEntry.grid(row=0,column=1,pady=9,padx=10)
bathsoapEntry.insert(0,0)
#####
facecreamLabel=Label(cosmeticsFrame,text='FaceCream',font=('times new roman ',15,'bold'),bg='lightblue',fg='black')
facecreamLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')
facecreamEntry=Entry(cosmeticsFrame,font=('times new roman ',15,'bold'),width=10,bd=5)
facecreamEntry.grid(row=1,column=1,pady=9,padx=10)
facecreamEntry.insert(0,0)
#####
facewashLabel=Label(cosmeticsFrame,text='FaceWash',font=('times new roman ',15,'bold'),bg='lightblue',fg='black')
facewashLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')
facewashEntry=Entry(cosmeticsFrame,font=('times new roman ',15,'bold'),width=10,bd=5)
facewashEntry.grid(row=2,column=1,pady=9,padx=10)
facewashEntry.insert(0,0)
######
hairserumLabel=Label(cosmeticsFrame,text='HairSerum',font=('times new roman ',15,'bold'),bg='lightblue',fg='black')
hairserumLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')
hairserumEntry=Entry(cosmeticsFrame,font=('times new roman ',15,'bold'),width=10,bd=5)
hairserumEntry.grid(row=3,column=1,pady=9,padx=10)
hairserumEntry.insert(0,0)
######
bodylotionLabel=Label(cosmeticsFrame,text='BodyLotion',font=('times new roman ',15,'bold'),bg='lightblue',fg='black')
bodylotionLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')
bodylotionEntry=Entry(cosmeticsFrame,font=('times new roman ',15,'bold'),width=10,bd=5)
bodylotionEntry.grid(row=4,column=1,pady=9,padx=10)
bodylotionEntry.insert(0,0)
######
groceryFrame=LabelFrame(productFrame,text='Grocery ',font=('times new roman ',15,'bold'),bg='lightblue',fg='black',bd=8,relief=GROOVE)
groceryFrame.grid(row=0,column=1)
#######
riceLabel=Label(groceryFrame,text='Rice',font=('times new roman ',15,'bold'),bg='lightblue',fg='black')
riceLabel.grid(row=0,column=1,pady=9,padx=10,sticky='w')
riceEntry=Entry(groceryFrame,font=('times new roman ',15,'bold'),width=10,bd=5)
riceEntry.grid(row=0,column=2,pady=9,padx=10)
riceEntry.insert(0,0)
########
oilLabel=Label(groceryFrame,text='Oil',font=('times new roman ',15,'bold'),bg='lightblue',fg='black')
oilLabel.grid(row=1,column=1,pady=9,padx=10,sticky='w')
oilEntry=Entry(groceryFrame,font=('times new roman ',15,'bold'),width=10,bd=5)
oilEntry.grid(row=1,column=2,pady=9,padx=10)
oilEntry.insert(0,0)
##########
daalLabel=Label(groceryFrame,text='Daal',font=('times new roman ',15,'bold'),bg='lightblue',fg='black')
daalLabel.grid(row=2,column=1,pady=9,padx=10,sticky='w')
daalEntry=Entry(groceryFrame,font=('times new roman ',15,'bold'),width=10,bd=5)
daalEntry.grid(row=2,column=2,pady=9,padx=10)
daalEntry.insert(0,0)
###########
sugarLabel=Label(groceryFrame,text='Sugar',font=('times new roman ',15,'bold'),bg='lightblue',fg='black')
sugarLabel.grid(row=3,column=1,pady=9,padx=10,sticky='w')
sugarEntry=Entry(groceryFrame,font=('times new roman ',15,'bold'),width=10,bd=5)
sugarEntry.grid(row=3,column=2,pady=9,padx=10)
sugarEntry.insert(0,0)
##########
teaLabel=Label(groceryFrame,text='Tea',font=('times new roman ',15,'bold'),bg='lightblue',fg='black')
teaLabel.grid(row=4,column=1,pady=9,padx=10,sticky='w')
teaEntry=Entry(groceryFrame,font=('times new roman ',15,'bold'),width=10,bd=5)
teaEntry.grid(row=4,column=2,pady=9,padx=10)
teaEntry.insert(0,0)
##########
fruitsFrame=LabelFrame(productFrame,text='Fruits ',font=('times new roman ',15,'bold'),bg='lightblue',fg='black',bd=8,relief=GROOVE)
fruitsFrame.grid(row=0,column=2)
################
mangoLabel=Label(fruitsFrame,text='Mango',font=('times new roman ',15,'bold'),bg='lightblue',fg='black')
mangoLabel.grid(row=0,column=2,pady=9,padx=10,sticky='w')
mangoEntry=Entry(fruitsFrame,font=('times new roman ',15,'bold'),width=10,bd=5)
mangoEntry.grid(row=0,column=3,pady=9,padx=10)
mangoEntry.insert(0,0)
#########
kiwiLabel=Label(fruitsFrame,text='Kiwi',font=('times new roman ',15,'bold'),bg='lightblue',fg='black')
kiwiLabel.grid(row=1,column=2,pady=9,padx=10,sticky='w')
kiwiEntry=Entry(fruitsFrame,font=('times new roman ',15,'bold'),width=10,bd=5)
kiwiEntry.grid(row=1,column=3,pady=9,padx=10)
kiwiEntry.insert(0,0)
######
bananaLabel=Label(fruitsFrame,text='Banana',font=('times new roman ',15,'bold'),bg='lightblue',fg='black')
bananaLabel.grid(row=2,column=2,pady=9,padx=10,sticky='w')
bananaEntry=Entry(fruitsFrame,font=('times new roman ',15,'bold'),width=10,bd=5)
bananaEntry.grid(row=2,column=3,pady=9,padx=10)
bananaEntry.insert(0,0)
######
pineappleLabel=Label(fruitsFrame,text='Pineapple',font=('times new roman ',15,'bold'),bg='lightblue',fg='black')
pineappleLabel.grid(row=3,column=2,pady=9,padx=10,sticky='w')
pineappleEntry=Entry(fruitsFrame,font=('times new roman ',15,'bold'),width=10,bd=5)
pineappleEntry.grid(row=3,column=3,pady=9,padx=10)
pineappleEntry.insert(0,0)
#######
orangeLabel=Label(fruitsFrame,text='Orange ',font=('times new roman ',15,'bold'),bg='lightblue',fg='black')
orangeLabel.grid(row=4,column=2,pady=9,padx=10,sticky='w')
orangeEntry=Entry(fruitsFrame,font=('times new roman ',15,'bold'),width=10,bd=5)
orangeEntry.grid(row=4,column=3,pady=9,padx=10)
orangeEntry.insert(0,0)
#########
billframe=Frame(productFrame, bd=8, relief=GROOVE)
billframe.grid(row=0, column=3,padx=10)
billareaLabel=Label(billframe, text='Bill Area', font=('times new roman', 15, 'bold'), bd=7, relief=GROOVE,width=55)
billareaLabel.pack(fill=X)
#######
Scrollbar=Scrollbar(billframe,orient=VERTICAL)
Scrollbar.pack(side=RIGHT,fill=Y)
textarea=Text(billframe,height=18,width=75,yscrollcommand=Scrollbar.set)
textarea.pack()
Scrollbar.config(command=textarea.yview)
#######
billmenuFrame=LabelFrame(root,text='Bill Menu ',font=('times new roman ',15,'bold'),bg='lightblue',fg='black',bd=8,relief=GROOVE)
billmenuFrame.pack(fill=X)
########
cosmeticspriceLabel=Label(billmenuFrame,text='Cosmetics Price',font=('times new roman ',15,'bold'),bg='lightblue',fg='black')
cosmeticspriceLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')
cosmeticspriceEntry=Entry(billmenuFrame,font=('times new roman ',15,'bold'),width=10,bd=5)
cosmeticspriceEntry.grid(row=0,column=1,pady=9,padx=10)
#####
grocerypriceLabel=Label(billmenuFrame,text='Grocery Price',font=('times new roman ',15,'bold'),bg='lightblue',fg='black')
grocerypriceLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')
grocerypriceEntry=Entry(billmenuFrame,font=('times new roman ',15,'bold'),width=10,bd=5)
grocerypriceEntry.grid(row=1,column=1,pady=9,padx=10)
###########
fruitspriceLabel=Label(billmenuFrame,text='Fruits Price',font=('times new roman ',15,'bold'),bg='lightblue',fg='black')
fruitspriceLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')
fruitspriceEntry=Entry(billmenuFrame,font=('times new roman ',15,'bold'),width=10,bd=5)
fruitspriceEntry.grid(row=2,column=1,pady=9,padx=10)
######
cosmeticstaxLabel=Label(billmenuFrame,text='Cosmetics Tax',font=('times new roman ',14,'bold'),bg='lightblue',fg='black')
cosmeticstaxLabel.grid(row=0,column=2,pady=6,padx=10,sticky='w')
cosmeticstaxEntry=Entry(billmenuFrame,font=('times new roman ',14,'bold'),width=10,bd=5)
cosmeticstaxEntry.grid(row=0,column=3,pady=6,padx=10)
######
grocerytaxLabel=Label(billmenuFrame,text='Grocery Tax',font=('times new roman ',14,'bold'),bg='lightblue',fg='black')
grocerytaxLabel.grid(row=1,column=2,pady=6,padx=10,sticky='w')
grocerytaxEntry=Entry(billmenuFrame,font=('times new roman ',14,'bold'),width=10,bd=5)
grocerytaxEntry.grid(row=1,column=3,pady=6,padx=10)
######
fruitsTaxLabel=Label(billmenuFrame,text='Fruits Tax',font=('times new roman ',14,'bold'),bg='lightblue',fg='black')
fruitsTaxLabel.grid(row=2,column=2,pady=6,padx=10,sticky='w')
fruitsTaxEntry=Entry(billmenuFrame,font=('times new roman ',14,'bold'),width=10,bd=5)
fruitsTaxEntry.grid(row=2,column=3,pady=6,padx=10)
######
buttonFrame=Frame(billmenuFrame,bd=8,relief=GROOVE)
buttonFrame.grid(row=0,column=4,rowspan=3)


totalbutton=Button(buttonFrame,text='Total',font=('arial',16,'bold'),bg='lightblue1',fg='black',bd=5,width=8,pady=10,command=total)
totalbutton.grid(row=0,column=0,pady=30,padx=10)
####
billbutton=Button(buttonFrame,text='Bill',font=('arial',16,'bold'),bg='lightblue1',fg='black',bd=5,width=8,pady=10,command=bill_area)
billbutton.grid(row=0,column=1,pady=30,padx=10)
####
printbutton=Button(buttonFrame,text='Print',font=('arial',16,'bold'),bg='lightblue1',fg='black',bd=5,width=8,pady=10,command=print_bill)
printbutton.grid(row=0,column=3,pady=30,padx=10)
#####
clearbutton=Button(buttonFrame,text='Clear',font=('arial',16,'bold'),bg='lightblue1',fg='black',bd=5,width=8,pady=10,command=clear)
clearbutton.grid(row=0,column=4,pady=30,padx=10)
root.mainloop() 