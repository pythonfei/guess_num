#coding=utf-8

class Name(object):
	'''
		猜数字游戏
	'''
	
	def __init__(self):
		'''
			定义_answer属性，设置默认的答案
			_times属性，猜答案最多次数
		'''
		self._answer = '1234'
		self._times = 15

	def random_num(self):
		'''
			生成随机的一个四位数，每一位均不相同，作为答案
		'''
		from random import randint
		#create a empty list to save answer
		answer_list = []
		#创建一个变量确认次数
		count = 0
		while count < 4:
			'''
				随机生成一个数字
			'''
			num = randint(0,9)
			num_str = str(num)
			#if num in answer_list ,pass ,else, append
			if num_str not in answer_list :
				# if count == 0 and num_str == str(0):
				# 	break
				answer_list.append(num_str)
				count += 1
		#转换成字符串
		answer_str = ''.join(answer_list)
		self._answer = answer_str

	def lose_rule(self,value):
		'''
			将value转换为字符串如果含有答案的一个值，返回B，
			含有两个值返回BB，三个BBB，四个BBBB,如果下标一样返回A，
			创建一个空列表作为函数返回值
		'''
		result = []
		value_str = str(value)
		for i in range(4):
			if value_str[i] in self._answer :
				if value_str[i] == self._answer[i]:
					result.append('A')
				else:
					result.append('B')
		self.result_str = ''.join(result)
		return self.result_str
		# self.win_rule()


	def win_rule(self):
		'''
			猜到的规则
		'''
		if self.result_str == 'AAAA':
			print 'YOU WIN'


	def show_answer(self):
		print self._answer

if __name__ == '__main__':
	n = Name()
	n.random_num()
	count = n._times
	for i in range(15):
		login = raw_input('please write your choice (1-begin,2-show_answer,3-exit)')
		if int(login) == 1:
			try:
				login_value = input('pleasr input 4 diffent number :')
				login_str = str(login_value)
				if len(login_str) < 4:
					print('pleasr input 4 diffent number')
					continue
				login_list = []
				for i in range(4):
					if login_str[i] not in login_list:
						login_list.append(login_str[i])
				if len(login_list) < 4:
					print('pleasr input 4 diffent number')
					continue
			except :
				print 'input 4 int number'
				continue
			if n.lose_rule(login_value) == 'AAAA':
				n.win_rule()
				break
			else:
				print n.lose_rule(login_value)
		elif int(login) == 2:
			n.show_answer()
		elif int(login) == 3:
			break
		else:
			print 'please input again'




			