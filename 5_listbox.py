from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480+300+100") # 가로 * 세로 + x좌표 + y좌표

listbox = Listbox(root, selectmode="extended", height=0) #height 숫자 만큼 화면에 보임 -> 스크롤바로 해결 가능
listbox.insert(0, "사과")
listbox.insert(1, "딸기")
listbox.insert(2, "바나나")
listbox.insert(END, "수박")
listbox.insert(END, "포도")
listbox.pack()

def btncmd():
    # listbox.delete(0) # 맨 앞 항목을 삭제
#    listbox.delete(END)
    # print("리스트에는", listbox.size(), "개가 있습니다.")

    # 항목 확인 (시작 idx, 끝 idx)
    print("1번째부터 3번째까지의 항목 : ", listbox.get(0, 2))

    #선택된 항목 확인(idx 값을 반환)
    print("선택된 항목 : ", listbox.curselection()) 


btn = Button(root, text="클릭", command = btncmd)
btn.pack()

root.mainloop()