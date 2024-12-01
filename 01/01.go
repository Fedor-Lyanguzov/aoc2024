package main

import (
	"fmt"
	"os"
	"slices"
	"strconv"
	"strings"
)

func Abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func main() {
	bytes, err := os.ReadFile("./input.txt")
	if err != nil {
		panic(err)
	}
	lists := strings.Split(strings.Trim(string(bytes[:]), "\n"), "\n")
	a := make([]int, len(lists))
	b := make([]int, len(lists))
	for i := 0; i < len(lists); i++ {
		x := strings.Split(lists[i], "   ")
		if t, e := strconv.Atoi(x[0]); e == nil {
			a[i] = t
		}
		if t, e := strconv.Atoi(x[1]); e == nil {
			b[i] = t
		}
	}
	slices.Sort(a)
	slices.Sort(b)
	s := 0
	for i := 0; i < len(a); i++ {
		s += Abs(a[i] - b[i])
	}
	fmt.Println(s)
	s = 0
	for i := 0; i < len(a); i++ {
		c := 0
		for j := 0; j < len(b); j++ {
			if a[i] == b[j] {
				c += 1
			}
		}
		s += a[i] * c
	}
	fmt.Println(s)
}
