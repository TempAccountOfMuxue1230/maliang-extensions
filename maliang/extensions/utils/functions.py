import typing
from tkinter import messagebox
import maliang as ml

def get_exit_ask_function(root_window: ml.Tk, title: str="退出", message:str="您确定要退出软件吗？"):
    root_win = root_window

    def exit_ask():
        if messagebox.askyesno(title, message):
            root_win.destroy()

    return exit_ask

def get_exit_ask_function_with_sth(root_window: ml.Tk, title: str="退出", message:str="您确定要退出软件吗？", function:typing.Callable=lambda x: x):
    root_win = root_window
    func = function

    def exit_ask():
        if messagebox.askyesno(title, message):
            func(root_win, True)
            root_win.destroy()
            return
        func(root_win, True)

    return exit_ask
