import re


class Solution:
    def validIPAddress(self, IP: str) -> str:
        ipv4 = IP.split(".")
        if len(ipv4) == 4:
            return self.validate_IPv4(ipv4)

        ipv6 = IP.split(":")
        if len(ipv6) == 8:
            return self.validate_IPv6(ipv6)

        return "Neither"

    @staticmethod
    def validate_IPv6(lst):
        for g in lst:
            if not (1 <= len(g) <= 4):
                return "Neither"
            hex_num = re.findall("(?i)[0-9a-fA-F]+", g)
            if len(hex_num) != 1 or len(g) != len(hex_num[0]):
                return "Neither"
        return "IPv6"

    @staticmethod
    def validate_IPv4(lst):
        for g in lst:
            check = re.findall("25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9]", g)
            if len(check) != 1 or len(g) != len(check[0]):
                return "Neither"
        return "IPv4"


check = Solution()
print(check.validIPAddress("2001:0db8:85a3:0000:0000:8a2e:0370:7334"))



"""
"2001:0db8:85a3:0000:0000:8a2e:0370:7334" "valid" 
"2001:0db8:85a3::8A2E:0370:7334" "invalid"

"02001:0db8:85a3:0000:0000:8a2e:0370:7334" "invalid"
"""
