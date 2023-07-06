from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480+300+100") # 가로 * 세로 + x좌표 + y좌표

txt = Text(root, width=30, height=5)
txt.pack()

txt.insert(END, "글자를 입력하세요") # 초기 텍스트(Hint Text)

e = Entry(root, width=30) # 엔트리는 줄바꿈 안됨 (ex. Login/PW 입력창)
e.pack()
e.insert(0, "한 줄만 입력해요")

def btncmd():
    print(txt.get("1.0", END)) # 처음부터 끝까지의 모든 텍스트를 가져옴 1: 라인 1부터, 0: 컬럼 0부터
    print(e.get())

    #내용 삭제
    txt.delete("1.0", END)
    e.delete(0, END)

btn = Button(root, text="클릭", command = btncmd)
btn.pack()

root.mainloop()