#[10,80,30,90,40,50,70]
def partition(Lst1, Start1, End1):
    pivot = Start1
    while Start1 < l and Lst1[Start1] >= Lst1[pivot]:
        Start1 += 1
    while Lst1[End1] < Lst1[pivot]:
        End1 -= 1

    if Start1 < End1:
        Lst1[Start1], Lst1[End1] = Lst1[End1], Lst1[Start1]
        partition(Lst1, Start1, End1)

    if End1 != pivot:
        Lst1[End1], Lst1[pivot] = Lst1[pivot], Lst1[End1]
    return End1

def quick_sort(Lst, Start, End):
    if Start < End:
        mid = partition(Lst, Start, End)
        quick_sort(Lst, Start, mid-1)
        quick_sort(Lst, mid+1, End)

B=int(input("Enter the number of bundles of books required"))
for i in range(B):
    lst=eval(input('Enter the list with number of pages'))
    l=len(lst)
    start=0
    end=l-1
    quick_sort(lst, start, end)
    print('The Sorted List wrt to number of pages',lst)
