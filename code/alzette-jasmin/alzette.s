	.att_syntax
	.text
	.p2align	5
	.globl	_alzette
	.globl	alzette
_alzette:
alzette:
	movl	%edx, %eax
	rorl	$31, %eax
	addl	%eax, %esi
	movl	%esi, %eax
	rorl	$24, %eax
	xorl	%eax, %edx
	xorl	%edi, %esi
	movl	%edx, %eax
	rorl	$17, %eax
	addl	%eax, %esi
	movl	%esi, %eax
	rorl	$17, %eax
	xorl	%eax, %edx
	xorl	%edi, %esi
	movl	%edx, %eax
	rorl	$0, %eax
	xorl	%eax, %esi
	movl	%esi, %eax
	rorl	$31, %eax
	xorl	%eax, %edx
	xorl	%edi, %esi
	movl	%edx, %eax
	rorl	$24, %eax
	addl	%eax, %esi
	movl	%esi, %eax
	movl	%eax, %ecx
	rorl	$16, %ecx
	xorl	%ecx, %edx
	xorl	%edi, %eax
	ret
