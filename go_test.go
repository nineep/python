package main
import "fmt"

func main() {
    var a string = "Runoob"
    fmt.Println(a)

    var b, c int = 1, 2
    fmt.Println(b, c)
}


package main
import "fmt"

func main() {
    var a = "RUNOOB"
    fmt.Println(a)
    var b int
    fmt.Println(b)

    var c bool
    fmt.Println(c)
}


package main
var x, y int
var (
    a int
    b bool
)

var c, d int = 1, 2
var e, f = 123, "hello"

func main() {
    g, h := 123, "hello"
    println(x, y, a, b, c, d, e, f, g, h)
}