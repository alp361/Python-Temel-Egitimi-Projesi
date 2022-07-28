"""
1- Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir. Örnek olarak:

input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

output: [1,'a','cat',2,3,'dog',4,5]
"""

def flatten(a_list):    
    new_list = []
    def loop(nested_list):
        for ele in nested_list:
            if (isinstance(ele, list)):
                loop(ele)
            else:
                new_list.append(ele)
    loop(a_list)
    return new_list
               
print(flatten([[1,'a',['cat'],2],[[[3]],'dog'],4,5]))






