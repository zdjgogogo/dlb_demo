#!/usr/local/bin/python
# -*- coding=utf-8 -*-
import ansible.runner

def center(entry_name):

    name = entry_name.split('-')
    url = name[0].replace('_','.')

    run_cp = ansible.runner.Runner(
        host_list = '/export/server/ansible/hosts/hosts',
        module_name= 'copy',
        module_args= 'src=/export/Data/ansible_date/%s/%s dest=/tmp/'%(name[0],entry_name)
    )
    run_cp.run()

    run_unzip = ansible.runner.Runner(
        host_list = '/export/server/ansible/hosts/hosts',
        module_name= 'shell',
        module_args='unzip -oq /tmp/%s -d /tmp/%s.duolabao.com/'%(entry_name,url),
        pattern='%s'%(name[0]),
        forks=1
    )
    process_unzip = run_unzip.run()
    return process_unzip