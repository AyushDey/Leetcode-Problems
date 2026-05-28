class Solution:

    def encode(self, strs: list[str]) -> str:
        return ''.join(f'{len(s)}#{s}' for s in strs)
            
    def decode(self, s: str) -> list[str]:
        res = []
        i = 0

        while i < len(s):
            j = s.find('#', i)
            str_len = int(s[j - 1])
            str_end = j + 1 + str_len
            res.append(s[j+1: str_end])
            i = str_end
        return res
            

if __name__ == '__main__':
    s = Solution()
    strs = ["Hello", "World"]
    encoded_string = s.encode(strs)
    print(encoded_string)
    decoded_list = s.decode(encoded_string)
    print(decoded_list)