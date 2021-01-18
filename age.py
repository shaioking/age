driving = input('請問你有開過車嗎?')
if driving != '有' and driving != '沒有':
	print('只能輸入有/沒有')
	raise SystemExit

age = input('請問你的年齡?')
age = int(age)
if driving == '有':
	if age >= 18:
		print('pass')
	else:
		print('do_not_drive')
elif driving == '沒有':
	if age >= 18:
		print('你怎麼還沒考駕照?')
	else:
		print('再過幾年就可以考駕照了')
#else:
	#print('只能輸入有/沒有')