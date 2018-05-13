class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        domains = {}
        for s in cpdomains:
            t = s.split(' ')
            cnt = int(t[0])
            d = t[1].split('.')
            p = d[-1]
            for i in range(len(d) - 2, -1, -1):
                if p not in domains:
                    domains[p] = cnt
                else:
                    domains[p] += cnt
                p = d[i] + '.' + p
            if p not in domains:
                domains[p] = cnt
            else:
                domains[p] += cnt
        result = []
        for key in domains.keys():
            result.append("{0} {1}".format(domains[key], key))
        return result


def main():
    my_solution = Solution()
    print(my_solution.subdomainVisits(["900 google.com", "1 leetcode.com"]))


if __name__ == "__main__":
    main()
