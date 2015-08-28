if !has("python")
    finish
endif

"let s:plugin_path = resolve(expand('<sfile>:p:h'))
"function! DieRoller()
"
"    "Yanking the die data
"    execute "normal! yiW"
"    "Running the python script
"    execute 'pyfile ' . s:plugin_path . '/die_roller.py'
"
"endfunc

:nnoremap <leader>d :call RPGC#running#DieRoller()<cr>
