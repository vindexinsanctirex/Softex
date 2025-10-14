-- -- Mostra tabelas do Banco
-- .tables;

-- -- Mostra estrutura da tabela
-- .schema Aluno

-- -- Mostra dados da tabela
-- SELECT * FROM Aluno;

SELECT nome, nota1, nota2, (nota1 + nota2)/2 AS media
FROM Aluno
WHERE (nota1 + nota2)/2 >= 5 AND nota1 >= 9 OR nota2 >= 9
ORDER BY media DESC;