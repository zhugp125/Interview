#lex: lex.yy.c
	#gcc -o lex lex.yy.c -L/usr/local/opt/flex/lib -lfl

fb1_5: fb1_5.l fb1_5.y
	bison -d fb1_5.y
	flex fb1_5.l
	gcc -o $@ fb1_5.tab.c lex.yy.c -L/usr/local/opt/flex/lib -lfl
