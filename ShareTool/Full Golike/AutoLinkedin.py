import sys
import requests
import time
import os
from art import text2art
from colorama import Fore, init
import random

# Khởi tạo colorama
init()

# Danh sách User-Agent (rút gọn để dễ quản lý, bạn có thể thêm lại toàn bộ danh sách)
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36",
]

def install_dependencies():
    """Cài đặt các thư viện cần thiết nếu chưa có."""
    required = ['requests', 'art', 'colorama']
    for lib in required:
        try:
            __import__(lib)
        except ImportError:
            os.system(f"pip install {lib}")

def countdown(time_sec):
    """Hiển thị bộ đếm ngược với màu sắc."""
    colors = [
        "\033[1;37mH\033[1;36mu\033[1;35mo\033[1;32mn\033[1;31mg \033[1;34mD\033[1;33me\033[1;36mv\033[1;36m🍉 - Tool\033[1;36m Vip \033[1;31m\033[1;32m",
        "\033[1;34mH\033[1;31mu\033[1;37mo\033[1;36mn\033[1;32mg \033[1;35mD\033[1;37me\033[1;33mv\033[1;32m🍉 - Tool\033[1;34m Vip \033[1;31m\033[1;32m",
    ]
    for remaining in range(time_sec, -1, -1):
        for color in colors:
            print(f"\r{color}|{remaining}| \033[1;31m", end="")
            time.sleep(0.12)
    print("\r                          \r", end="")
    print("\033[1;35mĐang Nhận Tiền         ", end="\r")

def banner():
    """Hiển thị biểu ngữ ASCII."""
    os.system("cls" if os.name == "nt" else "clear")
    ascii_art = text2art("Huong Dev", font="small")
    info = f"""
\033[1;97mTool By: \033[1;32mTrịnh Hướng            \033[1;97mPhiên Bản: \033[1;32m4.0     
\033[97m════════════════════════════════════════════════  
\033[1;97m[\033[1;91m❣\033[1;97m] Tool\033[1;31m     : \033[1;97m☞ \033[1;31mGolike - Linkedin\033[1;33m♔ \033[1;97m🔫
\033[1;97m[\033[1;91m❣\033[1;97m] Youtube\033[1;31m  : \033[1;97m☞ \033[1;36mHướng Dev - Kiếm Tiền Online\033[1;31m♔ \033[1;97m☜
\033[1;97m[\033[1;91m❣\033[1;97m] Zalo\033[1;31m     : \033[1;97m☞\033[1;31m0362166863☜
\033[97m════════════════════════════════════════════════
"""
    print(ascii_art + info)

def get_headers(auth_token):
    """Tạo tiêu đề HTTP với mã thông báo xác thực."""
    return {
        'Accept-Language': 'vi,en-US;q=0.9,en;q=0.8',
        'Referer': 'https://app.golike.net/',
        'Sec-Ch-Ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': "Windows",
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'T': 'VFZSamQwOUVSVEpQVkVFd1RrRTlQUT09',
        'User-Agent': random.choice(USER_AGENTS),
        "Authorization": auth_token,
        'Content-Type': 'application/json;charset=utf-8'
    }

