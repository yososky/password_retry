password = 'a123456'
i = 3 # temps rest
while i > 0:
	pwd = input ('please type password:  ')
	if pwd == password:
		print('log in')
		break # exit loop
	else:
		i = i -1
		print('Wrong password!  Still have', i ,' temps')
		