from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt, QTimer
import pickle
from pathlib import Path
import sys, os, os.path
from datetime import datetime
from cryptography.fernet import Fernet

app = QApplication([])
app.setStyle('Fusion')
window = QWidget()

password_cipher_key = b'kO-Mu7_bDPl1YJqpVWzk09w2xP_sCOKdW0zcrbdOTWc='
passwordcipher = Fernet(password_cipher_key)

notes_cipher_key = b'OSsbNvc0NfZnqji6Zq-LX1Bbr_17787PkJbJnexWt8w='
notescipher = Fernet(notes_cipher_key)
appdatalocation = os.getenv('APPDATA')

def main(self):
         window.setGeometry(220, 50,900, 575)
         window.setWindowTitle('MiNotes')



         frameGeometry = self.frameGeometry()
         DestkopWidget = QDesktopWidget().availableGeometry().center()
         frameGeometry.moveCenter(DestkopWidget)
         self.move(frameGeometry.topLeft())
        
         
         
         


         languagepacks =[
         ["Авторизация",'Авторизоваться','Логин',"Пароль","Вернуться","Регистрироваться", "Создать Заметку", "Сохранить", "Обновить", "Удалить", "Такого аккаунта не сушествует", "Неправельный пароль", "*Этот логин зарезервирован", "*Минимум 6 симболов","Напиши заметку", "Напиши больще симболов", "Настройки", "Удалить пользователя", "Поменять пароль", "Назад", "Сохранить пароль","создать нового пользователя", "Новый пароль","Повтори новый пароль", "Поискать заметки","Язык", "Темная тема", "Сменить пароль", "Настройки","Логин не может быть 'admin'","пароли не равны", "* Минимум 2 симбола", "Удалить все данные", "Файл", "Заметка", "Выйти", "Пользователь"],
         ["Login", "Login","Login", "Password", "Return","Register", "Create a note", "Save", "Update", "Delete","This login don't exist", "Incorrect password","*This login already exist","*Minimum 6 symbols","Write a note", "Write more simbols", "Settings", "Delete User", "Change password", "Return","Save password", "Create new User", "New password", "Repeat new password", "Find Note", "Language", "Night Theme", "Change Password","Settings","Login can't be 'admin'","passwords do not match", "*Minimum 2 symbols", "Delete all data", "File", "Note", "Exit", "User"],
         ["Logare",'Logheazăte','Login-ul',"Parola","Întoarce-te","Înregistrează-te", "Crează o notiţă", "Salvează", "Actualizează", "Şterge", "Nu există aşa login", "Parolă incorectă", "*Acest login este rezervat", "*Minim 6 simboluri","Scrie o notiţă", "Foloseşte mai multe simboluri","Setări", "Şterge Utilizatorul", "Schimbă parola", "Înapoi", "Salvează parola", "Crează un utilizator nou", "Parolă nouă", "Repetă parola"," Caută notiţa", "Limba", "Tema întunecată", "Schimba parola", "Setări", "Login-ul nu poate fi 'admin'","parolele nu coincid", "*Minim 2 simboluri", "Șterge toate datele", "Fail", "Notiţa", "Ieși-ți", "Utilizator" ]
         ]

         languagefileexist= Path(appdatalocation + "/Mi.Notes/langsets")



         if os.path.isdir(appdatalocation +"/Mi.Notes"):

            if not languagefileexist.is_file():
             languageindex = 1
             writelang = open(appdatalocation + '/Mi.Notes/langsets', "wb")
             pickle.dump(languageindex,writelang)
             writelang.close()

            else:
             readlang = open(appdatalocation +'/Mi.Notes/langsets', 'rb')
             languageindex = pickle.load(readlang)
             readlang.close()

         else:
            os.mkdir(appdatalocation +"/Mi.Notes")
            languageindex = 1
            writelang = open(appdatalocation +'/Mi.Notes/langsets', "wb")
            pickle.dump(languageindex,writelang)
            writelang.close()

         

         language = languagepacks[languageindex]
         mainMenu = QMenuBar(self)
         
         mainMenu.setVisible(True)

         fileMenu = mainMenu.addMenu(language[33])

         settingsaction = QAction(language[16], self)
         settingsaction.setToolTip("Alt+S")

         changeuseraction = QAction(language[4], self)
         changeuseraction.setToolTip("Esc")

         updatenoteaction = QAction(language[8], self)
         updatenoteaction.setToolTip("Alt+S")

         deletenoteaction = QAction(language[9], self)
         deletenoteaction.setToolTip("Ctrl+Del")


         savenoteaction = QAction(language[7], self)
         savenoteaction.setToolTip("Ctrl+S")

         exitaction = QAction(language[35], self)
         exitaction.setToolTip("Ctrl+Q")

         deleteuseraction = QAction(language[17], self)
         deleteuseraction.setToolTip("Alt+Del")

         changepasswordaction = QAction(language[27], self)
         changepasswordaction.setToolTip("Ctrl+P")

         deletealldataaction = QAction(language[32], self)
         deletealldataaction.setToolTip("Ctrl+Alt+Del")

         createnewuseraction = QAction(language[21], self)
         createnewuseraction.setToolTip("Ctrl+Alt+N")

         createnoteaction =QAction(language[6], self)
         createnoteaction.setToolTip("Ctrl+N")

         totalactions = [createnoteaction,createnewuseraction,deletealldataaction,changepasswordaction,deleteuseraction,exitaction,savenoteaction,deletenoteaction,updatenoteaction, changeuseraction,settingsaction]
         for i in totalactions:
            i.setVisible(True)
         fileMenu.addAction(settingsaction)
         fileMenu.addSeparator()
         fileMenu.addAction(exitaction)



         def basicmenubar():
            fileMenu.addAction(settingsaction)
            fileMenu.addSeparator()
            fileMenu.addAction(exitaction)
         def loginmenubar():
            userMenu = fileMenu.addMenu("User")
            fileMenu.addAction(createnoteaction)
            for i in usermenuactions:
                userMenu.addAction(i)
            fileMenu.addAction(settingsaction)
            fileMenu.addSeparator()
            fileMenu.addAction(exitaction)

         def notemenubar():
            fileMenu.clear()
            noteMenu = fileMenu.addMenu('Note')
            for i in noteactions:
                noteMenu.addAction(i)
            userMenu = fileMenu.addMenu("User")
            for i in usermenuactions:
                userMenu.addAction(i)
            fileMenu.addAction(settingsaction)
            fileMenu.addSeparator()
            fileMenu.addAction(exitaction)
         def adminmodemenubar():
            fileMenu.addAction(deletealldataaction)
            fileMenu.addAction(settingsaction)
            fileMenu.addSeparator()
            fileMenu.addAction(exitaction)
         def whenuserselectedmenubar():
            fileMenu.clear()
            fileMenu.addAction(createnoteaction)
            for i in usermenuactions:
                userMenu.addAction(i)
            fileMenu.addAction(deletealldataaction)
            fileMenu.addAction(settingsaction)
            fileMenu.addSeparator()
            fileMenu.addAction(exitaction)
         def adminmodenotemenubar():
            fileMenu.clear()
            noteMenu = fileMenu.addMenu('Note')
            for i in noteactions:
                noteMenu.addAction(i)
            userMenu = fileMenu.addMenu("User")
            for i in usermenuactions:
                userMenu.addAction(i)
            fileMenu.addAction(deletealldataaction)
            fileMenu.addAction(settingsaction)
            fileMenu.addSeparator()
            fileMenu.addAction(exitaction)
            

         



         usermenuactions = [changeuseraction, createnewuseraction, deleteuseraction]
         filmenuactions = [settingsaction, exitaction]

         noteactions = [createnoteaction, updatenoteaction, deletenoteaction]
         



         nightthemefileexist = Path(appdatalocation +"/Mi.Notes/themesets")
         self.nightmodecontrol = int()

         if not nightthemefileexist.is_file():
             self.nightthemecontrol = 0
             writetheme = open(appdatalocation + '/Mi.Notes/themesets', "wb")
             pickle.dump(self.nightthemecontrol,writetheme)
             writetheme.close()
         else:
             readtheme = open(appdatalocation +'/Mi.Notes/themesets', 'rb')
             self.nightmodecontrol = pickle.load(readtheme)
             readtheme.close()
         self.iffromstart = True


         logininput = QLineEdit("", self)
         logininput.setPlaceholderText(language[2],)
         logininput.setStyleSheet("font-size: 25px; font-family: Tahoma, Verdana;")
         logininput.setGeometry(150, 210,280,50)


         passwordinput = QLineEdit("", self)
         passwordinput.setPlaceholderText(language[3],)
         passwordinput.setStyleSheet("font-size: 25px; font-family: Tahoma, Verdana;")
         passwordinput.setGeometry(150, 305,280,50)
         passwordinput.setEchoMode(QLineEdit.Password)

         Login = QLabel(language[0], self)
         Login.move(150, 105)
         Login.setStyleSheet("font-size: 55px; font-family: Tahoma, Verdana;")


         ChangePasswordinsign = QLabel(language[27], self)
         ChangePasswordinsign.move(120, 95)
         ChangePasswordinsign.setStyleSheet("font-size: 55px; font-family: Tahoma, Verdana;")
         ChangePasswordinsign.setVisible(False)

         Settingsinsign = QLabel(language[28], self)
         Settingsinsign.move(35, 65)
         Settingsinsign.setStyleSheet("font-size: 55px; font-family: Tahoma, Verdana;")
         Settingsinsign.setVisible(False)



         Loginbutton = QPushButton(language[1], self)
         Loginbutton.setGeometry(150,400, 100, 50)
         Loginbutton.setStyleSheet("font-size: 16px; font-family: Tahoma, Verdana; background-color:#66c2ff")
         Loginbutton.setShortcut("Return")
         Loginbutton.setToolTip('Enter')

         Fromregisterreturnbutton = QPushButton(language[4], self)
         Fromregisterreturnbutton.setGeometry(150,400, 100, 50)
         Fromregisterreturnbutton.setStyleSheet("font-size: 16px; font-family: Tahoma, Verdana;background-color:#f6cd61")
         Fromregisterreturnbutton.setVisible(False)
         Fromregisterreturnbutton.setShortcut("Ctrl+Esc")
         Fromregisterreturnbutton.setToolTip("Ctrl+Esc")

         Registerbutton = QPushButton(language[5], self)
         Registerbutton.setGeometry(260,400, 170, 50)
         Registerbutton.setStyleSheet("font-size: 16px; font-family: Tahoma, Verdana; background-color:#8cff66")
         Registerbutton.setShortcut("Ctrl+Alt+N")
         Registerbutton.setToolTip("Ctrl+Alt+N")


         CreateNotebutton = QPushButton(language[6], self)
         CreateNotebutton.setGeometry(680,510, 200, 50)
         CreateNotebutton.setStyleSheet("font-size: 16px; font-family: Tahoma, Verdana; background-color:#66c2ff")
         CreateNotebutton.setVisible(False)
         CreateNotebutton.setShortcut("Ctrl+N")
         CreateNotebutton.setToolTip("Ctrl+N")

         ExtindedRegisterbutton = QPushButton(language[5], self)
         ExtindedRegisterbutton.setGeometry(260,400, 170, 50)
         ExtindedRegisterbutton.setStyleSheet("font-size: 16px; font-family: Tahoma, Verdana; background-color:#8cff66")
         ExtindedRegisterbutton.setVisible(False)
         ExtindedRegisterbutton.setShortcut("Return")
         ExtindedRegisterbutton.setToolTip("Enter")

         SaveNotebutton = QPushButton(language[7], self)
         SaveNotebutton.setGeometry(680,510, 200, 50)
         SaveNotebutton.setStyleSheet("font-size: 16px; font-family: Tahoma, Verdana; background-color:#8cff66")
         SaveNotebutton.setVisible(False)
         SaveNotebutton.setShortcut("Ctrl+S")
         SaveNotebutton.setToolTip("Ctrl+S")

         UpdateNotebutton = QPushButton(language[8], self)
         UpdateNotebutton.setGeometry(680,510, 200, 50)
         UpdateNotebutton.setStyleSheet("font-size: 16px; font-family: Tahoma, Verdana;background-color:#8cff66")
         UpdateNotebutton.setVisible(False)
         UpdateNotebutton.setShortcut("Alt+S")
         UpdateNotebutton.setToolTip('Alt+S')

         Returnbutton = QPushButton(language[4], self)
         Returnbutton.setGeometry(20,510, 200, 50)
         Returnbutton.setStyleSheet("font-size: 16px; font-family: Tahoma, Verdana;background-color:#f6cd61")
         Returnbutton.setVisible(False)
         Returnbutton.setShortcut("Esc")
         Returnbutton.setToolTip("Esc")

         DeleteNotebutton = QPushButton(language[9], self)
         DeleteNotebutton.setGeometry(475,510, 200, 50)
         DeleteNotebutton.setStyleSheet("font-size: 16px; font-family: Tahoma, Verdana;background-color:#fe4a49")
         DeleteNotebutton.setVisible(False)
         DeleteNotebutton.setShortcut("Ctrl+Del")
         DeleteNotebutton.setToolTip("Ctrl+Del")



         Deleteaccauntbutton =QPushButton(language[17], self)
         Deleteaccauntbutton.setGeometry(460,510, 200, 50)
         Deleteaccauntbutton.setStyleSheet("font-size: 16px; font-family: Tahoma, Verdana;background-color:#854442")
         Deleteaccauntbutton.setVisible(False)
         Deleteaccauntbutton.setShortcut("Ctrl+Alt+Del")
         Deleteaccauntbutton.setToolTip("Ctrl+Alt+Del")

         SecondReturnbutton = QPushButton(language[4], self)
         SecondReturnbutton.setGeometry(20,510, 200, 50)
         SecondReturnbutton.setStyleSheet("font-size: 16px; font-family: Tahoma, Verdana;background-color:#f6cd61")
         SecondReturnbutton.setVisible(False)
         SecondReturnbutton.setShortcut("Esc")
         SecondReturnbutton.setToolTip("Esc")

         Changepasswordbutton =QPushButton(language[18], self)
         Changepasswordbutton.setGeometry(240,510, 200, 50)
         Changepasswordbutton.setStyleSheet("font-size: 16px; font-family: Tahoma, Verdana;background-color:#fe4a49")
         Changepasswordbutton.setVisible(False)
         Changepasswordbutton.setShortcut("Ctrl+P")
         Changepasswordbutton.setToolTip("Ctrl+P")

         Returntologinbutton =QPushButton(language[19], self)
         Returntologinbutton.setGeometry(20,510, 200, 50)
         Returntologinbutton.setStyleSheet("font-size: 16px; font-family: Tahoma, Verdana;background-color:#f6cd61")
         Returntologinbutton.setVisible(False)
         Returntologinbutton.setShortcut('Esc')
         Returntologinbutton.setToolTip("Esc")

         ChangePasswordinput = QLineEdit("", self)
         ChangePasswordinput.setPlaceholderText(language[22],)
         ChangePasswordinput.setStyleSheet("font-size: 16px; font-family: Tahoma, Verdana;")
         ChangePasswordinput.setGeometry(150, 210,280,50)
         ChangePasswordinput.setVisible(False)

         SecondChangePasswordinput = QLineEdit("", self)
         SecondChangePasswordinput.setPlaceholderText(language[23],)
         SecondChangePasswordinput.setStyleSheet("font-size: 16px; font-family: Tahoma, Verdana;")
         SecondChangePasswordinput.setGeometry(150, 305,280,50)
         SecondChangePasswordinput.setVisible(False)
         SecondChangePasswordinput.setEchoMode(QLineEdit.Password)


         SaveNewPasswordButton= QPushButton(language[20], self)
         SaveNewPasswordButton.setGeometry(260,400, 170, 50)
         SaveNewPasswordButton.setStyleSheet("font-size: 16px; font-family: Tahoma, Verdana;background-color:#8cff66")
         SaveNewPasswordButton.setVisible(False)
         SaveNewPasswordButton.setShortcut('Return')
         SaveNewPasswordButton.setToolTip("Enter")

         CreateUserbutton = QPushButton(language[21], self)
         CreateUserbutton.setGeometry(680,510, 200, 50)
         CreateUserbutton.setStyleSheet("font-size: 16px; font-family: Tahoma, Verdana;background-color:#8cff66")
         CreateUserbutton.setVisible(False)
         CreateUserbutton.setShortcut("Ctrl+Alt+N")
         CreateUserbutton.setToolTip("Ctrl+Alt+N")

         SearchNoteinp = QLineEdit("", self)
         SearchNoteinp.setPlaceholderText(language[24])
         SearchNoteinp.setStyleSheet("font-size: 16px; font-family: Tahoma, Verdana;")
         SearchNoteinp.setGeometry(225,510, 450, 50)
         SearchNoteinp.setVisible(False)

         Deletealldatabutton =QPushButton(language[32], self)
         Deletealldatabutton.setGeometry(240,510, 200, 50)
         Deletealldatabutton.setStyleSheet("font-size: 16px; font-family: Tahoma, Verdana;background-color:#854442")
         Deletealldatabutton.setVisible(False)




         Regl = QLabel(language[5], self)
         Regl.move(150, 105)
         Regl.setStyleSheet("font-size: 55px; font-family: Tahoma, Verdana;")
         Regl.setVisible(False)

         tlde = QLabel(language[10], self)                #This login don't exist
         tlde.setStyleSheet("font-size: 20px; font-family: Tahoma, Verdana; color: Red")
         tlde.move(450, 221)
         tlde.setVisible(False)


         ipw = QLabel(language[11],self)           #Incorrect Password
         ipw.setStyleSheet("font-size: 20px; font-family: Tahoma, Verdana; color: Red")
         ipw.move(450, 315)
         ipw.setVisible(False)

         aep = QLabel(language[12],self)           #Login rezervat
         aep.setStyleSheet("font-size: 20px; font-family: Tahoma, Verdana; color: Red")
         aep.move(450, 221)
         aep.setVisible(False)

         tsp = QLabel(language[13],self)           # Parola prea scurta
         tsp.setStyleSheet("font-size: 20px; font-family: Tahoma, Verdana; color: Red")
         tsp.move(450, 315)
         tsp.setVisible(False)

         zametca = QTextEdit("", self)
         zametca.setPlaceholderText(language[14])
         zametca.setVisible(False)
         zametca.setGeometry(20,19, 860, 475)
         zametca.setStyleSheet("font-size: 16px; font-family: Tahoma, Verdana;")

         sm = QScrollArea(self)
         sm.setVisible(False)
         sm.setWidgetResizable(True)
         sm.setGeometry(20,19, 860, 475)

         vbox = QHBoxLayout()
         layout = QWidget()
         layout.setLayout(vbox)
         sm.setWidget(layout)

         ScrollAreaofAdmins = QScrollArea(self)
         ScrollAreaofAdmins.setVisible(False)
         ScrollAreaofAdmins.setWidgetResizable(True)
         ScrollAreaofAdmins.setGeometry(20,19, 860, 475)

         Hbox = QHBoxLayout()
         secondlayout = QWidget()
         secondlayout.setLayout(Hbox)
         ScrollAreaofAdmins.setWidget(secondlayout)

         languageselector = QComboBox(self)
         if languageindex == 0:
            languages ={ "Russian":0,"English":1,"Romanian":2}
         elif languageindex == 1:
            languages ={ "English":1,"Russian":0,"Romanian":2}
         elif languageindex == 2:
            languages ={"Romanian":2, "English":1,"Russian":0}
         
         languageselector.addItems(languages)
         languageselector.setGeometry(220,187, 200, 30)
         languageselector.setVisible(False)

         languageinsign = QLabel(language[25], self)
         languageinsign.move(60, 185)
         languageinsign.setStyleSheet("font-size: 25px; font-family: Tahoma, Verdana;")
         languageinsign.setVisible(False)


         nighttheme = QLabel(language[26], self)
         nighttheme.move(60, 245)
         nighttheme.setStyleSheet("font-size: 25px; font-family: Tahoma, Verdana;")
         nighttheme.setVisible(False)

         nightthemecheck = QCheckBox(self)
         nightthemecheck.move(220,255)
         nightthemecheck.setVisible(False)
         
         logincantbeadminerror = QLabel(language[29],self)      
         logincantbeadminerror.setStyleSheet("font-size: 20px; font-family: Tahoma, Verdana; color: Red")
         logincantbeadminerror.move(450, 221)
         logincantbeadminerror.setVisible(False)

         itsnotthesamepassword = QLabel(language[30],self)      
         itsnotthesamepassword.setStyleSheet("font-size: 20px; font-family: Tahoma, Verdana; color: Red")
         itsnotthesamepassword.move(450, 221)
         itsnotthesamepassword.setVisible(False)

         tooshortlogin = QLabel(language[31],self)      
         tooshortlogin.setStyleSheet("font-size: 20px; font-family: Tahoma, Verdana; color: Red")
         tooshortlogin.move(450, 221)
         tooshortlogin.setVisible(False)
         mainMenu.clear()
         fileMenu = mainMenu.addMenu(language[33])
         basicmenubar()
         mainMenu.setVisible(True)






         total = [zametca, sm, tsp, aep, Loginbutton, Registerbutton, CreateNotebutton, ExtindedRegisterbutton, SaveNotebutton, UpdateNotebutton, Returnbutton, DeleteNotebutton, Login, logininput, passwordinput, ipw, tlde, Regl, languageinsign, languageselector, nighttheme,nightthemecheck,ScrollAreaofAdmins, Deleteaccauntbutton, SecondReturnbutton, Changepasswordbutton, SecondChangePasswordinput, ChangePasswordinput,SaveNewPasswordButton, CreateUserbutton, Fromregisterreturnbutton, Returntologinbutton, SearchNoteinp, Settingsinsign, ChangePasswordinsign, logincantbeadminerror , itsnotthesamepassword, tooshortlogin, Deletealldatabutton]
         firstscreen = [Login, logininput, passwordinput,Loginbutton, Registerbutton, ]
         secondscreen = [CreateNotebutton,sm, Returntologinbutton,SearchNoteinp]
         thirdscreen = [zametca,SaveNotebutton, Returnbutton]
         fourthscreen = [zametca, Returnbutton, UpdateNotebutton,DeleteNotebutton]
         settingscreen = [languageselector, languageinsign, Returnbutton, nighttheme, nightthemecheck, Settingsinsign,]
         insigns = [Settingsinsign, Login, Regl, ChangePasswordinsign]
         buttons = {Deletealldatabutton: 2,Loginbutton: 1, Registerbutton: 0, CreateNotebutton:1, ExtindedRegisterbutton: 0, SaveNotebutton: 0, UpdateNotebutton: 0, Returnbutton: 3, DeleteNotebutton: 2, Deleteaccauntbutton: 4, SecondReturnbutton:3,  Changepasswordbutton:2, SaveNewPasswordButton: 0, CreateUserbutton: 0, Fromregisterreturnbutton: 3, Returntologinbutton:3, Deletealldatabutton: 4}
         inputs = [logininput, passwordinput, ChangePasswordinput, SecondChangePasswordinput, SearchNoteinp,]

         dbaexist= Path(appdatalocation +"/Mi.Notes/savedbafile")
         dbexist= Path(appdatalocation +"/Mi.Notes/savedbfile")
         self.textfromnote = ""
         self.a = ""
         self.forgoodret = False
         self.checkiflogined = False
