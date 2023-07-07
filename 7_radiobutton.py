from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480+300+100") # 가로 * 세로 + x좌표 + y좌표

Label(root, text="메뉴를 선택하세요").pack()


burger_var = IntVar()
btn_burger1 = Radiobutton(root, text="햄버거", value=1, variable=burger_var)
# btn_burger1.select() # 초기값 설정도 가능
btn_burger2 = Radiobutton(root, text="치즈버거", value=2, variable=burger_var)
btn_burger3 = Radiobutton(root, text="치킨버거", value=3, variable=burger_var)


btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

Label(root, text="음료를 선택하세요").pack()
drink_var = StringVar()
btn_drink1 = Radiobutton(root, text="콜라", value="콜라", variable=drink_var)
btn_drink2 = Radiobutton(root, text="사이다", value="사이다", variable=drink_var)
btn_drink3 = Radiobutton(root, text="오렌지주스", value="오렌지주스", variable=drink_var)

btn_drink1.pack()
btn_drink2.pack()
btn_drink3.pack()



def btncmd():
  
    print(burger_var.get()) # 햄버거 중에서 선택된 라디오 항목의 값(value)을 반환
    print(drink_var.get())


btn = Button(root, text="주문", command = btncmd)
btn.pack()

root.mainloop()