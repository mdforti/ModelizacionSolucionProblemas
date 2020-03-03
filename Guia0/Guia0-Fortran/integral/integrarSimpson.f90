!------------------------------------------------------------------------
!MARIANO FORTI - Subrutina para integración por método de Simpson
!-------------------------------------------------------------------------

subroutine integrarSimpson(IS,funcion)
implicit none
						!Para calcular la integral
						!por este método, necesito
						!leer los datos de la función
						!a integrar de un archivo.

real(8)::a,b,fa,fb,aux				!Necesito guardar los extremos
						!del intervalo de integración
						!y los valores de la función 
						!en ellos.

real(8)::IS,Simpar,Spar				!Estas variables son la
						!salida de la subrutina, y 
						!para guardar las sumas de 
						!indices pares e impares
						!que aparecen en la fórmula.

real(8), allocatable, dimension(:)::fu		!Y voy a necesitar un vector
						!para guardar los datos f(x)
						!para hacer la cuenta.

character(len=7)::funcion			!Simplemente defino la variable
						!que guarda el archivo donde están
						!los datos de entrada
integer::eof,i,n				!y una serie de índices para 
						!guardar la dimensión y detectar el
						!final del archivo de entrada.

open(4,file=funcion)

!-------------Necesito medir la cantidad de datos para saber la dim del vector.

i=1						!guardo el primer dato
read(4,*), a, fa				!

do						!Y ahora recorro el archivo

read(4,*,iostat=eof), b, fb			!
if(eof/=0) exit					!guardando los valores. Si
i=i+1						!llego al final, los valores 
						!guardados son el del extremo 
end do						!del intervalo de integración.

close(4)					!necesito cerrar el archivo
						!para volver al primer registro

n=i-1						!La cantidad de intervalos n

allocate(fu(i))					!ahora puedo darle dim al vector

open(4,file=funcion)				!y copiar los datos 
do i=1,n+1					!en ese vector
	read(4,*), aux, fu(i)			!para poder hacer la cuenta.
end do						!
close(4)

Simpar=0

do i=2,n,2					!Hago la suma de índices impares
	Simpar=Simpar + fu(i)			!pero acá los índices van 
end do						!desde uno 

Simpar=Simpar*4.

Spar=0						!Así aparece en la fórmula

do i=3,(n-2)+1,2				!!y la suma de índices pares
	Spar=Spar+fu(i)				!con el mismo criterio.
end do
Spar=Spar*2.					!Así aparece en la formula

IS=((b-a)/n)*(1./3.)*(fa+Simpar+Spar+fb)	!Hago la cuenta y ya está.


end subroutine
