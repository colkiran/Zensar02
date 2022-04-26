
class TooYoung(Exception):
    pass

class TooOld(Exception):
    pass

class TooLittle(Exception):
    pass


age = 23
try:
    if age <= 10:
        raise TooLittle("Too very little to decide the leader....")
    elif age <= 15:
        raise TooYoung("Age is less to cast your valuable vote....")
    elif age > 100:
        raise TooOld("To Old to decide the leader.....")
    else:
        print("You can cast your valuable vote.......")

except TooLittle as l:
    print(l)
except TooYoung as y:
    print(y)
except TooOld as o:
    print(o)
except Exception as e:
    print(e)
finally:
    print("completed the process of voting.....")
