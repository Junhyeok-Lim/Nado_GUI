import tkinter.ttk as ttk
from tkinter import *


root = Tk()
root.title("Nado GUI")
root.geometry("640x480+300+100") # 가로 * 세로 + x좌표 + y좌표

values = [str(i) + "일" for i in range(1, 32)]
combobox = ttk.Combobox(root, height=5, values=values)
combobox.pack()
combobox.set("카드 결제일")

readonly_combobox = ttk.Combobox(root, height=10, values=values, state="readonly") # height는 보여지는 목록 갯수
readonly_combobox.current(0) # 0번째 인덱스 값 초기 설정
readonly_combobox.pack()


def btncmd():
    print(combobox.get())
    print(readonly_combobox.get())


btn = Button(root, text="선택", command = btncmd)
btn.pack()

root.mainloop()