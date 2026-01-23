"""
iTunes Search Tool - Tìm kiếm bài hát trên iTunes API

Cách dùng: python itunes.py "tên bài hát"
"""
import json
import requests
import sys

def search_itunes(query: str) -> None:
    """
    Tìm kiếm bài hát trên iTunes API và in ra kết quả.
    
    Args:
        query (str): Từ khóa tìm kiếm (tên bài hát hoặc nghệ sĩ)
    """
    # Gọi API iTunes với query từ user
    url = f"https://itunes.apple.com/search?entity=song&limit=50&term={query}"
    response = requests.get(url)
    
    # Parse JSON response
    data = response.json()
    
    # Lưu ý: Key là "results" (số nhiều), không phải "result"
    for result in data["results"]:
        print(result["trackName"])

if __name__ == "__main__":
    # Kiểm tra xem user có nhập đủ argument không
    if len(sys.argv) != 2:
        sys.exit("Usage: python itunes.py 'song name'")
    
    # Lấy query từ command line argument
    search_query = sys.argv[1]
    
    # Thực hiện tìm kiếm
    search_itunes(search_query)