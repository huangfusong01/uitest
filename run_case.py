import tkinter


def get_screen():
    screen = tkinter.Tk()
    # 获取当前屏幕的宽
    x = screen.winfo_screenwidth()
    # 获取当前屏幕的高
    y = screen.winfo_screenheight()

    return x, y

if __name__ == "__main__":
    l = get_screen()
    print(l[0])