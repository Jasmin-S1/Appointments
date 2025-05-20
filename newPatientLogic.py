from PyQt5 import QtWidgets, QtCore
from newPatient import Ui_Dialog
from sqlalchemy import text
from database import get_db_session


class NewPatientDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.WindowTitleHint | QtCore.Qt.WindowCloseButtonHint)
        
        self.ui.saveNewPatientButton.clicked.connect(self.save_new_patient)

    def save_new_patient(self):
        name_surname = self.ui.nameLineEdit.text().strip()
        year_of_birth = self.ui.yearsLineEdit.text().strip()
        gender = "Male" if self.ui.radioButtonMale.isChecked() else "Female"
        address = self.ui.comboBox.currentText().strip()
        phone_number = self.ui.phoneLineEdit.text().strip()
        if len(name_surname.split()) < 2:
            QtWidgets.QMessageBox.warning(self, "Warning", "Please enter both first and last name.")
            return
        try:
            year_of_birth = int(year_of_birth)
            current_year = QtCore.QDate.currentDate().year()
            if year_of_birth < 1900 or year_of_birth > current_year:
                QtWidgets.QMessageBox.warning(self, "Warning", "Please enter a valid year of birth.")
                return
        except ValueError:
            QtWidgets.QMessageBox.warning(self, "Warning", "Year of birth must be a number.")
            return

        patient_data = [name_surname, year_of_birth, gender, address, phone_number]

        if not all([name_surname, year_of_birth, gender, address, phone_number]):
            QtWidgets.QMessageBox.warning(self, "Warning", "Fill all required fields!")
            return
        

        session = next(get_db_session())
        try: 
            query = text("""INSERT INTO patients (name_surname, year_of_birth, address, phone_number, gender)
                   VALUES (:name_surname, :year_of_birth, :address, :phone_number, :gender)""")
        
        
            session.execute(query, {
                    'name_surname': name_surname,
                    'year_of_birth': year_of_birth,
                    'address': address,
                    'phone_number': phone_number,
                    'gender': gender
                })
            session.commit()
        
            QtWidgets.QMessageBox.information(self, "Success", "New patient added!")
            self.close()

        except Exception as e:
            session.rollback()
            QtWidgets.QMessageBox.critical(self, "Error", f"An error: {e}!")
        finally:
            session.close()

        
            
