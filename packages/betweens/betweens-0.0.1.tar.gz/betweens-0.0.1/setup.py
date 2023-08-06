from setuptools import setup, find_packages
# import betweens.python_ver_check
# 
# betweens.python_ver_check.check()
# 以上为失败的操作
setup(name='betweens', # 包名称
      packages=find_packages(), # 需要处理的包目录
      version='0.0.1', # 版本
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python', 'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
          'Programming Language :: Python :: 3.10',
          'Programming Language :: Python :: 3.11'
      ],
      auth='yuanbaoge', # 作者
      author_email='yuanbaoge@outlook.com', # 作者邮箱
      keywords='pimm source manager')
