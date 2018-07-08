.data
x: .space 1000
yo: .asciiz "is prime\n"
no: .asciiz "not prime\n"
.text
li $t1,4
li $t2,0
li $t4,1
li $t3,8
sw $t2,x($t2)
sw $t2,x($t1)
addi $t1,$t1,4
loop1:
	beq $t1,1000,loop2
	sw $t4,x($t1)
	addi $t1,$t1,4
	# kk yugi h
	j loop1
loop2:
	beq $t3,1000,check
	div $t5,$t3,4
	#ny kynk kn knkh
	lw $t6,x($t3)
	addi $t3,$t3,4
	beq $t6,1,loop3	
loop3:

	mul $t5,$t5,4
	
	add $t5,$t5,$t5      #comment 1
	
	bgt $t5,1000,l
	
	sw $t2,x($t5)
	
	mul $t7,$t5,4        #comment 2
	slt $s0,$t0,$t1
	sll $t0,arr($t1),3
	addi $t5,$t7,0
	j loop3
l:
	j loop2
check:
	li $v0,5
	syscall
	
	move $t0,$v0	
	mul $t0,$t0,4		# comment 3
	
	
	
	lw $t1,x($t0)	
	bne $t1,1,n
	beq $t1,1,yes
	li $v0,10
	syscall
yes:
	li $v0,4
	la $a0,yo
	syscall
	j check			# comment 4
n:
	li $v0,4
	la $a0,no
	syscall 
