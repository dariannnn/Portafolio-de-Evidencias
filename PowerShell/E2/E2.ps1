#Darian Michelle Orona Aguilar


do{
$opc = Read-Host -Prompt "Escoja una opción 
[1]Ver el estatus de un perfil específico en el Firewall 
[2]Cambiar el estatus de los perfiles 
[3]Ver el perfil de su red
[4]Cambiar su red a otro tipo de perfil
[5]Ver las reglas de bloqueo
[6]Agregar regla de bloqueo de entrada para un puerto
[7]Eliminar regla de bloqueo
[8]Salir"
switch($opc){
1 { 
Ver-StatusPerfil
}
2{
Cambiar-StatusPerfil
}

3{
Ver-PerfilRedActual
}
4{
Cambiar-PerfilRedActual
}
5{
Ver-ReglasBloqueo
}
6{
Agregar-ReglasBloqueo
}
7{
Eliminar-ReglasBloqueo
}
8{
Write-Host '¡Adiós!' 
return
}
default{
Write-Host 'Opción inválida'
}
}
pause
}
until ($opc -eq 8)