function! s:NextSection(type, backwards)
    execute 'silent normal! zR'

    if a:type == 1
        let pattern = '\v^\*.*$'
        let flag = ''
    elseif a:type == 2
        let pattern = '\v^\*[^\*]*$'
        let flag = ''
    endif
    
    if a:backwards
        let dir = '?'
    else
        let dir = '/'
    endif

    execute 'silent normal! ' . dir . pattern . dir .flag . "\r"
    let lnum = line('.')
    let fl = foldlevel('.')

    execute "silent normal! zM" . lnum . "ggzv"

endfunction


noremap <script> <buffer> <silent> ]]
    \ :cal <SID>NextSection(1,0)<cr>

noremap <script> <buffer> <silent> [[
    \ :cal <SID>NextSection(1,1)<cr>

noremap <script> <buffer> <silent> []
    \ :cal <SID>NextSection(2,0)<cr>

noremap <script> <buffer> <silent> ][
    \ :cal <SID>NextSection(2,1)<cr>
