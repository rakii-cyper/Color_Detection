from utilities.util import *
from utilities.drive_api import download_files_from_google_drive


def main():
    images_path = 'images'

    str_01 = input("Do you have videos?(Y/n): ")

    if str_01 == 'Y' or str_01 == 'y':
        if download_files_from_google_drive('Images_Vip_Team', dest_path=images_path):
            print("Download Successful")
        else:
            print("Download error")
            return

    list_img_direct = os.listdir(images_path)
    for img in list_img_direct:
        img_path = os.path.join(images_path, img)
        histogram = histogram_calculate(img_path)

        np.sort(histogram, axis=0, kind='mergesort')

        bgr_img = cv2.imread(img_path)
        hsv_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2HSV)
        cv2.imshow('image:', hsv_img)

        height, width, channel = hsv_img.shape

        color_detected = np.zeros([height, width, channel], dtype=np.uint8)

        for h in range(0, height):
            for w in range(0, width):
                for c in range(0, channel):
                    color_detected[h, w, c] = histogram[-1, c]

        cv2.imshow('color:', color_detected)
        cv2.waitKey(0)


if __name__ == '__main__':
    main()
