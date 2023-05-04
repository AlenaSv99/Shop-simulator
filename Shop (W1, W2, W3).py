from tkinter import *
from tkinter import ttk
import Pokupatel as pk
import Sotrudnik as sot

'''первое окно: информация о магазине'''
window = Tk()
window.title('Информация о магазине')
window.geometry('370x550+120+100')

def Details():
    nazv_1 = ttk.Label(text='Детали', font='Arial 12 bold roman')
    nazv_1.pack(anchor="nw", padx=20, pady=15)

    i_1 = 'Минимальная сумма покупки ' + str(pk.min_sum) + ' ₽'
    info1 = ttk.Label(text=i_1, font='Arial 11 normal roman')
    info1.pack(anchor="nw", padx=20)

    i_2 = 'Максимальная сумма покупки ' + str(sot.max_sum) + ' ₽'
    info2 = ttk.Label(text=i_2, font='Arial 11 normal roman')
    info2.pack(anchor="nw", padx=20)

    i_3 = 'Принимаем заказы весом не более ' + str(sot.max_weight) + ' КГ'
    info3 = ttk.Label(text=i_3, font='Arial 11 normal roman')
    info3.pack(anchor="nw", padx=20)

def Delivery():
    nazv_2 = ttk.Label(text='Стоимость доставки', font='Arial 12 bold roman')
    nazv_2.pack(anchor="nw", padx=20, pady=15)

    i_4 = 'Итоговая сумма зависит от стоимости и веса заказа,\nрасстояния между вами и магазином и того, на\nмашине ли курьер.'
    info4 = ttk.Label(text=i_4, font='Arial 10 normal roman')
    info4.pack(anchor="nw", padx=20)

    i_5 = 'на заказ 200-999 ₽                                        99 ₽'
    info5 = ttk.Label(text=i_5, font='Arial 11 normal roman')
    info5.pack(fill=X, anchor="nw", padx=20, pady=7)

    i_6 = 'на заказ от 1000 ₽                                         0 ₽'
    info6 = ttk.Label(text=i_6, font='Arial 11 normal roman')
    info6.pack(fill=X, anchor="nw", padx=20)

Details()
propusk = ttk.Label(text=' ') # добавление пустой надписи для красоты
propusk.pack()
Delivery()

def next_window():
    window.withdraw()  #скрыть окно
    second_window = Toplevel()
    second_window.protocol("WM_DELETE_WINDOW", window.destroy()) #при закрытии дочернего окна убиваем главное окно
    # или так: second_window.protocol("WM_DELETE_WINDOW", root.destroy)

zakaz = Button(window, text='Понятно, спасибо!', font='Arial 11 bold roman', command=next_window)
zakaz.pack(padx=30, pady=45, ipadx=15, ipady=12)
window.mainloop()

'''второе окно: информация о товарах, цене и наличии'''
okno = Tk()
okno.title('Товары в наличии')
okno.geometry('720x700+600+40')

'''
def next_window1():
    #okno.withdraw()  # скрыть окно
    okno.deiconify()
    second_window = Toplevel()
    second_window.protocol("WM_DELETE_WINDOW", okno.destroy())
'''

def create_frame(label_text, pic, a):
    frame = ttk.Frame(borderwidth=1, relief=SOLID, padding=[7, 10])

    picture = PhotoImage(file=pic)
    label_1 = ttk.Label(frame, image=picture)
    label_1.image_ref = picture
    label_1.pack(anchor=CENTER)

    label = ttk.Label(frame, text=label_text) #добавление метки - текстового поля
    label.pack(anchor=CENTER)

    spinbox_var = IntVar(value=0)
    #kolich_prod = [i for i in range(s.cp[a] + 1)]
    spinbox = ttk.Spinbox(frame, textvariable=spinbox_var, from_=0, to=sot.sp_nalich[a]) #values=kolich_prod)
    spinbox.pack(anchor=CENTER)

    vibor_polz = []
    def b1_click():
        vibor_polz.append(spinbox.get())
        return vibor_polz
    button1 = ttk.Button(frame, text='Выбрать', command=b1_click)
    button1.pack(anchor=CENTER)

    def b2_click():
        spinbox.set(0)
    button2 = ttk.Button(frame, text='Очистить выбор')
    button2.config(command=b2_click)
    button2.pack(anchor=CENTER)

    return frame

def For_pokupatel():
    str_gl = 'Добро пожаловать в наш магазин! Ознакомьтесь с информацией о товарах в наличии'
    gl_stroka = ttk.Label(text=str_gl, font='Arial 10 normal roman')
    gl_stroka.pack(anchor="nw", padx=20, pady=30)

    for i in range(len(sot.sp_product)):
        str_1 = 'Наименование товара: ' + sot.sp_product[i]
        str_2 = 'Цена: ' + str(sot.sp_cen[i]) + '₽.'
        str_3 = 'В наличии: ' + str(sot.sp_nalich[i]) + 'ШТ.'

        stroka_1 = ttk.Label(text=str_1, font='Arial 10 normal roman')
        stroka_1.pack(anchor="nw", padx=20)

        stroka_2 = ttk.Label(text=str_2, font='Arial 10 normal roman')
        stroka_2.pack(anchor="nw", padx=20)

        stroka_3 = ttk.Label(text=str_3, font='Arial 10 normal roman')
        stroka_3.pack(anchor="nw", padx=20)

def Coffee():
        '''окошко для выбора кофе'''
        W_coffee = Toplevel()
        W_coffee.title("Выбор кофе")
        W_coffee.geometry("800x700")
        coffee_frame = create_frame("Выберите количество кофе в зёрнах Jardin, 1 кг:", "./coffee.png", 0)
        coffee_frame.pack(anchor=NW, fill=X, padx=5, pady=5)
        W_coffee.mainloop()

