from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from shop import *

def buy_item(price,img):
    data = read_file()
    if data["money"] >= price:
        data["skin"] = img
        data["money"] -= price
        save_file(data)
    else:
        print("Недостатньо грошей")
def shop_window():
    window = QDialog()

    elements = [
        {
            "name": "test1",
            "img":  "rocket.png",
            "price": 100,
            "name2": "test2",
            "img2": "завантаження-removebg-preview.png",
            "price2": 200,
            "name3": "test3",
            "img3": "png-clipart-white-spaceship-rocket-rocket-photography-spacecraft-removebg-preview.png",
            "price3": 300


        }
    ]

    main_line = QHBoxLayout()
    for element in elements:
        ver = QVBoxLayout()
        ver2 = QVBoxLayout()
        ver3 = QVBoxLayout()
        name_lbl = QLabel(element["name"])
        name_lbl2 = QLabel(element["name2"])
        name_lbl3 = QLabel(element["name3"])
        img_lbl = QLabel()
        img_lbl2 = QLabel()
        img_lbl3 = QLabel()
        img_pm = QPixmap(element["img"])
        img_pm = img_pm.scaledToWidth(100)
        img_lbl.setPixmap(img_pm)
        img_pm2 = QPixmap(element["img2"])
        img_pm2 = img_pm2.scaledToWidth(100)
        img_lbl2.setPixmap(img_pm2)
        img_pm3 = QPixmap(element["img3"])
        img_pm3 = img_pm3.scaledToWidth(100)
        img_lbl3.setPixmap(img_pm3)
        price_lbl = QLabel(str(element["price"]))
        buy_btn = QPushButton("Купити")
        buy_btn.clicked.connect(lambda _,price =element["price"],img = element["img"]: buy_item(price,img) )
        price_lbl2 = QLabel(str(element["price2"]))
        buy_btn2 = QPushButton("Купити")
        price_lbl3 = QLabel(str(element["price3"]))
        buy_btn3 = QPushButton("Купити")
        buy_btn3.clicked.connect(lambda _,price =element["price3"],img = element["img3"]: buy_item(price,img) )
        buy_btn2.clicked.connect(lambda _,price =element["price2"],img = element["img2"]: buy_item(price,img) )
        ver.addWidget(name_lbl)
        ver.addWidget(img_lbl)
        ver.addWidget(price_lbl)
        ver.addWidget(buy_btn)
        ver2.addWidget(name_lbl2)
        ver2.addWidget(img_lbl2)
        ver2.addWidget(price_lbl2)
        ver2.addWidget(buy_btn2)
        ver3.addWidget(name_lbl3)
        ver3.addWidget(img_lbl3)
        ver3.addWidget(price_lbl3)
        ver3.addWidget(buy_btn3)
        main_line.addLayout(ver)
        main_line.addLayout(ver2)
        main_line.addLayout(ver3)




    window.setLayout(main_line)
    window.show()
    window.exec()
