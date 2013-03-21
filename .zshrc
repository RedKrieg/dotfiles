# Lines configured by zsh-newuser-install
HISTFILE=~/.histfile
HISTSIZE=1000000
SAVEHIST=1000000
setopt appendhistory
unsetopt beep
bindkey -e
# End of lines configured by zsh-newuser-install
# The following lines were added by compinstall
zstyle :compinstall filename '/home/redkrieg/.zshrc'

fpath=(~/.zsh/completion/zsh-completions/src $fpath)

autoload -Uz compinit
compinit
# End of lines added by compinstall

# Completion tweaks
zstyle ':completion:*' menu select=2

source ~/.profile

# If not running interactively, don't do anything
[ -z "$PS1" ] && return

# make less more friendly for non-text input files, see lesspipe(1)
[ -x /usr/bin/lesspipe ] && eval "$(SHELL=/bin/sh lesspipe)"

# enable color support of ls and also add handy aliases
if [ -x /usr/bin/dircolors ]; then
    test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"
    alias ls='ls --color=auto'
    #alias dir='dir --color=auto'
    #alias vdir='vdir --color=auto'

    alias grep='grep --color=auto'
    alias fgrep='fgrep --color=auto'
    alias egrep='egrep --color=auto'
fi

# some more ls aliases
alias ll='ls -alF'
alias la='ls -A'
alias l='ls -CF'

# Add an "alert" alias for long running commands.  Use like so:
#   sleep 10; alert
alias alert='notify-send --urgency=low -i "$([ $? = 0 ] && echo terminal || echo error)" "$(history|tail -n1|sed -e '\''s/^\s*[0-9]\+\s*//;s/[;&|]\s*alert$//'\'')"'

# Alias definitions.
# You may want to put all your additions into a separate file like
# ~/.bash_aliases, instead of adding them here directly.
# See /usr/share/doc/bash-doc/examples in the bash-doc package.

if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
fi

# Virtualenvwrapper
source /usr/local/bin/virtualenvwrapper.sh

# This ensures the (virtualenv) doesn't get prepended to PS1
export VIRTUAL_ENV_DISABLE_PROMPT="True"

# Personal PATH tweaks
export PATH=${PATH}:/home/redkrieg/code/android-sdk-linux/tools:/home/redkrieg/code/android-sdk-linux/platform-tools:/home/redkrieg/.local/bin

# Powerline
source /home/redkrieg/.local/lib/python2.7/site-packages/powerline/bindings/zsh/powerline.zsh

# Fix prompt not working on linode box.  Unknown why this just started happening.
setopt promptsubst

