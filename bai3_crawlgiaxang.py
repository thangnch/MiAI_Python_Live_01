from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# # Khoi tao webdriver
browser = webdriver.Chrome(executable_path="./chromedriver")
#
# # Mo trang web can crawl
# browser.get("https://www.petrolimex.com.vn/thong-tin-khach-hang.html")
#
# # Tim den bang du lieu
# bang_xang = browser.find_element(by = By.XPATH,value="/html/body/div[1]/div[2]/div[2]/div[5]/div/section/div/div/div[1]/div/div[2]")
# print(bang_xang.text)

# Luu firebase (luu thu 1 doan text)
from firebase import firebase
firebase = firebase.FirebaseApplication("https://testpython-326ce-default-rtdb.firebaseio.com/", None)

data = {
    'Loai': 'Xang A95',
    'Vung 1': 20000,
    'Vung 2': 19000,
    'Ngay': '11/12/2021'
}

result = firebase.post('/',data)
print("Ket qua ghi du lieu = ", result)