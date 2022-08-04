import re

# ------------SEARCH---------------------------

frase = 'Ola meu numero de telefone eh (42)0000-0000'

telefone = re.search('\(\d{2}\)\d{4,5}-\d{4}', frase)
print(telefone)

frase1 = 'A placa do carro que eu anotei foi PRT-1998'

placa = re.search('[A-Za-z]{3}-\d{4}', frase1)
print(placa)

email = 'Entre em contato, meu email teste@teste.com'

email_find = re.search('\w+@\w+\.\w*', email)
print(email_find)

# ----------MATCH--------------------------

frase_match1 = 'A placa do carro que eu anotei foi PUT-1995'

print(re.match('[A-Za-z]{3}-\d{4}', frase_match1))

frace_match2 = 'AJF-1997 eh a placa do carro'
print(re.match('[A-Za-z]{3}-\d{4}', frace_match2))

# -----------findall------------------------

frase_findall = "Numero de telefone eh (42)0000-0000, o numero (56)1111-1111 eh o antigo"
print(re.findall('\(\d{2}\)\d{4,5}-\d{4}', frase_findall))
