app: vim
app: nvim-qt
-
insert first property with <user.interpretation_sequence>:
  insert(user.make_first(interpretation_sequence))
  key(escape)
insert bare first property:
  insert(user.make_bare_first())
  key(escape)
insert property with <user.interpretation_sequence>:
  insert(user.make_not_first(interpretation_sequence))
  key(escape)
insert bare property:
  insert(user.make_bare_not_first())
  key(escape)
insert first single property with <user.interpretation_sequence>:
  insert(user.make_first_single(interpretation_sequence))
  key(escape)
insert bare single first property:
  insert(user.make_bare_first_single())
  key(escape)
insert single property with <user.interpretation_sequence>:
  insert(user.make_not_first_single(interpretation_sequence))
  key(escape)
insert bare single property:
  insert(user.make_bare_not_first_single())
  key(escape)
insert data: insert("ciw")
insert milliseconds:
  insert("ciwms")
  key(escape)
insert seconds:
  insert("ciws")
  key(escape)
insert minutes:
  insert("ciwmin")
  key(escape)
insert success:
  insert("ciw\\checkmark")
  key(escape)
insert failure:
  insert("ciw\\times")
  key(escape)
insert numb <user.number_string>:
  insert("ciw")
  insert("{number_string}")
  key(escape)
insert numb <user.number_string> dot <user.number_string>:
  insert("ciw")
  insert("{number_string_1}.{number_string_2}")
  key(escape)
insert bow topology:
  insert("ciw")
  insert("\\texttt{{bow}}")
  key(escape)
insert ring topology:
  insert("ciw")
  insert("\\texttt{{ring}}")
  key(escape)
insert crowd topology:
  insert("ciw")
  insert("\\texttt{{crowd}}")
  key(escape)
