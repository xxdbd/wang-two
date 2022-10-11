 """
  Project Name : 哪吒大战三太子
  Created On : 7/30/2019 00:30:00 
  @Author : 严小样儿
"""
 
 
class Role():
  def __init__(self,role_name):
    self.__name = role_name
    self.lifevalue = 500
    self.attack = 45
    self.status = True
  
  def __str__(self):
    return "My name is %s,and my lifevalue is %d,and my attack is %d" %(self.__name,self.lifevalue,self.attack)
  
  def commonskill(self,obj):
    obj.lifevalue -= self.attack
    if (obj.lifevalue < 50) & (obj.lifevalue > 0) :
      obj.attack = obj.lifevalue
      print("Be beated %d times,%s in danger!" %(count,obj.__name))
    elif obj.lifevalue <=0:
      obj.status = False
      obj.lifevalue = 0
      obj.attack = 0
      print("Be beated %d times,%s dead." %(count,obj.__name))      
    else:
      pass
      
  def addtool(self,tool):
    if self.lifevalue == 0:
      print(" 已经死亡，不能购买兵器")
    elif self.lifevalue < 20:
      print(" 濒临死亡，不能购买兵器")
    else:
      global get 
      get = True
      self.tool = tool.name
      self.lifevalue += tool.lifeplus
      self.attack += tool.attackplus
  
  @property
  def name(self):
    return self.__name
  
  @name.setter
  def name(self,value):
    print("%s已改名为：%s" %(self.__name,value))
    print("\n"+"*"*50)
    self.__name = value
    
class Tool():
  def __init__(self,name,lifeplus,attackplus):
    self.name = name
    self.lifeplus = lifeplus
    self.attackplus = attackplus
     
print("***********************游戏开始***********************")
r1 = Role("哪吒")
print(r1)
 
 
print("\n"+"*"*50)
 
 
r2 = Role("敖丙")
print(r2)
 
 
print("\n"+"*"*50)
 
 
r2.name = "东海三太子"
print(r1.name+"没有改名",end='\n\n')
 
 
t1 = Tool("百麟甲",100,50)
 
 
get = None 
count = 0
while True:
  n = input("请输入%s攻击%s次数："%(r1.name,r2.name))
  #import random
  #n = random.randint(0,12)
  #print(n)
  try:
    n = int(n)  
  except Exception as error:
    print(error,end='\n\n')
    continue
  else:
    if n == 0:
      print("\n"+"***********************游戏结束***********************")
      break
    print("开打~\n")
    for i in range(n):
      if r2.status:
        count += 1
        r1.commonskill(r2)
    
  print(r2.name,"剩余生命值",r2.lifevalue)
  print(r2.name,"当前攻击力",r2.attack)
 
 
  print("\n"+"*"*50)
 
 
  if r2.lifevalue == 0:
    print("经过%d轮单方暴打，%s被活活打死!" %(count,r2.name))
    print("\n"+"***********************游戏结束***********************")      
    break
  else:
    times = 0
    while times < 3:
      help = input("帮助敖丙装备武器吗？[y/n]")
      #help = random.choice(['Y','y','N','n',0,'s'])
      #print(help)
      if help == 'Y' or help == 'y':
        r2.addtool(t1)
        if get:
          print(r2.name,"已装上",r2.tool)
          print(r2.name,"生命值属性 +",t1.lifeplus)
          print(r2.name,"攻击力属性 +",t1.attackplus)
          print("\n"+"*"*50)
        break
      elif help == 'N' or help == 'n':
        print("\n"+"*"*50)        
        break
      else:
        print("ValueError：Type [y/n] only\n")
        times += 1
        if times == 2 :
          print("仅剩一次机会，请谨慎操作！")
    if times == 3 :
      print("\n"+"***********************游戏结束***********************")
      break 
       