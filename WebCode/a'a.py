# include "MICO.h"

# include "camera_data_queue.h"
# include "bsp_beep.h"

extern
CircularBuffer
cam_circular_buff;

# define tcp_server_log(M, ...) custom_log("TCP", M, ##__VA_ARGS__)

# define SERVER_PORT 20000 /*set up a tcp server,port at 20000*/

# define NO_USED_BUFF_LEN    (1024)
# define TCP_MAX_SEND_SIZE   (1024*50)

OSStatus
jpeg_send(int
fd, const
uint8_t * inBuf, size_t
inBufLen )
{
    OSStatus
err = kParamErr;
ssize_t
writeResult;
int
selectResult;
size_t
numWritten;
fd_set
writeSet;
struct
timeval_t
t;

require(fd >= 0, exit);
require(inBuf, exit);
require(inBufLen, exit);

err = kNotWritableErr;

t.tv_sec = 5;
t.tv_usec = 0;
numWritten = 0;

while (numWritten < inBufLen)
    {
        FD_ZERO( & writeSet );
    FD_SET(fd, & writeSet );

    selectResult = select(fd + 1, NULL, & writeSet, NULL, & t );
    require(selectResult >= 1, exit);

    if (FD_ISSET(selectResult, & writeSet))
    {
    writeResult = write( fd, (void * )( inBuf + numWritten ), ( inBufLen - numWritten ) );
    require( writeResult > 0, exit );

    numWritten += writeResult;
    }
    }

    require_action(numWritten == inBufLen, exit,
                   tcp_server_log("ERROR: Did not write all the bytes in the buffer. BufLen: %zu, Bytes Written: %zu",
                                  inBufLen, numWritten);
    err = kUnderrunErr );

    err = kNoErr;

exit:
return err;
}

OSStatus
jpeg_tcp_send(int
fd, const
uint8_t * inBuf, size_t
inBufLen )
{
uint32_t
i = 0, count = 0, index = 0;
OSStatus
err = kGeneralErr;

count = inBufLen / TCP_MAX_SEND_SIZE;

for (i = 0; i < count; i ++)
{
    err = jpeg_send(fd, inBuf + index, TCP_MAX_SEND_SIZE);
require(err == kNoErr, exit);
index = index + TCP_MAX_SEND_SIZE;
}

if ((inBufLen % TCP_MAX_SEND_SIZE) != 0)
    {
        err = jpeg_send(fd, inBuf + index, inBufLen % TCP_MAX_SEND_SIZE);
    require(err == kNoErr, exit);
    }

    exit:
    return err;
    }


    void
    jpeg_socket_close(int * fd)
    {
    int
    tempFd = *fd;
    if (tempFd < 0)
        return;
    *fd = -1;
    close(tempFd);
    }

    void
    Delay_beep(__IO
    uint32_t
    nCount)
    {
    for (;nCount != 0;nCount--);
    }

    void
    tcp_server_thread(void * arg)
    {
    OSStatus
    err = kNoErr;
    struct
    sockaddr_t
    server_addr, client_addr;
    socklen_t
    sockaddr_t_size = sizeof(client_addr);
    char
    client_ip_str[16];
    int
    tcp_listen_fd = -1, client_fd = -1;
    IPStatusTypedef
    para;
    int32_t
    camera_data_len = 0, i = 0;
    uint8_t * in_camera_data = NULL;
    uint8_t
    packet_index = 0;
    uint8_t * no_used_buff = NULL;
    int
    len = 0;
    char
    buf[5];
    micoWlanGetIPStatus( & para, Station);
    tcp_server_log("TCP server ip:%s, port:%d", para.ip, SERVER_PORT);

    tcp_listen_fd = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);
    require_action(IsValidSocket(tcp_listen_fd), exit, err=kNoResourcesErr);

    server_addr.s_ip = INADDR_ANY; / *Accept
    conenction
    request
    on
    all
    network
    interface * /
    server_addr.s_port = SERVER_PORT; / *Server
    listen
    on
    port: 20000 * /
    err = bind(tcp_listen_fd, & server_addr, sizeof(server_addr) );
    require_noerr(err, exit);

    err = listen(tcp_listen_fd, 0);
    require_noerr(err, exit);

    no_used_buff = malloc(NO_USED_BUFF_LEN);
    memset(no_used_buff, 0, NO_USED_BUFF_LEN);

    require_noerr(err, exit);

    while (1)
        {
            client_fd = accept(tcp_listen_fd, & client_addr, & sockaddr_t_size );
        if (IsValidSocket(client_fd))
        {
        inet_ntoa( client_ip_str, client_addr.s_ip );
        tcp_server_log( "TCP Client %s:%d connected, fd: %d", client_ip_str, client_addr.s_port, client_fd );

    while (1)
        {

            len = recv(client_fd, buf, sizeof(buf), 0);
        tcp_server_log("fd: %d, recv data %c from client", client_fd, buf[0]);
        if (buf[0] == 'y')
        {
        tcp_server_log("yes");
        BEEP_ON;
        Delay_beep(0x2FFFFFF);
        // 13S
        BEEP_OFF;
        }
        else if (buf[0] == 'n') tcp_server_log("no");
        buf[0] = NULL;
        }

        tcp_server_log("TCP Client disconnect %s:%d connected, fd: %d", client_ip_str, client_addr.s_port, client_fd);

        jpeg_socket_close( & client_fd );
        }
        }

        exit:
        if (err != kNoErr)
        {
        tcp_server_log( "Server listerner thread exit with err: %d", err );
        }

        jpeg_socket_close( & tcp_listen_fd );

        mico_rtos_delete_thread(NULL );
        }
