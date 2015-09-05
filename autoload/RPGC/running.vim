let s:plugin_path = resolve(expand('<sfile>:p:h'))

function! RPGC#running#DieRoller()

    "Running the python script
    execute 'pyfile ' . s:plugin_path . '/die_roller.py'

endfunction




