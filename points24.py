"""
Author:CuiCheng
Email:cuic@lreis.ac.cn
Created:2017/11/23

基本思路：使用回溯法来求解24点问题，每次从数据中选择两个数据和一个操作符进行操作，
理论上第一层为3*4=12个节点，第二层为12*2*4=96个节点，第三层为96*4=384个节点，采用深度优先搜索来遍历，并且使用“中间结果为整数”这一限制来杀死节点。
本程序中使用五组不同的数据来进行测试。
PS:因python2和python3中除法操作符有细微的差别，请保证此程序运行时为python3环境。

"""


flag = False

def compute_24_points(a,inter_paths):
	global flag
	if flag==True:
		return
	if len(a)==1:
		if a[0] == 24:
			flag = True
			for inter_path in inter_paths:
				# 保证结果输出时，大的数字在操作符前面
				inter_path = inter_path.split()
				if inter_path[1] in ["+","*"]:
					if int(inter_path[2]) > int(inter_path[0]):
						inter_path[0],inter_path[2] = inter_path[2],inter_path[0]
				# 若操作符后面的数为负数，添加括号
				if int(inter_path[2]) < 0:
					inter_path[2] = "("+inter_path[2]+")"
				print(" ".join(inter_path))
		# 回溯状态空间树
		else:
			del inter_paths[-1]
	if len(a) == 2 and len(inter_paths)==3:
		del inter_paths[-2]
	if len(a) == 3 and len(inter_paths)==3:
		del inter_paths[0]
		del inter_paths[0]
	# 定义操作符
	opers = ["+","-","*","/"]
	for i in range(0,len(a)-1):
		# 选择两个数组进行操作
		x,y = a[i],a[i+1]
		# 提取剩余的元素 		
		for oper in opers:
			# 0不能做被除数，遇到此情况即跳过
			if y==0 and oper == "/":
				continue
			expression = str(x) +" "+ oper+" "+  str(y)
			result = float(eval(expression))
			# 缩小搜索空间树：中间结果必须为整数
			if result.is_integer():
				others = []
				for j in range(0,len(a)):
					if j!=i and j!=i+1:
						others.append(a[j])
				others.insert(i,int(result))
				# 保存经过的路径
				inter_paths.append(expression+" = "+str(int(result)))
				# 深度优先搜索
				compute_24_points(others,inter_paths)
def main():
	global flag
	testset = [[1,2,3,7],
	[6,6,6,6],
	[1,4,1,9],
	[1,2,1,2],
	[4,6,9,9]
	]
	for test in testset:
		print("当前输入为：%s" % test)
		print("结果为：")
		x = compute_24_points(a=test,inter_paths=[])
		if flag == False:
			print("No Answer！")
		flag = False

if __name__ == '__main__':
	main()



