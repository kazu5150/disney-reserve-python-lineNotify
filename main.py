import requests
from dotenv import load_dotenv
import os


def check_hotel_availability():
    research_month = "20240901"
    url = "https://reserve.tokyodisneyresort.jp/hotel/api/queryHotelPriceStock/"
    headers = {
        "User-Agent": "PostmanRuntime/7.38.0"
    }
    payload = {
        "commodityCD": "HOTDHSCL0005N",
        "useDate": research_month,
        "stayingDays": "1",
        "adultNum": "2",
        "childNum": "0",
        "roomsNum": "1",
        "stockQueryType": "3",
        "rrc3005ProcessingType": "update"
    }

    response = requests.post(url, headers=headers, data=payload)
    response_json = response.json()
    
    room_urls = extract_room_urls(response_json)
    if room_urls:
        for url in room_urls:
            print(f"{research_month}")
            print("予約可能な部屋のURL:", url)
        notify_line(f"\n 空きがあります！ \n 対象月: {research_month}  \n URL: {room_urls[0]}")
    else:
        print("空きはありません。")


def notify_line(message):
    load_dotenv()  # .envファイルを読み込む
    line_notify_token = os.getenv("LINE_NOTIFY_TOKEN")
    line_notify_api = "https://notify-api.line.me/api/notify"
    headers = {
        "Authorization": f"Bearer {line_notify_token}"
    }
    data = {
        "message": message
    }
    requests.post(line_notify_api, headers=headers, data=data)
    
    
def generate_room_url(hotel_cd, commodity_cd, use_date):
    base_url = "https://reserve.tokyodisneyresort.jp/hotel/reserve"
    return f"{base_url}?hotelCd={hotel_cd}&commodityCd={commodity_cd}&useDate={use_date}"


def extract_room_urls(response_json):
    room_urls = []
    ec_room_stock_infos = response_json.get('ecRoomStockInfos', {})
    
    for hotel_key, hotel_info in ec_room_stock_infos.items():
        hotel_cd = hotel_info.get('hotelCd')
        room_stock_infos = hotel_info.get('roomStockInfos', {})
        
        for room_name, room_info in room_stock_infos.items():
            room_bed_stock_range_infos = room_info.get('roomBedStockRangeInfos', {})
            
            for commodity_cd, stock_info in room_bed_stock_range_infos.items():
                current_stock = stock_info.get('currentRoomBedStock', {})
                use_date = current_stock.get('useDate')
                
                if 'remainStockNum' in current_stock:
                    room_url = generate_room_url(hotel_cd, commodity_cd, use_date)
                    room_urls.append(room_url)
    
    return room_urls


if __name__ == "__main__":
    check_hotel_availability()
