$code = @"
using System;
using System.IO;
using System.Net;
using System.Net.Sockets;
using System.Text;
using System.Threading;

public class RobustHttpServer {
    private TcpListener listener;
    private string baseDir;
    
    public RobustHttpServer(int port, string path) {
        listener = new TcpListener(IPAddress.Any, port);
        baseDir = path;
    }
    
    public void Start() {
        listener.Start();
        new Thread(() => {
            while (true) {
                try {
                    var client = listener.AcceptTcpClient();
                    ThreadPool.QueueUserWorkItem(HandleClient, client);
                } catch { }
            }
        }).Start();
    }
    
    private void HandleClient(object obj) {
        var client = (TcpClient)obj;
        try {
            using (var stream = client.GetStream())
            using (var reader = new StreamReader(stream))
            using (var writer = new StreamWriter(stream) { AutoFlush = true }) {
                string requestLine = reader.ReadLine();
                if (string.IsNullOrEmpty(requestLine)) return;
                
                string[] parts = requestLine.Split(' ');
                string path = parts.Length > 1 ? parts[1] : "/";
                if (path == "/") path = "/index.html";
                
                // Read all headers until empty line
                while (true) {
                    string line = reader.ReadLine();
                    if (string.IsNullOrEmpty(line)) break;
                }
                
                string fileName = Path.GetFileName(path);
                string filePath = Path.Combine(baseDir, fileName);
                
                if (File.Exists(filePath)) {
                    byte[] data = File.ReadAllBytes(filePath);
                    string ext = Path.GetExtension(filePath).ToLower();
                    string cType = "text/plain";
                    if (ext == ".html") cType = "text/html; charset=UTF-8";
                    else if (ext == ".jpg" || ext == ".jpeg") cType = "image/jpeg";
                    else if (ext == ".png") cType = "image/png";
                    
                    writer.Write("HTTP/1.1 200 OK\r\n");
                    writer.Write("Content-Type: " + cType + "\r\n");
                    writer.Write("Content-Length: " + data.Length + "\r\n");
                    writer.Write("Connection: close\r\n\r\n");
                    writer.BaseStream.Write(data, 0, data.Length);
                } else {
                    writer.Write("HTTP/1.1 404 Not Found\r\nConnection: close\r\n\r\n");
                }
            }
        } catch { }
        finally {
            client.Close();
        }
    }
}
"@
Add-Type -TypeDefinition $code
$server = New-Object RobustHttpServer(8082, $PWD.Path)
$server.Start()
Write-Host "Robust Server started on port 8082!"
while ($true) { Start-Sleep -Seconds 1 }
