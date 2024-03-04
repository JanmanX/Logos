CC = as
AR = ar
CFLAGS = -o

all: libc.a

libc.a: libc.o
	$(AR) -rc $@ $^

libc.o: libc.s
	$(CC) $(CFLAGS) $@ $^

clean:
	rm -f libc.o libc.a

