import os
import time

array = []

with open('data.txt') as file:
    array = file.readlines()

data = [s.strip('\n') for s in array]
data_path = os.listdir("./input")
start = time.time()
def main():
    event_name = input('Enter Event Name: ')

    for i in range(len(data_path)):
        filename = data_path[i]
        name = data[i]
        dst_init = event_name + '_' + name + ".jpg"
        src = './input/' + filename
        dst = './input/' + dst_init
        os.rename(src,dst)
        print(f'renamed {filename} to {dst_init}')
if __name__ == '__main__':
    main()
else:
    print("Error running code")
end = time.time()
run_time = round(end-start,3)        
print(f'Task finished [{run_time}ms]')