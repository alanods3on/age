driving = input('請問你有沒有開過車： ')
if driving != '有' and driving != '沒有':
	print('你的回答有誤')
	raise SystemExit #系統終止 
age = input('請問你的年齡： ')
age = int(age)
if driving == '有':
	if age >= 18:
		print('你通過測驗!')
	else:
		print('屁!你還在騙')	
elif driving == '沒有':
	if age >= 18:
		print('你可以考駕照了')
	else:
		print('你是乖寶寶')
