// https://www.codewars.com/kata/545af3d185166a3dec001190

package kata

func EachCons(arr []int, n int) (res [][]int) {
	for i := 0; i+n <= len(arr); i++ {
		res = append(res, arr[i:i+n])
	}
	return
}
