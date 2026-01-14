data=[18,21,35,4,5,6,7,6,5,4,33]
it=iter(data)
print(next(it))
print(next(it))
print(next(it))

class count:

    def __init__(self,limit):
        self.limit=limit
        self.current=1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current<=self.limit:
            val=self.current
            self.current +=1
            return val
        else:
            raise StopIteration

obj=count(3)

for num in obj:
    print(num)