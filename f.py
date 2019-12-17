from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import pickle
from pathlib import Path
import sys, os, os.path
import hashlib
from datetime import datetime

app = QApplication([])
app.setStyle('Fusion')
window = QWidget()
def main(self):
         window.setGeometry(220, 50,900, 575)
         window.setWindowTitle('MiNotes')


         frameGeometry = self.frameGeometry()
         DestkopWidget = QDesktopWidget().availableGeometry().center()
         frameGeometry.moveCenter(DestkopWidget)
         self.move(frameGeometry.topLeft())


         languagepacks =[
         ["Авторизация",'Авторизоваться','Логин',"Пароль","Вернуться","Регистрироваться", "Создать Заметку", "Сохранить", "Обновить", "Удалить", "Такого аккаунта не сушествует", "Неправельный пароль", "*Этот логин зарезервирован", "*Слишком короткий пароль","Напиши заметку", "Напиши больще симболов", "Настройки", "Удалить пользователя", "Поменять пароль", "Поменять пользователя", "Сохранить пароль","создать нового пользователя", "Новый пароль","Повтори новый пароль", "Поискать заметки","Язык", "Темная тема", "Сменить пароль", "Настройки"],
         ["Login", "Login","Login", "Password", "Return","Register", "Create a note", "Save", "Update", "Delete","This login don't exist", "Incorrect password","*This login already exist","*Too short password","Write a note", "Write more simbols", "Settings", "Delete User", "Change password", "Change User","Save password", "Create new User", "New password", "Repeat new password", "Find Note", "Language", "Night Theme", "Change Password","Settings"],
         ["Logare",'Logheazăte','Login-ul',"Parola","Întoarce-te","Înregistrează-te", "Crează o notiţă", "Salvează", "Actualizează", "Şterge", "Nu există aşa login", "Parolă incorectă", "*Acest login este rezervat", "*Parolă prea scurtă","Scrie o notiţă", "Foloseşte mai multe simboluri","Setări", "Şterge Utilizatorul", "Schimbă parola", "Schimbă Utilizatorul", "Salvează parola", "Crează un utilizator nou", "Parolă nouă", "Repetă parola"," Caută notiţa", "Limba", "Tema întunecată", "Schimba parola", "Setări" ]
         ]

         languagefileexist= Path("C:/Users/user/AppData/Roaming/Mi.Notes/langsets")



         if os.path.isdir("C:/Users/user/AppData/Roaming/Mi.Notes"):

            if not languagefileexist.is_file():
             languageindex = 1
             writelang = open('C:/Users/user/AppData/Roaming/Mi.Notes/langsets', "wb")
             pickle.dump(languageindex,writelang)
             writelang.close()

            else:
             readlang = open('C:/Users/user/AppData/Roaming/Mi.Notes/langsets', 'rb')
             languageindex = pickle.load(readlang)
             readlang.close()

         else:
            os.mkdir("C:/Users/user/AppData/Roaming/Mi.Notes")
            languageindex = 1
            writelang = open('C:/Users/user/AppData/Roaming/Mi.Notes/langsets', "wb")
            pickle.dump(languageindex,writelang)
            writelang.close()

         

         language = languagepacks[languageindex]

         nightthemefileexist = Path("C:/Users/user/AppData/Roaming/Mi.Notes/themesets")
         self.nightmodecontrol = int()

         if not nightthemefileexist.is_file():
             self.nightthemecontrol = 0
             writetheme = open('C:/Users/user/AppData/Roaming/Mi.Notes/themesets', "wb")
             pickle.dump(self.nightthemecontrol,writetheme)
             writetheme.close()
         else:
             readtheme = open('C:/Users/user/AppData/Roaming/Mi.Notes/themesets', 'rb')
             self.nightmodecontrol = pickle.load(readtheme)
             readtheme.close()
         self.iffromstart = True


         logininput = QLineEdit("", self)
         logininput.setPlaceholderText(language[2],)
         logininput.setStyleSheet("font-size: 25px; font-family: Tahoma, Verdana;")
         logininput.setGeometry(150, 210,280,50)
         #logininput.setToolTip()


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
         Fromregisterreturnbutton.setStyleSheet("font-size: 16px; font-family: Tahoma, Verdana;")
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
         CreateNotebutton.setStyleSheet("font-size: 16px; font-family: Tahoma, Verdana;")
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
         SaveNotebutton.setStyleSheet("font-size: 16px; font-family: Tahoma, Verdana;")
         SaveNotebutton.setVisible(False)
         SaveNotebutton.setShortcut("Ctrl+S")
         SaveNotebutton.setToolTip("Ctrl+S")

         UpdateNotebutton = QPushButton(language[8], self)
         UpdateNotebutton.setGeometry(680,510, 200, 50)
         UpdateNotebutton.setStyleSheet("font-size: 16px; font-family: Tahoma, Verdana;")
         UpdateNotebutton.setVisible(False)
         UpdateNotebutton.setShortcut("Ctrl+S")
         UpdateNotebutton.setToolTip('Ctrl+S')

         Returnbutton = QPushButton(language[4], self)
         Returnbutton.setGeometry(20,510, 200, 50)
         Returnbutton.setStyleSheet("font-size: 16px; font-family: Tahoma, Verdana;")
         Returnbutton.setVisible(False)
         Returnbutton.setShortcut("Esc")
         Returnbutton.setToolTip("Esc")

         DeleteNotebutton = QPushButton(language[9], self)
         DeleteNotebutton.setGeometry(480,510, 200, 50)
         DeleteNotebutton.setStyleSheet("font-size: 16px; font-family: Tahoma, Verdana;")
         DeleteNotebutton.setVisible(False)
         DeleteNotebutton.setShortcut("Ctrl+Del")
         DeleteNotebutton.setToolTip("Ctrl+Del")

         SecondDeleteNotebutton = QPushButton(language[9], self)
         SecondDeleteNotebutton.setGeometry(480,510, 200, 50)
         SecondDeleteNotebutton.setStyleSheet("font-size: 16px; font-family: Tahoma, Verdana;")
         SecondDeleteNotebutton.setVisible(False)
         SecondDeleteNotebutton.setShortcut("Ctrl+Del")
         SecondDeleteNotebutton.setToolTip("Ctrl+Del")

         SecondUpdateNotebutton = QPushButton(language[8], self)
         SecondUpdateNotebutton.setGeometry(680,510, 200, 50)
         SecondUpdateNotebutton.setStyleSheet("font-size: 16px; font-family: Tahoma, Verdana;")
         SecondUpdateNotebutton.setVisible(False)
         SecondUpdateNotebutton.setShortcut("Ctrl+S")
         SecondUpdateNotebutton.setToolTip("Ctrl+S")

         settingsbtn = QPushButton(language[16], self)
         settingsbtn.setGeometry(20,510, 200, 50)
         settingsbtn.setStyleSheet("font-size: 16px; font-family: Tahoma, Verdana;")
         settingsbtn.setVisible(False)
         settingsbtn.setShortcut("Alt+S")
         settingsbtn.setToolTip("Alt+S")

         Deleteaccauntbutton =QPushButton(language[17], self)
         Deleteaccauntbutton.setGeometry(460,510, 200, 50)
         Deleteaccauntbutton.setStyleSheet("font-size: 16px; font-family: Tahoma, Verdana;")
         Deleteaccauntbutton.setVisible(False)
         Deleteaccauntbutton.setShortcut("Ctrl+Alt+Del")
         Deleteaccauntbutton.setToolTip("Ctrl+Alt+Del")

         SecondReturnbutton = QPushButton(language[4], self)
         SecondReturnbutton.setGeometry(20,510, 200, 50)
         SecondReturnbutton.setStyleSheet("font-size: 16px; font-family: Tahoma, Verdana;")
         SecondReturnbutton.setVisible(False)
         SecondReturnbutton.setShortcut("Esc")
         SecondReturnbutton.setToolTip("Esc")

         Changepasswordbutton =QPushButton(language[18], self)
         Changepasswordbutton.setGeometry(240,510, 200, 50)
         Changepasswordbutton.setStyleSheet("font-size: 16px; font-family: Tahoma, Verdana;")
         Changepasswordbutton.setVisible(False)
         Changepasswordbutton.setShortcut("Ctrl+P")
         Changepasswordbutton.setToolTip("Ctrl+P")

         Returntologinbutton =QPushButton(language[19], self)
         Returntologinbutton.setGeometry(220,510, 200, 50)
         Returntologinbutton.setStyleSheet("font-size: 16px; font-family: Tahoma, Verdana;")
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
         SaveNewPasswordButton.setStyleSheet("font-size: 16px; font-family: Tahoma, Verdana;")
         SaveNewPasswordButton.setVisible(False)
         SaveNewPasswordButton.setShortcut('Return')
         SaveNewPasswordButton.setToolTip("Enter")

         CreateUserbutton = QPushButton(language[21], self)
         CreateUserbutton.setGeometry(680,510, 200, 50)
         CreateUserbutton.setStyleSheet("font-size: 16px; font-family: Tahoma, Verdana;")
         CreateUserbutton.setVisible(False)
         CreateUserbutton.setShortcut("Ctrl+Alt+N")
         CreateUserbutton.setToolTip("Ctrl+Alt+N")

         SearchNoteinp = QLineEdit("", self)
         SearchNoteinp.setPlaceholderText(language[24])
         SearchNoteinp.setStyleSheet("font-size: 16px; font-family: Tahoma, Verdana;")
         SearchNoteinp.setGeometry(420,510, 260, 50)
         SearchNoteinp.setVisible(False)




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
         zametca.setGeometry(20,20, 860, 475)
         zametca.setStyleSheet("font-size: 16px; font-family: Tahoma, Verdana;")

         sm = QScrollArea(self)
         sm.setVisible(False)
         sm.setWidgetResizable(True)
         sm.setGeometry(20,20, 860, 475)

         vbox = QHBoxLayout()
         layout = QWidget()
         layout.setLayout(vbox)
         sm.setWidget(layout)

         ScrollAreaofAdmins = QScrollArea(self)
         ScrollAreaofAdmins.setVisible(False)
         ScrollAreaofAdmins.setWidgetResizable(True)
         ScrollAreaofAdmins.setGeometry(20,20, 860, 475)

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





         total = [zametca, sm, tsp, aep, Loginbutton, Registerbutton, CreateNotebutton, ExtindedRegisterbutton, SaveNotebutton, UpdateNotebutton, Returnbutton, DeleteNotebutton, SecondDeleteNotebutton, Login, logininput, passwordinput, ipw, tlde, Regl, SecondUpdateNotebutton, settingsbtn, languageinsign, languageselector, nighttheme,nightthemecheck,ScrollAreaofAdmins, Deleteaccauntbutton, SecondReturnbutton, Changepasswordbutton, SecondChangePasswordinput, ChangePasswordinput,SaveNewPasswordButton, CreateUserbutton, Fromregisterreturnbutton, Returntologinbutton, SearchNoteinp, Settingsinsign, ChangePasswordinsign ]
         firstscreen = [Login, logininput, passwordinput,Loginbutton, Registerbutton, ]
         secondscreen = [CreateNotebutton,sm, settingsbtn, Returntologinbutton,SearchNoteinp]
         thirdscreen = [zametca,SaveNotebutton, Returnbutton]
         fourthscreen = [zametca, Returnbutton, UpdateNotebutton,DeleteNotebutton]
         settingscreen = [languageselector, languageinsign, Returnbutton, nighttheme, nightthemecheck, Settingsinsign]
         insigns = [Settingsinsign, Login, Regl, ChangePasswordinsign]
         buttons = [Loginbutton, Registerbutton, CreateNotebutton, ExtindedRegisterbutton, SaveNotebutton, UpdateNotebutton, Returnbutton, DeleteNotebutton, SecondDeleteNotebutton, SecondUpdateNotebutton, settingsbtn, Deleteaccauntbutton, SecondReturnbutton,  Changepasswordbutton, SaveNewPasswordButton, CreateUserbutton, Fromregisterreturnbutton, Returntologinbutton]

         dbaexist= Path("C:/Users/user/AppData/Roaming/Mi.Notes/savedbafile")
         dbexist= Path("C:/Users/user/AppData/Roaming/Mi.Notes/savedbfile")
         self.textfromnote = ""
         self.forgoodret = False
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
             Savedbafile = open('C:/Users/user/AppData/Roaming/Mi.Notes/savedbafile', "wb")
             pickle.dump(dba, Savedbafile)
             Savedbafile.close()
             registration()
         else:
             readdba = open('C:/Users/user/AppData/Roaming/Mi.Notes/savedbafile', 'rb')
             dba = pickle.load(readdba)
             readdba.close()
         if not dbexist.is_file():
             db = {}
             Savedbfile = open('C:/Users/user/AppData/Roaming/Mi.Notes/savedbfile', "wb")
             pickle.dump(db, Savedbfile)
             Savedbfile.close()
             
         else:
             readdb = open('C:/Users/user/AppData/Roaming/Mi.Notes/savedbfile', 'rb')
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


         if languageindex == 0:
             Loginbutton.setStyleSheet("font-size: 12px; font-family: Tahoma, Verdana; background-color:#66c2ff")
             CreateUserbutton.setStyleSheet("font-size: 14px; font-family: Tahoma, Verdana;")
             Regl.move(130, 105)
         elif languageindex == 2:
             nightthemecheck.move(270,255)



         def SetDarkMode():
             window.setStyleSheet("background-color : #262626")
             zametca.setStyleSheet(" color: #FFF;font-size: 16px; border: 1px solid #e6e6e6; border-radius: 3px; background-color:#666")
             nighttheme.setStyleSheet("font-size: 25px; font-family: Tahoma, Verdana; color:#FFF")
             nightthemecheck.setStyleSheet("color:#FFF; border: 0px solid #FFF;border-radius: 3px;")
             languageselector.setStyleSheet("border: 1px solid #e6e6e6; border-radius: 3px; font-size: 16px; color: #FFF;")
             layout.setStyleSheet("background-color:#333333")
             if self.iffromstart:
                 nightthemecheck.toggle()
             logininput.setStyleSheet("background-color:#666;border: 1px solid #e6e6e6; border-radius: 3px; font-size: 16px; ;color:#FFF")
             passwordinput.setStyleSheet("background-color:#666;border: 1px solid #e6e6e6; border-radius: 3px; font-size: 16px;;color:#FFF")
             SecondChangePasswordinput.setStyleSheet("background-color:#666;border: 1px solid #e6e6e6; border-radius: 3px; font-size: 16px;;color:#FFF")
             ChangePasswordinput.setStyleSheet("background-color:#666;border: 1px solid #e6e6e6; border-radius: 3px; font-size: 16px;;color:#FFF")
             ChangePasswordinsign.setStyleSheet("color: #FFF;font-size: 55px")
             SearchNoteinp.setStyleSheet("background-color:#666;border: 1px solid #e6e6e6; border-radius: 3px; font-size: 16px;;color:#FFF")
             languageinsign.setStyleSheet("color: #FFF;font-size: 25px")
             for i in insigns:
                i.setStyleSheet("color: #FFF;font-size: 55px")
             for i in buttons:
                 i.setStyleSheet('border: 1px solid #e6e6e6;; border-radius: 3px; font-size: 16px; color: #FFF; background-color: #333333')

         if self.nightmodecontrol ==1:
             SetDarkMode()



         self.show()

         def SearchNote():
             for i in self.dbn:
                 vbox.removeWidget(i)
                 i.setVisible(False)
             for i in self.dbn:
                 if SearchNoteinp.text() in i.toPlainText():
                     i.setVisible(True)
                     vbox.addWidget(i)



         def ChangeUser():
             changeuserreply = QMessageBox.question(self, 'Go to Login',
                "Are you sure?", QMessageBox.Yes |
                QMessageBox.No, QMessageBox.No)
             if changeuserreply == QMessageBox.Yes:
                clear()
                setcashdeleting()
                for i in firstscreen:
                  i.setVisible(True)
                logininput.setText("")
                self.adminmodeseted = False
                passwordinput.setText("")

             

         def setcashdeleting():
             savelogin = open('C:/Users/user/AppData/Roaming/Mi.Notes/cash', "wb")
             pickle.dump({0:"user"}, savelogin)
             savelogin.close()




         def setlistofnotes():
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
             whenuserselected()

         def SaveNewPassword():
             if ChangePasswordinput.text() == SecondChangePasswordinput.text() and len(ChangePasswordinput.text()) > 5:
                 dba[self.loginptxt] = ChangePasswordinput.text()
                 writedbainfile()
                 whenuserselected()


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
                adminmode()
             


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
                     SecondUpdateNotebutton.setVisible(True)
                     SecondDeleteNotebutton.setVisible(True)
                     CreateNotebutton.setVisible(False)
                     zametca.setText(self.dbn[self.a].toPlainText())
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
             clear()
             setcashdeleting()
             listofadmins()
             Fromregisterreturnbutton.setVisible(True)
             Fromregisterreturnbutton.setGeometry(20,510, 200, 50)
             ScrollAreaofAdmins.setVisible(True)
             CreateUserbutton.setVisible(True)
             settingsbtn.setVisible(True)
             settingsbtn.setGeometry(230,510, 200, 50)
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
             savethemesets = open('C:/Users/user/AppData/Roaming/Mi.Notes/themesets', "wb")
             savethemesets.truncate()
             pickle.dump(self.nightmodecontrol, savethemesets)
             savethemesets.close()




         def changelanguage(language):
             languageindex = languages[language]
             writelang = open('C:/Users/user/AppData/Roaming/Mi.Notes/langsets', "wb")
             writelang.truncate()
             pickle.dump(languageindex,writelang)
             writelang.close()
             self.cashforlogin = {1:self.loginptxt}
             writecashinfile()
             python = sys.executable
             os.execl(python, python, * sys.argv)




         def writedbinfile():
             Savedbfile = open('C:/Users/user/AppData/Roaming/Mi.Notes/savedbfile', "wb")
             Savedbfile.truncate()
             pickle.dump(db, Savedbfile)
             Savedbfile.close()

         def writedbainfile():
             Savedbafile = open('C:/Users/user/AppData/Roaming/Mi.Notes/savedbafile', "wb")
             Savedbafile.truncate()
             pickle.dump(dba, Savedbafile)
             Savedbafile.close()

         def writecashinfile():
             self.cashforlogin = {1:self.loginptxt}
             savecash = open('C:/Users/user/AppData/Roaming/Mi.Notes/cash', "wb")
             savecash.truncate()
             pickle.dump(self.cashforlogin, savecash)
             savecash.close()

         def savecash():
             oldtime = {(int(datetime.now().strftime("%d"))) * 1440 + (int(datetime.now().strftime("%H"))) *60 + (int(datetime.now().strftime("%M"))+ 15):(int(datetime.now().strftime("%m")))}
             saveoldtime = open('C:/Users/user/AppData/Roaming/Mi.Notes/secash', "wb")
             saveoldtime.truncate()
             pickle.dump(oldtime, saveoldtime)
             saveoldtime.close()
             




         def clear():
             savecash()
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
             if self.loginptxt not in dba and self.loginptxt != "admin":
                 aep.setVisible(False)
                 if not len(pasinptxt)<6:
                     aep.setVisible(False)
                     tsp.setVisible(False)
                     newacc = {self.loginptxt: pasinptxt}
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





         def login():
             if not self.checkforcash:
                self.loginptxt = logininput.text()
                self.passinptxt = passwordinput.text()
             if self.loginptxt in dba and self.loginptxt != "admin":
                 tlde.setVisible(False)
                 if self.passinptxt == dba[self.loginptxt]:
                     writecashinfile()
                     clear()
                     notes()
                     savecash()
                     a = 0
                     self.adminmodeseted = False
                     self.forgoodret = False


                     for i in range(len(self.dbn)):
                         def changenote(a = a):
                             clear()
                             for l in thirdscreen:
                                 l.setVisible(True)
                             self.a = a
                             SecondUpdateNotebutton.setVisible(True)
                             SecondDeleteNotebutton.setVisible(True)
                             CreateNotebutton.setVisible(False)
                             zametca.setText(self.dbn[self.a].toPlainText())
                             self.adminmodeseted = False
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
                     settingsbtn.setGeometry(20,510, 200, 50)

                 else:
                     ipw.setVisible(True)
             elif self.loginptxt == 'admin':
                 if self.passinptxt == "root":
                     adminmode()
             elif self.loginptxt not in dba:
                 tlde.setVisible(True)


         cash = Path('C:/Users/user/AppData/Roaming/Mi.Notes/cash')
         seccash = Path('C:/Users/user/AppData/Roaming/Mi.Notes/secash')
         if not seccash.is_file():
             savetime = open('C:/Users/user/AppData/Roaming/Mi.Notes/secash', "wb")
             pickle.dump({0:13}, savetime)
             savetime.close()
         else:
            readtime = open('C:/Users/user/AppData/Roaming/Mi.Notes/secash', 'rb')
            oldtime = pickle.load(readtime)
            readtime.close()
            for i in oldtime:
                if not oldtime[i] >12:
                    oldminutes = i
                    if oldtime[oldminutes] == int(datetime.now().strftime("%m")) and oldminutes < int(datetime.now().strftime("%d")) * 1440 + int(datetime.now().strftime("%H")) *60 + int(datetime.now().strftime("%M")):
                        savetime = open('C:/Users/user/AppData/Roaming/Mi.Notes/secash', "wb")
                        pickle.dump({0:13}, savetime)
                        savetime.close()
                        setcashdeleting()
             



         if not cash.is_file():
             savelogin = open('C:/Users/user/AppData/Roaming/Mi.Notes/cash', "wb")
             pickle.dump({0:"Alan"}, savelogin)
             savelogin.close()

         else:
             readlogin = open('C:/Users/user/AppData/Roaming/Mi.Notes/cash', 'rb')
             self.cashforlogin = pickle.load(readlogin)
             for i in self.cashforlogin:
                 if i == 1:
                     self.checkforcash = True
                     self.loginptxt = self.cashforlogin[1]
                     self.passinptxt = dba[self.loginptxt]
                     login()

             readlogin.close()




         def newnote():
             clear()
             if not self.adminmodeseted:
                savecash()
             for i in thirdscreen:
                 i.setVisible(True)
             if self.forgoodret:
                 Returnbutton.setVisible(False)
                 SecondReturnbutton.setGeometry(20,510, 200, 50)
                 SecondReturnbutton.setVisible(True)
             zametca.setText("")

         def savenote():
             if not self.adminmodeseted:
                savecash()
             self.note = zametca.toPlainText()
             if len(self.note) >0:
                 UpdateNotebutton.setVisible(True)
                 DeleteNotebutton.setVisible(True)
                 CreateNotebutton.setVisible(False)

                 db[self.loginptxt].append(self.note)
                 writedbinfile()
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
                 self.index = db[self.loginptxt].index(self.note)
                 db[self.loginptxt].remove(self.note)
                 db[self.loginptxt].insert(self.index, self.newnote)
                 self.note = zametca.toPlainText()
                 writedbinfile()
                 zametca.setPlaceholderText(language[14])
             else:
                 zametca.setPlaceholderText(language[15])



         def upnote1():
             if not self.adminmodeseted:
                savecash()
             self.newnote = zametca.toPlainText()
             if len(self.newnote)>0:
                 self.index = db[self.loginptxt].index(self.dbn[self.a].toPlainText())
                 db[self.loginptxt].remove(self.dbn[self.a].toPlainText())
                 db[self.loginptxt].insert(self.index, self.newnote)
                 self.note = zametca.toPlainText()
                 notes()
                 writedbinfile()
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
                index = db[self.loginptxt].index(self.dbn[self.a].toPlainText())
                db[self.loginptxt].pop(index)
                if not self.forgoodret:
                    login()
                else:
                    secondret()
             writedbinfile()
         def nosimpleremove():
             if not self.adminmodeseted:
                savecash()
             secondremovereply = QMessageBox.question(self, 'Delete Note',
                "Are you sure?", QMessageBox.Yes |
                QMessageBox.No, QMessageBox.No)
             if secondremovereply == QMessageBox.Yes:
                db[self.loginptxt].pop(len(db[self.loginptxt])-1)
                if not self.forgoodret:
                     login()
                else:
                     secondret()
                writedbinfile()

             
         def settings():
             clear()
             if not self.adminmodeseted:
                savecash()
             for i in settingscreen:
                 i.setVisible(True)



        #


         CreateNotebutton.clicked.connect(newnote)
         UpdateNotebutton.clicked.connect(upnote)
         Loginbutton.clicked.connect(login)
         SaveNotebutton.clicked.connect(savenote)
         Returnbutton.clicked.connect(ret)
         DeleteNotebutton.clicked.connect(nosimpleremove)
         SecondDeleteNotebutton.clicked.connect(simpleremove)
         SecondUpdateNotebutton.clicked.connect(upnote1)
         Registerbutton.clicked.connect(registration)
         settingsbtn.clicked.connect(settings)
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





if __name__ == '__main__':
    main(window)

    app.exec_()