#         logininput.setText('Alan')
 #        passwordinput.setText("wellcome")
         
         def clear():
             for i in total:
                 i.setVisible(False)
         def registration():
             clear()
             Fromregisterreturnbutton.setGeometry(150,400, 100, 50)
             logininput.setVisible(True)
             passwordinput.setVisible(True)
             ExtindedRegisterbutton.setVisible(True)
             Regl.setVisible(True)
             Fromregisterreturnbutton.setVisible(True)
             logininput.setText("")
             passwordinput.setText("")


         if not dbaexist.is_file():
             dba = {}
             Savedbafile = open(appdatalocation +'/Mi.Notes/savedbafile', "wb")
             pickle.dump(dba, Savedbafile)
             Savedbafile.close()
             registration()
         else:
             readdba = open(appdatalocation +'/Mi.Notes/savedbafile', 'rb')
             dba = pickle.load(readdba)
             readdba.close()
         if not dbexist.is_file():
             db = {}
             Savedbfile = open(appdatalocation +'/Mi.Notes/savedbfile', "wb")
             pickle.dump(db, Savedbfile)
             Savedbfile.close()
             
         else:
             readdb = open(appdatalocation +'/Mi.Notes/savedbfile', 'rb')
             db = pickle.load(readdb)
             readdb.close()


         self.dbn = []
         self.listofusers = []
         self.checkforcash = False
         self.adminmodeseted = False
         AreYouSure = QLabel(language[5], self)
         AreYouSure.move(150, 105)
         AreYouSure.setStyleSheet("font-size: 16px; font-family: Tahoma, Verdana;")
         AreYouSure.setVisible(False)
         mainMenu.setStyleSheet("color: #000")

         if languageindex == 0:
             Loginbutton.setStyleSheet("font-size: 12px; font-family: Tahoma, Verdana; background-color:#66c2ff")
             CreateUserbutton.setStyleSheet("font-size: 14px; font-family: Tahoma, Verdana;")
             Regl.move(130, 105)
         elif languageindex == 2:
             nightthemecheck.move(270,255)
            



         def SetDarkMode():
             mainMenu.setStyleSheet("color: #fff")
             window.setStyleSheet("background-color : #262626")
             zametca.setStyleSheet("color: #FFF;font-size: 16px; border: 1px solid #e6e6e6; border-radius: 3px; background-color:#666")
             nighttheme.setStyleSheet("font-size: 25px; font-family: Tahoma, Verdana; color:#FFF")
             nightthemecheck.setStyleSheet("color:#FFF; border: 0px solid #FFF;border-radius: 3px;")
             languageselector.setStyleSheet("border: 1px solid #e6e6e6; border-radius: 3px; font-size: 16px; color: #FFF;")
             layout.setStyleSheet("background-color:#333333")
             ChangePasswordinsign.setStyleSheet("color: #FFF;font-size: 55px")
             languageinsign.setStyleSheet("color: #FFF;font-size: 25px")
             if self.iffromstart:
                 nightthemecheck.toggle()
             for i in inputs:
                i.setStyleSheet("background-color:#666;border: 2px solid #e6e6e6; border-radius: 3px; font-size: 16px; ;color:#FFF")
             for i in insigns:
                i.setStyleSheet("color: #FFF;font-size: 55px")
             for i in buttons:
                if buttons[i] == 0:
                    i.setStyleSheet('border: 2px solid #8cff66; border-radius: 3px; font-size: 16px; color: #FFF; background-color: #333')
                elif buttons[i] == 1:
                    i.setStyleSheet('border: 2px solid #66c2ff; border-radius: 3px; font-size: 16px; color: #FFF; background-color: #333')
                elif buttons[i] == 2:
                    i.setStyleSheet('border: 2px solid #fe4a49 ; border-radius: 3px; font-size: 16px; color: #FFF; background-color: #333')
                elif buttons[i] == 3:
                    i.setStyleSheet('border: 2px solid #f6cd61 ; border-radius: 3px; font-size: 16px; color: #FFF; background-color: #333')
                elif buttons[i] == 4:
                    i.setStyleSheet('border: 2px solid #854442; border-radius: 3px; font-size: 16px; color: #FFF; background-color: #333')

         if self.nightmodecontrol == 1:
             SetDarkMode()



         self.show()

         def Deletingalldata():
            deletealldatareply = QMessageBox.question(self, 'Delete all data?',
                "Are you sure?", QMessageBox.Yes |
                QMessageBox.No, QMessageBox.No)
            if deletealldatareply == QMessageBox.Yes:
                os.remove(appdatalocation +'/Mi.Notes/cash')
                os.remove(appdatalocation +'/Mi.Notes/langsets')
                os.remove(appdatalocation +'/Mi.Notes/secash')
                os.remove(appdatalocation +'/Mi.Notes/savedbafile')
                os.remove(appdatalocation +'/Mi.Notes/savedbfile')
                os.remove(appdatalocation +'/Mi.Notes/themesets')
                python = sys.executable
                os.execl(python, python, * sys.argv)

         def SearchNote():
             for i in self.dbn:
                 vbox.removeWidget(i)
                 i.setVisible(False)
             for i in self.dbn:
                 if SearchNoteinp.text() in i.toPlainText():
                     i.setVisible(True)
                     vbox.addWidget(i)



         def ChangeUser():
                fileMenu.clear()
                basicmenubar()
                self.checkiflogined = False
                clear()
                setcashdeleting()
                for i in firstscreen:
                  i.setVisible(True)
                logininput.setText("")
                self.adminmodeseted = False
                passwordinput.setText("")

             

         def setcashdeleting():
             savelogin = open(appdatalocation +'/Mi.Notes/cash', "wb")
             pickle.dump({0:"user"}, savelogin)
             savelogin.close()




         def setlistofnotes():
             greenline()
             for i in db[self.loginptxt]:
                 i = QTextEdit(i, self)
                 i.setGeometry(20,20, 200, 230)
                 i.setStyleSheet("font-size: 16px; font-family: Tahoma, Verdana;")
                 if self.nightmodecontrol == 1:
                     i.setStyleSheet("background-color:#666;border: 1px solid #e6e6e6; border-radius 3px; font-size: 16px; color:#FFF")
                 i.setFixedHeight(430)
                 i.setFixedWidth(400)
                 self.dbn.append(i)
                 vbox.addWidget(i)
                 total.append(i)











         def secondret():
             if self.adminmodeseted:
                whenuserselected()
             else:
                ret()

         def SaveNewPassword():
             if ChangePasswordinput.text() == SecondChangePasswordinput.text() and len(ChangePasswordinput.text()) > 5:
                 encryptedpassword = passwordcipher.encrypt((ChangePasswordinput.text()).encode('utf-8'))
                 dba[self.loginptxt] = encryptedpassword
                 writedbainfile()
                 whenuserselected()
             elif ChangePasswordinput.text() != SecondChangePasswordinput.text():
                itsnotthesamepassword.setVisible(True)
                if len(ChangePasswordinput.text()) > 5:
                    tsp.setVisible(False)
             elif len(ChangePasswordinput.text()) <= 5:
                tsp.setVisible(True)
                if ChangePasswordinput.text() == SecondChangePasswordinput.text():
                    itsnotthesamepassword.setVisible(False)


         def ChangePassword():
             clear()
             setcashdeleting()
             SecondReturnbutton.setVisible(True)
             SecondReturnbutton.setGeometry(150,400, 100, 50)
             ChangePasswordinsign.setVisible(True)
             SecondChangePasswordinput.setVisible(True)
             ChangePasswordinput.setVisible(True)
             SaveNewPasswordButton.setVisible(True)




         def deleteuser():
             reply = QMessageBox.question(self, 'Delete User',
                "Are you sure?", QMessageBox.Yes |
                QMessageBox.No, QMessageBox.No)
             if reply == QMessageBox.Yes:
                del dba[self.loginptxt]
                del db[self.loginptxt]
                writedbinfile()
                writedbainfile()
                setcashdeleting()
                python = sys.executable
                os.execl(python, python, * sys.argv)
             


         def listofadmins():
             self.listofusers.clear()
             for i in dba:
                i = QTextEdit(i, self)
                i.setVisible(True)
                i.setGeometry(20,20, 200, 230)
                i.setStyleSheet("font-size: 16px; font-family: Tahoma, Verdana;")
                if self.nightmodecontrol == 1:
                    i.setStyleSheet("background-color:#666;border: 1px solid #e6e6e6; border-radius 3px; font-size: 16px; color:#FFF")
                i.setFixedHeight(430)
                i.setFixedWidth(400)
                Hbox.addWidget(i)
                total.append(i)
                self.listofusers.append(i)


         def whenuserselected():
             fileMenu.clear()
             userMenu = fileMenu.addMenu('User')
             for i in usermenuactions:
                userMenu.addAction(i)
             adminmodemenubar()
             clear()
             notes()
             setcashdeleting()
             Returnbutton.setVisible(True)
             Changepasswordbutton.setVisible(True)
             sm.setVisible(True)
             self.forgoodret = True
             Deleteaccauntbutton.setVisible(True)
             CreateNotebutton.setVisible(True)
             a = 0
             for i in range(len(self.dbn)):
                 def changenote(a = a):
                     clear()
                     for l in thirdscreen:
                         l.setVisible(True)
                     self.a = a
                     UpdateNotebutton.setVisible(True)
                     DeleteNotebutton.setVisible(True)
                     CreateNotebutton.setVisible(False)
                     zametca.setText(self.dbn[self.a].toPlainText())
                     adminmodenotemenubar()
                     if self.forgoodret:
                         Returnbutton.setVisible(False)
                         SecondReturnbutton.setGeometry(20,510, 200, 50)
                         SecondReturnbutton.setVisible(True)
                         

                 if a != 3:
                     self.dbn[a].cursorPositionChanged.connect(changenote, a)

                 elif len(self.dbn) >2:
                       if a == 3:
                           self.dbn[3].cursorPositionChanged.connect(changenote)
                 a += 1






         def adminmode():
             adminmodemenubar()
             fileMenu.clear()
             fileMenu.addAction(deletealldataaction)
             basicmenubar()
             clear()
             setcashdeleting()
             listofadmins()
             self.checkiflogined = False
             Deletealldatabutton.setVisible(True)
             Fromregisterreturnbutton.setVisible(True)
             Fromregisterreturnbutton.setGeometry(20,510, 200, 50)
             ScrollAreaofAdmins.setVisible(True)
             CreateUserbutton.setVisible(True)
             Changepasswordbutton.setGeometry(240,510, 200, 50)
             self.adminmodeseted = True
             a = 0
             for i in range(len(self.listofusers)):
                 def selectadmin(a = a):
                     clear()
                     self.selecteduser = a
                     self.loginptxt = self.listofusers[a].toPlainText()
                     whenuserselected()

                 if a != 3:
                     self.listofusers[a].cursorPositionChanged.connect(selectadmin, a)

                 elif len(self.listofusers) >2:
                       if a == 3:
                           self.listofusers[3].cursorPositionChanged.connect(selectadmin)
                 a += 1








         def SetWhiteMode():
             if self.checkiflogined:
                self.cashforlogin = {1:self.loginptxt}
                writecashinfile()
             python = sys.executable
             os.execl(python, python, * sys.argv)


         def ThemeSettings(state):
            if state == Qt.Checked:
                self.iffromstart = False
                SetDarkMode()
                self.nightmodecontrol = 1

                writethemeinfile()

            else:
                self.nightmodecontrol = 0
                writethemeinfile()
                SetWhiteMode()
         def writethemeinfile():
             print(self.nightmodecontrol)
             savethemesets = open(appdatalocation +'/Mi.Notes/themesets', "wb")
             savethemesets.truncate()
             pickle.dump(self.nightmodecontrol, savethemesets)
             savethemesets.close()




         def changelanguage(language):
             languageindex = languages[language]
             writelang = open(appdatalocation + '/Mi.Notes/langsets', "wb")
             writelang.truncate()
             pickle.dump(languageindex,writelang)
             writelang.close()
             if self.checkiflogined:
                self.cashforlogin = {1:self.loginptxt}
                writecashinfile()
             python = sys.executable
             os.execl(python, python, * sys.argv)




         def writedbinfile():
             Savedbfile = open(appdatalocation + '/Mi.Notes/savedbfile', "wb")
             Savedbfile.truncate()
             pickle.dump(db, Savedbfile)
             Savedbfile.close()

         def writedbainfile():
             Savedbafile = open(appdatalocation + '/Mi.Notes/savedbafile', "wb")
             Savedbafile.truncate()
             pickle.dump(dba, Savedbafile)
             Savedbafile.close()

         def writecashinfile():
             self.cashforlogin = {1:self.loginptxt}
             savecash = open(appdatalocation + '/Mi.Notes/cash', "wb")
             savecash.truncate()
             pickle.dump(self.cashforlogin, savecash)
             savecash.close()

         def savecash():
             oldtime = {(int(datetime.now().strftime("%d"))) * 1440 + (int(datetime.now().strftime("%H"))) *60 + (int(datetime.now().strftime("%M"))+ 15):(int(datetime.now().strftime("%m")))}
             saveoldtime = open(appdatalocation + '/Mi.Notes/secash', "wb")
             saveoldtime.truncate()
             pickle.dump(oldtime, saveoldtime)
             saveoldtime.close()


         def bordercolorsetnormal():
            if self.nightmodecontrol == 1:
                zametca.setStyleSheet("color: #FFF;font-size: 16px; border: 1px solid #e6e6e6; border-radius: 3px; background-color:#666")
            else:
                zametca.setStyleSheet("font-size: 16px; font-family: Tahoma, Verdana;")
                 
             




         def clear():
             savecash()
             readdba = open(appdatalocation +'/Mi.Notes/savedbafile', 'rb')
             dba = pickle.load(readdba)
             readdba.close()
             readdb = open(appdatalocation +'/Mi.Notes/savedbfile', 'rb')
             db = pickle.load(readdb)
             readdb.close()
             self.checkforcash = False
             SearchNoteinp.setText("")
             for i in total:
                 i.setVisible(False)
             for i in self.dbn:
                 vbox.removeWidget(i)
             zametca.setPlaceholderText(language[14])


         def notes():
              self.dbn.clear()
              for i in db[self.loginptxt]:
                  i = (notescipher.decrypt(i)).decode('utf-8')
                  i = QTextEdit(i, self)
                  i.setVisible(True)
                  i.setStyleSheet("font-size: 16px; font-family: Tahoma, Verdana;")
                  if self.nightmodecontrol == 1:
                      i.setStyleSheet("background-color:#666;border: 1px solid #e6e6e6; border-radius 3px; font-size: 16px; color:#FFF")
                  i.setFixedHeight(430)
                  i.setFixedWidth(400)
                  self.dbn.append(i)
                  vbox.addWidget(i)
                  total.append(i)


         

         def proccesofregistration():
             self.loginptxt = logininput.text()
             pasinptxt = passwordinput.text()
             tsp.setVisible(False)
             if self.loginptxt not in dba and self.loginptxt != "admin" and len(self.loginptxt) >1:
                 aep.setVisible(False)
                 logincantbeadminerror.setVisible(False)
                 tooshortlogin.setVisible(False)

                 if not len(pasinptxt)<6:
                     aep.setVisible(False)
                     tsp.setVisible(False)
                     encryptedpassword = passwordcipher.encrypt((pasinptxt).encode('utf-8'))
                     newacc = {self.loginptxt: encryptedpassword}
                     notesfornewacc = {self.loginptxt: []}
                     dba.update(newacc)
                     db.update(notesfornewacc)
                     login()
                     writedbainfile()
                     writedbinfile()
                 else:
                    if len(pasinptxt)<6:
                     tsp.setVisible(True)
             elif self.loginptxt in dba:
                 aep.setVisible(True)
             elif self.loginptxt == 'admin':
                logincantbeadminerror.setVisible(True)
             elif len(self.loginptxt) < 2:
                tooshortlogin.setVisible(True)





         def login():
             if not self.checkforcash:
                self.loginptxt = logininput.text()
                self.passinptxt = passwordinput.text()
             if self.loginptxt in dba and self.loginptxt != "admin":
                 tlde.setVisible(False)
                 if self.passinptxt ==(passwordcipher.decrypt(dba[self.loginptxt])).decode('utf-8') :

                     writecashinfile()
                     clear()
                     notes()
                     savecash()
                     a = 0
                     self.adminmodeseted = False
                     self.forgoodret = False
                     self.checkiflogined = True
                     fileMenu.clear()
                     loginmenubar()


                     for i in range(len(self.dbn)):
                         def changenote(a = a):
                             clear()
                             for l in thirdscreen:
                                 l.setVisible(True)
                             self.a = a
                             UpdateNotebutton.setVisible(True)
                             DeleteNotebutton.setVisible(True)
                             CreateNotebutton.setVisible(False)
                             zametca.setText(self.dbn[self.a].toPlainText())
                             self.adminmodeseted = False
                             notemenubar()
                             if self.forgoodret:
                                 Returnbutton.setVisible(False)

                                 SecondReturnbutton.setVisible(True)

                         if a != 3:
                             self.dbn[a].cursorPositionChanged.connect(changenote, a)

                         elif len(self.dbn) >2:
                               if a == 3:
                                   self.dbn[3].cursorPositionChanged.connect(changenote)
                         a += 1

                     for i in secondscreen:
                         i.setVisible(True)

                 else:
                     ipw.setVisible(True)
             elif self.loginptxt == 'admin':
                 if self.passinptxt == "root":
                     adminmode()
                 else:
                    ipw.setVisible(True)
             elif self.loginptxt not in dba:
                 tlde.setVisible(True)


         cash = Path(appdatalocation + '/Mi.Notes/cash')
         seccash = Path(appdatalocation + '/Mi.Notes/secash')
         if not seccash.is_file():
             savetime = open(appdatalocation + '/Mi.Notes/secash', "wb")
             pickle.dump({0:13}, savetime)
             savetime.close()
         else:
            readtime = open(appdatalocation + '/Mi.Notes/secash', 'rb')
            oldtime = pickle.load(readtime)
            readtime.close()
            for i in oldtime:
                if not oldtime[i] >12:
                    oldminutes = i
                    if oldtime[oldminutes] == int(datetime.now().strftime("%m")) and oldminutes < int(datetime.now().strftime("%d")) * 1440 + int(datetime.now().strftime("%H")) *60 + int(datetime.now().strftime("%M")):
                        savetime = open(appdatalocation + '/Mi.Notes/secash', "wb")
                        pickle.dump({0:13}, savetime)
                        savetime.close()
                        setcashdeleting()
             



         if not cash.is_file():
             savelogin = open(appdatalocation + '/Mi.Notes/cash', "wb")
             pickle.dump({0:"Alan"}, savelogin)
             savelogin.close()

         else:
             readlogin = open(appdatalocation + '/Mi.Notes/cash', 'rb')
             self.cashforlogin = pickle.load(readlogin)
             for i in self.cashforlogin:
                 if i == 1:
                     self.checkforcash = True
                     self.loginptxt = self.cashforlogin[1]
                     self.passinptxt = (passwordcipher.decrypt(dba[self.loginptxt])).decode('utf-8') 
                     login()

             readlogin.close()




         def newnote():
             clear()
             self.a = ""
             if not self.adminmodeseted:
                savecash()
             else:
                adminmodemenubar()
             for i in thirdscreen:
                 i.setVisible(True)

             if self.forgoodret:
                 Returnbutton.setVisible(False)
                 SecondReturnbutton.setGeometry(20,510, 200, 50)
                 SecondReturnbutton.setVisible(True)
             zametca.setText("")

         def savenote():
             notemenubar()
             if not self.adminmodeseted:
                savecash()
             else:
                adminmodenotemenubar()
             self.note = zametca.toPlainText()
             if len(self.note) >0:
                 UpdateNotebutton.setVisible(True)
                 DeleteNotebutton.setVisible(True)
                 CreateNotebutton.setVisible(False)
                 db[self.loginptxt].append(notescipher.encrypt((self.note).encode('utf-8')))
                 writedbinfile()
                 if self.nightmodecontrol == 1:
                    zametca.setStyleSheet("color: #FFF;font-size: 16px; border: 1px solid #00ff00; border-radius: 3px; background-color:#666")
                 else:
                    zametca.setStyleSheet("font-size: 16px; font-family: Tahoma, Verdana;border: 1px solid #00ff00")
                 
                 QTimer.singleShot(500, bordercolorsetnormal)
                 zametca.setPlaceholderText(language[14])
             else:
                 zametca.setPlaceholderText(language[15])




         def ret():
             self.checkforcash = True
             login()
             if self.adminmodeseted:
                adminmode()

         def upnote():
             if not self.adminmodeseted:
                savecash()
             self.newnote = zametca.toPlainText()
             if len(self.newnote)>0:
                 if type(self.a) is str:
                    db[self.loginptxt].pop(len(db[self.loginptxt])-1)
                    db[self.loginptxt].append(notescipher.encrypt((self.newnote).encode('utf-8')))
                 elif type(self.a) is int:
                    db[self.loginptxt].pop(self.a)
                    db[self.loginptxt].insert(self.a, notescipher.encrypt((self.newnote).encode('utf-8')))
                 self.note = zametca.toPlainText()
                 writedbinfile()
                 


                 if self.nightmodecontrol == 1:
                    zametca.setStyleSheet("color: #FFF;font-size: 16px; border: 1px solid #00ff00; border-radius: 3px; background-color:#666")
                 else:
                    zametca.setStyleSheet("font-size: 16px; font-family: Tahoma, Verdana;border: 1px solid #00ff00")
                 
                 QTimer.singleShot(1000, bordercolorsetnormal)
                 zametca.setPlaceholderText(language[14])
             else:
                 zametca.setPlaceholderText(language[15])


         def simpleremove():
             if not self.adminmodeseted:
                savecash()
             removereply = QMessageBox.question(self, 'Delete Note',
                "Are you sure?", QMessageBox.Yes |
                QMessageBox.No, QMessageBox.No)
             if removereply == QMessageBox.Yes:
                if type(self.a) is int:
                    db[self.loginptxt].pop(self.a)
                elif type(self.a) is str:
                    db[self.loginptxt].pop(len(db[self.loginptxt])-1)
                if not self.forgoodret:
                    ret()
                else:
                    secondret()
             writedbinfile()

             
         def settings():
             clear()
             if not self.adminmodeseted:
                savecash()
                Changepasswordbutton.setVisible(True)
                Changepasswordbutton.setGeometry(60,310, 200, 50)
             for i in settingscreen:
                 i.setVisible(True)
             if not self.checkiflogined:
                Changepasswordbutton.setVisible(False)
                Returnbutton.setVisible(False)
                Fromregisterreturnbutton.setVisible(True)
                Fromregisterreturnbutton.setGeometry(20,510, 200, 50)
         def exit():
            quit()


         CreateNotebutton.clicked.connect(newnote)
         UpdateNotebutton.clicked.connect(upnote)
         Loginbutton.clicked.connect(login)
         SaveNotebutton.clicked.connect(savenote)
         Returnbutton.clicked.connect(ret)
         DeleteNotebutton.clicked.connect(simpleremove)
         Registerbutton.clicked.connect(registration)
         languageselector.activated[str].connect(changelanguage)
         nightthemecheck.stateChanged.connect(ThemeSettings)
         ExtindedRegisterbutton.clicked.connect(proccesofregistration)
         SecondReturnbutton.clicked.connect(secondret)
         Deleteaccauntbutton.clicked.connect(deleteuser)
         Changepasswordbutton.clicked.connect(ChangePassword)
         SaveNewPasswordButton.clicked.connect(SaveNewPassword)
         CreateUserbutton.clicked.connect(registration)
         Fromregisterreturnbutton.clicked.connect(ChangeUser)
         Returntologinbutton.clicked.connect(ChangeUser)
         SearchNoteinp.textChanged.connect(SearchNote)
         Deletealldatabutton.clicked.connect(Deletingalldata)
         settingsaction.triggered.connect(settings)
         exitaction.triggered.connect(exit)

         settingsaction.triggered.connect(settings)
         
         changeuseraction.triggered.connect(ChangeUser)
         updatenoteaction.triggered.connect(upnote)
         deletenoteaction.triggered.connect(simpleremove)
         savenoteaction.triggered.connect(savenote)
         exitaction.triggered.connect(exit)
         deleteuseraction.triggered.connect(deleteuser)
         changepasswordaction.triggered.connect(ChangePassword)
         deletealldataaction.triggered.connect(Deletingalldata)
         createnewuseraction.triggered.connect(registration)
         createnoteaction.triggered.connect(newnote)





if __name__ == '__main__':
    main(window)

    app.exec_()
