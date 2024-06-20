	.att_syntax
	.text
	.p2align	5
	.globl	_schwaemm
	.globl	schwaemm
_schwaemm:
schwaemm:
	subq	%rdi, %rsi
	subq	%rdx, %rcx
	testq	$31, %rsi
	je  	Lschwaemm$12
Lschwaemm$12:
	testq	$31, %rcx
	je  	Lschwaemm$11
Lschwaemm$11:
	cmpq	$0, %rsi
	je  	Lschwaemm$6
	jmp 	Lschwaemm$9
Lschwaemm$10:
	addq	$-32, %rsi
Lschwaemm$9:
	cmpq	$256, %rsi
	jb  	Lschwaemm$10
	vpxor	%ymm1, %ymm1, %ymm1
	movq	$0, %rax
	jmp 	Lschwaemm$7
Lschwaemm$8:
	incq	%rax
Lschwaemm$7:
	cmpq	%rsi, %rax
	jb  	Lschwaemm$8
Lschwaemm$6:
	cmpq	$0, %rcx
	je  	Lschwaemm$1
	jmp 	Lschwaemm$4
Lschwaemm$5:
	addq	$-32, %rcx
Lschwaemm$4:
	cmpq	$256, %rcx
	jb  	Lschwaemm$5
	vpxor	%ymm1, %ymm1, %ymm1
	movq	$0, %rax
	jmp 	Lschwaemm$2
Lschwaemm$3:
	incq	%rax
Lschwaemm$2:
	cmpq	%rcx, %rax
	jb  	Lschwaemm$3
Lschwaemm$1:
	ret
