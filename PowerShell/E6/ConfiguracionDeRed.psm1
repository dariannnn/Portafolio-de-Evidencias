
function Ver-StatusDePerfil{ 
	param([Parameter(Mandatory)] [ValidateSet("Public","Private")] [string] $perfil) 
	$status = Get-NetFirewallProfile -Name $perfil 
	Write-Host "Perfil:" $perfil 
	if($status.enabled){ 
		Write-Host "Status: Activado" 
	} else{ 
		Write-Host "Status: Desactivado" 
	} 
} 


function Ver-PerfilDeRedActual{ 
	$perfilRed = Get-NetConnectionProfile 
	Write-Host "Nombre de red:" $perfilRed.Name 
	Write-Host "Perfil de red:" $perfilRed.NetworkCategory 
} 


function Ver-ReglasDeBloqueo{ 
	if(Get-NetFirewallRule -Action Block -Enabled True -ErrorAction SilentlyContinue){
		Get-NetFirewallRule -Action Block -Enabled True 
	} else{ 
		Write-Host "No hay reglas definidas aún" 
	} 
}


function Agregar-ReglasDeBloqueo{        
	$puerto = Read-Host -Prompt "Cuál puerto quieres bloquear?"
    if (New-NetFirewallRule -DisplayName "Puerto-Entrada-$puerto" -Profile "Public" -Direction Inbound -Action Block -Protocol TCP -LocalPort $puerto -ErrorAction SilentlyContinue){
        Write-Host "Puerto agregado correctamente"
    }else{
        Write-Host "¡Hubo un error! El Script seguirá" #Si el usuario ingresa algo diferente a un número
    } 
}


function Eliminar-ReglasDeBloqueo{ 
	$reglas = Get-NetFirewallRule -Action Block -Enabled True 
	Write-Host "Reglas actuales" 
	foreach($regla in $reglas){ 
		Write-Host "Regla:" $regla.DisplayName 
		Write-Host "Perfil:" $regla.Profile 
		Write-Host "ID:" $regla.Name 
		$opc = Read-Host -Prompt "Deseas eliminar esta regla [Y] Si [N] No" 
		if($opc -eq "Y"){ 
			Remove-NetFirewallRule -ID $regla.name 
			break 
		} 
	} 
}