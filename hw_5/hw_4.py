from decor import logger


# Итератор, который принимает список списков, и возвращает их плоское представление.
# Задания № 1,3 
class FlatIterator:

    @logger(path_to_log='files1')
    def __init__(self, list_for_processing):
        self.flat_list = self.flattener(list_for_processing)
        self.cursor = -1        

    @logger(path_to_log='files1')
    def __iter__(self):
        return self

    @logger(path_to_log='files1')
    def __next__(self):        
        self.cursor += 1
        if self.cursor == len(self.flat_list):
            raise StopIteration
        return self.flat_list[self.cursor]

    @logger(path_to_log='files2')
    def flattener(self, some_list):
        flattened_list = []
        for item in some_list:
            if isinstance(item, (tuple, list)):
                flattened_list.extend(self.flattener(item))
            else:
                flattened_list.append(item)                             
        return flattened_list
    
# Генератор, который принимает список списков, и возвращает их плоское представление.
# Задания № 2,4 
@logger(path_to_log='files3')
def flat_generator(list_for_processing):
    for item in list_for_processing:
        if isinstance(item, (tuple, list)):
            yield from flat_generator(item)            
        else:
            yield item
    

if __name__ == '__main__':

    nested_list = [
	['a', ['b', 'c']],
	[[[[['d', ], 'e'], 'f'], 'h'], False],
	[1, 2, None],
]     

print()
print('Последовательность из вложенных элементов списка, обработанного итератором:')
for item in FlatIterator(nested_list):
    print(item)

print()
print('Плоский список из вложенных элементов списка, обработанного итератором:')
flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)

print()
print('Последовательность из вложенных элементов списка, обработанного генератором:')
for item in flat_generator(nested_list):
    print(item)