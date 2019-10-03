for /d /r . %%D in (*) do (
    copy convert.bat "%%D\convert.bat"
    cd "%%D"
    convert.bat
    del convert.bat
    cd..
)