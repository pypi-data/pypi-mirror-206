from tkinter import messagebox
from tkinter import *
import tkinter
from PIL import ImageTk, Image
from io import BytesIO
from time import sleep
import requests
import base64
import os


coords = [0,0]
debug = False
boolc = False
window = None
time_cview = 0

def interface(window):
    "Bind motion mouse in dubplicate window."
    window.bind('<Motion>', move)

def move(event):
    "Subfunction for interface, call while move mouse and print coordinates to console."
    global coords
    coords[0] = event.x
    coords[1] = event.y
    if(boolc):
        try:sleep(time_cview); print(coords[0], coords[1])
        except:raise TypeError("Read Documentation[About bind mouse motion] | time_cview should be integer or float.")
        
def run(window):
    "Run bind mouse motion in dublicate window."
    interface(window)

def coord_view(window,boolc):
    "Creating dublicate window for viewing mouse coordinates."
    interface(window)

def typely(listm):
    "Looks on types in page type."
    typely = True
    for coord in listm:
        try:
            for coords in coord[1]:
                try:
                    ex = coord[1][0] + coord[1][1]
                except:
                    typely = False
                finally:
                    if(typely == True):return True
                    else: return False
        except:
            return False
                    
def create_mpage(window,ui_page,size):
    "Add ui and set size in new window."
    if(typely(ui_page)):
        window.geometry(size)
        for ui in ui_page:
            ui[0].pack()
            ui[0].place({"x": ui[1][0], "y": ui[1][1]})
        if(debug == True):
            print("Page ui loaded.")
    else:
        try:
            for ui in ui_page:
                ui[0].pack(side=ui[1][0])
                ui[0].place(x=ui[1][0], y=ui[1][1])
        except:
            for ui in ui_page:
                ui[0].pack()
                ui[0].place()
    
def redirect_pages(page_ui_1,page_ui_2,side=None):
    "This function makes redirecting from page_1 to page_2, ui reconstruction."
    if(type(page_ui_1) and type(page_ui_2) == list):
        if(type(side) != list and type(side) != str and side != None): raise TypeError("Read Documentation[About type pages] | redirect_pages(ui_page_1,ui_page_2,side), side should be str type.")
        else:
            if debug == True: print("Start Redirecting.")
            for ui_page in page_ui_1:
                if debug == True: print("Forget object:", ui_page[0])
                ui_page[0].place_forget()
                ui_page[0].pack_forget()
            if(type(side) != list and side != None and type()):
                for ui_page_2 in page_ui_2:
                    ui_page_2.pack(side=side)
                    if debug == True: print("Packed ui.")
            else:
                if(side in ["bottom","top","right","left"]):
                    side_index = 0
                    for ui_page_2 in page_ui_2:
                        try:
                            ui_page_2.pack(side=side[side_index])
                        except:
                            raise SyntaxError("Read Documentation[About redirect pages] | if side is a list, count index side should be == count index ui_page_2.")
                    side_index += 1
                    if debug: print("Packed ui.")
                else:
                    if(typely(page_ui_2)):
                        for sidec in page_ui_2:
                            if debug: print(sidec[1][0])
                            try:
                                sidec[0].place(x=sidec[1][0],y=sidec[1][1])
                                if debug: print("x: {},\ny:{}.".format(sidec[1][0],sidec[1][1]))
                            except:
                                raise SyntaxError("Read Documentation[About redirect pages] | if side is a list, count index side should be == count index ui_page_2.")
                            if debug == True: print("Packed ui.")
                    else:
                        raise SyntaxError("Read Documentation[About redirect pages] | list error.")
                
    else:
        raise TypeError("Read Documentation[About redirect pages] | redirect_pages(ui_page), page_ui_1 and page_ui_2 should be list type.")

def add_url_image(window: tkinter.Tk, image_url: str, size=set):
    "Add image from url address as object(label)."
    image = BytesIO(requests.get(image_url).content)
    image_sub_obj = ImageTk.PhotoImage(Image.open(image).resize(size) if size is not set else Image.open(image))
    image_obj = Label(window, image=image_sub_obj)
    image_obj.image_sub_obj = image_sub_obj
    return image_obj



def window_exit(title: str, message: str):
    "Message Box for Exit(two buttons 'Yes','No' and Title text and message text boxs)."
    output = tkinter.messagebox.askyesno(title=title,message=message)
    if(output==True):
        if debug == True:
            print("Program Exit.")
        exit()


def documentation():
    "Show link documentation for ManagerTk."
    print("Documentation: https://pypi.org/project/ManagerTk/")
