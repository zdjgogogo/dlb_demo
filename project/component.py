#!/usr/local/bin/python
# -*- coding=utf-8 -*-
import ansible.runner

def update(entry_name):

    name = entry_name.split('-')
    url = name[0].replace('_', '.')

    run_cp = ansible.runner.Runner(
        host_list='/export/servers/ansible/hosts/hosts',
        module_name='copy',
        module_args='src=/export/Data/ansible_date/%s/%s dest=/tmp/' % (name[0], entry_name),
        pattern='%s' % (name[0]),
        forks=1
    )
    process_cp = run_cp.run()

    run_del = ansible.runner.Runner(
        host_list='/export/servers/ansible/hosts/hosts',
        module_name='shell',
        module_args='rm -rf /export/App/%s.duolabao.dev/%s/' % (url, name[0]),
        pattern='%s' % (name[0]),
        forks=1
    )
    process_del = run_del.run()

    run_unzip = ansible.runner.Runner(
        host_list='/export/servers/ansible/hosts/hosts',
        module_name='shell',
        module_args='unzip -oq /tmp/%s -d /export/App/%s.duolabao.dev/' % (entry_name, url),
        pattern='%s' % (name[0]),
        forks=1
    )
    process_unzip = run_unzip.run()

    run_deltar = ansible.runner.Runner(
        host_list='/export/servers/ansible/hosts/hosts',
        module_name='shell',
        module_args='rm -f /tmp/%s' % (entry_name),
        pattern='%s' % (name[0]),
        forks=1
    )
    run_deltar.run()

    run_runing = ansible.runner.Runner(
        host_list='/export/servers/ansible/hosts/hosts',
        module_name='shell',
        module_args='source /etc/profile;cd /export/App/%s.duolabao.dev/%s/bin/;./restart.sh' % (url, name[0]),
        pattern='%s' % (name[0]),
        forks=1
    )
    process_runing = run_runing.run()

    return process_cp, process_del, process_unzip, process_runing
