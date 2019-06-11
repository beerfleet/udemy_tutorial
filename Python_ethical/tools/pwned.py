import requests
from pprint import pprint
from hashlib import sha1

user_agent = {'User-Agent': 'ETION-pw-security'}
base_url = 'https://haveibeenpwned.com/api/v2/'

def is_my_account_hacked(account):
  url = f"{base_url}breachedaccount/{account}?includeUnverified=true"
  request = requests.get(url, user_agent)
  if request.ok:
    for el in request.json():
      print(f"\n{el}\n")
  else:
    print("Er is nog geen lek bekend met uw emailadres !")

def is_my_password_known(keuze):
  # url = f"{base_url}pwnedpassword/{keuze}"
  m = sha1()  
  m.update(f"{keuze}".encode("utf-8"))
  hex_digest = m.hexdigest()
  head_hex_digest = hex_digest[:5]
  url = f"https://api.pwnedpasswords.com/range/{head_hex_digest}"
  request = requests.get(url, user_agent)
  pwned = []
  for el in request:
    tail_hex_digest = hex_digest[5:]
    if tail_hex_digest.upper() in el.decode():
      lines = el.decode().split('\r\n')
      for line in lines:
        if tail_hex_digest.upper() in line:
          pwned = line.split(':')
  if pwned:
    print(f"Uw wachtwoord is al {pwned[1]} keer gekaapt")
  else:
    print(f"Uw wachtwoord is voorlopig veilig")


if __name__ == "__main__":
  menu_str = "[1] Nagaan of uw account ooit gekaapt is ; [2] Nagaan of uw wachtwoord gelekt / al in gebruik is ; [q] Stoppen : "
  keuze = ''
  keuze = input(menu_str)
  while keuze in '12' and keuze != 'q':
    if keuze == '1':
      account = input("Vul hier uw emailadres in: ")
      is_my_account_hacked(account)
    elif keuze == '2':
      paswoord = input("Vul hier uw op te zoeken wachtwoord in: ")
      is_my_password_known(paswoord)
    print(f"\nWil u nog een opzoeking doen ?: ")
    keuze = input(menu_str)

