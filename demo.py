from requests import post


def main():
    url = "http://ec2-54-175-148-98.compute-1.amazonaws.com:5000/snapshot"
    headers = {'enctype': "multipart/form-data"}
    files = {'snapshot': open("../test_letters.jpg")}
    data = {'mailbox': "temp_fd5c7ba5-c2db-4923-8075-046cbead8173"}

    request = post(url, headers=headers, data=data, files=files)

    if request.status_code == 200:
        print("Success")
    else:
        print("Failure")

if __name__ == '__main__':
    main()
