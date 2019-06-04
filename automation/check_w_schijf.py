import openpyxl
import datetime
import shutil

filename = 'W:/03_Ondersteuning/03_03_ICT/Prive/Infra/Storage/W-schijf-storage-afname.xlsx'

class WChecker():

  def __init__(self, bestand):
    # totale storage
    self.w_total_stor = shutil.disk_usage('w:/').total / 1024 / 1024 / 1024

    # laad werkboek
    self.doc = openpyxl.load_workbook(bestand)
    self.bestand = bestand

    # laad sheet
    self.sheet = self.doc['Plot']

    # kolom C: datums
    self.col_c = self.sheet['C']

    # kolom D: % vrij
    self.col_d = self.sheet['D']

    # laatste rij index + 1 om lege te vinden
    self.new_index = self.col_c[-1].row + 1
  

  def _storage_left(self):
    return shutil.disk_usage('w:/').free / 1024 / 1024 / 1024


  def add_date(self):
    # datum aan kol c in nieuwe rij toevoegen
    self.datum_cel = self.sheet[f"C{self.new_index}"]
    # self.datum_cel.style = self.col_c[-1].style
    self.datum_cel.value = datetime.date.today()


  def add_storage_left(self):
    self.storage_cel = self.sheet[f"D{self.new_index}"]
    self.storage_cel.value = self._storage_left() / self.w_total_stor * 100


  def save(self):
    # wijzigingen opslaan    
    self.doc.save(self.bestand)


  def do(self):
    self.add_date()
    self.add_storage_left()
    self.add_date()
    self.save()


if __name__ == "__main__":
  checker = WChecker(filename)
  checker.do()
  