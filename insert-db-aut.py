from connectdb import *
while(True):
	
	nomeCampeao=''
	nomeInvocador = str(input('Qual seu nome invocador? \n'))	
	campeaoEscolhido = int(input('Seja Bem vindo qual campeão você ira jogar?\n Escreva o número correspondente \n 1-Vi \n 2-Ekko\n Escolha:'))
 	
	if campeaoEscolhido == 1:
		nomeCampeao = "Vi"
		print ('\n\nSe divirta',nomeInvocador,' com ',nomeCampeao,', em Summoners rift!\n\n\n')
	elif campeaoEscolhido == 2:
		nomeCampeao = "Ekko"
		print ('\n\nSe divirta',nomeInvocador,' com ',nomeCampeao,', em Summoners rift!\n\n\n')
	else:
		print("\n+--------------------------+")	
		print("+Campeão informado invalido+")
		print("+--------------------------+\n")	
	
	insert_db(nomeInvocador,nomeCampeao)