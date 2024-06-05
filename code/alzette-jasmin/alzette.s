	.att_syntax
	.text
	.p2align	5
	.globl	_alzette
	.globl	alzette
_alzette:
alzette:
	movl	$47073, %ecx
	movl	%esi, %eax
	rorl	$31, %eax
	addl	%eax, %edi
	movl	%edi, %eax
	rorl	$24, %eax
	xorl	%eax, %esi
	xorl	%ecx, %edi
	movl	%esi, %eax
	rorl	$17, %eax
	addl	%eax, %edi
	movl	%edi, %eax
	rorl	$17, %eax
	xorl	%eax, %esi
	xorl	%ecx, %edi
	movl	%esi, %eax
	rorl	$0, %eax
	xorl	%eax, %edi
	movl	%edi, %eax
	rorl	$31, %eax
	xorl	%eax, %esi
	xorl	%ecx, %edi
	movl	%esi, %eax
	rorl	$24, %eax
	addl	%eax, %edi
	movl	%edi, %eax
	movl	%eax, %edx
	rorl	$16, %edx
	xorl	%edx, %esi
	movl	%esi, %edx
	xorl	%ecx, %eax
	ret
