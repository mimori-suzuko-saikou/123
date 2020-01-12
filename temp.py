from modules.Speaker import Speaker

#        猜猜看8
        
import random

speaker1 = Speaker()
name = speaker1.ask('请问阁下尊姓大名？')
speaker1.speak('您好！'+str(name))
speaker1.speak('欢迎来到猜数字游戏，数字范围在1到100之间')

target_number = random.randint(1, 100)
for i in range(8):
    guess_number = int(speaker1.ask('猜一个数字：'))
    if guess_number == target_number:
        break
    elif guess_number > target_number:
        speaker1.speak('猜大了')
    else:
        speaker1.speak('猜小了')       
        
if guess_number == target_number:
    speaker1.speak('您太厉害了！猜了'+str(i+1)+'次')        
else:
    speaker1.speak('您需要努力啊')            
    speaker1.speak('要猜的数字是'+str(target_number))  
