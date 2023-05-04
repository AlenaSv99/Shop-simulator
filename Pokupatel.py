import Sotrudnik as sot
from tkinter import *
from tkinter import ttk

class Shopcase():
    def __init__(self, tovari, kolich, k_t, summa, min_summa, ves_pokupki):
        self.tovari = tovari #список добавленных товаров
        self.kolich = kolich #количество добавленных товаров
        self.k_t = k_t #количество товаров (пока не используется)
        self.summa = summa #сумма покупки
        self.min_summa = min_summa #минимальная сумма покупки
        self.ves_pokupki = ves_pokupki #вес заказа

    def full(self):
        '''наполнение корзины'''
        #print('Минимальная сумма покупки', self.min_summa, '₽')
        #print('Максимальная сумма покупки', sr.max_summa,'₽')
        #print('Принимаем заказы весом не более', sr.max_weight, 'КГ')

        print('! Выберите товары, которые имеются в наличии !')
        self.summa = 0
        self.ves_pokupki = 0
        self.min_summa = min_sum
        count = 0
        while True:
            a = input('Укажите товар, который хотите добавить в корзину (если хотите оформить заказ, наберите "Оформить заказ"): ').lower()
            for i in range(len(sot.sp_product)):
                if a in sot.sp_product[i]:
                    count = 1
                    pr = sot.sp_product[i]
                    self.tovari.append(pr)
                    ind = sot.sp_product.index(pr)
                    ind_cen = sot.sp_cen[ind]
                    ind_weight = sot.sp_vesov[ind]
                    b = int(input('Сколько штук добавить в корзину? (только число) >> '))
                    if b > sot.sp_nalich[ind]:
                        print('Слишком много. Пожалуйста, укажите количество товара в пределах ' + str(sot.sp_v_nalichii[ind]) + ' ШТ.')
                    else:
                        self.kolich.append(b)
                        self.summa += b * ind_cen  # подсчёт суммы покупки
                        self.ves_pokupki += b * ind_weight  # подсчёт веса заказа
                        tovs.append(a)  # создание списка добавленных товаров
                        kol.append(b)  # создание списка количества каждого товара, добавленного в корзину
            if count == 0:
                print('Такого товара у нас нет :(' + '\n' + 'Пожалуйста, выберите другой')
                continue

            razn_cen = self.min_summa - self.summa

            b = input('Хотите добавить что-нибудь ещё в корзину? (да/нет) >> ').lower()
            if b == 'нет' or self.summa >= razn_cen:
                print('Заказ оформлен. Сумма заказа: ' + str(self.summa) + '₽')
                break
            else:
                if self.summa >= sr.max_sum or self.ves_pokupki >= sot.max_weight:
                    print('Вы не можете добавить больше товаров в корзину')
                    break
                else:
                    print('До минимальной суммы заказа не хватает', razn_cen, '₽')
                    continue

tovs = [] #список добавленных товаров (проверить, есть ли необходимость)
kol = [] #список количества добавленных товаров (проверить, есть ли необходимость)
k_t = 0
s = 0
min_sum = 200 #минимальная сумма заказа
max_weight = 15000 #максимальный вес заказа (в граммах)
pokupatel = Shopcase(tovs, kol, k_t, s, min_sum, max_weight)
pokupatel.full()
