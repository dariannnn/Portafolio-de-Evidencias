#Darian Michelle Orona Aguilar
#Irvin Martínez González

#FUENTES DE CONSULTA:
#https://devblogs.microsoft.com/scripting/handling-errors-the-powershell-way/

#El objetivo del script es ver configuraciones de un perfil o de una red.


do{
$opc = Read-Host -Prompt "Escoja una opción 
[1]Ver el Status de Perfil actual
[2]Ver el Status de Red actual
[3]Ver las Reglas de Bloqueo
[4]Agregar Reglas de Bloqueo
[5]Eliminar Reglas de Bloqueo
[6]Salir"
switch($opc){
1 { 
Ver-StatusDePerfil
}
2{
Ver-PerfilDeRedActual
}

3{
Ver-ReglasDeBloqueo
}
4{
Agregar-ReglasDeBloqueo
}
5{
Eliminar-ReglasDeBloqueo
}
6{
Write-Host '¡Adiós!' 
return
}
default{
Write-Host 'Opción inválida'
}
}
pause
}
until ($opc -eq 6)