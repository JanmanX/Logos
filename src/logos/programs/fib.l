ritual main() {
	a = 10
	x = fib(10)

	end x
}

ritual fib(n) {
	if n < 2 {
		a = fib(n-1)
		b = fib(n-2)
		end a + b
	}

	end 1
}
