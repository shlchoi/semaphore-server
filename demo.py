import util.data_util as handler
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

    handler.process_data(db_url, email, secret,
                         "temp_fd5c7ba5-c2db-4923-8075-046cbead8173",
                         max(letters, 0), max(magazines, 0), max(newspapers, 0), max(parcels, 0))


if __name__ == '__main__':
    main()
