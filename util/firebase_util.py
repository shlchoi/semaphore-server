from firebase import firebase


def put_snapshot(database_url, email, secret, mailbox_id, timestamp, letters, magazines,
                 newspapers, parcels):
    """
    :param database_url:
    :param email:
    :param secret:
    :param mailbox_id:
    :param timestamp
    :param letters:
    :param magazines:
    :param newspapers:
    :param parcels:
    :return:
    :usage:
        >>> email = ''
        >>> secret = ''
        >>> database_url = 'https://smartbox-041.firebaseio.com'
        >>> mailbox_id = 'temp_fd5c7ba5-c2db-4923-8075-046cbead8173'
        >>> timestamp = 1469471720
        >>> letters, magazines, newspapers, parcels = 0, 0, 0, 1
        >>> put_snapshot(database_url, email, secret, mailbox_id, letters,
        >>>              magazines, newspapers, parcels)
    """
    _authentication = firebase.FirebaseAuthentication(secret, email)
    _firebase = firebase.FirebaseApplication(database_url, _authentication)
    _data = {'timestamp': timestamp, 'letters': letters, 'magazines': magazines,
             'newspapers': newspapers, 'parcels': parcels}
    return _firebase.put('/snapshots/{}'.format(mailbox_id), timestamp, _data)


def load_snapshot(database_url, email, secret, mailbox_id):
    """
    :param database_url:
    :param email:
    :param secret:
    :param mailbox_id:
    :return:
    :usage:
        >>> email = ''
        >>> secret = ''
        >>> database_url = 'https://smartbox-041.firebaseio.com'
        >>> mailbox_id = 'temp_fd5c7ba5-c2db-4923-8075-046cbead8173'
        >>> load_snapshot(database_url, email, secret, mailbox_id)
    """

    params = {'orderBy': '"$key"',
              'limitToLast': 1}

    _authentication = firebase.FirebaseAuthentication(secret, email)
    _firebase = firebase.FirebaseApplication(database_url, _authentication)
    result = _firebase.get('/snapshots/', mailbox_id, params=params)
    return result


def put_delivery(database_url, email, secret, mailbox_id, timestamp, letters, magazines,
                 newspapers, parcels):
    """
    :param database_url:
    :param email:
    :param secret:
    :param mailbox_id:
    :param letters:
    :param magazines:
    :param newspapers:
    :param parcels:
    :return:
    :usage:
        >>> email = 'mailbox@semaphore.ca'
        >>> secret = '56yZNdR1DApjhiKNKS3jcElWzWYSCWEfWPxjYHYf'
        >>> database_url = 'https://smartbox-041.firebaseio.com'
        >>> mailbox_id = 'temp_fd5c7ba5-c2db-4923-8075-046cbead8173'
        >>> timestamp = 1469471720
        >>> letters, magazines, newspapers, parcels = 0, 0, 0, 1
        >>> put_delivery(database_url, email, secret, mailbox_id, letters,
        >>>              magazines, newspapers, parcels)
    """
    _authentication = firebase.FirebaseAuthentication(secret, email)
    _firebase = firebase.FirebaseApplication(database_url, _authentication)
    _data = {'timestamp': timestamp, 'letters': letters, 'magazines': magazines,
             'newspapers': newspapers, 'parcels': parcels}
    return _firebase.put('/deliveries/{}'.format(mailbox_id), timestamp, _data)
