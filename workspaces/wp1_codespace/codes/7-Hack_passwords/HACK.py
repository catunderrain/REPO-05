import pyautogui
import time

time.sleep(2)
nums = [str(i) for i in range(1000,1111)]
for num in nums:
    pas = ''
    for i in range(6 - len(num)):
        pas += '0'
    pas += num
    # time.sleep(50/1000)

    pyautogui.typewrite(pas)
    pyautogui.press('enter')
    