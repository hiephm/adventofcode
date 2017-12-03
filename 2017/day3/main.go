package main

import (
	"fmt"
	"log"
)

var input = 277678
var m = make([][]int, 1000)

func main() {
	fmt.Printf("Part 1: %d\n", 475) // input < 277729 = 527^2. 475 = 527 / 2 + (527 / 2 -  (277729 - 277678))
	fmt.Printf("Part 2: %d\n", part2())
}

func part2() int {
	for i := 0; i < cap(m); i++ {
		m[i] = make([]int, 1000)
	}

	x, y := 500, 500
	m[y][x] = 1

	previousDir := ""
	nextNum := 0
	for i := 1; i < 1000000; i++ {
		x, y, previousDir = move(x, y, previousDir)
		nextNum = calculate(x, y)
		m[y][x] = nextNum
		if nextNum > input {
			return nextNum
		}
	}
	return 0
}

func move(x, y int, previousMove string) (x1, y1 int, dir1 string) {
	// move right
	if previousMove == "" || previousMove == "down" {
		if m[y][x+1] == 0 {
			return x + 1, y, "right"
		} else {
			return x, y + 1, "down"
		}
	}

	// move up
	if previousMove == "right" {
		if m[y-1][x] == 0 {
			return x, y - 1, "up"
		} else {
			return x + 1, y, "right"
		}
	}

	// move left
	if previousMove == "up" {
		if m[y][x-1] == 0 {
			return x - 1, y, "left"
		} else {
			return x, y - 1, "up"
		}
	}

	// move down
	if previousMove == "left" {
		if m[y+1][x] == 0 {
			return x, y + 1, "down"
		} else {
			return x - 1, y, "left"
		}
	}

	log.Fatal("Invalid move")
	return
}

func calculate(x, y int) int {
	return m[y+1][x] + m[y][x+1] + m[y-1][x] + m[y][x-1] + m[y+1][x+1] + m[y+1][x-1] + m[y-1][x+1] + m[y-1][x-1]
}
