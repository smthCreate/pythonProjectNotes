def insertion_sort(alist):
    for i in range(1, len(alist)):
        temp = alist[i]
        j = i - 1
        while (j >= 0 and temp < alist[j]):
            alist[j + 1] = alist[j]
            j = j - 1
        alist[j + 1] = temp


alist = {"hdfvbdh":23,"djfhkdj":32,"jdxfvb":1}
# insertion_sort(alist)
# print('Sorted list: ', end='')
newD = dict(sorted(alist.items(),key=lambda item: item[1]))
for i in newD.items():
    print(i[0])

