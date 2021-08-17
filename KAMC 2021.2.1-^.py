from io import StringIO
import os
import os.path

print("KCS AutoMacchanger 2021.2.1-^")
print("GUİ moduna geçmek için : 0")
print("Gerekli Paketleri Kurmak İçin : 1")
print("Gerekli Paketleri Kurmak Artından Mac Değiştirmek İçin : 2")
print("Sadece Mac Değiştirmek İçin : 3")
print("Ağ Cihazını Metin Belgesine Kaydetmek İçin : 4")
print("Metin Belgesine Kayıt Edilmiş Ağ Cihazını Kullanmak İçin : 5")
print("Hakkında Kısmına Bakmak İçin : 6")
secenekler = input("")
if secenekler == "0":


 from PyQt5 import QtCore, QtGui, QtWidgets
 class Ui_Form(object):
    def bas4(self):
        import os
        if os.system('xterm -e "ifconfig; sleep 300"') == 0:
            self.label_3.setText("Xterm Başarıyla Başlatıldı.")
        else:
            self.label_3.setText("Eksik Paket Mevcut. (xterm)")

    def bas3(self):
        from io import StringIO
        import os
        import os.path
        import subprocess

        import os

        def alan():
            if os.system('macchanger') == 0:
                if os.system('ifconfig') == 0:
                    try:
                        with open("agcihazi.txt", "r") as f:
                            icerik = f.read()
                            agcihazi = icerik
                            if agcihazi == "":
                                self.label_3.setText("agcihazı.txt boş olduğundan işlem uygulanamıyor.")
                            else:
                                if os.system(
                                        "sudo ifconfig " + agcihazi + " down && sudo macchanger -r " + agcihazi + " && sudo ifconfig " + agcihazi + " up") == 0:

                                    self.label_3.setText("Komut Başarıyla Uygulandı.")
                                else:
                                    self.label_3.setText("Komut Uygulanamadı Bir Sorun Var. Terminali Kontrol Edin.")
                    except FileNotFoundError:
                        self.label_3.setText("agcihazi.txt dosyasına erişilemiyor.")



                else:
                    print("Eksik Paketler Mevcut.")
                    self.label_3.setText("Eksik Paket Mevcut. (ifconfig)")
            else:
                self.label_3.setText("Eksik Paket Mevcut. (macchanger)")

        alan()

    def bas2(self):
        yazi = self.textEdit.toPlainText()
        self.textEdit.setPlainText(yazi)
        if yazi == "":

            self.label_3.setText("Ağ Cihazını Girin.")

        else:

            with open("agcihazi.txt", "w") as f:
                agcihazi2 = yazi
                f.write(agcihazi2)
                self.label_3.setText("Ağ Cihazı Kayıt Edildi.")

    def bas1(self):

        yazi = self.textEdit.toPlainText()
        self.textEdit.setPlainText(yazi)
        if yazi == "":
            self.label_3.setText("Ağ Cihazını Girin.")

        else:
            from io import StringIO
            import os
            import os.path
            import subprocess
            agcihazi = yazi

            import os

            def alan():
                if os.system('macchanger') == 0:
                    if os.system('ifconfig') == 0:
                        if os.system(
                                "sudo ifconfig " + agcihazi + " down && sudo macchanger -r " + agcihazi + " && sudo ifconfig " + agcihazi + " up") == 0:

                            self.label_3.setText("Komut Başarıyla Uygulandı.")
                        else:
                            self.label_3.setText("Komut Uygulanamadı Bir Sorun Var. Terminali Kontrol Edin.")
                    else:
                        print("Eksik Paketler Mevcut.")
                        self.label_3.setText("Eksik Paketler Mevcut. (ifconfig)")
                else:
                    self.label_3.setText("Eksik Paketler Mevcut. (macchanger)")

            alan()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(643, 308)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(120, 170, 481, 17))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(120, 10, 401, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 50, 401, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(120, 90, 401, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(120, 190, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(120, 130, 401, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(-10, 270, 1141, 51))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(110, 10, 1501, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.pushButton.clicked.connect(self.bas1)
        self.pushButton_2.clicked.connect(self.bas2)
        self.pushButton_3.clicked.connect(self.bas3)

        self.pushButton_5.clicked.connect(self.bas4)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "KCS AutoMacchangerGUİ 2021.1.1-^"))
        self.label.setText(_translate("Form", "Ağ cihazını yazın örnek : wlp3s0 veya wlan0"))
        self.pushButton.setText(_translate("Form", "Mac Adresini Değiştir"))
        self.pushButton_2.setText(_translate("Form", "Ağ Cihazını Metin Belgesine Kaydet"))
        self.pushButton_3.setText(_translate("Form", "Kayıt Edilmiş Ağ Cihazını Kullan"))

        self.pushButton_5.setText(_translate("Form", "Ağ Bilgilerini Xterm İle Göster"))
        self.label_3.setText(_translate("Form", "İşlem Yok"))
        self.label_2.setText(_translate("Form", "Durum : "))


 if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
if secenekler == "1":
    print("Hangi dağıtımı kullanıyorsunuz?")
    print("ARCH : 1")
    print("OPENSUSE : 2")
    print("Debian & Ubuntu : 3")
    print("Fedora : 4")
    dagitim = input("")

    if dagitim == "1":
     os.system("pacman -Syy")
     os.system("pacman -S net-tools-deprecated")
     os.system("pacman -S macchanger")
     os.system("pacman -S python3-pip")
     os.system("pacman -S xterm")
     os.system("pip install pyqt5")
     print("İşlem tamamlandi!")
     
    if dagitim == "2":
     os.system("zypper refresh")
     os.system("zypper install net-tools-deprecated")
     os.system("zypper install macchanger")
     os.system("zypper install python3-pip")
     os.system("pip install pyqt5")
     os.system("zypper install xterm")
     print("İşlem tamamlandi!")
  
  
    if dagitim == "3":
     os.system("apt update")
     os.system("apt install net-tools -y")
     os.system("apt install macchanger -y")
     os.system("apt install python3-pip")
     os.system("pip install pyqt5")
     os.system("apt install xterm -y")
     print("İşlem tamamlandi!")
    if dagitim == "4":
     os.system("dnf upgrade --refresh")
     os.system("dnf install net-tools")
     os.system("dnf install net-tools-deprecated")
     os.system("dnf install macchanger")
     os.system("dnf install python3-pip")
     os.system("pip install pyqt5")
     os.system("apt install xterm -y")
     print("İşlem tamamlandi!")
if secenekler == "2":
    print("Hangi dağıtımı kullanıyorsunuz?")
    print("ARCH : 1")
    print("OPENSUSE : 2")
    print("Debian & Ubuntu : 3")
    print("Fedora : 4")

    dagitim = input("")
    if dagitim == "1":
     os.system("pacman -Syy")
     os.system("pacman -S net-tools-deprecated")
     os.system("pacman -S macchanger")
     os.system("pacman -S xterm")
     os.system("pacman -S python3-pip")
     os.system("pip install pyqt5")
     os.system("ifconfig")
     print("Ağcihazi komutu şuna benzer wlp3s0 wlp2s0 veya wlan0 ağ aygıtı kısmına benzer kodu girin.")
     agcihazi = input("Ağ aygiti girin:")   
     os.system("sudo ifconfig "+ agcihazi + " down && sudo macchanger -r "+ agcihazi+" && sudo ifconfig "+ agcihazi +" up")
     print("İşlem tamamlandi!")

    if dagitim == "2":
     os.system("zypper refresh")
     os.system("zypper install net-tools-deprecated")
     os.system("zypper install macchanger")
     os.system("zypper install xterm")
     os.system("zypper install python3-pip")
     os.system("pip install pyqt5")
     os.system("ifconfig")
     print("Ağcihazi komutu şuna benzer wlp3s0 wlp2s0 veya wlan0 ağ aygıtı kısmına benzer kodu girin.")
     agcihazi = input("Ağ aygiti girin:")   
     os.system("sudo ifconfig "+ agcihazi + " down && sudo macchanger -r "+ agcihazi+" && sudo ifconfig "+ agcihazi +" up")
     print("İşlem tamamlandi!")
  
  
    if dagitim == "3":
     os.system("apt update")
     os.system("apt install net-tools -y")
     os.system("apt install macchanger -y")
     os.system("apt install python3-pip")
     os.system("pip install pyqt5")
     os.system("apt install xterm -y")
     os.system("ifconfig")
     print("Ağcihazi komutu şuna benzer wlp3s0 wlp2s0 veya wlan0 ağ aygıtı kısmına benzer kodu girin.")
     agcihazi = input("Ağ aygiti girin:")   
     os.system("sudo ifconfig "+ agcihazi + " down && sudo macchanger -r "+ agcihazi+" && sudo ifconfig "+ agcihazi +" up")
     print("İşlem tamamlandi!")
    if dagitim == "4":
     os.system("dnf upgrade --refresh")
     os.system("dnf install net-tools")
     os.system("dnf install net-tools-deprecated")
     os.system("dnf install python3-pip")
     os.system("pip install pyqt5")
     os.system("dnf install xterm")
     os.system("dnf install macchanger")
     print("İşlem tamamlandi!")
     os.system("ifconfig")
     print("Ağcihazi komutu şuna benzer wlp3s0 wlp2s0 veya wlan0 ağ aygıtı kısmına benzer kodu girin.")
     agcihazi = input("Ağ aygiti girin:")   
     os.system("sudo ifconfig "+ agcihazi + " down && sudo macchanger -r "+ agcihazi+" && sudo ifconfig "+ agcihazi +" up")
     print("İşlem tamamlandi!")
if secenekler == "3":
  
    os.system("ifconfig")
    print("Ağcihazi komutu şuna benzer wlp3s0 wlp2s0 veya wlan0 ağ aygıtı kısmına benzer kodu girin.")
    agcihazi = input("Ağ aygiti girin:")   
 
    os.system("sudo ifconfig "+ agcihazi + " down && sudo macchanger -r "+ agcihazi+" && sudo ifconfig "+ agcihazi +" up")
    print("İşlem tamamlandi!")
    os.system("exit")

if secenekler == "4":
     os.system("ifconfig")
     print("Kayıt edilecek ağ aygıtını girin.")
     print("Ağcihazi komutu şuna benzer wlp3s0 wlp2s0 veya wlan0 ağ aygıtı kısmına benzer kodu girin.")
     agcihazi = input("Ağ aygiti girin:")   
     with open("agcihazi.txt", "w") as f:
         agcihazi2 = agcihazi
         f.write(agcihazi2)
         print("agcihazi.txt kayıt edildi.")
         os.system("exit")
if secenekler == "5":
   with open("agcihazi.txt","r") as f:
       icerik = f.read() 
       agcihazi = icerik
       os.system("sudo ifconfig "+ agcihazi + " down && sudo macchanger -r "+ agcihazi+" && sudo ifconfig "+ agcihazi +" up")
       print("İşlem tamamlandi!")

       os.system("exit")
       pass
if secenekler == "6":
 print("Yeni Yapımcı : Arda KC : Eski Yapımcı Furkan Karasu.")
pass
