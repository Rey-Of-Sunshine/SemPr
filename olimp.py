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


def numb(arr):
    arr1=list(arr)
    global dt
    for i in range(len(arr1)):
        k=str(i)+'_'+arr1[i][0]+'_'+str(len(arr1[i]))
        dt[k]=arr1[i]
    return


spet=('матиматика', 'информаника', 'физика')
_list={}
vse=set()
un=set()
dt={}
kl1, kl2=0, 0

for i in spet:
    print ('Введите участников олимпиады по направлению "{}". Когда закончите введите ещё раз Enter'.format(i))
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