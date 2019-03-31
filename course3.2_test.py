#3-4嘉宾名单
guests=['huangshan','amei','jiashu']
guest_form = '嘉宾名单'
print(guest_form+guests[0]+","+guests[1]+","+guests[2])
print(guests[2])
guests[1]='ashan'
guest_form = '嘉宾名单（新）'
print(guest_form+guests[0]+","+guests[1]+","+guests[2])
print('我找到了一个更大的餐桌')
guests.insert(0,"nainai")
guests.insert(2,"laoba")
guests.append("huangshang")
guest_form = '嘉宾名单（最新）'
print(guest_form+','.join(guests))
print('不好意思桌子没有到,现在只能邀请两个人')
print('不好意思'+guests.pop()+'不能邀请你去了')
print('不好意思'+guests.pop()+'不能邀请你去了')
print('不好意思'+guests.pop()+'不能邀请你去了')
print('不好意思'+guests.pop()+'不能邀请你去了')
print('你们还可以来'+','.join(guests))
del guests[0]
del guests[0]
print(guests)