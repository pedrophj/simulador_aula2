
# **********************************************************
#
# Autor: Pedro Henrique de Jesus 
# Classe para manipular objetos no VREP de maneira simples.
# Data: 21/12/2020
# 
# Se for utilizar no youtube, 
# mencione o link do canal, por favor.
# **********************************************************

import time
import vrep

class objeto:

	def __init__(self):
		self.tempo=10
		print('Programa VREP iniciou a simulação')
		#vrep.simxFinish(-1)  
		self.cliente = vrep.simxStart('127.0.0.1', 19997, True, True, 5000, 5)  # Connect to V-REP
		vrep.simxSynchronous(self.cliente, True)
		vrep.simxStartSimulation(self.cliente, vrep.simx_opmode_blocking)

	def rodar(self):
		vrep.simxSynchronousTrigger(self.cliente)

	def obter(self,nome):
		errorCode, obj = vrep.simxGetObjectHandle(self.cliente, str(nome), vrep.simx_opmode_oneshot_wait)
		return obj

	def velocidade(self,objeto,valor):
		vrep.simxSetJointTargetVelocity(self.cliente, objeto, float(valor/57.2958), vrep.simx_opmode_streaming)

	def obterPosX(self,c):
		pos = vrep.simxGetObjectPosition(self.cliente, c, -1, vrep.simx_opmode_streaming)
		return pos[1][0]
		#print(pos[1][0])

	def obterPosY(self,c):
		pos = vrep.simxGetObjectPosition(self.cliente, c, -1, vrep.simx_opmode_streaming)
		return pos[1][1]
		#print(pos[1][1])

	def obterPosZ(self,c):
		pos = vrep.simxGetObjectPosition(self.cliente, c, -1, vrep.simx_opmode_streaming)
		return pos[1][2]
		#print(pos[1][2])


	def obterVelocidade(self,corpo):
		angVel = vrep.simxGetObjectVelocity(self.cliente, corpo, vrep.simx_opmode_streaming)
		print(angVel)
		return angVel[1]

	def lerSensor(self,corpo):
		x=vrep.simxReadVisionSensor(self.cliente, corpo, vrep.simx_opmode_streaming)
		return x[1]

	def delay(self,t):
		tempo=int(t/self.tempo)
		for i in range(tempo):
			vrep.simxSynchronousTrigger(self.cliente)