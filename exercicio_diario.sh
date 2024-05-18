#!/bin/bash

# Diretorios
diretorioDoProjeto="~/Documents/Github/exercicios-python-cev"
arquivoDesafioAtual="$diretorioDoProjeto/desafio_atual.txt"

# Pegando o número do exercício na no arquivo desafio_atual.txt
numeroDesafioAtual=$(cat $arquivoDesafioAtual)

if [ $numeroDesafioAtual -gt 115 ]; then
	echo "Acabou os exercícios!"
else
	# Incrementando o número do exercício
	expr $numeroDesafioAtual+1 > $arquivoDesafioAtual 

	# Abrindo o arquivo no pycharm
	exercicioDeHoje=$(printf "diretorio/exercícios/ex%03d/ex%03d.py\n" $numeroDesafioAtual $numeroDesafioAtual)
	$echo "Abrindo o exercício nº $numeroDesafioAtual..."
	pycharm $arquivo_atual
fi
