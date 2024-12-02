package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func SplitByLines(bytes []byte) []string {
	return strings.Split(strings.Trim(string(bytes[:]), "\n"), "\n")
}

func Less(a, b int) bool {
	return a < b
}
func More(a, b int) bool {
	return a > b
}
func P(f func(int, int) bool, a, b int) bool {
	return f(a, b) && Abs(a-b) <= 3
}
func Abs(x int) int {
	if x < 0 {
		x = -x
	}
	return x
}
func Safe1(l []int) bool {
	if l[0] == l[1] {
		return false
	}
	f := Less
	if l[0] > l[1] {
		f = More
	}
	j := 1
	for j < len(l) && P(f, l[j-1], l[j]) {
		j++
	}
	r := j < len(l)
	return !r
}
func Safe2(l []int) bool {
	cl := 0
	cm := 0
	cq := 0
	il := -1
	im := -1
	iq := -1
	for i := 1; i < len(l); i++ {
		a := l[i-1]
		b := l[i]
		if a >= b {
			cl++
			if il == -1 {
				il = i
			}
		}
		if a <= b {
			cm++
			if im == -1 {
				im = i
			}
		}
		if Abs(a-b) > 3 {
			cq++
			if iq == -1 {
				iq = i
			}
		}
	}
	if cq == 0 && (cm == 0 || cl == 0) {
		return true
	}
	if cq > 2 || cl > 2 && cm > 2 {
		return false
	}
	if cq == 2 {
		return Safe1(Skip(l, iq))
	}
	if iq != -1 {
		return Safe1(Skip(l, iq)) || Safe1(Skip(l, iq-1))
	}
	if 0 < cl && cl <= 2 {
		return Safe1(Skip(l, il)) || Safe1(Skip(l, il-1))
	}
	if 0 < cm && cm <= 2 {
		return Safe1(Skip(l, im)) || Safe1(Skip(l, im-1))
	}
	return false
}
func Skip(l []int, i int) []int {
	n := make([]int, len(l)-1)
	k := 0
	for j, x := range l {
		if j != i {
			n[k] = x
			k++
		}
	}
	return n
}
func main() {
	bytes, err := os.ReadFile("./input.txt")
	if err != nil {
		panic(err)
	}
	lines := SplitByLines(bytes)
	data := make([][]int, len(lines))
	for i, l := range lines {
		nums := strings.Split(l, " ")
		data[i] = make([]int, len(nums))
		for j, c := range nums {
			if k, e := strconv.Atoi(c); e == nil {
				data[i][j] = k
			}
		}
	}
	s := 0
	for _, l := range data {
		if Safe1(l) {
			s++
		}
	}
	fmt.Println(s)
	s = 0
	for _, l := range data {
		if Safe2(l) {
			s++
		}
	}
	fmt.Println(s)
}
