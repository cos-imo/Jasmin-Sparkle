	.att_syntax
	.text
	.p2align	5
	.globl	_alzette
	.globl	alzette
_alzette:
alzette:
	movl	$-1209970334, %ecx
	rorl	$31, %esi
	addl	%esi, %edi
	rorl	$1, %esi
	rorl	$24, %edi
	xorl	%edi, %esi
	rorl	$8, %edi
	xorl	%ecx, %edi
	rorl	$17, %esi
	addl	%esi, %edi
	rorl	$15, %esi
	rorl	$17, %edi
	xorl	%edi, %esi
	rorl	$15, %edi
	xorl	%ecx, %edi
	rorl	$0, %esi
	xorl	%esi, %edi
	rorl	$31, %edi
	xorl	%edi, %esi
	movl	%esi, %edx
	rorl	$1, %edi
	xorl	%ecx, %edi
	rorl	$24, %edx
	addl	%edx, %edi
	movl	%edi, %eax
	rorl	$8, %edx
	rorl	$16, %eax
	xorl	%eax, %edx
	rorl	$16, %eax
	xorl	%ecx, %eax
	ret
