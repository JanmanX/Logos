ritual main () {
	a = 4
	b = alloc 32

	while a > 0 {
		[b] = a
		a = a - 1
		b = b + 1
	}
}


