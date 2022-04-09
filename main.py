# import Important modules
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtMultimedia
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType

from os import path
import sys,time
import sqlite3

# import UI file
FORM_CLASS,_ = loadUiType(path.join(path.dirname("untitled.ui"),"untitled.ui"))

class mainApp(QMainWindow, FORM_CLASS):
    def __init__(self, parent=None):
        super(mainApp,self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.initui()
        self.auto_complete()          ### auto_compelete
        self.handle_btns()

    def initui(self):
        self.setWindowTitle('برنامج إدارة السيارات')
        self.setWindowIcon(QIcon(r'images\title_icon.png'))
        # self.setIconSize(QSize(100, 100))
        self.tabWidget.tabBar().setVisible(False)

    def handle_btns(self):
        ### Cars_tap_buttons
        self.pushButton.clicked.connect(self.add_Car)
        self.pushButton_2.clicked.connect(self.update_Car)
        self.pushButton_3.clicked.connect(self.delete_Car)

        ### Fuel_tap_functions
        self.pushButton_15.clicked.connect(self.add_Fuel)
        self.pushButton_16.clicked.connect(self.update_Fuel)

        ### Maintenance_tap_buttons
        self.pushButton_14.clicked.connect(self.add_Maintenance)
        self.pushButton_13.clicked.connect(self.update_Maintenance)

        ### Licence_tap_buttons
        self.pushButton_17.clicked.connect(self.add_Licence)
        self.pushButton_18.clicked.connect(self.update_Licence)

        ### Revenue_tap_buttons
        self.pushButton_20.clicked.connect(self.add_Revenue)
        self.pushButton_19.clicked.connect(self.update_Revenue)

        ### Rents_tap_buttons
        self.pushButton_22.clicked.connect(self.add_Rents)
        self.pushButton_21.clicked.connect(self.update_Rents)

        ### Electricity_tap_buttons
        self.pushButton_23.clicked.connect(self.add_Electricity)
        self.pushButton_24.clicked.connect(self.update_Electricity)

        ### search_btn
        self.pushButton_4.clicked.connect(self.search_fun)
        self.tabWidget.currentChanged.connect(self.auto_complete)

    def click_voice(self):
        # produce sound when click
        url = QtCore.QUrl.fromLocalFile(r"D:\Python courses\مشاريع\7\voices\click-voice.wav")
        content = QtMultimedia.QMediaContent(url)
        player = QtMultimedia.QMediaPlayer(self)  # its is important to put self inside, does not work without
        player.setMedia(content)
        player.setVolume(100)
        player.play()

    def auto_complete(self):
        self.names_list = []
        db = sqlite3.connect('database\osama.db')
        cr = db.cursor()
        if self.tabWidget.currentIndex()==0:
            self.names = cr.execute('''select number from car_info''')
        elif self.tabWidget.currentIndex() == 1:
            self.names = cr.execute('''select number from fuel_info''')
        elif self.tabWidget.currentIndex() == 2:
            self.names = cr.execute('''select number from maintenance_info''')
        elif self.tabWidget.currentIndex() == 3:
            self.names = cr.execute('''select number from licence_info''')
        elif self.tabWidget.currentIndex() == 4:
            self.names = cr.execute('''select number from revenues_info''')
        elif self.tabWidget.currentIndex() == 5:
            self.names = cr.execute('''select number from rents_info''')
        elif self.tabWidget.currentIndex() == 6:
            self.names = cr.execute('''select number from water_electricity''')
        for n in self.names:
            self.names_list.append(str(n[0]))
        # create Qcompeleter and add it to Widget
        completer = QCompleter()
        self.lineEdit_67.setCompleter(completer)
        # create model and add list to it
        model = QStringListModel()
        model.setStringList(self.names_list)
        # add model to compeleter
        completer.setModel(model)

    ################################################################################
    ### search_function
    def search_fun(self):
        self.click_voice()
        car_number = int(self.lineEdit_67.text())

        ### Fill all UI_fields
        db = sqlite3.connect('database\osama.db')
        cr1 = db.cursor()
        try:
                if self.tabWidget.currentIndex()==0:
                    a = cr1.execute('''SELECT * FROM car_info WHERE number={}'''.format(car_number))
                    ind0_list = []
                    for n in a.fetchall()[0]:
                        ind0_list.append(n)
                    self.lineEdit.setText(str(ind0_list[0]))
                    self.lineEdit_2.setText(ind0_list[1])
                    self.lineEdit_3.setText(ind0_list[2])
                    self.comboBox.setCurrentText(ind0_list[3])
                    self.lineEdit_5.setText(ind0_list[4])
                    self.lineEdit_6.setText(ind0_list[5])
                    self.comboBox_2.setCurrentText(ind0_list[6])
                    self.lineEdit_7.setText(ind0_list[7])
                    self.lineEdit_8.setText(ind0_list[8])
                    self.lineEdit_9.setText(ind0_list[9])
                    self.lineEdit_10.setText(ind0_list[10])
                    self.lineEdit_11.setText(ind0_list[11])
                    self.lineEdit_12.setText(ind0_list[12])
                    self.statusBar.showMessage('تم عرض المعلومات بنجاح', 6000)

                elif self.tabWidget.currentIndex() == 1:
                    b = cr1.execute('''SELECT * FROM fuel_info WHERE number={}'''.format(car_number))
                    ind0_list = []
                    for n in b.fetchall()[0]:
                        ind0_list.append(n)
                    self.lineEdit_14.setText(ind0_list[1])
                    self.lineEdit_15.setText(ind0_list[2])
                    self.lineEdit_4.setText(ind0_list[3])
                    self.lineEdit_13.setText(ind0_list[4])
                    self.lcdNumber.display(ind0_list[5])
                    self.statusBar.showMessage('تم عرض المعلومات بنجاح', 6000)

                elif self.tabWidget.currentIndex() == 2:
                    c = cr1.execute('''SELECT * FROM maintenance_info WHERE number={}'''.format(car_number))
                    ind0_list = []
                    for n in c.fetchall()[0]:
                        ind0_list.append(n)
                    # print(ind0_list)
                    self.lineEdit_49.setText(ind0_list[1])
                    self.lineEdit_47.setText(ind0_list[2])
                    self.lineEdit_48.setText(ind0_list[3])
                    self.lineEdit_46.setText(ind0_list[4])
                    self.lineEdit_50.setText(ind0_list[5])
                    self.lineEdit_51.setText(ind0_list[6])
                    self.lineEdit_53.setText(ind0_list[7])
                    self.lineEdit_52.setText(ind0_list[8])
                    self.plainTextEdit.setPlainText(ind0_list[9])
                    self.statusBar.showMessage('تم عرض المعلومات بنجاح', 6000)

                elif self.tabWidget.currentIndex() == 3:
                    d = cr1.execute('''SELECT * FROM licence_info WHERE number={}'''.format(car_number))
                    ind0_list = []
                    for n in d.fetchall()[0]:
                        ind0_list.append(n)
                    # print(ind0_list)
                    self.lineEdit_61.setText(ind0_list[1])
                    self.lineEdit_56.setText(ind0_list[2])
                    self.lineEdit_60.setText(ind0_list[3])
                    self.lineEdit_54.setText(ind0_list[4])
                    self.lineEdit_57.setText(ind0_list[5])
                    self.lineEdit_58.setText(ind0_list[6])
                    self.lineEdit_55.setText(ind0_list[7])
                    self.lineEdit_59.setText(ind0_list[8])
                    self.statusBar.showMessage('تم عرض المعلومات بنجاح', 6000)

                elif self.tabWidget.currentIndex() == 4:
                    e = cr1.execute('''SELECT * FROM revenues_info WHERE number={}'''.format(car_number))
                    ind0_list = []
                    for n in e.fetchall()[0]:
                        ind0_list.append(n)
                    # print(ind0_list)
                    self.lineEdit_62.setText(ind0_list[1])
                    self.lineEdit_64.setText(ind0_list[2])
                    self.lineEdit_63.setText(ind0_list[3])
                    self.statusBar.showMessage('تم عرض المعلومات بنجاح', 6000)

                elif self.tabWidget.currentIndex() == 5:
                    f = cr1.execute('''SELECT * FROM rents_info WHERE number={}'''.format(car_number))
                    ind0_list = []
                    for n in f.fetchall()[0]:
                        ind0_list.append(n)
                    # print(ind0_list)
                    self.lineEdit_65.setText(ind0_list[1])
                    self.lineEdit_66.setText(ind0_list[2])
                    self.statusBar.showMessage('تم عرض المعلومات بنجاح', 6000)

                elif self.tabWidget.currentIndex() == 6:
                    g = cr1.execute('''SELECT * FROM water_electricity WHERE number={}'''.format(car_number))
                    ind0_list = []
                    for n in g.fetchall()[0]:
                        ind0_list.append(n)
                    # print(ind0_list)
                    self.lineEdit_68.setText(ind0_list[1])
                    self.lineEdit_69.setText(ind0_list[2])
                    self.statusBar.showMessage('تم عرض المعلومات بنجاح', 6000)

                db.commit()
        except:
            self.lineEdit.setText('')
            self.lineEdit_2.setText('')
            self.lineEdit_3.setText('')
            self.comboBox.setCurrentIndex(0)
            self.lineEdit_5.setText('')
            self.lineEdit_6.setText('')
            self.comboBox_2.setCurrentIndex(0)
            self.lineEdit_7.setText('')
            self.lineEdit_8.setText('')
            self.lineEdit_9.setText('')
            self.lineEdit_10.setText('')
            self.lineEdit_11.setText('')
            self.lineEdit_12.setText('')
            self.lineEdit_14.setText('')
            self.lineEdit_15.setText('')
            self.lineEdit_4.setText('')
            self.lineEdit_13.setText('')
            self.lcdNumber.display('')
            self.lineEdit_49.setText('')
            self.lineEdit_47.setText('')
            self.lineEdit_48.setText('')
            self.lineEdit_46.setText('')
            self.lineEdit_50.setText('')
            self.lineEdit_51.setText('')
            self.lineEdit_53.setText('')
            self.lineEdit_52.setText('')
            self.plainTextEdit.setPlainText('')
            self.lineEdit_61.setText('')
            self.lineEdit_56.setText('')
            self.lineEdit_60.setText('')
            self.lineEdit_54.setText('')
            self.lineEdit_57.setText('')
            self.lineEdit_58.setText('')
            self.lineEdit_55.setText('')
            self.lineEdit_59.setText('')
            self.lineEdit_62.setText('')
            self.lineEdit_64.setText('')
            self.lineEdit_63.setText('')
            self.lineEdit_65.setText('')
            self.lineEdit_66.setText('')
            self.lineEdit_68.setText('')
            self.lineEdit_69.setText('')
            self.statusBar.showMessage('رقم السيارة غير موجود', 6000)

    ################################################################################
    ### Cars_tap_functions
    def add_Car(self):
        self.click_voice()
        db = sqlite3.connect('database\osama.db')
        cr = db.cursor()

        # get data from UI_input_cells
        num = int(self.lineEdit.text())
        owner= self.lineEdit_2.text()
        branch = self.lineEdit_3.text()
        service= self.comboBox.currentText()
        shaceh = self.lineEdit_5.text()
        motor = self.lineEdit_6.text()
        fuel = self.comboBox_2.currentText()
        car = self.lineEdit_7.text()
        model = self.lineEdit_8.text()
        load = self.lineEdit_9.text()
        weight = self.lineEdit_10.text()
        shape = self.lineEdit_11.text()
        color = self.lineEdit_12.text()

        cr.execute('''INSERT INTO car_info(number, owner_company, branch, service_mode, shaceh_number, motor_number, fuel_type, car_type, car_model, car_load, car_weight, car_shape, car_color)
        VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)''',(num,owner,branch,service,shaceh,motor,fuel,car,model,load,weight,shape,color))

        # ### create car_number in all tables
        cr.execute('''INSERT INTO fuel_info(number) VALUES({})'''.format(num))
        cr.execute('''INSERT INTO licence_info(number) VALUES({})'''.format(num))
        cr.execute('''INSERT INTO maintenance_info(number) VALUES({})'''.format(num))
        cr.execute('''INSERT INTO rents_info(number) VALUES({})'''.format(num))
        cr.execute('''INSERT INTO revenues_info(number) VALUES({})'''.format(num))
        cr.execute('''INSERT INTO water_electricity(number) VALUES({})'''.format(num))
        db.commit()

        self.lineEdit.setText('')
        self.lineEdit_2.setText('')
        self.lineEdit_3.setText('')
        self.comboBox.setCurrentIndex(0)
        self.lineEdit_5.setText('')
        self.lineEdit_6.setText('')
        self.comboBox_2.setCurrentIndex(0)
        self.lineEdit_7.setText('')
        self.lineEdit_8.setText('')
        self.lineEdit_9.setText('')
        self.lineEdit_10.setText('')
        self.lineEdit_11.setText('')
        self.lineEdit_12.setText('')

        self.auto_complete()   ## add new added car_number to auto_complete_search_bar
        self.statusBar.showMessage('تم إضافة المعلومات بنجاح', 6000)

    def update_Car(self):
        self.click_voice()
        db = sqlite3.connect('database\osama.db')
        cr = db.cursor()

        # get data from UI_input_cells
        num = int(self.lineEdit.text())
        owner = self.lineEdit_2.text()
        branch = self.lineEdit_3.text()
        service = self.comboBox.currentText()
        shaceh = self.lineEdit_5.text()
        motor = self.lineEdit_6.text()
        fuel = self.comboBox_2.currentText()
        car = self.lineEdit_7.text()
        model = self.lineEdit_8.text()
        load = self.lineEdit_9.text()
        weight = self.lineEdit_10.text()
        shape = self.lineEdit_11.text()
        color = self.lineEdit_12.text()

        # ### update car_data
        cr.execute('''UPDATE car_info SET owner_company='{}', branch='{}', service_mode='{}', shaceh_number='{}', motor_number='{}', fuel_type='{}', car_type='{}', car_model='{}', car_load='{}', car_weight='{}', car_shape='{]', car_color='{}' WHERE number={}'''.format(owner, branch, service, shaceh, motor, fuel, car, model, load, weight, shape, color, num))
        db.commit()
        db.close()

        self.lineEdit.setText('')
        self.lineEdit_2.setText('')
        self.lineEdit_3.setText('')
        self.comboBox.setCurrentIndex(0)
        self.lineEdit_5.setText('')
        self.lineEdit_6.setText('')
        self.comboBox_2.setCurrentIndex(0)
        self.lineEdit_7.setText('')
        self.lineEdit_8.setText('')
        self.lineEdit_9.setText('')
        self.lineEdit_10.setText('')
        self.lineEdit_11.setText('')
        self.lineEdit_12.setText('')

    def delete_Car(self):
        self.click_voice()
        db = sqlite3.connect('database\osama.db')
        cr = db.cursor()
        index = int(self.lineEdit_67.text())
        cr.execute('''DELETE FROM car_info WHERE number={}'''.format(index))
        db.commit()

        ###clear cells after delete
        self.lineEdit_67.setText('')
        self.lineEdit.setText('')
        self.lineEdit_2.setText('')
        self.lineEdit_3.setText('')
        self.comboBox.setCurrentIndex(0)
        self.lineEdit_5.setText('')
        self.lineEdit_6.setText('')
        self.comboBox_2.setCurrentIndex(0)
        self.lineEdit_7.setText('')
        self.lineEdit_8.setText('')
        self.lineEdit_9.setText('')
        self.lineEdit_10.setText('')
        self.lineEdit_11.setText('')
        self.lineEdit_12.setText('')
        self.lineEdit_14.setText('')
        self.lineEdit_15.setText('')
        self.lineEdit_4.setText('')
        self.lineEdit_13.setText('')
        self.lcdNumber.display('')
        self.lineEdit_49.setText('')
        self.lineEdit_47.setText('')
        self.lineEdit_48.setText('')
        self.lineEdit_46.setText('')
        self.lineEdit_50.setText('')
        self.lineEdit_51.setText('')
        self.lineEdit_53.setText('')
        self.lineEdit_52.setText('')
        self.plainTextEdit.setPlainText('')
        self.lineEdit_61.setText('')
        self.lineEdit_56.setText('')
        self.lineEdit_60.setText('')
        self.lineEdit_54.setText('')
        self.lineEdit_57.setText('')
        self.lineEdit_58.setText('')
        self.lineEdit_55.setText('')
        self.lineEdit_59.setText('')
        self.lineEdit_62.setText('')
        self.lineEdit_64.setText('')
        self.lineEdit_63.setText('')
        self.lineEdit_65.setText('')
        self.lineEdit_66.setText('')
        self.lineEdit_68.setText('')
        self.lineEdit_69.setText('')

    ################################################################################
    ### Fuel_tap_functions
    def add_Fuel(self):
        self.click_voice()

    def update_Fuel(self):
        self.click_voice()


    ################################################################################
    ### Maintenance_tap_functions
    def add_Maintenance(self):
        self.click_voice()

    def update_Maintenance(self):
        self.click_voice()

    ################################################################################
    ### Licence_tap_functions
    def add_Licence(self):
        self.click_voice()

    def update_Licence(self):
        self.click_voice()

    ################################################################################
    ### Revenue_tap_functions
    def add_Revenue(self):
        self.click_voice()

    def update_Revenue(self):
        self.click_voice()

    ################################################################################
    ### Rents_tap_functions
    def add_Rents(self):
        self.click_voice()

    def update_Rents(self):
        self.click_voice()

    ################################################################################
    ### Electricity_tap_functions
    def add_Electricity(self):
        self.click_voice()

    def update_Electricity(self):
        self.click_voice()

    ################################################################################
    ### Reports_tap_functions



def main():
    app = QApplication(sys.argv)
    window = mainApp()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()