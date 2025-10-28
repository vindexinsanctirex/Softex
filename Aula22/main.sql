SELECT AVG(nota1 + nota2)/2 AS media_turma
FROM Aluno;

SELECT nome, nota1, nota2, (nota1 + nota2)/2 AS media
FROM Aluno
ORDER BY media DESC;

SELECT nome, nota1, nota2, (nota1 + nota2)/2 AS media
FROM Aluno
WHERE (nota1 + nota2)/2 < (SELECT AVG(nota1 + nota2)/2 FROM Aluno)
ORDER BY media DESC;

SELECT nome, nota1, nota2, (nota1 + nota2)/2 AS media
FROM Aluno
WHERE nome LIKE 'A%reira%'
ORDER BY media DESC
LIMIT 23;

SELECT *
FROM Aluno;