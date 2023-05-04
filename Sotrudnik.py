class Rabotnik():
    def __init__(self, name_product, st_product, kol_product, weight):
        self.name_product = name_product # наименование продукта
        self.st_product = st_product # стоимость продукта
        self.kol_product = kol_product # количество продукта в наличии
        self.weight = weight # вес продукта (в граммах)

    def Info_dlya_rabotnika(self):
        '''вывод информации о каждом товаре, его цене, количестве и весе, для сотрудника'''
        print()
        for i in range(4):
            print('Наименования товара: '+ self.name_product[i].upper() + '. Информация:')
            print('Цена: '+str(self.st_product[i])+' ₽')
            print('В наличии: '+str(self.kol_product[i])+' ШТ')
            print('Весом '+str(self.weight[i]/1000)+' КГ')
            print()
        print('Максимальная сумма покупки: '+ str(max_sum)+' ₽')
        print('Максимальный вес заказа: '+ str(max_weight)+' КГ')

sp_product = ['кофе в зёрнах Jardin, 1 кг',
              'молоко ультрапастеризованное Домик в деревне 3.2%, 950г',
              'русский сахар сахарный песок, 1 кг',
              'корица молотая натуральная, 300 г'] #продукты в наличии в магазине
sp_cen = [920, 89, 81, 342] #список цен для каждого продукта в рублях
sp_nalich = [203, 155, 83, 300]
sp_vesov = [1000, 950, 1000, 300]

max_sum = 50000
max_weight = 10

v = Rabotnik(sp_product, sp_cen, sp_nalich, sp_vesov)
v.Info_dlya_rabotnika()
