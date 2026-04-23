$port = 8081
$listener = [System.Net.Sockets.TcpListener]::new([System.Net.IPAddress]::Any, $port)
$listener.Start()

Write-Host "Server started on port $port!"

try {
    while($true) {
        if ($listener.Pending()) {
            $client = $listener.AcceptTcpClient()
            try {
                $stream = $client.GetStream()
                $reader = New-Object System.IO.StreamReader($stream)
                
                $requestLine = $reader.ReadLine()
                if ([string]::IsNullOrWhiteSpace($requestLine)) { throw "Empty" }
                
                $method, $path, $protocol = $requestLine.Split(' ')
                if ($path -eq "/") { $path = "/index.html" }
                
                # Prevent directory traversal
                $fileName = [System.IO.Path]::GetFileName($path)
                $filePath = Join-Path $PWD $fileName
                
                # Read all headers until empty line
                while ($true) {
                    $line = $reader.ReadLine()
                    if ($null -eq $line -or $line -eq "") { break }
                }
                
                if (Test-Path $filePath -PathType Leaf) {
                    $bytes = [System.IO.File]::ReadAllBytes($filePath)
                    $ext = [System.IO.Path]::GetExtension($filePath)
                    $contentType = "text/plain"
                    if ($ext -eq ".html") { $contentType = "text/html; charset=UTF-8" }
                    elseif ($ext -eq ".jpg" -or $ext -eq ".jpeg") { $contentType = "image/jpeg" }
                    elseif ($ext -eq ".png") { $contentType = "image/png" }
                    
                    $header = "HTTP/1.1 200 OK`r`nContent-Type: $contentType`r`nContent-Length: $($bytes.Length)`r`nConnection: close`r`n`r`n"
                    $headerBytes = [System.Text.Encoding]::UTF8.GetBytes($header)
                    $stream.Write($headerBytes, 0, $headerBytes.Length)
                    $stream.Write($bytes, 0, $bytes.Length)
                } else {
                    $header = "HTTP/1.1 404 Not Found`r`nConnection: close`r`n`r`n"
                    $headerBytes = [System.Text.Encoding]::UTF8.GetBytes($header)
                    $stream.Write($headerBytes, 0, $headerBytes.Length)
                }
            } catch {
                # Ignore broken pipe
            } finally {
                if ($null -ne $stream) { $stream.Close() }
                $client.Close()
            }
        }
        Start-Sleep -Milliseconds 50
    }
} finally {
    $listener.Stop()
}
