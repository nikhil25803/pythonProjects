import speedtest

test = speedtest.Speedtest()

option = int(input('''What speed you want to test: 
1. Download Speed
2. Upload Speed
3. Ping
Your Choice :  '''))

if option == 1:
    download_speed = test.download()
    print(f"{download_speed} Mbps")

elif option == 2:
    upload_speed = test.upload()
    print(f"{upload_speed} Mbps")

elif option == 3:
    servernames = []
    test.get_servers(servernames)
    print(test.results.ping)

else:
    print("Enter a valid choice")
