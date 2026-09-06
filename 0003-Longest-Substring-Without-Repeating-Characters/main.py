def lengthOfLongestSubstring(s: str) -> int:
    left = 0
    right = 0
    output = 0
    seen = set()
    while right < len(s):
        if s[right] not in seen:
            seen.add(s[right])
            right += 1
            if len(seen) > output:
                output = len(seen)
        else:
            seen.remove(s[left])
            left += 1
    
    return output

if __name__ == '__main__':
    print(lengthOfLongestSubstring(s="abcabcbb"))