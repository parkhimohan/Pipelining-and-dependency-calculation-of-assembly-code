def instructionsInList(list1):
	for i in range(len(list1)):
		if "," in list1[i]:
			list1[i]=list1[i].split(',')
		else:
			list1[i]=list1[i].split(' ')
	for j in list1:
		if " " in j[0]:
			splitAgain=j[0]
			l=splitAgain.split(" ")
			j[0]=l[0]
			j.insert(1,l[1])
	return list1

def storeFileInput(codename):
	file=open(codename)
	x=file.readlines()
	list1=[]
	for i in x:
		i=i.strip()
		list1.append(i)
	for j in range(len(list1)):
		if list1[j]==".text":
			list1=list1[j+1:]
			break
	for i in list1:
		if i.find(':')>=0 or i.find('#')==0:
			list1.remove(i)
		elif i.find('#')>0:
			j=i.find('#')
			k=list1.index(i)
			list1.remove(i)
			i=i[0:j]
			i=i.strip()
			list1.insert(k,i)
	for i in list1:
		if i=='syscall':
			list1.remove(i)
	return list1

def splitInstructions(list):
	fresh_list=[]
	instructions=[]
	in_list=[]
	out_list=[]
	for i in list:
		y=len(i)
		if(y>2):

			if((i[0]!="li") and (i[1]!="$v0")):
				if((i[0]!="sw") and (i[0]!="lw") and (i[0]!="lb") and (i[0]!="sb") and (i[0]!="bgt") and (i[0]!="blt") and (i[0]!="beqz") and (i[0]!="bne") and (i[0]!="beq") and (i[0]!="bge")):
					if((i[0]=="sll")):
						instructions.append('mul')
					elif((i[0]=="srl")):
						instructions.append('div')
					else:
						instructions.append(i[0])
					out_list.append(i[1])
					in_list=[]
					in_list=i[2:]
					i=[]
					i.append(instructions)
					i.append(out_list)
					i.append(in_list)
					fresh_list.append(i)
					instructions=[]
					out_list=[]
				elif i[0]=="lw" or i[0]=="lb" or i[0]=="move":
					instructions.append(i[0])
					out_list.append(i[1])
					in_list=[]
					i=i[2:]
					in_list=i[0].split('(')
					in_list.remove(in_list[0])
					in_list[0]=in_list[0][:-1]
					i=[]
					i.append(instructions)
					i.append(out_list)
					i.append(in_list)
					fresh_list.append(i)
					instructions=[]
					out_list=[]
				elif i[0]=="sw" or i[0]=="sb":
					instructions.append(i[0])
					out_list.append(i[1])
					in_list=[]
					i=i[2:]
					in_list=i[0].split('(')
					in_list.remove(in_list[0])
					in_list[0]=in_list[0][:-1]
					i=[]
					i.append(instructions)
					i.append(in_list)
					i.append(out_list)
					fresh_list.append(i)
					instructions=[]
					out_list=[]

				elif((i[0]=="beqz")):
					instructions.append(i[0])
					in_list=[]
					in_list.append(i[1])
					in_list.append('0')
					out_list=i[2:]
					i=[]
					i.append(instructions)
					i.append(out_list)
					i.append(in_list)
					fresh_list.append(i)
					instructions=[]
					out_list=[]
				elif i[0]=="bgt" or i[0]=="blt" or i[0]=="bne" or i[0]=="beq" or i[0]=="bge":
					instructions.append(i[0])
					in_list=[]
					in_list.append(i[1])
					in_list.append(i[2])
					out_list=i[3:]
					i=[]
					i.append(instructions)
					i.append(out_list)
					i.append(in_list)
					fresh_list.append(i)
					instructions=[]
					out_list=[]	
				else:
					instructions.append(i[0])
					out_list.append(i[1])
					in_list=i[2:]
					i=[]
					i.append(instructions)
					i.append(in_list)
					i.append(out_list)
					fresh_list.append(i)
					instructions=[]
					out_list=[]
			elif((i[0]=="li") and (i[1]=="$v0")):
				in_list=[]
				instructions.append('addi')
				out_list.append(i[1])
				in_list.append(i[2])
				in_list.append('$zero')
				i=[]
				i.append(instructions)
				i.append(out_list)
				i.append(in_list)
				fresh_list.append(i)
				instructions=[]
				out_list=[]
	return fresh_list


def ofThe2Lists(check_1,check_2):
	flag=0
	if(check_1==check_2):
		flag=1
	return flag

def matchInstruction(to_check):
	instructionsands={'add':3 , 'sub' :3 , 'mul':3 , 'div':3 , 'lw':4 , 'sw':5 ,'slt':1, 'beq':1,'beqz':1,'bge':1, 'bgt':1, 'blt':1,'li':1 ,'bne':1,'la':1 ,'lb':4,'sb':5,'move':5 ,'addi':3}
	return instructionsands[to_check]

def withoutBypassingDependencyRAW(list):
	x=len(list)
	for i in range(x-4):
		for j in range(i+1,i+4):
			if ((list[i][1][0] in list[j][2])):
				print(list[i][1][0],list[j][2],i+1,j+1,"=>dependency(-r-a-w-)")
	for i in range(x-4,x-3):
		for j in range(x-3,x):
			if ((list[i][1][0] in list[j][2])):
				print(list[i][1][0],list[j][2],i+1,j+1,"=>dependency(-r-a-w-)")
	for i in range(x-3,x-2):
		for j in range(x-2,x):
			if ((list[i][1][0] in list[j][2])):
				print(list[i][1][0],list[j][2],i+1,j+1,"=>dependency(-r-a-w-)")
	for i in range(x-2,x-1):
		for j in range(x-1,x):
			if ((list[i][1][0] in list[j][2])):
				print(list[i][1][0],list[j][2],i+1,j+1,"=>dependency(-r-a-w-)")

