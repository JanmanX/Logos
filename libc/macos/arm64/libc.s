.text

.global exit
exit:
	mov x16, #1
	svc #0x80

.global write
write:
	mov X16, #4
	svc #0x80
