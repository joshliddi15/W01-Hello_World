import ctypes
user_name = input("What is your name? ")
ctypes.windll.user32.MessageBoxW(0, "Hello %s" %(user_name), "This is a message box", 0)