#include <stdio.h>
#include <stdlib.h>

// Finds the first n fib numbers and prints in reverse order
void reverseFibonacci(int n) {
	int fib[n];
	
	fib[0] = 0;
	fib[1] = 1;
	
	//fill out fib array
	for (int i = 2; i<n; i++) {
		fib[i] = fib[i-2] + fib[i-1];
	}
	
	//reverse
	int start = 0;
	int end = n-1;
	while (start < end) {
		int temp = fib[start];
		fib[start] = fib[end];
		fib[end] = temp;
		start++;
		end--;
	}
	
	//print array
	for (int i = 0; i<n; i++) {
		printf("%d\n", fib[i]);
	}
}

// main takes in num of desired fibonacci numbers 
int main(int argc, char**argv) {
	int num;
	if (argc > 1) {
		num = atoi(argv[1]);
	} else {
		printf("Requires one numeric argument\n");
		exit(1);
	}
	reverseFibonacci(num);
}
