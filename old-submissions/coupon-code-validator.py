class Solution:
    def validateCoupons(self, code, businessLine, isActive):
        categories = ["electronics", "grocery", "pharmacy", "restaurant"]
        order = {c: i for i, c in enumerate(categories)}

        valid = []

        for i in range(len(code)):
            if (
                code[i]
                and all(ch.isalnum() or ch == '_' for ch in code[i])
                and businessLine[i] in order
                and isActive[i]
            ):
                valid.append((order[businessLine[i]], code[i]))

        valid.sort()
        return [c for _, c in valid]
