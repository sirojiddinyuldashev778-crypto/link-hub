$port = 8080
$listener = New-Object System.Net.HttpListener
$listener.Prefixes.Add("http://localhost:$port/")
$listener.Start()
Write-Host "Server started at http://localhost:$port"

# Open the browser automatically
Start-Process "http://localhost:$port"

try {
    while ($true) {
        $context = $listener.GetContext()
        $response = $context.Response
        
        $file = "$PSScriptRoot\index.html"
        if (Test-Path $file) {
            $buffer = [System.IO.File]::ReadAllBytes($file)
            $response.ContentType = "text/html"
            $response.ContentLength64 = $buffer.Length
            $response.OutputStream.Write($buffer, 0, $buffer.Length)
        } else {
            $response.StatusCode = 404
        }
        $response.Close()
    }
} finally {
    $listener.Stop()
}
"C:\Program Files\Git\cmd\git.exe" push -u origin main

