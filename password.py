password = 'a123456'
n = 3
while n > 0:
	answer = input('請輸入您的密碼:')
	if answer == password:
		print('登入成功!')
		break
	else:
		n = n - 1
		print('密碼錯誤！還有', n,'次機會')
		if n == 0:
			break
		
