package main

import "fmt"

// helper function for getting an integer from standard input
func readInt() int {
	var n int
	fmt.Scanln(&n)
	return n
}

// helper function for getting a string from standard input
func readString() string {
	var s string
	fmt.Scanln(&s)
	return s
}

func print(s string) {
	fmt.Println(s)
}

func main() {
	// TODO: implement problem solution here

	var a int = readInt()
	var b int = readInt()

	print(fmt.Sprint(a + b))

	var s string = readString()
	print(s)
}
