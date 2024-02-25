ritual main() {
	a = 10
	x = fib(10)

	return x
}

ritual fib(n) {
	if n < 2 {
		return 1
	}

	a = fib(n-1)
	b = fib(n-2)
	
	return a + b
}
