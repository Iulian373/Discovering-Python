voted = {} #<=>voted=dict()

def check_voter(name):
    if voted.get(name):
        print ('kick them out!')
    else:
        voted[name] = True
        print ('let them vote!')

voted['Dan']=True

check_voter('Dan')
check_voter('Ion')


book=dict()
book['apple']=0.67
book['milk']=0.49
book['avocado']=1.49
print(book)

phone_book=dict()
phone_book['Ana']='+373 693 456 31'
phone_book['Ion']='+373 605 574 83'
phone_book['Dan']='+40 23839 19213'
print(phone_book)
