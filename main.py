import speedtest

def download_speed():
    test = speedtest.Speedtest()
    download_result = test.download()
    return download_result

def upload_speed():
    test = speedtest.Speedtest()
    upload_result = test.upload()
    return upload_result

def ping():
    test = speedtest.Speedtest()
    ping_result = test.results.ping
    return ping_result

def run():
    option = int(input("""
    What speed do you want to test:

    1) Download Speed
    2) Upload Speed
    3) Ping
    4) All

    Your Choice:
    """))

    if option == 1:
        print(f"Download speed: {float(download_speed() / 1024 / 1024):.2f} Mbps")
        print("------------------------------------------------------")
    elif option == 2:
        print(f"Upload speed: {float(upload_speed() / 1024 / 1024):.2f} Mbps")
        print("------------------------------------------------------")
    elif option == 3:
        print(f"Ping: {int(ping())} ms")
        print("------------------------------------------------------")
    elif option == 4:
        print(f"Ping: {int(ping())} ms")
        print("------------------------------------------------------")
        print(f"Download speed: {float(download_speed()/ 1024 / 1024):.2f} Mbps")
        print("------------------------------------------------------")
        print(f"Upload speed: {float(upload_speed() / 1024 / 1024):.2f} Mbps")
        print("------------------------------------------------------")
    else:
        print('Please enter a correct choice !')


if __name__ == '__main__':
    run()












