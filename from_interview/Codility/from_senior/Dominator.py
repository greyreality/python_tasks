# Detected time complexity: O(N)
# correctness 100%
# hz kak sdelal
def solution(A):
    candidate_ele = ''
    candidate_cnt = 0

    for value in A:
        if candidate_ele == '':
            candidate_ele = value
            candidate_cnt = 1
        else:
            if value != candidate_ele:
                candidate_cnt -= 1
                if candidate_cnt == 0:
                    candidate_ele = ''
            else:
                candidate_cnt += 1

    if candidate_cnt == 0:
        return -1

    cnt = 0
    last_idx = 0

    for idx, value in enumerate(A):
        if value == candidate_ele:
            cnt += 1
            last_idx = idx

    if cnt > len(A) // 2:
        return last_idx

    return -1

test = [4,0,0,0,1]
print('res=', solution(test))