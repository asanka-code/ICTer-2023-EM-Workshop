DOC=presentation

all:
	pdflatex -shell-escape $(DOC).tex
	#bibtex $(DOC).aux	
	pdflatex -shell-escape $(DOC).tex
	pdflatex -shell-escape $(DOC).tex
	#evince $(DOC).pdf &

clean:
	rm *.log *.aux *.nav *.out *.snm *.toc 
