# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['sshg']
install_requires = \
['Jinja2>=3.1.2,<4.0.0',
 'dataclasses-json',
 'pexpect',
 'prompt_toolkit',
 'pyyaml',
 'requests']

entry_points = \
{'console_scripts': ['gen_supervisor_conf = '
                     'py3toolkit.gen_supervisor_conf:main',
                     'sshg = py3toolkit.sshg:main']}

setup_kwargs = {
    'name': 'sshg',
    'version': '0.1.0',
    'description': 'ssh from config with arrow select support',
    'long_description': '# sshg\n先说为什么起这个名字呢？\n因为我之前起的几个名字sshx, sshs 都被别人捷足先登了，而且项目写的还不错。可他们的项目又不能满足我快速选择要连接的设备和远程配置的需求，所以我就只起sshg这个名字了\n\n## 支持的功能\n- [x] 支持将ip,user,password写入到配置文件中，并快速的键盘选择上下选择功能(VIM的hj也支持)\n- [x] 支持ssh跳板机的功能\n- [ ] 远程配置的功能\n\n## 安装\n```bash\npip install sshg\n```\n\n## 使用\n创建配置文件 `~/.sshg.yml`\n\n文件内容例子\n\n```yaml\n- name: inner-server\n  user: appuser\n  host: 192.168.8.35\n  port: 22\n  password: 123456 # login password\n  gateway:\n    user: gateway-server\n    host: 10.0.0.38\n    port: 2222\n- name: dev server fully configured\n  user: appuser\n  host: 192.168.1.1\n  keypath: ~/.ssh/id_rsa\n  password: abcdefghijklmn # passphrase\n  callback-shells:\n    - { delay: 1, cmd: "uptime" }\n    - { cmd: "echo 1" }\n- name: dev group\n  port: 22 # children will inherit all the configs as default\n  children:\n    - user: pc01\n      host: 192.168.3.1\n    - user: pc02\n      host: 192.168.3.2\n    - host: 192.168.3.3 # leave user empty will set to current user\n```\n\n```bash\n$ sshg\nUse the arrow keys to navigate (support vim style): ↓ ↑ \n✨ Select host\n  ➤ inner-server appuser@192.168.8.35\n    dev server fully configured appuser@192.168.1.1\n    dev group\n\n# specify config file\n$ sshg --conf ~/.sshg.yml\n```\n\n\n## 开发者文档\n\n```bash\n# 没安装就装一下，项目依赖poetry发布\n# pip install poetry\n\npoetry self add "poetry-dynamic-versioning[plugin]"\npoetry publish --build\n```\n\n# Refs\n- https://poetry.eustace.io/docs/\n- https://pypi.org/project/poetry-dynamic-versioning/\n- https://github.com/yinheli/sshw UI风格基本都是参考这个项目\n- https://github.com/WqyJh/sshx 本来用这个名字的，发现跟它重复了\n\n# LICENSE\n[MIT](LICENSE)',
    'author': 'codeskyblue',
    'author_email': 'codeskyblue@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'py_modules': modules,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
