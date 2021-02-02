import vrep
from vrepbr import *

robo = objeto()
motor1 = robo.obter('DynamicLeftJoint')
motor2 = robo.obter('DynamicRightJoint')
corpo = robo.obter('LineTracer')

while True: # Loop inifinito

    
    robo.velocidade(motor1,200)
    robo.velocidade(motor2,200)
    robo.delay(2000)
    robo.velocidade(motor1,0)
    robo.velocidade(motor2,-200)
    robo.delay(2000)
    robo.rodar()


