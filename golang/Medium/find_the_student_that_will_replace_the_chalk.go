// https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/description/

package main

import "fmt"

func chalkReplacer(chalk []int, k int) int {
	sum_of_chalk := 0
	for i := range chalk {
		sum_of_chalk += chalk[i]
	}
	left := k % sum_of_chalk
	if left == 0 {
		return 0
	}
	for i, number := range chalk {
		if left-number < 0 {
			return i
		}
		left -= number
	}
	return 0
}
func main() {
	chalk := []int{3, 4, 1, 2}
	fmt.Println(chalkReplacer(chalk, 25))

}

