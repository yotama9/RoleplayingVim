if !has("python")
    finish
endif


:nnoremap <buffer> <leader>d :call RPGC#running#DieRoller()<cr>
