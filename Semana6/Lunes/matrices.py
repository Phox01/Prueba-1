def counting():
    count=0
    accounts=[[1,2,3], [2, 3, 4]]
    for lista in accounts:
        if sum(lista)>count:
            count=sum(lista)
        return count
counting()
