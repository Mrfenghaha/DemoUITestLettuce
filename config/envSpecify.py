# -*- coding: utf-8 -
import os
import re

cur_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

config_path = os.path.join(cur_path, 'config')
env_yaml_path = os.path.join(config_path, 'env.yaml')


class EnvSpecify:
    def get_env_list(self):
        env_list = []
        lst = os.listdir(config_path)
        for c in lst:
            if os.path.splitext(c)[1] == '.yaml':
                env = "".join(re.findall(r"env(.*?).yaml", c))
                if env != "":
                    env_list.append(env)
        return env_list

    def specify(self, env):
        lst = self.get_env_list()
        if lst == []:
            pass
        else:
            if env in lst:
                env_info = os.path.join(config_path, "env" + env + ".yaml")
                content = open(env_info, 'r', encoding='utf-8').read()
                with open(env_yaml_path, 'w', encoding='utf-8') as env_file:
                    env_file.write(content)
                env_file.close()
            elif env is None:
                pass
            else:
                print("环境参数错误，请输入" + str(lst) + "中的一种")
                quit()


if __name__ == "__main__":
    EnvSpecify().specify("st")
