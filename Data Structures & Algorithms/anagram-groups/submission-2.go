func groupAnagrams(strs []string) [][]string {
    // create storage
    group := make(map[[26]int][]string)

    for _, value := range strs {
        var count [26]int
        for _, c := range value {
            count[c-'a']++
        }
        group[count] = append(group[count], value)
    }

    // covert to list of sublist
    var output [][]string
    for _, value := range group {
        output = append(output, value)
    }

    return output
}
