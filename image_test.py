import cv2


def image_subtract(image_name, background_name):
    background = cv2.imread(background_name, cv2.IMREAD_GRAYSCALE)
    image = cv2.imread(image_name, cv2.IMREAD_GRAYSCALE)
    result = cv2.absdiff(image, background)
    subtracted = cv2.inRange(result, 0x10, 0xff)

    print("{0}: {1}".format(image_name, cv2.countNonZero(subtracted)))
    return subtracted


def main():
    cv2.imwrite("out_3l.jpg", image_subtract("test_images/black_3l.jpg", "test_images/black_empty.jpg"))
    cv2.imwrite("out_1b.jpg", image_subtract("test_images/black_1b.jpg", "test_images/black_empty.jpg"))
    cv2.imwrite("out_3l1b.jpg", image_subtract("test_images/black_3l1b.jpg", "test_images/black_empty.jpg"))


if __name__ == '__main__':
    main()
