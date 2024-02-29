ritual main() {
	a = 10
	x = fib(10)
	end x
}

ritual fib(n) {
	if n < 2 {
		end n
	}

	a = fib(n-1)
	b = fib(n-2)

	end a + b
}