def withoutBypassingDependencyWAWoutputRegReadAfter(list):
	x=len(list)
	for i in range(x-4):
		if((matchInstruction(list[i][0][0])==3) or (matchInstruction(list[i][0][0])==4) or (matchInstruction(list[i][0][0])==5)):
			for j in range(i+1,i+2):
				if ((list[i][1][0]==list[j][1][0]) or (ofThe2Lists(list[i][1][0],list[j][2])==1)):
					print(list[i][1][0],list[j][1][0],i+1,j+1,"=>dependency(-w-a-w-)")
	for i in range(x-4,x-3):
		if((matchInstruction(list[i][0][0])==3) or (matchInstruction(list[i][0][0])==4) or (matchInstruction(list[i][0][0])==5)):
			for j in range(x-3,x):
				if ((list[i][1][0]==list[j][1][0]) or (ofThe2Lists(list[i][1][0],list[j][2])==1)):
					print(list[i][1][0],list[j][1][0],i+1,j+1,"=>dependency(-w-a-w-)")
	for i in range(x-3,x-2):
		if((matchInstruction(list[i][0][0])==3) or (matchInstruction(list[i][0][0])==4) or (matchInstruction(list[i][0][0])==5)):
			for j in range(x-2,x):
				if ((list[i][1][0]==list[j][1][0]) or (ofThe2Lists(list[i][1][0],list[j][2])==1)):
					print(list[i][1][0],list[j][1][0],i+1,j+1,"=>dependency(-w-a-w-)")	
	for i in range(x-2,x-1):
		if((matchInstruction(list[i][0][0])==3) or (matchInstruction(list[i][0][0])==4) or (matchInstruction(list[i][0][0])==5)):
			for j in range(x-1,x):
				if ((list[i][1][0]==list[j][1][0]) or (ofThe2Lists(list[i][1][0],list[j][2])==1)):
					print(list[i][1][0],list[j][1][0],i+1,j+1,"=>dependency(-w-a-w-)")

def withBypassingDependencyRAW(list):
	x=len(list)
	for i in range(x-4):
		if((list[i][0][0]=="lw") or (list[i][0][0]=="la")):
			for j in range(i+1,i+2):
				if ((list[i][1][0] in list[j][2])):
					print(list[i][1][0],list[j][2],i+1,j+1,"=>dependency(-r-a-w-)")	
		elif((list[i][0][0]=="sw") or (list[i][0][0]=="sb") or (list[i][0][0]=="move")):
			for j in range(i+1,i+3):
				if ((list[i][1][0] in list[j][2])):
					print(list[i][1][0],list[j][2],i+1,j+1,"=>dependency(-r-a-w-)")
	for i in range(x-4,x-3):
		if((list[i][0][0]=="lw") or (list[i][0][0]=="la")):
			for j in range(x-3,x-2):
				if ((list[i][1][0] in list[j][2])):
					print(list[i][1][0],list[j][2],i+1,j+1,"=>dependency(-r-a-w-)")	
		elif((list[i][0][0]=="sw") or (list[i][0][0]=="sb") or (list[i][0][0]=="move")):
			for j in range(x-3,x-1):
				if ((list[i][1][0] in list[j][2])):
					print(list[i][1][0],list[j][2],i+1,j+1,"=>dependency(-r-a-w-)")
	for i in range(x-3,x-2):
		if((list[i][0][0]=="lw") or (list[i][0][0]=="la")):
			for j in range(x-2,x-1):
				if ((list[i][1][0] in list[j][2])):
					print(list[i][1][0],list[j][2],i+1,j+1,"=>dependency(-r-a-w-)")	
		elif((list[i][0][0]=="sw") or (list[i][0][0]=="sb") or (list[i][0][0]=="move")):
			for j in range(x-2,x):
				if ((list[i][1][0] in list[j][2])):
					print(list[i][1][0],list[j][2],i+1,j+1,"=>dependency(-r-a-w-)")	
	for i in range(x-2,x-1):
		if((list[i][0][0]=="lw") or (list[i][0][0]=="la")):
			for j in range(x-1,x):
				if ((list[i][1][0] in list[j][2])):
					print(list[i][1][0],list[j][2],i+1,j+1,"=>dependency(-r-a-w-)")	
		elif((list[i][0][0]=="sw") or (list[i][0][0]=="sb") or (list[i][0][0]=="move")):
			for j in range(x-1,x):
				if ((list[i][1][0] in list[j][2])):
					print(list[i][1][0],list[j][2],i+1,j+1,"=>dependency(-r-a-w-)")					

def main():
	ins=storeFileInput("randomCode.asm")
	comm=instructionsInList(ins)
	print("ASSUMPTION: 'It takes an entire cycle to read and write'")
	finalList=splitInstructions(comm)
	print("------------------------------------------------------------------")
	for i in range(len(finalList)):
		print(finalList[i]," ===> ",i+1)
	print("\n----------READ AFTER WRITE DEPENDENCY WITHOUT BYPASSING----------")
	withoutBypassingDependencyRAW(finalList)
	'''print("\n----------write-after-write-dependencies-without---------")
	withoutBypassingDependencyWAWoutputRegReadAfter(finalList)'''
	print("\n----------READ AFTER WRITE DEPENDENCY WITH BYPASSING----------")
	withBypassingDependencyRAW(finalList)

main()