def linkedin_tasks(ses, headers):
    """Xử lý các tác vụ LinkedIn."""
    try:
        response = ses.get('https://gateway.golike.net/api/linkedin-account', headers=headers)
        response.raise_for_status()
        accounts = response.json().get('data', [])
    except (requests.RequestException, ValueError) as e:
        print(f"Lỗi khi lấy danh sách tài khoản: {e}")
        return

    if not accounts:
        print("Không tìm thấy tài khoản LinkedIn nào.")
        return

    # Hiển thị danh sách tài khoản
    for i, account in enumerate(accounts, 1):
        name = account.get('name', 'Unknown')
        status = Fore.GREEN + "Hoạt Động" + Fore.RESET
        print(f'\033[1;36m[{i}] \033[1;36m✈ \033[1;97mTài Khoản┊\033[1;32m㊪ :\033[1;93m {name} \033[1;97m|\033[1;32m㊪ :\033[1;93m {status}')
        print('\033[97m════════════════════════════════════════════════')

    # Chọn tài khoản
    try:
        choice = int(input('\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;32mNhập Tài Khoản : '))
        if not 1 <= choice <= len(accounts):
            print("Lựa chọn không hợp lệ!")
            return
    except ValueError:
        print("Vui lòng nhập số nguyên!")
        return

    account = accounts[choice - 1]
    account_id = account['id']
    cookie_file = f'COOKIELINKEDIN{account_id}.txt'

    # Quản lý cookie
    if not os.path.isfile(cookie_file):
        banner()
        cookie = input(Fore.GREEN + '\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;32mNhập Cookie Linkedin: ')
        with open(cookie_file, 'w') as f:
            f.write(cookie)
    else:
        with open(cookie_file, 'r') as f:
            cookie = f.read().strip()

    os.system("cls" if os.name == "nt" else "clear")
    banner()

    # Nhập số lượng job và delay
    try:
        job_count = int(input(Fore.RED + '\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  Nhập Số Lượng Job : '))
        delay = int(input(Fore.RED + '\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  Nhập Delay : '))
    except ValueError:
        print("Vui lòng nhập số nguyên!")
        return

    print('\033[97m════════════════════════════════════════════════')
    print(f'\033[1;36m|STT\033[1;97m| \033[1;33mThời gian ┊ \033[1;32mStatus | \033[1;31mType Job | \033[1;32mID Acc | \033[1;32mXu |\033[1;33m Tổng')

    total_coins = 0
    success_count = 0

    for _ in range(job_count):
        try:
            job_url = f'https://gateway.golike.net/api/advertising/publishers/linkedin/jobs?account_id={account_id}&data=null'
            job_response = ses.get(job_url, headers=headers)
            job_data = job_response.json()

            if job_data.get('status') != 200:
                print(job_data.get('message', 'Lỗi không xác định'))
                countdown(15)
                continue

            job_link = job_data['data']['link']
            ads_id = job_data['data']['id']
            object_id = job_data['data']['object_id']
            job_type = job_data['data']['type']

            countdown(delay)

            if job_type == 'follow':
                linkedin_headers = {
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                    'cookie': cookie,
                    'user-agent': random.choice(USER_AGENTS),
                }
                response = requests.get(job_link, headers=linkedin_headers).text

                complete_data = {'account_id': account_id, 'ads_id': ads_id}
                complete_url = 'https://gateway.golike.net/api/advertising/publishers/linkedin/complete-jobs'
                complete_response = ses.post(complete_url, headers=headers, json=complete_data).json()

                if complete_response.get('success'):
                    success_count += 1
                    prices = complete_response['data']['prices']
                    total_coins += prices
                    current_time = time.strftime("%H:%M:%S", time.localtime())
                    print(f"\033[1;31m| \033[1;36m{success_count}\033[1;97m | \033[1;33m{current_time}\033[1;97m | \033[1;32msuccess\033[1;97m | \033[1;31m{job_type}\033[1;97m | \033[1;32mẨn ID\033[1;97m | \033[1;32m+{prices}\033[1;97m | \033[1;33m{total_coins} vnđ")
                else:
                    skip_url = 'https://gateway.golike.net/api/advertising/publishers/linkedin/skip-jobs'
                    ses.post(skip_url, headers=headers, params={'ads_id': ads_id, 'account_id': account_id, 'object_id': object_id})
            # Thêm logic cho 'like' nếu cần
        except Exception as e:
            print(f"Lỗi khi thực hiện job: {e}")

def main():
    """Hàm chính để chạy chương trình."""
    install_dependencies()
    banner()

    # Kiểm tra và lấy mã thông báo
    if not os.path.isfile('user.txt'):
        auth_token = input(Fore.GREEN + '\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;32mNHẬP Authorization Golike : ')
        with open('user.txt', 'w') as f:
            f.write(auth_token)
    else:
        with open('user.txt', 'r') as f:
            auth_token = f.read().strip()

    ses = requests.Session()
    headers = get_headers(auth_token)

    # Kiểm tra đăng nhập
    try:
        response = ses.get('https://gateway.golike.net/api/users/me', headers=headers)
        response.raise_for_status()
        user_data = response.json()
    except (requests.RequestException, ValueError) as e:
        print(f"Lỗi đăng nhập: {e}")
        if os.path.isfile('user.txt'):
            os.remove('user.txt')
        return

    if user_data.get('status') == 200:
        print('ĐĂNG NHẬP THÀNH CÔNG')
        time.sleep(3)
        os.system("cls" if os.name == "nt" else "clear")
        banner()
        username = user_data['data']['username']
        coin = user_data['data']['coin']
        print(Fore.GREEN + f'\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;32mTài Khoản : {username}')
        print(Fore.GREEN + f'\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;32mTổng Tiền : {coin}')
        print(Fore.RED + '\033[97m════════════════════════════════════════════════')
        print("\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;32mNhập \033[1;31m1 \033[1;33mđể vào \033[1;34mTool Linkedin")
        print(Fore.RED + '\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;31mNhập 2 Để Xóa Authorization Hiện Tại')

        try:
            choice = int(input(Fore.WHITE + 'Nhập Lựa Chọn : '))
            if choice == 1:
                linkedin_tasks(ses, headers)
            elif choice == 2:
                if os.path.isfile('user.txt'):
                    os.remove('user.txt')
                    print("Đã xóa Authorization!")
            else:
                print("Lựa chọn không hợp lệ!")
        except ValueError:
            print("Vui lòng nhập số nguyên!")
    else:
        print(Fore.RED + 'ĐĂNG NHẬP THẤT BẠI')
        if os.path.isfile('user.txt'):
            os.remove('user.txt')

if __name__ == "__main__":
    main()
