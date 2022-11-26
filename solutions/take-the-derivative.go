package kata

import "fmt"

func Derive(coefficient, exponent int) (res string) {
	product := coefficient * exponent
	res = fmt.Sprintf("%dx^%d", product, exponent-1)
	return
}
