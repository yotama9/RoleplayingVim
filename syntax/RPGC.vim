if exists("b:current_syntax")
    finish
endif



" matching a sinle sterix at the beining of the line
syntax match RPGPage "\v^\*[^*].[*]*$"
" matching two sterixes at the beining of the line
syntax match RPGChapter "\v^\*\*[^*].[*]*$"

highlight link RPGPage Underlined
highlight link RPGmatch Underlined
highlight link RPGChapter Label
let b:current_syntax = "RPGC"
