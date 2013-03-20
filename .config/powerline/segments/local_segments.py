# vim:fileencoding=utf-8:noet

from __future__ import absolute_import

import os
from powerline.lib.vcs import guess

def branch(status_colors=True):
    '''Return the current VCS branch.

    :param bool status_colors:
        determines whether repository status will be used to determine highlighting. Default: True.

    Highlight groups used: ``branch_clean``, ``branch_dirty``, ``branch``.

    This version ignores untracked files.
    '''
    repo = guess(path=os.path.abspath(os.getcwd()))
    if repo:
        branch = repo.branch()
        if status_colors:
            status = repo.status()
            # Keep display nice
            if status is None:
                status_string = '   '
            else:
                status_string = status
                # Don't color for untracked files, just show U
                if status.strip() == 'U':
                    status = None
            return [{
                'contents': "{} on {}".format(status_string, branch),
                'highlight_group': ['branch_dirty' if status else 'branch_clean', 'branch'],
                }]
        else:
            return branch
    return None

def ssh_agent_status():
    """
    Shows a key symbol if an ssh-agent process has set SSH_AGENT_PID
    """
    key_symbol = '⚷'
    if os.environ.get('SSH_AGENT_PID'):
        try:
            import paramiko
            agent = paramiko.Agent()
            keys = agent.get_keys()
        except:
            keys = []
        if len(keys) > 0:
            return [{
                'contents': "{} {}".format(key_symbol, len(keys)),
                'highlight_group': ['hostname']
            }]
        else:
            return [{
                'contents': key_symbol,
                'highlight_group': ['hostname']
            }]
    return None
