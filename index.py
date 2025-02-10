#1
print('Hello,Python!')

#2
print('  ')
print('Привет,Python!')
print('Hello,Python!')
print('Bonjour,Python!')
print('Hej,Python!')
print('Hola,Python!')
#3
print('   ')
q='Привет '
p='Python'
print(q+p)

#4
print('(' + chr(92) + '___/)')
print(f'(=' + chr(39) + '.' + chr(39) + '=)')
print('(")_(")')

#5
print('  ')
print('Привет,Python! \nHello,Python!\nBonjour,Python!\nHej,Python!\nHola,Python!')

#6
print('  ')
name=input('Как вас зовут ?')
print('Здравствуйте,',name)

#7
print('   ')
name=input('Как вас зовут ?')
print('Здравствуйте,',name,'.')
like=input('Что вам нравится?')
print('Отлично,',like,'-отличное увлечение.')
food=input('Какую еду вы любите?')
print('Круто,',food,'-это хороший выбор.')
colour=input('Какой цвет вы любите?')
print('Между прочим,',colour,'вам к лицу.')
old=input('Сколько вам лет?')
print(old,'- самое время начать жить полной жизнью')

#8
print('Login:')
login = input()
print('Password:')
password = input()
print('New password:')
password = input()
print('User durov has changed the password to querty')

#9
playlistpapa=['Ace Of Base-All That She Wands','No Doubt-Dont Speak','Bad Boys Blue - You Are A Woman','E-Type - Angels Crying','Haddaway - What Is Love' ]
playlistmama=playlistpapa[::-1]
stroka= '\n'.join(playlistmama)
print(stroka)

#10
print('   ')
print('Номер рейса')
FlightNumber=input()
print('Название авиакомпании на русском')
AirlineNameRussian=input()
print('Название авиакомпании на английском')
AirlineNameEnglish=input()
print('Город прилета на русском')
ArrivalСityRussian=input()
print('Город прилета на английском')
ArrivalСityEnglish=input()
print('Закакнчивается посадка на рейс',FlightNumber,AirlineNameRussian,'до',ArrivalСityRussian)
print('This is the final boarding call for ',AirlineNameEnglish,'flight',FlightNumber,'to',ArrivalСityEnglish)

#11
name=input('Как вас зовут?')
print(f'Привет, {name}!')

#12
price=int(input())
GoldWatch=96//16
SilverWatch=96
PriceSilver=48
PriceGold=(price-(SilverWatch*PriceSilver))//GoldWatch
print(PriceGold)

#13
import math
radius1=int(input('Радиус слеаой зоны'))
radius2=int(input('Радиус дальности приема'))
S=((radius2**2)-(radius1**2))*(math.pi)
print(abs(S))

#14
number=int(input())
decision=((number+2)*3-6)//3-4
print(decision)

#15
centimeters=int(input())
inch=centimeters/2.54
foot=inch/12
yard=foot/3
mile=yard/1760
print(f'{yard}\n{mile}\n{foot}\n{inch}')


