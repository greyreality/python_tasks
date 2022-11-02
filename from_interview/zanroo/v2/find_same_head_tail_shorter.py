# Given a string 'source', find the longest sub-string that appears at both the head and tail of the
# string. Note that the strings at the head and tail should not overlap.
# find_same_head_tail(source)
# find_same_head_tail('abcdeab') → ‘ab'
# find_same_head_tail('aa') → ‘a’
# find_same_head_tail('bbb') → ‘b’

def find_same_head_tail(source):
    for i in range(len(source) // 2, 0, -1):
        print('i=',source[:i],'; -i=',source[-i:])
        if source[:i] == source[-i:]:
            return source[:i]

    return 'None'

print('answer=',find_same_head_tail('abcdeab'))
print('answer=',find_same_head_tail('aa'))
print('answer=',find_same_head_tail('bbb'))
print('answer=',find_same_head_tail('abcdeabg'))