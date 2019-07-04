class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        hashmap = defaultdict(int)
        for low_domain in cpdomains:
            visites, full_domain = low_domain.split(" ")
            visites = int(visites)
            domains = full_domain.split(".")
            
            if len(domains) >= 3:
                # full domain
                hashmap[full_domain] += visites
                # second to last domain
                mid = ".".join(domains[-2:])
                hashmap[mid] += visites
                # last domain
                hashmap[domains[-1]] += visites

            else:
                hashmap[full_domain] += visites 
                hashmap[domains[-1]] += visites
                    
                    
            result = []
            for key, val in hashmap.items():
                result.append(f"{val} {key}")
                
        return result


test = ["901 discuss.leetcode.com"]
#Test output

print(test)
