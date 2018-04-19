import multiprocessing


def calculate_area(params, result, pi):
	pi.value = 3.14
	for index, redius in enumerate(params):
		result[index] = pi.value  * redius * redius

if __name__ == '__main__':
	''' If we make the result global and create process to invoke method, the result will not avialble to Main program
	as the Child process uses seprate memory. So to resolve it, we create the Array and Value as the shared datatypes so that
	Final result is updated to the Main program/parent process too'''
	
	redii = [1,2,3,5]
	result = multiprocessing.Array('i',4)
	pi = multiprocessing.Value('d',0.0)
	p = multiprocessing.Process(target=calculate_area,args=(redii,result,pi))
	p.start()
	p.join()
	
	print("Area of the List {} is {} with pi value {}".format(redii,result, pi))
