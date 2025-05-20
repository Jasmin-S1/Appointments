from PyQt5 import QtWidgets, QtCore
from sqlalchemy import text
from database import get_db_session
from newAppointment import Ui_Dialog


class NewAppointmentDialog(QtWidgets.QDialog):
    def __init__(self, selected_day, month, year, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.WindowTitleHint | QtCore.Qt.WindowCloseButtonHint)
        
        self.ui.saveNewAppointmentButton.clicked.connect(self.save_new_appointment)

        self.selected_day = selected_day
        self.month = month
        self.year = year
        self.ui.dateText.setText(f"{self.selected_day} {month} {year}")

        self.populate_patients_combobox()
        self.populate_treatment_combobox()
        self.populate_time_combobox()
      

        
    def get_patients_from_db(self):
        session = next(get_db_session())
        try:
            query = text("""SELECT name_surname,year_of_birth, address FROM patients""")
            result = session.execute(query).fetchall()
            names_surnames = [row[0] for row in result]
            year_of_birth = [row[1] for row in result]
            address = [row[2] for row in result]
            return names_surnames, year_of_birth, address
        except Exception as e:
                session.rollback()
                QtWidgets.QMessageBox.critical(self, "Error", f"An error: {e}!")
        finally:
             session.close()

    def populate_patients_combobox(self):
        patients = self.get_patients_from_db()
        items_for_combobox = list(zip(*patients))    
        for item in items_for_combobox:
            display_patient_info = f"{item[0]} | {item[1]} | {item[2]}"
            self.ui.comboBoxPatients.addItem(display_patient_info, item)

   
    def populate_treatment_combobox(self):
        treatment_list = ["Vadjenje zuba", 
                      "Popravljanje zuba", 
                      "Lijecenje zuba", 
                      "Ciscenje zubi",
                      "Izbjeljivanje zubi",
                      "Kontrola",
                      "Postavljanje proteze",
                      "Izrada navlaka",
                    ]
        for item in treatment_list:
             self.ui.comboBoxTreatment.addItem(item)

    def populate_time_combobox(self):
        selected_date = self.ui.dateText.text().strip()
        session = next(get_db_session())
        query = text("""SELECT appoint_time FROM appointments WHERE appoint_day = :selected_date""")
        result = session.execute(query, {"selected_date": selected_date})
        selected_appointments = [row[0] for row in result.fetchall()]
        selected_appointments_str = [appointments_time.strftime("%H:%M") for appointments_time in selected_appointments]

        appointmens_time_list = ["09:00", "09:30", "10:00", "10:30",
                                 "11:00", "11:30", "12:00", "12:30", 
                                 "13:00", "13:30", "14:00", "14:30", 
                                 "15:00", "15:30", "16:00"]
        
        free_appointments = sorted(set(appointmens_time_list) - set(selected_appointments_str))
        
        for item in free_appointments:
             self.ui.comboBoxTime.addItem(item)

    
    def save_new_appointment(self):
        appoint_day = self.ui.dateText.text().strip()
        appoint_time = self.ui.comboBoxTime.currentText().strip()
        treatment = self.ui.comboBoxTreatment.currentText().strip()
        patient_data = self.ui.comboBoxPatients.currentData()
        patient = f"{patient_data[0], patient_data[1], patient_data[2]}"

        appointment_data = [appoint_day, appoint_time, treatment, patient]

        if not all([appoint_day, appoint_time, treatment, patient]):
            QtWidgets.QMessageBox.warning(self, "Warning", "Fill all required fields!")
            return
        
        session = next(get_db_session())
        try: 
            query = text("""INSERT INTO appointments (appoint_day, appoint_time, treatment, patient)
                   VALUES (:appoint_day, :appoint_time, :treatment, :patient)""")
        
            session.execute(query, {
                    'appoint_day': appoint_day,
                    'appoint_time': appoint_time,
                    'treatment': treatment,
                    'patient': patient
                  
                })
            session.commit()
        
            QtWidgets.QMessageBox.information(self, "Success", "New appointment added!")
            self.close()

        except Exception as e:
            session.rollback()
            QtWidgets.QMessageBox.critical(self, "Error", f"An error: {e}!")
        finally:
            session.close()



