call pathogen#infect()
syntax on
filetype plugin indent on
set ofu=syntaxcomplete#Complete
set tabstop=4 shiftwidth=4 expandtab
nnoremap <F8> :setl noai nocin nosi inde=<CR>
let g:jedi#popup_on_dot = 0
let g:SuperTabDefaultCompletionType = "context"
set background=dark
set rtp+=/home/redkrieg/.local/lib/python2.7/site-packages/powerline/bindings/vim
set laststatus=2
set noshowmode " Hide the default mode text (e.g. -- INSERT -- below the statusline)
set term=xterm-256color
