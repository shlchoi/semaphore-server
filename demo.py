import util.client_handler as handler
from json import load
from os.path import isfile


def main():
    letters = input("Letters? ")
    magazines = input("Magazines? ")
    newspapers = input("Newspapers? ")
    parcels = input("Parcels? ")

    db_url = ''
    email = ''
    secret = ''

    if isfile('config'):
        with open('config', 'r') as _txt_file:
            _data = load(_txt_file)
            db_url = _data['db_url']
            email = _data['email']
            secret = _data['secret']
            _txt_file.close()

    data = {"mailbox": "temp_fd5c7ba5-c2db-4923-8075-046cbead8173",
            "letters": max(letters, 0),
            "magazines": max(magazines, 0),
            "newspapers": max(newspapers, 0),
            "parcels": max(parcels, 0)}

    handler.process_data(db_url, email, secret, data)


if __name__ == '__main__':
    main()
