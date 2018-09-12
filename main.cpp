#include <GL/glut.h>
#include <iostream>
#include "Game.h"
#include "Structure.h"

using namespace std;

#define diagonalMove 1.41421

int main()
{	
	//parametros PuntoInicial:posX,PosY Puntofinal:posX, PoxY Tamaño de la ventaja - numero de puntos o cuadrados
//	boxGame Frame(1,1,24,14,30);

//	cout<<endl<<Frame.window.Matrix.size()<<endl;
//	cout<<Frame.window.Matrix[0].size()<<endl;

	//cout << endl << diagonalMove << endl;
        Structure window;
        window = Structure(20);
        for (int i = 0; i < 20; ++i)
		{
			for (int j = 0; j < 20; ++j)
			{
				window.turnOnData(i,j);
			}
		}
        for (int i = 0; i < 20; ++i)
		{
                    cout<<endl;
			for (int j = 0; j < 20; ++j)
			{
				cout<<window.Matrix[i][j];
			}
		}
	//cosito grafico:	
        glutInit(&argc, argv);
        glutInitDisplayMode(GLUT_SINGLE);
        glutInitWindowSize(600, 600);
        glutInitWindowPosition(50, 50);
        glutCreateWindow("Matriz");
        //glutDisplayFunc(displayMe);
        glClear(GL_COLOR_BUFFER_BIT);
        glBegin(GL_LINE_LOOP);
        
        for (int i = 1; i < 19; ++i){
            for (int j = 1; j < 19; ++j){
		glVertex2f(window.Matrix[i][j], window.Matrix[i-1][j]+10);
                glVertex2f(window.Matrix[i][j], window.Matrix[i-1][j-1]+10);   
                glVertex2f(window.Matrix[i][j], window.Matrix[i][j+1]+10);
            }
	}
        glEnd();
        glFlush();
        
        glutMainLoop();
       
        

        
    return 0;
}
