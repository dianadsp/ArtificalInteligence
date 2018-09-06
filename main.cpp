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
        

        
    return 0;
}
