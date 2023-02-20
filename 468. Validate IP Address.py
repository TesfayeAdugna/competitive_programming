class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        l = queryIP.split('.')
        l1=queryIP.split(':')
        if len(l)>0 and len(l)==4:
            for x in l:
                if len(x)>1 and x[0]=='0':
                    return 'Neither'
                if len(x)==0:
                    return 'Neither'
                for k in x:
                    if k.isdigit() == False:
                        return 'Neither'
                if int(x)>=256:
                    return 'Neither'
            return 'IPv4'
        elif len(l1)>0 and len(l1)==8:
            d={'0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','A','B','C','D','E','F'}
            for x in l1:
                if len(x)==0:
                    return 'Neither'
                elif len(x)>4:
                    return 'Neither'
                else:
                    for k in x:
                        if k.isalnum():
                            if  k not in d:
                                return 'Neither'
                        else:
                            return 'Neither'
            return 'IPv6'                    
        else:
            return 'Neither'
