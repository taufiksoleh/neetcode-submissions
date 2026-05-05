import "slices"

func groupAnagrams(strs []string) [][]string {
    // create storage
    group := map[string][]string{}

    for _, value := range strs {
        // sort the string value for storage key
        sorted := sortString(value)

        added := append(group[sorted], value)
        group[sorted] = added
    }

    // covert to list of sublist
    output := [][]string{}
    for _, value := range group {
        output = append(output, value)
    }

    return output
}

func sortString(value string) string {
    r := []rune(value)
    slices.Sort(r)
    return string(r)
}
