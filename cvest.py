dlin=10
zdor=100
uv=20
ves=30
import random

def noch(dlin, zdor, uv, ves):
	dlin -=2
	zdor +=20
	uv -=2
	ves -=5
	return dlin, zdor, uv, ves
	
def kop(dlin, zdor):
	print('Как копать? Интенсивно - 1, Лениво - 2 ', end='\n')
	a= int(input())
	if a == 1:
		dlin +=5
		zdor -=30
		return dlin, zdor
	elif a== 2:
		dlin +=2
		zdor -=10
		return dlin, zdor

def est(ves, zdor):
	print ('Что будешь есть? Мелкую дичь и ягоды - 1, Крупную добычу - 2 ', end='\n')
	a= int(input())
	if a == 1:
		ves +=15
		zdor +=10
		return ves, zdor
	elif (a == 2) and (uv >= 30):
		ves +=30
		zdor +=30
		return ves, zdor
	elif (a == 2) and (uv < 30):
		ves +=0
		zdor +=0
		print ('Прости, но сегодня не твой день. Тебе не хватает уважения, чтобы охотиться в компании, наберии 30 или боле очков уважения и возвращайся. ', end='\n')
		return ves, zdor

def draka(zdor, uv, ves):
	print ('С кем будешь драться? С слабым - 1, с средним - 2, с сильным - 3', end='\n')
	d= int(input())
	if d==1:
		b= random.choice([10, 20, 30])
		print ('Противник веса: ', b)
		delt=10
	elif d==2:
		b= random.choice([40, 50, 60])
		print ('Противник веса: ', b)
		delt=20
	elif d==3:
		b= random.choice([70, 80, 90])
		print ('Противник веса: ', b)
		delt=30
	a= ves+b+1
	c= random.randint(0, a)
	if (c<=ves):
		uv+=(delt+(b-ves)//5)
		return zdor, uv, ves
	else:
		uv-=(delt//2+(b-ves)//6)
		zdor-=(delt//2+(b-ves)//6)
		return zdor, uv, ves

	
print ('Привет! Внезапно, ты стал представителем лисьего рода.\n'' У тебя есть характеристики здоровья, уважения, веса и величины норы.\n',' Твоя задача добиться уважения более 100 и не допустить, что бы другие характеристики достигли 0.\n')
print ('Твои характеристики сейчас: величина норы - ',  dlin, ", здоровье - ", zdor, ", уважение - ", uv, ", вес - ", ves, end='\n')
print ("Ночью величина норы уменьшаетс на 2 единицы, к здоровью прибавляется 20 единиц, уважение падает на 2 единицы, вес уменьшается на 5 единиц\n")
while ((zdor >0) and (dlin >0) and (uv >0) and (uv <100) and (ves >0)):
	print ("Сейчас день, что будешь делать? Копать норку - 1, есть - 2, драться - 3, спать - 4")
	print ('Твои характеристики: величина норы - ',  dlin, ", здоровье - ", zdor, ", уважение - ", uv, ", вес - ", ves)
	de= int(input())
	if de == 1:
		dlin, zdor = kop(dlin, zdor)
		print ('Величина норы - ',  dlin, ", здоровье - ", zdor, ", уважение - ", uv, ", вес - ", ves)
	elif de == 2:
		ves, zdor = est(ves, zdor)
		print ('Величина норы - ',  dlin, ", здоровье - ", zdor, ", уважение - ", uv, ", вес - ", ves)
	elif de == 3:
		zdor, uv, ves = draka(zdor, uv, ves)
		print ('Величина норы - ',  dlin, ", здоровье - ", zdor, ", уважение - ", uv, ", вес - ", ves)
	elif de == 4:
		dlin, zdor, uv, ves = noch(dlin, zdor, uv, ves)
	print ('Вот день и закончился. Спокойной ночи', end='\n')
	print ( end='\n')
	dlin, zdor, uv, ves = noch(dlin, zdor, uv, ves)
if uv >=100:
	print ("Ты молодец. Теперь ты крут, до встречи!")
else:
	print ('Видимо твоя тактика не сработала. Выбири новую стратегию и начни заново.')