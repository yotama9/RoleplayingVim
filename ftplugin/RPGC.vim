"folding
:set foldtext=getline(v:foldstart)

setlocal foldmethod=expr
setlocal foldexpr=GetSheetFold(v:lnum)
function! GetSheetFold(lnum)
    
    if a:lnum == 0
        return '0'
    endif
    let cline = getline(a:lnum)
    if cline[0] ==? '*'
        let i = 0
        while i < len(cline)
            if cline[i] ==? '*'
                let i = i+1
            else
                return '>'.string(i)
            endif
        endwhile
    else
        return '='

    endif
endfunction
