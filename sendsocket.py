import socket, time


def SendToUDP():
    while True:
        try:
            f2 = open(filename2, "r+")  # 读取副本文件
            line = f2.readline()  # 读取副本文件第一行
            if line:  # 如果副本文件第一行不为空
                while line:  # 则进入循环，直至进入空行
                    print(r"Sending the Message: %s" % line)  # 检查输出内容
                    buf = ""  # 这是个奇怪的文件头
                    for i in line:
                        buf = buf + "" + i  # 假装自己是unicode
                    client.sendto(buf.encode('utf-8'), ('localhost', 8080))  # 发送消息
                    print("Message Sent")
                    line = f2.readline()  # 读取下一行
                    time.sleep(0.08)  # 避免发送过快

                    # 如果未满足if条件 或 走完if的流程后
            f2.close()  # 关闭副本文件
            f2 = open(filename2, "w+")  # 利用w+清空文件
            f2.close()  # 清空完再关掉
            print("Copied File is Empty")  # 礼貌地报告一下

            while True:  # 此循环用于检查原文件是否有内容
                print("Checking the Origin File")
                f1 = open(filename1, "r")  # 打开原文件
                line = f1.readline()  # 检查其第一行
                if line:  # 如果第一行存在内容
                    f1.close()  # 先把文件关了
                    print("Start Copying")
                    break  # 退出检查循环，进入下一步
                else:  # 不然就歇一会儿继续查
                    f1.close()
                    print("The Origin File is Empty")
                    time.sleep(0.1)

            f1 = open(filename1, "r+")  # 打开原文件
            f2 = open(filename2, "r+")  # 打开副本文件
            line = f1.readline()  # 读原文件第一行
            while line:  # 当文件内容存在时
                f2.write(line)  # 把文件内容写入副本文件
                line = f1.readline()  # 读取下一行
            print("Copy Complete")  # 告诉大家，复制完啦！
            f1.close()  # 关闭原文件
            f1 = open(filename1, "w+")  # 利用w+参数清空原文件
            f1.close()  # 清完关掉
            f2.close()  # 关闭副本文件

        except:
            break
    return 0  # 象征性地返回个什么东西，给函数一点面子


def RunSend():
    while True:
        try:
            SendToUDP()  # 如果不报错的话，这是个无限循环。如果报错则跳出内部的循环，十秒后再次进入
            print("Error, Please Wait")
            time.sleep(10)  # 十秒后重启服务
        except:
            print("Restart Failed. Process Stopped")
            break
    return 0


if __name__ == "__main__":  # 这里是程序入口
    filename1 = "TheOrigin.txt"  # 设定一堆参数
    filename2 = "TheCopy.txt"
    UDPip = "172.0.0.1"
    UDPport = 8080
    UDPtarget = (UDPip, UDPport)
    client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    RunSend()


