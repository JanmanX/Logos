ritual main() {
	a = 10
	x = fib(10)

	end x
}

ritual fib(n) {
	t = n - 2 # I don't have le,leq,ge,geq operators yet, so I test like this ;) 
	if t {
		a = fib(n-1)
		b = fib(n-2)
		end a + b
	}

	end 1
}
