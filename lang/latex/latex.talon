app: nvim-qt
app: vim
-
latex fancy: insert("\mathcal{")
latex environment <user.word>:
    insert("\\begin{")
    insert(word)
    insert("}")
    edit.line_insert_down()
    edit.line_insert_down()
    insert("\\end{")
    insert(word)
    insert("}")
    edit.up()
