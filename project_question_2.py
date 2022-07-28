"""
2- Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün. Örnek olarak:

input: [[1, 2], [3, 4], [5, 6, 7]]

output: [[7, 6, 5], [4, 3], [2, 1]]
"""

def rev_list(a_list):
    if isinstance(a_list, list):
        a_list.reverse()
        for ele in a_list:
            rev_list(ele)
    return a_list


print(rev_list([1, 2], [3, 4], [5, 6, 7]))