def Milk():
        '''окошко для выбора молока'''
        W_milk = Toplevel()
        W_milk.title("Выбор молока")
        W_milk.geometry("800x700")
        milk_frame = create_frame("Выберите количество молока Домик в деревне 3.2%, 950г:", "./milk.png", 1)
        milk_frame.pack(anchor=NW, fill=X, padx=5, pady=5)
        W_milk.mainloop()

def Sugar():
        '''окошко для выбора сахара'''
        W_sugar = Toplevel()
        W_sugar.title("Выбор молока")
        W_sugar.geometry("800x700")
        sugar_frame = create_frame("Выберите количество сахара песка, 1 кг:", "./sugar.png", 2)
        sugar_frame.pack(anchor=NW, fill=X, padx=5, pady=5)
        W_sugar.mainloop()

def Cinnamon():
        '''окошко для выбора корицы'''
        W_cinn = Toplevel()
        W_cinn.title("Выбор молока")
        W_cinn.geometry("800x700")
        cinnamon_frame = create_frame("Выберите количество корицы молотой натуральной, 300 г:", "./cinnamon.png", 3)
        cinnamon_frame.pack(anchor=NW, fill=X, padx=5, pady=5)
        W_cinn.mainloop()

For_pokupatel()

vibor_coffee = Button(okno, text='Перейти к выбору ' + str(sot.sp_product[0]), font='Arial 10 bold roman', command=Coffee)
vibor_coffee.pack(padx=20, pady=15, ipadx=10, ipady=10)

vibor_milk = Button(okno, text='Перейти к выбору ' + str(sot.sp_product[1]), font='Arial 10 bold roman', command=Milk)
vibor_milk.pack(padx=20, pady=15, ipadx=10, ipady=10)

vibor_sugar = Button(okno, text='Перейти к выбору ' + str(sot.sp_product[2]), font='Arial 10 bold roman', command=Sugar)
vibor_sugar.pack(padx=20, pady=15, ipadx=10, ipady=10)

vibor_cinn = Button(okno, text='Перейти к выбору ' + str(sot.sp_product[3]), font='Arial 10 bold roman', command=Cinnamon)
vibor_cinn.pack(padx=20, pady=15, ipadx=10, ipady=10)

okno.mainloop()


'''
def next_window1():
    okno.withdraw()  #скрыть окно
    second_window = Toplevel()
    second_window.protocol("WM_DELETE_WINDOW", okno.destroy()) #при закрытии дочернего окна убиваем главное окно
    # или так: second_window.protocol("WM_DELETE_WINDOW", root.destroy)

next_W = Button(okno, text='Перейти к товарам', font='Arial 11 bold roman', command=next_window1)
next_W.pack(padx=30, pady=45, ipadx=15, ipady=12)
okno.mainloop()
'''

'''остальные окошки: выбор каждого товара'''
'''
def create_frame(W, label_text, pic, a):
    frame = ttk.Frame(borderwidth=1, relief=SOLID, padding=[7, 10])

    picture = PhotoImage(file=pic)
    label_1 = ttk.Label(frame, image=picture)
    label_1.image_ref = picture
    label_1.pack(anchor=CENTER)

    label = ttk.Label(frame, text=label_text) #добавление метки - текстового поля
    label.pack(anchor=CENTER)

    spinbox_var = IntVar(value=0)
    #kolich_prod = [i for i in range(s.cp[a] + 1)]
    spinbox = ttk.Spinbox(frame, textvariable=spinbox_var, from_=0, to=sot.sp_nalich[a]) #values=kolich_prod)
    spinbox.pack(anchor=CENTER)

    vibor_polz = []
    def b1_click():
        vibor_polz.append(spinbox.get())
        return vibor_polz
    button1 = ttk.Button(frame, text='Выбрать', command=b1_click)
    button1.pack(anchor=CENTER)

    def b2_click():
        spinbox.set(0)
    button2 = ttk.Button(frame, text='Очистить выбор')
    button2.config(command=b2_click)
    button2.pack(anchor=CENTER)

    return frame



W_coffee = Tk()
W_coffee.title("Выбор кофе")
W_coffee.geometry("800x700")

coffee_frame = create_frame(W_coffee, "Выберите количество кофе в зёрнах Jardin, 1 кг:", "./coffee.png", 0)
coffee_frame.pack(anchor=NW, fill=X, padx=5, pady=5)

W_coffee.mainloop()


W_milk = Tk()
W_milk.title("Выбор молока")
W_milk.geometry("800x700")

milk_frame = create_frame(W_milk, "Выберите количество молока Домик в деревне 3.2%, 950г:", "./milk.png", 1)
milk_frame.pack(anchor=NW, fill=X, padx=5, pady=5)

W_milk.mainloop()



W_sugar = Tk()
W_sugar.title("Выбор молока")
W_sugar.geometry("800x700")

sugar_frame = create_frame(W_sugar, "Выберите количество сахара песка, 1 кг:", "./sugar.png", 2)
sugar_frame.pack(anchor=NW, fill=X, padx=5, pady=5)

W_sugar.mainloop()


W_cinn = Tk()
W_cinn.title("Выбор молока")
W_cinn.geometry("800x700")

cinnamon_frame = create_frame(W_cinn, "Выберите количество корицы молотой натуральной, 300 г:", "./cinnamon.png", 3)
cinnamon_frame.pack(anchor=NW, fill=X, padx=5, pady=5)

W_cinn.mainloop()

'''