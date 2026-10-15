class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        s_counts = Counter(s)
        odd_chars = []
        
        for char, count in s_counts.items():
            if count % 2 != 0:
                odd_chars.append(char)

        if n % 2 == 0 and len(odd_chars) > 0:
            return ""
        if n % 2 != 0 and len(odd_chars) != 1:
            return ""

        middle_char = odd_chars[0] if odd_chars else ""

        half_counts = Counter()
        for char, count in s_counts.items():
            half_counts[char] = count // 2
            

        half_len = n // 2

        def build_palindrome(half_str):
            return half_str + middle_char + half_str[::-1]

        def find_smallest_half(index, current_half, counts):
            if index == half_len:
                result = build_palindrome(current_half)
                return result if result > target else ""

            for char_code in range(ord('a'), ord('z') + 1):
                c = chr(char_code)

                if counts[c] > 0:
                    prefix = current_half + c
                    target_prefix = target[:index + 1]

                    if prefix < target_prefix:
                        continue

                    counts[c] -= 1

                    if prefix > target_prefix:
                        remaining_half = ""
                        for fil_cc in range(ord('a'), ord('z')+1):
                            fil_c = chr(fil_cc)
                            remaining_half += fil_c * counts[fil_c]

                        half = prefix + remaining_half
                        result = build_palindrome(half)
                        return result

                    found = find_smallest_half(index+1, prefix, counts)
                    counts[c] += 1

                    if found:
                        return found

            return ""

        return find_smallest_half(0, "", half_counts)
        