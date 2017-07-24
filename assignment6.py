def swap(l, begin, end):
    tmp = l[begin]
	l[begin] = l[end]
	l[end] = tmp

def rearrage(src, target):

	free = 0

	src_ind = dict([(a, i) for i, a in enumerate(src)])
	target_ind = dict([(a, i) for i, a in enumerate(target)])

	i = src_ind[free]
	if target_ind[free] == i:
		swap(src, i, i + 1)
		src_ind[free] = i + 1
		src_ind[src[i]] = i

	while i != target_ind[free]:
		j = src_ind[target[i]]
		swap(src, i, j)
		src_ind[src[i]] = i
		i = j
