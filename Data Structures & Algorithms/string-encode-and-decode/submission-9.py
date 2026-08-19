class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""

        for s in strs:
            encoded_str += f"{len(s)}#{s}"

        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_str = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != '#':
                j += 1

            lng = int(s[i:j])

            word_start = j + 1
            word_end = word_start + lng
            
            decoded_str.append(s[word_start:word_end])

            i = word_end

        return decoded_str


        
