from gui import * 

def main():
    window = Tk()
    window.title('Searching & Sorting Explorer')
    window.geometry('600x800')
    window.resizable(True, True)
    gui(window)
    window.mainloop()

if __name__ == '__main__':
    main()