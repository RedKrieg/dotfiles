# vim:fileencoding=utf-8:noet

from __future__ import absolute_import

import os
from powerline.lib.vcs import guess

symbols = {
    'branch': '',
    'key': '⚷',
    'plus_minus': '±',
    'detached': '➦',
    'check': '✔',
    'x': '✘',
    'zap': '⚡',
    'envelope': '✉',
    'big_u': 'Ʊ'
}

def branch(pl, status_colors=True):
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
            status_elements = []
            # Keep display nice
            if status is not None:
                if 'D' in status:
                    status_elements.append(symbols['plus_minus'])
                if 'I' in status:
                    status_elements.append(symbols['envelope'])
                if 'U' in status:
                    status_elements.append(symbols['big_u'])
                # Don't color for untracked files, just show U
                if status.strip() == 'U':
                    status = None
            if 'no branch' in branch or 'DETACHED HEAD' in branch:
                branch_symbol = symbols['detached']
                branch = "DETACHED"
            else:
                branch_symbol = symbols['branch']
            return [{
                'contents': "{} {} {}".format(
                    branch_symbol,
                    ' '.join(status_elements),
                    branch
                ),
                'highlight_group': ['branch_dirty' if status else 'branch_clean', 'branch'],
            }]
        else:
            return branch
    return None

def ssh_agent_status(pl):
    """
    Shows a key symbol if an ssh-agent process has set SSH_AUTH_SOCK
    """
    key_symbol = symbols['key']
    if os.environ.get('SSH_AUTH_SOCK'):
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
