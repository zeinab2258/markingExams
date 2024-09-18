import cv2
import numpy as np

def whichGozineh(x):
    print(f"x={x}")
    #ناحیه اول و دوم
    if x >= 270 and x <= 400:
        if x > 270 and x <= 319:
            print(x)
            return 1
        elif x >= 320 and x <= 354:
            return 2
        elif x >= 355 and x <= 388:
            return 3
        elif x > 388 and x <= 421:
            return 4
        # ناحیه اول و دوم
    elif x >= 485 and x <= 620:
        if x > 485 and x <= 510:
            return 1
        elif x >= 525 and x <= 540:
            return 2
        elif x >= 560 and x <= 576:
            return 3
        elif x > 598 and x <= 615:
            return 4
def whichQuastion(y,x):
    #print(f"x={x} y={y}")
    #ناحیه اول
    if y > 0 and y < 290 and x >= 270 and x <= 400:
        if y>0 and y<9:
            return 0
        elif y > 35 and y < 42:
            return 1
        elif y > 65 and y < 78:
            return 2
        elif y > 94 and y < 114:
            return 3
        elif y > 125 and y < 131:
            return 4
        elif y > 158 and y < 165:
            return 5
        elif y > 192 and y < 200:
            return 6
        elif y > 220 and y < 230:
            return 7
        elif y > 250 and y < 260:
            return 8
        elif y > 280 and y < 290:
            return 9
    #ناحیه دوم
    elif y > 340 and y < 640 and x >= 270 and x <= 400:
        if y>339 and y<353:
            return 10
        elif y > 369 and y < 380:
            return 11
        elif y > 400 and y < 410:
            return 12
        elif y > 430 and y < 442:
            return 13
        elif y > 460 and y < 472:
            return 14
        elif y > 493 and y < 505:
            return 15
        elif y > 522 and y < 538:
            return 16
        elif y > 554 and y < 570:
            return 17
        elif y > 585 and y < 601:
            return 18
        elif y > 618 and y < 630:
            return 19
    # ناحیه سوم
    elif y > 0 and y < 290 and  x>= 485 and x <= 620:
        if y > 0 and y < 9:
            return 20
        elif y > 35 and y < 42:
            return 21
        elif y > 65 and y < 78:
            return 22
        elif y > 94 and y < 114:
            return 23
        elif y > 125 and y < 131:
            return 24
        elif y > 158 and y < 165:
            return 25
        elif y > 192 and y < 200:
            return 26
        elif y > 220 and y < 230:
            return 27
        elif y > 250 and y < 260:
            return 28
        elif y > 280 and y < 290:
            return 29
    # ناحیه چهارم
    elif y > 340 and y < 640 and x>= 485 and x <= 620:
        if y > 339 and y < 353:
            return 30
        elif y > 369 and y < 380:
            return 31
        elif y > 400 and y < 410:
            return 32
        elif y > 430 and y < 442:
            return 33
        elif y > 460 and y < 472:
            return 34
        elif y > 493 and y < 505:
            return 35
        elif y > 522 and y < 538:
            return 36
        elif y > 554 and y < 570:
            return 37
        elif y > 585 and y < 601:
            return 38
        elif y > 618 and y < 630:
            return 39


image_path = r'D:\project\prjprogramm\python\pythonProject7\images\new.jpg'
image = cv2.imread(image_path)

# نمایش تصویر اصلی
cv2.imwrite(r'D:\project\prjprogramm\python\pythonProject7\images\new.jpg', image)

# تبدیل تصویر به grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# حذف بخش بالای تصویر (کادر نام و نام خانوادگی)
height, width = gray.shape
gray = gray[int(height * 0.185):, :]  # حدود 20 درصد از بالای تصویر را حذف می‌کنیم

# نمایش تصویر پس از حذف بخش نام و نام خانوادگی
cv2.imwrite(r'D:\project\prjprogramm\python\pythonProject7\mnt\data\without_name.jpg', gray)

# اعمال threshold
_, thresh = cv2.threshold(gray, 235, 255, cv2.THRESH_BINARY_INV)

# نمایش تصویر threshold شده
cv2.imwrite(r'D:\project\prjprogramm\python\pythonProject7\mnt\data\thresh_image.jpg', thresh)

# پیدا کردن کانتورهای مربوط به گزینه‌ها
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# فیلتر کردن کانتورهای کوچک و بزرگ
# options_contours = [cnt for cnt in contours if 30 < cv2.boundingRect(cnt)[2] < 300 and 20 < cv2.boundingRect(cnt)[3] < 300]

options_contours = [cnt for cnt in contours]
#for cnt in contours:
#    print(cv2.boundingRect(cnt)[2] * cv2.boundingRect(cnt)[3])
#    print("s")
# کپی تصویر برای نمایش کانتورهای تشخیص داده شده
contour_image = cv2.cvtColor(thresh, cv2.COLOR_GRAY2BGR)
pashokhname=[0] * 40
array = list(range(1, 41))
# رسم کانتورهای تشخیص داده شده بر روی تصویر
for cnt in options_contours:
    area = cv2.contourArea(cnt)
    x, y, w, h = cv2.boundingRect(cnt)  # مختصات و ابعاد ناحیه
    roi = thresh[y:y + h, x:x + w]  # استخراج ناحیه از تصویر
    num_white_pixels = cv2.countNonZero(roi)
    #print(f"Number of white pixels in the region: {num_white_pixels} and area: {area}")

    if area > 520 and area < 700 and num_white_pixels > 350:
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(contour_image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        #cv2.imshow('s', contour_image)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()
        #print(f"x={x} y={y}")
        print(f"x={x} and y={y}")
        pashokhname[int(whichQuastion(y,x))]=whichGozineh(x)
        print(f"soal: {whichQuastion(y,x)} |gozineh: {whichGozineh(x)}")

# نمایش تصویر با کانتورهای رسم شده
cv2.imwrite(r'D:\project\prjprogramm\python\pythonProject7\mnt\data\contour_image.jpg', contour_image)
print(pashokhname)
# لیست نهایی پاسخ‌ها
detected_answers = []


# پاسخنامه صحیح
answer_key = [1, 3, 3, 2, 3, 1, 2, 4, 3, 1,
              4, 3, 4, 1, 2, 3, 3, 4, 2, 4,
              2, 1, 2, 3, 4, 1, 2, 3, 4, 1,
              2, 3, 2, 1, 2, 3, 4, 1, 2, 3]

# محاسبه نمره
score = 0
category = 'english'
for i, answer in enumerate(pashokhname):
    if i >= 10:
        category = 'persian'
        if i == 40:
            break
        if answer == answer_key[i]:
            score += 1
    else:
        category = 'persian'
        if answer == answer_key[i]:
            score += 1
print(f"Final Score: {score} / 40")
print(category)


