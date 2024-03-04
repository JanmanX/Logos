ritual is_prime(n)
{
	if n <= 1 {
		end 0
	}

	divisor = 2
	while divisor * divisor <= n {

		m = n / divisor


		if divisor * m  == n {
			end 0
		}

		divisor = divisor + 1
	}

	end 1

}

ritual main()
{
	x = is_prime(4441)
	end x
}
