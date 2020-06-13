import time

def bubble_sort(data, drawData, timeTick):
    for _ in range(len(data)-1):
        for j in range(len(data)-1):
            if data[j] > data[j+1]:
                data[j],data[j+1] = data[j+1], data[j]
                drawData(data, ['green' if x == j or x == j+1 else 'red' for x in range(len(data))])
                time.sleep(timeTick)
    drawData(data, ['green' for x in range(len(data))])
    # return data

# data = [1,4,2,7,3,6,5]
# data = bubble_sort(data)
# print(data)
