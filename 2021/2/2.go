package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"strconv"
	"strings"
)

type Adjustment struct {
	instruction string
	magnitude   int
}

func (this Adjustment) getAim() int {
	switch this.instruction {
	case "up":
		return -1 * this.magnitude
	case "down":
		return this.magnitude
	default:
		return 0
	}
}

func (this Adjustment) getForward() int {
	switch this.instruction {
	case "forward":
		return this.magnitude
	default:
		return 0
	}
}

func main() {
	adjustments := buildAgg()
	part1(adjustments)
	part2(adjustments)
}

func part2(adjustments []Adjustment) {
	depth := 0
	aim := 0
	horizontal := 0

	for _, adjustment := range adjustments {
		aim = aim + adjustment.getAim()
		forward := adjustment.getForward()
		horizontal = horizontal + forward
		depth = depth + forward*aim
	}

	product := horizontal * depth

	fmt.Println(fmt.Sprintf("Part 2: %d", product))
}

func part1(adjustments []Adjustment) {
	aggregate := make(map[string]int)
	aggregate["forward"] = 0
	aggregate["up"] = 0
	aggregate["down"] = 0

	for _, val := range adjustments {
		aggregate[val.instruction] = aggregate[val.instruction] + val.magnitude
	}

	fmt.Println(aggregate)

	depth := aggregate["down"] - aggregate["up"]
	horizontal := aggregate["forward"]
	product := depth * horizontal

	fmt.Println(fmt.Sprintf("Part 1: %d", product))
}

func buildAgg() []Adjustment {
	const filename = "2-input.csv"

	contents, err := ioutil.ReadFile(filename)
	handleError(err)

	tokens := strings.Split(string(contents), "\n")

	var adjustments []Adjustment

	for i, val := range tokens {
		split := strings.Split(val, " ")

		if len(split) < 2 {
			fmt.Printf("Row %d cannot split '%s'\n", i, val)
			continue
		}

		direction := split[0]
		magnitude, err := strconv.Atoi(split[1])
		handleError(err)

		adjustments = append(adjustments, Adjustment{direction, magnitude})
	}

	return adjustments
}

func handleError(err error) {
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
}

func statfile(filename string) {
	f, err := os.Open(filename)
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
	fmt.Println(f.Stat())
	defer f.Close()
}
