from tkinter import *
from mydb import Database
from myapi import Api
from  tkinter import messagebox

class NLPApp:
    def __init__(self):
        
        # Importing the Database class from mydb.py
        self.dbo = Database()
        self.api = Api()
                
        # create root variable that have tkinter class
        self.root = Tk()
        
        # To change the Title of the App
        self.root.title(' NLP App ')
        
        # To change the App Icon.
        self.root.iconbitmap('C:\\Users\\sachi\\OneDrive\\Desktop\\Python\\NLP APP\\Resources\\favicon.ico')
        
        # We can able to set the Gui Size
        self.root.geometry('370x700')
        
        # we change the Color code of background
        self.root.configure(bg= '#3333ff')
        
        # Calling the Login Function
        self.Login()
        
        # it will help to hold the gui.
        self.root.mainloop()
        
        
        
    def Login(self):
        
        # Destory Function
        self.clear()
        
        heading = Label(self.root, text= 'NLP APP')
        heading.pack(pady=(50,80),padx=(40,30))
        heading.configure(font=('Tommy', 28, 'bold'), bg = '#3333ff', fg='White')
        
        # for Email
        
        email_l = Label(self.root, text='Email')
        email_l.pack(padx=(20,212))
        email_l.configure(font=('Times Roman', 20,'bold'),bg='#3333ff',fg='White')
        
        self.email_input = Entry(self.root)
        self.email_input.pack(pady=(5,30),padx=(50,24),ipady=5)
        self.email_input.configure(width=48,border=4)
        
        
        # For password
        password_l = Label(self.root, text='Password')
        password_l.pack(padx=(40,175))
        password_l.configure(font=('Times Roman', 20,'bold'),bg='#3333ff',fg='White')
        
        self.password_input = Entry(self.root,show='*')
        self.password_input.pack(pady=(5,10),padx=(50,24),ipady=5)
        self.password_input.configure(width=48,border=4)
        
        
        # Button
        
        login_button = Button(self.root, text='Login',command=self.perform_login)
        login_button.pack(pady=(20,10))
        login_button.configure(font=('Arial', 18,'bold'), bg='black',fg='White',width=10,height=1)
        
        # Not a Member
        NMB = Label(self.root,text='Not a Member?')
        NMB.pack(pady=(10,10))
        NMB.configure(font=('arial',16,'italic'),bg='#3333ff',fg='White')
        
        register = Button(self.root,text='Register',command= self.register_gui)
        register.pack(pady=(5,10))
        register.configure(font=('arial',18,'bold'),bg='Black',fg='White',width=10,height=1)
        
        
    def register_gui(self):
        # to clear the Gui we use Destroy Function
        self.clear()
        
        heading = Label(self.root, text= 'NLP APP')
        heading.pack(pady=(50,80),padx=(40,30))
        heading.configure(font=('Tommy', 28, 'bold'), bg = '#3333ff', fg='White')
        
        # for Name
        
        Name_l = Label(self.root, text='Name')
        Name_l.pack(padx=(20,212))
        Name_l.configure(font=('Times Roman', 20,'bold'),bg='#3333ff',fg='White')
        
        self.name_input = Entry(self.root)
        self.name_input.pack(pady=(5,30),padx=(50,24),ipady=5)
        self.name_input.configure(width=48,border=4)
        
        # For Email
        
        remail_l = Label(self.root, text='Email')
        remail_l.pack(padx=(20,212))
        remail_l.configure(font=('Times Roman', 20,'bold'),bg='#3333ff',fg='White')
        
        self.remail_input = Entry(self.root)
        self.remail_input.pack(pady=(5,30),padx=(50,24),ipady=5)
        self.remail_input.configure(width=48,border=4)
        
        
        # For password
        r_password_l = Label(self.root, text='Password')
        r_password_l.pack(padx=(40,175))
        r_password_l.configure(font=('Times Roman', 20,'bold'),bg='#3333ff',fg='White')
        
        self.r_password_input = Entry(self.root,show='*')
        self.r_password_input.pack(pady=(5,10),padx=(50,24),ipady=5)
        self.r_password_input.configure(width=48,border=4)
        
        
        # Button
        
        r_login_button = Button(self.root, text='Register', command= self.perform_registration)
        r_login_button.pack(pady=(20,10))
        r_login_button.configure(font=('Arial', 18,'bold'), bg='black',fg='White',width=10,height=1)
        
        # Not a Member
        AMB = Label(self.root,text='Already a Member?')
        AMB.pack(pady=(10,10))
        AMB.configure(font=('arial',16,'italic'),bg='#3333ff',fg='White')
        
        loginA = Button(self.root,text='Login Again', command= self.Login)
        loginA.pack(pady=(5,10))
        loginA.configure(font=('arial',18,'bold'),bg='Black',fg='White',width=10,height=1)
        
    
    # This can we make as utility function
    def clear(self):
        # to clear the Gui we use Destroy Function
        for i in self.root.pack_slaves():
            i.destroy()
        
    def perform_registration(self):
        name = self.name_input.get()
        email = self.remail_input.get()
        password = self.r_password_input.get()
        
        # this function is used store the database
        response = self.dbo.add_data(name,email,password)
        
        if response:
            messagebox.showinfo('Success', 'Registration Successful. \nLogin Now')
        else:
            messagebox.showinfo('Error', 'User Already Exist')
    
    
    def perform_login(self):
        email = self.email_input.get()
        password = self.password_input.get()
        
        
        # Verification result from Database file i.e. mydb.py
        responses = self.dbo.search(email,password)
        if responses:
            messagebox.showinfo('Success', 'Login Successful')
            self.home_gui()
            
        else:
            messagebox.showinfo('Error', 'Invalid Email/Password')
    
    def home_gui(self):
        self.clear()
        
        # This is home Gui
        heading = Label(self.root, text= 'NLP APP')
        heading.pack(pady=(50,80),padx=(40,30))
        heading.configure(font=('Tommy', 28, 'bold'), bg = '#3333ff', fg='White')
        
        Sentiment_button = Button(self.root,text='Sentiment Analysis', command=self.sentiment_Gui)
        Sentiment_button.pack(pady=(5,20))
        Sentiment_button.configure(font=('arial',18,'bold'),bg='Black',fg='White',width=20,height=1)
        
        ner_button = Button(self.root,text='Name Entity Recognition',command= self.ner_Gui)
        ner_button.pack(pady=(5,20))
        ner_button.configure(font=('arial',18,'bold'),bg='Black',fg='White',width=20,height=1)

        emotion_button = Button(self.root,text='Emotion Prediction',command=self.emotion_Gui)
        emotion_button.pack(pady=(5,20))
        emotion_button.configure(font=('arial',18,'bold'),bg='Black',fg='White',width=20,height=1)
        
        
        Logout_home = Button(self.root,text='Logout',command=self.Login)
        Logout_home.pack(pady=(25,10))
        Logout_home.configure(font=('arial',18,'bold'),bg='Black',fg='White',width=10,height=1)
        
    def sentiment_Gui(self):
        self.clear()
        
        Back_home = Button(self.root,text='Back',command=self.home_gui)
        Back_home.pack(pady=(5,0),padx=(0,275))
        Back_home.configure(font=('arial',14,'bold'),bg='Black',fg='White',width=5,height=1)
        
        
        heading = Label(self.root, text= 'NLP APP')
        heading.pack(pady=(30,20),padx=(40,30))
        heading.configure(font=('Tommy', 28, 'bold'), bg = '#3333ff', fg='White')
        
        heading2 = Label(self.root, text= 'Sentimental Analysis')
        heading2.pack(pady=(20,50),padx=(20,20))
        heading2.configure(font=('Tommy', 20), bg = '#3333ff', fg='White')
        
        user_label = Label(self.root, text='Enter the Text')
        user_label.pack(padx=(35,170))
        user_label.configure(font=('Times Roman', 16),bg='#3333ff',fg='White')
        
        self.sentiment_input = Entry(self.root)
        self.sentiment_input.pack(pady=(15,10),padx=(50,24),ipady=10)
        self.sentiment_input.configure(width=48,border=4)
        
        sentimental_btn = Button(self.root,text='Analyze', command=self.output_sentiment)
        sentimental_btn.pack(pady=(20,10))
        sentimental_btn.configure(font=('arial',18,'bold'),bg='Black',fg='White',width=8,height=1)
        
        self.Result_label = Label(self.root, text='' )
        self.Result_label.pack(padx=(0,0))
        self.Result_label.configure(font=('Times Roman', 16),bg='#3333ff',fg='White')
        
    def output_sentiment(self):
        text = self.sentiment_input.get()
        
        response1 = self.api.sentiment(text)
        txt = ''
        
        for i in response1['sentiment']:
            txt = txt + i + ' --> ' + str(response1['sentiment'][i]) + ' \n '
        
        self.Result_label['text'] = txt
        print(text)
        print(txt)

        
    def ner_Gui(self):
        self.clear()
        
        Back_home = Button(self.root,text='Back',command=self.home_gui)
        Back_home.pack(pady=(5,0),padx=(0,275))
        Back_home.configure(font=('arial',14,'bold'),bg='Black',fg='White',width=5,height=1)
        
        
        heading = Label(self.root, text= 'NLP APP')
        heading.pack(pady=(30,20),padx=(40,30))
        heading.configure(font=('Tommy', 28, 'bold'), bg = '#3333ff', fg='White')
        
        heading2 = Label(self.root, text= 'Name Entity Recognition')
        heading2.pack(pady=(20,50),padx=(20,20))
        heading2.configure(font=('Tommy', 20), bg = '#3333ff', fg='White')
        
        user_label = Label(self.root, text='Enter the Text')
        user_label.pack(padx=(35,170))
        user_label.configure(font=('Times Roman', 16),bg='#3333ff',fg='White')
        
        self.ner_input = Entry(self.root)
        self.ner_input.pack(pady=(15,10),padx=(50,24),ipady=10)
        self.ner_input.configure(width=48,border=4)
        
        ner_btn = Button(self.root,text='Recognize', command= self.output_ner)
        ner_btn.pack(pady=(20,10))
        ner_btn.configure(font=('arial',18,'bold'),bg='Black',fg='White',width=8,height=1)
        
        self.Result_label = Label(self.root, text='')
        self.Result_label.pack(padx=(35,170))
        self.Result_label.configure(font=('Times Roman', 16),bg='#3333ff',fg='White')
        
    def output_ner(self):
        text = self.ner_input.get()
        response = self.api.ner(text)
        print(response)
        
        
        
    def emotion_Gui(self):
        self.clear()
        
        
        Back_home = Button(self.root,text='Back',command=self.home_gui)
        Back_home.pack(pady=(5,0),padx=(0,275))
        Back_home.configure(font=('arial',14,'bold'),bg='Black',fg='White',width=5,height=1)
        
        
        heading = Label(self.root, text= 'NLP APP')
        heading.pack(pady=(30,20),padx=(40,30))
        heading.configure(font=('Tommy', 28, 'bold'), bg = '#3333ff', fg='White')
        
        heading2 = Label(self.root, text= 'Emotion Prediction')
        heading2.pack(pady=(20,50),padx=(20,20))
        heading2.configure(font=('Tommy', 20), bg = '#3333ff', fg='White')
        
        user_label = Label(self.root, text='Enter the Text')
        user_label.pack(padx=(35,170))
        user_label.configure(font=('Times Roman', 16),bg='#3333ff',fg='White')
        
        self.emotion_input = Entry(self.root)
        self.emotion_input.pack(pady=(15,10),padx=(50,24),ipady=10)
        self.emotion_input.configure(width=48,border=4)
        
        emotion_btn = Button(self.root,text='Predict', command= self.output_emotion)
        emotion_btn.pack(pady=(20,10))
        emotion_btn.configure(font=('arial',18,'bold'),bg='Black',fg='White',width=8,height=1)
        
        
        self.Result_label = Label(self.root, text='')
        self.Result_label.pack(padx=(35,170))
        self.Result_label.configure(font=('Times Roman', 16),bg='#3333ff',fg='White')
        
    def output_emotion(self):
        text = self.emotion_input.get()
        response1 = self.api.emotions(text)
        print(response1)
        
        
nlp = NLPApp()