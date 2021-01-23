# string permutation in lexicographically order with repetition of characters in the string
# https://github.com/mission-peace/interview/blob/master/python/recursion/stringpermutation.py


def permute(input):
    count_map = {}
    for ch in input:
        if ch in count_map.keys():
            count_map[ch] = count_map[ch] + 1
        else:
            count_map[ch] = 1

    keys = sorted(count_map)
    str = []
    count = []
    for key in keys:
        str.append(key)
        count.append(count_map[key])
    result = [0 for x in range(len(input))]
    permute_util(str, count, result, 0)

def permute_util(str, count, result, level):
    if level == len(result):
        print(result)
        return

    for i in range(len(str)):
        if count[i] == 0:
            continue;
        result[level] = str[i]
        count[i] -= 1
        permute_util(str, count, result, level + 1)
        count[i] += 1

if __name__ == '__main__':
    # input = ['B', 'C', 'A', 'A']
    input = [1,2,3]
    permute(input)