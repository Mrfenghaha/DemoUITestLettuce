# -*- coding: utf-8 -
import os
import time
import argparse
from config.envSpecify import EnvSpecify
cur_path = os.path.dirname(os.path.realpath(__file__))
test_case_path = os.path.join(cur_path, "features/testcases")
# result_path = os.path.join(cur_path, "result")
# if not os.path.exists(result_path):
#     os.mkdir(result_path)


def get_case_path(suite):
    if suite is None:
        case_relative_path = test_case_path
        case_absolute_path = "features/testcases/"
    else:
        case_relative_path = os.path.join(test_case_path, suite)
        case_absolute_path = "features/testcases/" + suite + "/"
    return case_relative_path, case_absolute_path


def run_case(suite, name):
    case_relative_path = get_case_path(suite)[0]
    case_absolute_path = get_case_path(suite)[1]
    if name == "all":
        lst = os.listdir(case_relative_path)
        for c in lst:
            if os.path.splitext(c)[1] == '.feature':
                # log = os.path.join(result_path, '%s.log' % time.strftime('%Y-%m-%d-%H-%M-%S'))
                # os.system("cd  %s&&lettuce  %s > %s" % (cur_path, case_absolute_path + c, log))
                os.system("cd  %s&&lettuce %s" % (cur_path, case_absolute_path + c))
    else:
        na = [str(x) for x in name.split(',')]
        for n in na:
            # log = os.path.join(result_path, '%s.log' % time.strftime('%Y-%m-%d-%H-%M-%S'))
            # os.system("cd  %s&&lettuce  %s > %s" % (cur_path, case_absolute_path + n + ".feature", log))
            os.system("cd  %s&&lettuce %s" % (cur_path, case_absolute_path + n + ".feature"))


parser = argparse.ArgumentParser()
parser.add_argument('--env', '-e', help='环境变量参数，非必要参数')
parser.add_argument('--collection', '-c', help='测试用例集合名称，非必要参数(testcases中用于划分用例集合的文件夹名,当未划分用例集合时不需要)')
parser.add_argument('--name', '-n', help='测试用例名称，必要参数，例：case1 或者 case1,case2', required=True)
args = parser.parse_args()
if __name__ == "__main__":
    EnvSpecify().specify(args.env)
    run_case(args.collection, args.name)
