import csv
from itertools import islice
import dns
from dns import resolver


def laad_csv_bestand(bestand: str):
  with open(bestand) as csvfile:
    lees_csv = csv.reader(csvfile, delimiter=",")
    lijst = []
    for rij in (lees_csv):
      lijst.append(rij)
    for rij in lijst[3:]:
      print(f"{rij[10]}: \n{check_mx_record(rij[10])}")

    

def check_mx_record(email: str):
  mijnResolver = resolver.Resolver()  
  mijnAntwoorden = mijnResolver.query(email.split('@')[1], "MX")
  for answer in mijnAntwoorden:
    print(answer)


laad_csv_bestand("stemformulier_kempenaar_2019.csv")