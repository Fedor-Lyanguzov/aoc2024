package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
	"slices"
)

func SplitByLines(bytes []byte) []string {
	return strings.Split(strings.Trim(string(bytes[:]), "\n"), "\n")
}

func Less(a, b int) bool {
	return a<b
}
func More(a, b int) bool {
	return a>b
}
func P(f func (int, int) bool, a, b int) bool {
	return f(a, b) && Abs(a-b)<=3
}
func Abs(x int) int {
	if x<0 {
		x = -x
	}
	return x
}
func Safe1(l []int, j, e int) bool {
	f := Less
	if l[j-1]>l[j] { f = More }
	for j<e && P(f, l[j-1], l[j]){
		j++
	}
	r := j<e
	return !r
}
func Safe2(l []int) bool {
	if l[0]==l[1] { return false }
	f := Less
	if l[0]>l[1] { f = More }
	c := 0
	j := 2
	for j<len(l) && c<2 {
		if !(P(f, l[j-1], l[j])) && (P(f, l[j-2], l[j])) { 
			c++ 
		}
		j++
	}
	return c<2
}
func main() {
	bytes, err := os.ReadFile("./input.txt")
	if err != nil { panic(err) }
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
		if Safe1(l, 1, len(l)) { s++ }
	}
	fmt.Println(s)
	s = 0
	for _, l := range data {
		t := make([]int, len(l))
		copy(t, l)
		t = slices.Delete(t, 1, 2)
		if Safe1(l, 1, len(l)) || 
			Safe1(l, 2, len(l)) || 
			Safe1(t, 1, len(t)) || 
			Safe1(l, 1, len(l)-1) {
			s++ 
		} else if Safe2(l) { 
			fmt.Println(l)
			s++ 
		}
	}
	fmt.Println(s)
	println(len(data))
}
