#1
price=int(input())
GoldWatch=96//16
SilverWatch=96
PriceSilver=48
PriceGold=(price-(SilverWatch*PriceSilver))//GoldWatch
print(PriceGold)

#2
country=input('Введите страну ')
r=country.replace(' ' , '\n')
print(r)

#3
price=input('Введите стоимость ')
c=price.split(' ')
n=int(c[0])+int(c[1])
print(n)

#4
i = 1
human = 1
wives = 7
bags_per_wife = 7  # Мешков у каждой жены
cats_per_bag = 7   # Кошек в каждом мешке
kittens_per_cat = 7 # Котят у каждой кошки
number_of_bags = wives * bags_per_wife # кол-во мешков
total_people = i + human + wives # общее количество людей
# общее количество животных
total_cats = number_of_bags * cats_per_bag
total_kittens = total_cats * kittens_per_cat
total_animals = total_cats + total_kittens
total = total_people + total_animals
print(total)


#5
totalSalesVolume=int(input('Введите сумму общего объема продаж '))
profit=totalSalesVolume*(0.19)
print(profit-(profit*0.01))

#6
height=int(input())
weight=int(input())
EMT=weight/((height/100)**2)
print(EMT-(EMT%0.01))

#7
quantityH=int(input('Введите количество гектаров '))
hectare=quantityH*100*100
quantityP=int(input('Введите уровень осадков '))
precipitation=quantityP/100
volume=precipitation*hectare*1000
print(volume)

#8
friendscandies=input('Введите колличество друзей и конфет ')
c=friendscandies.split(' ')
n=(int(c[1]))//(int(c[0])+1)
print(n)

#9
quantity=input('Введите колличество быков и семей ')
c=quantity.split(' ')
n=(int(c[0]))%(int(c[1]))
print(n)

#10
meters=int(input('Введите количество метров '))
miles=(meters//1609.34)
print(miles)
