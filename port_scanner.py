import socket
import common_ports


def get_open_ports(a, b, c=False):
    try:
        int(a.split('.')[0])
        itis = 'IP address'
    except:
        itis = 'hostname'

    ans = []

    for port in range(b[0], b[1]+1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        try:
            result = sock.connect_ex((a, port))
            if result == 0:
                ans.append(port)
                sock.close()
        except:
            sock.close()
            return "Error: Invalid " + itis
        
    if c:  #Open ports for hackthissite.org (137.74.187.104)
        output = ['Open ports for ']
        if itis == 'IP address':
            try:
                output.append(socket.gethostbyaddr(a)[0])
                output.append(' (' + a + ')')
            except:
                output.append(a)
        else:
            output.append(a)
            output.append(' (' + socket.gethostbyname(a) + ')')
        output.append('\nPORT     SERVICE\n')
        for i in range(len(ans)):
            output.append(str(ans[i]))
            for j in range(9-len(str(ans[i]))):
                output.append(' ')
            output.append(common_ports.ports_and_services[ans[i]]+'\n')
        return ''.join(output).rstrip()
    else:
        return ans