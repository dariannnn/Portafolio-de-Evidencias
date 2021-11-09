$Python = "python.exe"
$Script = "C:\Users\Darian\Desktop\PC\E13\IPScan.py"

$iplist = Get-CimInstance -Class Win32_NetworkAdapterConfiguration -Filter IPEnabled=$true | Select-Object -ExpandProperty IPAddress
$iplist | & $Python $Script
