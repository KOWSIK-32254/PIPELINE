def isPalindrome(s) {
    return s == s.reverse()
}

// Driver code
String s = "malayalam"
boolean ans = isPalindrome(s)

if (ans) {
    println("Yes")
} else {
    println("No")
}
