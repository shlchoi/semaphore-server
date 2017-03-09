import cv2


def image_subtract(image_name, background_name):
    background = cv2.imread(background_name, cv2.IMREAD_GRAYSCALE)
    image = cv2.imread(image_name, cv2.IMREAD_GRAYSCALE)
    result = cv2.absdiff(background, image)
    subtracted = cv2.inRange(result, 0x50, 0xff)

    print("{0}: {1}".format(image_name, cv2.countNonZero(subtracted)))
    return subtracted


def main():
    cv2.imwrite("out_empty1_empty1.jpg", image_subtract("test_images/empty1.jpg", "test_images/empty1.jpg"))
    cv2.imwrite("out_empty2_empty1.jpg", image_subtract("test_images/empty2.jpg", "test_images/empty1.jpg"))
    cv2.imwrite("out_empty3_empty1.jpg", image_subtract("test_images/empty3.jpg", "test_images/empty1.jpg"))
    cv2.imwrite("out_letter1_empty1.jpg", image_subtract("test_images/letter1.jpg", "test_images/empty1.jpg"))
    cv2.imwrite("out_letter2_empty1.jpg", image_subtract("test_images/letter2.jpg", "test_images/empty1.jpg"))
    cv2.imwrite("out_letter3_empty1.jpg", image_subtract("test_images/letter3.jpg", "test_images/empty1.jpg"))
    cv2.imwrite("out_2letters_empty1.jpg", image_subtract("test_images/2letters.jpg", "test_images/empty1.jpg"))
    cv2.imwrite("out_3letters_empty1.jpg", image_subtract("test_images/3letters.jpg", "test_images/empty1.jpg"))

    cv2.imwrite("out_letter1_letter1.jpg", image_subtract("test_images/letter1.jpg", "test_images/letter1.jpg"))
    cv2.imwrite("out_letter2_letter1.jpg", image_subtract("test_images/letter2.jpg", "test_images/letter1.jpg"))
    cv2.imwrite("out_letter3_letter1.jpg", image_subtract("test_images/letter3.jpg", "test_images/letter1.jpg"))
    cv2.imwrite("out_2letters_letter1.jpg", image_subtract("test_images/2letters.jpg", "test_images/letter1.jpg"))
    cv2.imwrite("out_3letters_letter1.jpg", image_subtract("test_images/3letters.jpg", "test_images/letter1.jpg"))


if __name__ == '__main__':
    main()
