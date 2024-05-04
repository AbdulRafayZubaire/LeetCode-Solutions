class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:

        if not version1 and version2:
            return 0
        if not version1:
            return -1
        if not version2:
            return 1
        
        v_1 = version1.split('.')
        v_2 = version2.split('.')
        new_v_1 = []
        new_v_2 = []

        for i in range(len(v_1)):
            if v_1[i] != '0':
                v_1[i] = v_1[i].lstrip('0')
            if v_1[i] == '':
                new_v_1.append('0')
                continue    
            new_v_1.append(v_1[i])

        for i in range(len(v_2)):
            if v_2[i] != '0':
                v_2[i] = v_2[i].lstrip('0')
            if v_2[i] == '':
                new_v_2.append('0')
                continue
            new_v_2.append(v_2[i])
        print(new_v_1)
        print(new_v_2)

        for i in range(max(len(new_v_1), len(new_v_2))):
            if i < len(new_v_1) and i < len(new_v_2):

                if int(new_v_1[i]) > int(new_v_2[i]):
                    return 1
                elif int(new_v_1[i]) < int(new_v_2[i]):
                    return -1
            else:
                temp_1 = ''.join(new_v_1).rstrip('0')
                temp_2 = ''.join(new_v_2).rstrip('0')
                if len(temp_1) > len(temp_2):
                    return 1
                elif len(temp_1) < len(temp_2):
                    return -1
                else:
                    return 0
        return 0