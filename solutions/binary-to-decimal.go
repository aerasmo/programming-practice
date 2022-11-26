package kata

import "strconv"

func BinToDec(bin string) int {
	r, _ := strconv.ParseInt(bin, 2, 64)
	return int(r)
}
