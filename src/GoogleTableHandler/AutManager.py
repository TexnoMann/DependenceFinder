import json

import gspread
import getpass
from oauth2client.service_account import ServiceAccountCredentials


def authorized():
    while True:
        autkey = input("Введите путь до ключа аутентификации: ")
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        try:
            creds = ServiceAccountCredentials.from_json_keyfile_name(autkey, scope)
            client = gspread.authorize(creds)
            print("[Google Sheets] Authentification Complete!")
            return client
        except FileNotFoundError:
            print("Файл "+ autkey + " не найден!")
        except json.decoder.JSONDecodeError:
            print("Файл не является ключом!")
            continue
