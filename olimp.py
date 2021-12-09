def participant():
    num=1
    li=[]
    while num>0:
        peple = input()
        if peple == '':
            break
        li.append(peple)
        num+=1
    return set(li)


def dliname(n):
    g=-1
    dl=0
    for k in range(len(n)):
        if n[k]==' ':
            g=k
            break
    for i in range(g+1, len(n)):
        dl+=1
        if n[i]==' ':
            dl-=1
            break
    return dl


def numb(arr):
    arr1=list(arr)
    a, b=0, 0
    global dt
    for i in range(len(arr1)):
        k=str(i+1)+'_'+arr1[i][0]+'_'+str(dliname(arr1[i]))
        dt[k]=arr1[i]
    return


spet=('матиматика', 'информаника', 'физика')
_list={}
vse=set()
un=set()
dt={}
kl1, kl2=0, 0
ball=[]

for i in spet:
    print ('Введите ФИО участников олимпиады по направлению "{}". Когда закончите введите ещё раз Enter'.format(i))
    _list[i]=participant()
    vse = vse| _list[i]
    if un==set():
        un= un| _list[i]
    un= un & _list[i]
for i in spet:
    print('Участники олимпиады "{}":\n {}'.format(i, _list[i]))
print('Участников олимпиад всего: {} \n Участвовали во всех олимпиадах {} человек(а)'.format(len(vse), len(un)))

numb(vse)
print (dt)

for i in range(len(spet)):
    print ('Введите баллы участников олимпиады по направлению "{}". Когда закончите введите ещё раз Enter'.format(spet(i)))
    ball.append()
    for j in range(len(_list[i])):
        ball[i].append()
        print(_list[i][j], end=' ')
        ball[i][j]=input()
        
    