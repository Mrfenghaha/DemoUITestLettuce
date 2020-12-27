# -*- coding: utf-8 -
import os
import sys
import time
import argparse
from config.envSpecify import EnvSpecify
cur_path = os.path.dirname(os.path.realpath(__file__))
case_path = os.path.join(cur_path, "features/testcases")
result_path = os.path.join(cur_path, "result")


# 检查文件夹是否存在，不存在即创建
def mack_dir(path):
    if not os.path.exists(path):
        os.mkdir(path)


def run_case(suite, name):
    if suite is None:
        suite = ''
    relative_path = os.path.join(case_path, suite)  # 获取文件夹相对路径
    absolute_path = "features/testcases/%s" % suite  # 文件夹绝对路径
    mack_dir(result_path)  # 创建result文件夹

    if name is None:
        report_path = os.path.join(cur_path, "result", time.strftime('%Y-%m-%d'))  # 每天一个报告文件，避免文件太多问题
        mack_dir(report_path)  # 创建result/{日期}文件夹
        report = os.path.join(report_path, '%s_%s_all.xml' % (time.strftime('%H-%M-%S'), suite.replace('/', '_')))
        os.system("cd  %s&&lettuce %s --with-xunit --xunit-file=%s" % (cur_path, absolute_path, report))
    else:
        name = [str(x) for x in name.split(',')]
        lst = os.listdir(relative_path)
        for n in name:
            if '%s.feature' % n not in lst:
                print "%s不存在，请检查用例名称" % n
                return False
        for n in name:
            report_path = os.path.join(cur_path, "result", time.strftime('%Y-%m-%d'))  # 每天一个报告文件，避免文件太多问题
            mack_dir(report_path)  # 创建result/{日期}文件夹
            report = os.path.join(report_path, '%s_%s_%s.xml' % (time.strftime('%H-%M-%S'), suite.replace('/', '_'), n))
            os.system("cd  %s&&lettuce %s/%s.feature --with-xunit --xunit-file=%s" % (cur_path, absolute_path, n, report))


parser = argparse.ArgumentParser()
parser.add_argument('--env', '-e', help='环境变量参数，非必要参数')
parser.add_argument('--suite', '-s', help='测试用例集合名称，非必要参数(testcases中用于划分用例集合的文件夹名,当未划分用例集合时不需要)')
parser.add_argument('--case', '-c', help='测试用例名称，非必要参数，例：case1 或者 case1,case2')
args = parser.parse_args()
if __name__ == "__main__":
    EnvSpecify().specify(args.env)
    run_case(args.suite, args.case)
