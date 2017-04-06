# Semaphore - Server

Semaphore is a system that monitors physical mailboxes for deliveries and notifies users when mail arrives. In addition, Semaphore also categorizes and counts the number of items that are currently inside the mailbox and displays the information to the user in an associated smartphone application.  

This repository contains the Web Server Component.

Semaphore was created for the Electrical and Computer Engineering Capstone Design Symposium 2017 at the University of Waterloo.


## About Semaphore
See the [main project page](https://shlchoi.github.io/semaphore) for more information.

### Other Semaphore Repositories
* [Mailbox Device](https://github.com/shlchoi/semaphore-mailbox)
* [Image Processing Algorithm](https://github.com/mattcwc/semaphore-raspi)
* [Android Application](https://github.com/shlchoi/semaphore-android)
* [iOS Application](https://github.com/shlchoi/semaphore-ios)

## Installation Instructions
### Install Requirements
1. Run `pip install -r requirements.txt` from root folder

### Configure server
2. Create a file called `config`
3. In `config`, add the following information:
```
{
    "db_url": [url to Firebase Realtime Database Instance],
    "email": [email address for server user for Firebase],
    "secret": [secret for server user from Firebase],
    "port": [port to be used]
}
```

### Verify 
4. Go to `https://localhost:[PORT]/`
   A 200 OK response should be recieved.


## Authors
* Samson Choi 	[Github](https://github.com/shlchoi)
* Matthew Chum 	[Github](https://github.com/mattcwc)
* Lawrence Choi	[Github](https://github.com/l2choi)
* Matthew Leung [Github](https://github.com/mshleung)


## Acknowledgments
* [Armin Ronacher](http://lucumr.pocoo.org/about/) - [Flask](http://flask.pocoo.org/)
* [Ozgur Vatansever](https://github.com/ozgur) - [Python-firebase](http://ozgur.github.io/python-firebase/)
* OpenCV Dev Team - [opencv-python](http://docs.opencv.org/3.0-beta/)
* NumPy Developers - [NumPy](http://www.numpy.org/)
* PyData Development Team - [pandas](http://pandas.pydata.org/)
* Scikit-image Development Team - [scikit-image](http://scikit-image.org/)
* Matplotlib Development Team - [matplotlib](http://matplotlib.org/)
* SciPy Developers - [SciPy](https://www.scipy.org/)

## License

Distributed under the GNU GPLv3 license. See [LICENSE](https://github.com/shlchoi/semaphore-android/blob/master/LICENSE) for more information.

Libraries are used under the [BSD License](https://opensource.org/licenses/BSD-3-Clause), the [MIT License](https://opensource.org/licenses/MIT) and the [Python Software Foundation License](https://docs.python.org/3/license.html).

### BSD License
* [Flask](http://flask.pocoo.org/)
* [opencv-python](http://docs.opencv.org/3.0-beta/index.html)
* [NumPy](http://www.numpy.org/)
* [pandas](http://pandas.pydata.org/)
* [scikit-image](http://scikit-image.org/)
* [SciPy](https://www.scipy.org/)

### MIT License
* [Python-firebase](http://ozgur.github.io/python-firebase/)

### Python Software Foundation License
* [matplotlib](http://matplotlib.org/)
