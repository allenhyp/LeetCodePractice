class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        return ''.join('{0}:{1}'.format(len(s), s) for s in strs)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        ret = []
        i = 0
        while i < len(s):
            j = s.find(':', i)
            i = j+1+int(s[i:j])
            ret.append(s[j+1:i])
        return ret


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
