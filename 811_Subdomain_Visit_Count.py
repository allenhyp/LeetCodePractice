class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        dic = {}
        for cpdomain in cpdomains:
            parser = cpdomain.split(' ')
            num, domain_str = int(parser[0]), parser[1]
            domains = domain_str.split('.')
            domain = domains[-1]
            dic[domain] = dic.get(domain, 0) + num
            for i in range(len(domains) - 2, -1, -1):
                domain = domains[i] + '.' + domain
                dic[domain] = dic.get(domain, 0) + num
        
        res = []
        for key, val in dic.items():
            res.append("{0} {1}".format(key, val))
        return res


def main():
    my_solution = Solution()
    print(my_solution.subdomainVisits(["900 google.com", "1 leetcode.com"]))


if __name__ == "__main__":
    main()
