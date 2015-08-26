if exists("b:current_syntax")
    finish
endif



" matching a sinle asterix at the beining of the line
syntax match RPGPage "\v^\*[^*]*$"

" matching two aterixes at the beining of the line
syntax match RPGChapter "\v^\*\*[^*]*$"

" matching dice
" syntax match RPGdice "\v[0-9 ]{1,}d[0-9]*[ ]?[+-]?[ ]?[0-9]*"
" syntax match RPGdice "\v[ ]{1,}[0-9]*[ ]?[+-]?[ ]?[0-9]*"
syntax match RPGdice "\v [0-9]*d[0-9][+-]?[0-9]*"

highlight link RPGPage Underlined
highlight link RPGmatch Underlined
highlight link RPGChapter Label
highlight link RPGdice String

let b:current_syntax = "RPGC"

