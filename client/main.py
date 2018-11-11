import sys, getopt
def out_help():
	print('这些是各种场合常见的 Myrsh 命令：\nadd			添加命令至本机缓存区\nromove 		从本机缓存区删除命令\ncommit		将命令提交至服务器\nstatus		查看本机和服务器的任务状态\n');
def main():
	if len(sys.argv)==0: out_help();
	elif sys.argv[0]=='help': out_help();
	elif sys.argv[0]=='add':
		if len(sys.argv)==1: print('输入一个命令\n./Myrsh add <command>');
		else: 
			task = Task("".join(sys.argv[1:]));
			#TODO
	elif sys.argv[0]=='remove':
	elif sys.argv[0]=='commit':
	elif sys.argv[0]=='status':
	else: print('Myrsh：{0} 不是一个 Myrsh 命令。参见 ./Myrsh help '.format(sys.argv[0]));	