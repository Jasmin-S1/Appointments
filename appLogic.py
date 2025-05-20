import calendar
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import Qt, QTimer
from mainwindow import Ui_MainWindow
from newPatientLogic import NewPatientDialog
from newAppointmentLogic import NewAppointmentDialog
from database_operation import get_patients_from_database
from datetime import datetime
import calendar
import ast
from sqlalchemy import text
from database import get_db_session
from newAppointmentLogic import NewAppointmentDialog
from dateutil.relativedelta import relativedelta
import sys

class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
    
        self.setFixedSize(1920, 990)

        self.ui.patientsButton.clicked.connect(self.show_all_patients)
        self.ui.addNewPatientButton.clicked.connect(self.open_new_patient_form)
        self.ui.addNewAppointmentButton.clicked.connect(self.open_new_appointment_form)

        self.ui.patientsButton.clicked.connect(self.change_buton_style)
        self.ui.appointmentsButton.clicked.connect(self.change_buton_style)
        self.ui.appointmentsButton.clicked.connect(lambda: (self.ui.stackedWidget.setCurrentIndex(0),
                                                            self.buttonGroup1.setExclusive(False),
                                                            self.ui.monthlyButton.setChecked(True),
                                                            self.buttonGroup1.setExclusive(True)))
        self.ui.statisticsButton.clicked.connect(self.change_buton_style)
        self.ui.dailyButton.clicked.connect(lambda: (self.ui.stackedWidget.setCurrentIndex(1),
                                                    self.buttonGroup.setExclusive(False),
                                                    self.ui.appointmentsButton.setChecked(True),
                                                    self.ui.patientsButton.setChecked(False),
                                                    self.buttonGroup.setExclusive(True)))
        self.ui.monthlyButton.clicked.connect(lambda: (self.ui.stackedWidget.setCurrentIndex(0),
                                                       self.buttonGroup.setExclusive(False),
                                                       self.ui.appointmentsButton.setChecked(True),
                                                       self.ui.patientsButton.setChecked(False),
                                                       self.buttonGroup.setExclusive(True)))
        
        self.ui.monthlyAppointsTable.cellClicked.connect(self.select_day)
        
        
        

        self.ui.dailyAppointsTable.setHorizontalHeaderLabels(["09:00", "09:30", "10:00", "10:30", "11:00", "11:30", "12:00", "12:30", "13:00", "13:30", "14:00", "14:30", "15:00", "15:30", "16:00"])        
        self.ui.dailyAppointsTable.verticalHeader().setFixedWidth(1)
        self.ui.dailyAppointsTable.verticalHeader().setVisible(True)
        self.ui.monthlyAppointsTable.verticalHeader().setFixedWidth(1)
        
        
      
        
        self.current_date = datetime.now().replace(day=1)
        self.update_month_year_label()
        self.get_calendar()
        QTimer.singleShot(0, self.fill_daily_table)
        self.ui.nextMonthButton.clicked.connect(lambda: self.change_month(+1))
        self.ui.previousMonthButton.clicked.connect(lambda: self.change_month(-1))

        self.ui.dateLabel.setText(datetime.now().strftime("%A, %d.%m.%Y"))
        

        self.buttonGroup = QtWidgets.QButtonGroup(self)
        self.buttonGroup.setExclusive(True)
        buttons = [self.ui.patientsButton,
                   self.ui.appointmentsButton,
                   self.ui.statisticsButton]
        for button in buttons:
            self.buttonGroup.addButton(button)
        self.ui.appointmentsButton.setChecked(True)


        self.buttonGroup1 = QtWidgets.QButtonGroup(self)
        self.buttonGroup1.setExclusive(True)
        buttons1 = [self.ui.filterButton,
                    self.ui.searchButton,
                    self.ui.dailyButton,
                    self.ui.monthlyButton]
        for button in buttons1:
            self.buttonGroup1.addButton(button)
        self.ui.monthlyButton.setChecked(True)

    def open_new_patient_form(self):
        self.new_patient_dialog = NewPatientDialog(self)
        self.new_patient_dialog.exec_()
        

    def open_new_appointment_form(self):
        month, year = self.ui.monthYearLabel.text().split(", ")
        if not hasattr(self, "selected_day") or self.selected_day is None:
            QtWidgets.QMessageBox.warning(self, "Warning", "Please select a date first.")
            return
        self.new_appointment_dialog = NewAppointmentDialog(self.selected_day, month, year)
        self.new_appointment_dialog.exec_()
    
 

    def select_day(self, row, column):
        item = self.ui.monthlyAppointsTable.item(row, column)
        if item and item.text():
            self.selected_day = int(item.text())
        else:
            self.selected_day = None


    def show_all_patients(self):
        patients_data = get_patients_from_database(self)
        self.ui.tableWidgetPatients.setRowCount(0)
        for row in patients_data:
            row_position = self.ui.tableWidgetPatients.rowCount()
            self.ui.tableWidgetPatients.insertRow(row_position)
            for column_index, value in enumerate(row):
                self.ui.tableWidgetPatients.setItem(row_position, column_index, QtWidgets.QTableWidgetItem(str(value)))
        self.ui.stackedWidget.setCurrentIndex(2)
        self.buttonGroup1.setExclusive(False)
        self.ui.monthlyButton.setChecked(False)
        self.ui.dailyButton.setChecked(False)
        self.buttonGroup1.setExclusive(True)

    
    def update_month_year_label(self):
        current_month = self.current_date.strftime("%B")
        current_year = self.current_date.year
        self.ui.monthYearLabel.setText(f"{current_month}, {current_year}")
    
    def get_calendar(self):
        current_month_name, current_year = self.ui.monthYearLabel.text().split(", ")
        month = list(calendar.month_name).index(current_month_name)
        month_days = calendar.monthcalendar(int(current_year), int(month))

        for row_index, week in enumerate(month_days):
            for column_index, day in enumerate(week):
                if day != 0:
                    item = QtWidgets.QTableWidgetItem(str(day))
                    item.setFont(QtGui.QFont("", 14))
                    current_date = datetime.now()
                    if (day == current_date.day and int(month) == current_date.month and int(current_year) == current_date.year):
                        item.setBackground(QtGui.QColor(230, 230, 230))
                    self.ui.monthlyAppointsTable.setItem(row_index, column_index, item)
                        
                else:
                    self.ui.monthlyAppointsTable.setItem(row_index, column_index, QtWidgets.QTableWidgetItem(""))
    
    def fill_daily_table(self):
        daily_appointments_date = datetime.today().strftime("%Y-%m-%d")
        session = next(get_db_session())  
        query = text("""SELECT patient, treatment, appoint_time FROM appointments WHERE appoint_day = :daily_appointments_date""")
        result = session.execute(query, {"daily_appointments_date": daily_appointments_date})
        patients_daily_appointments = result.fetchall()
        column_count = self.ui.dailyAppointsTable.columnCount()
        for patient_data, treatment, appointments_times in patients_daily_appointments:
            patient = ast.literal_eval(patient_data)[0]
            for column in range(column_count):
                header_name = self.ui.dailyAppointsTable.horizontalHeaderItem(column)
                if header_name.text() == appointments_times.strftime("%H:%M"):
                    cell_item =  QtWidgets.QTableWidgetItem(f"{patient}\n\n{treatment}")
                    cell_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                    self.ui.dailyAppointsTable.setItem(0, column, cell_item) 
                    break


            

    def change_month(self, offset):
        self.current_date = self.current_date + relativedelta(months=offset)
        self.update_month_year_label()
        self.get_calendar()
       


    def change_buton_style(self):
        clicked_button = self.sender()
        button_text = clicked_button.text()
        self.ui.logoText.setText(button_text)

    def center_window(self):
        screen = QtWidgets.QApplication.primaryScreen().availableGeometry()   
        window = self.frameGeometry()
        x = (screen.width() - window.width()) // 2
        y = (screen.height() - window.height()) // 2
        self.move(x, y)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    window.center_window()
    sys.exit(app.exec_())