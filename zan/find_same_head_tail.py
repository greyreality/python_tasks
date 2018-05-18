# Given a string 'source', find the longest sub-string that appears at both the head and tail of the
# string. Note that the strings at the head and tail should not overlap.
# find_same_head_tail(source)
# find_same_head_tail('abcdeab') → ‘ab'
# find_same_head_tail('aa') → ‘a’
# find_same_head_tail('bbb') → ‘b’

def find_same_head_tail(source):
    # print('source=', source)
    if len(source) > 1:
        mid = len(source) // 2

        if len(source) % 2 == 0:
            lefthalf = source[:mid]
            righthalf = source[mid:]
        else:
            lefthalf = source[:mid]
            righthalf = source[mid+1:]
    # print('lefthalf=',lefthalf)
    # print('righthalf=',righthalf)

    head = ''
    result = None
    for i in range(0,mid):
        head = head + lefthalf[i]
        # print('head=', head)
        if head in righthalf:
            # print('its here',head)
            result = head
    if result[-1::] == righthalf[-1::]:
        return result

print(find_same_head_tail('abcdeab'))# → ‘ab'
print(find_same_head_tail('aa'))#  → ‘a’
print(find_same_head_tail('bbb'))#  → ‘b’
print(find_same_head_tail('abcdeabg'))# → ‘'