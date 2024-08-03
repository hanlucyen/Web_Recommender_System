# Web_Recommender_System
NTHN_KLTN
## 1. Procedure Artificial Intelligence
### 1.1. Collecting Data ( Thu thập dữ liệu)
Bộ dữ liệu thứ cấp MyAnimeList của Kaggle được tải lên năm 2020 bởi 
QUANG-VINH DO tại https://www.kaggle.com/datasets/qvinhdo/myanimelist .
Tập dữ liệu với dung lượng khoảng 943 MB chứa tập hợp các anime, người dùng 
và xếp hạng được lấy từ MyAnimeList.net. Tập dữ liệu này chứa 4 tệp.
- animes.csv: gồm 17058 phim hoạt hình chứa thông tin về tiêu đề, anime_id, 
trạng thái phát sóng, số tập và tóm tắt.
- user.csv: gồm 302674 người dùng chứa thông tin người dùng đơn giản như tên 
người dùng, giới tính, vị trí, ngày sinh và ngày tham gia.
- user_watches.csv: gồm 68235827 xếp hạng danh sách anime của người dùng 
cùng với điểm số và trạng thái xem.
- mal_db.dump - Tệp kết xuất của cơ sở dữ liệu postgresql chứa tất cả 3 thông tin 
csv ở trên cùng với Primary Key/ Foreign Key thích hợp, các ràng buộc và chỉ
mục khác.
### 1.2. Preparing Data ( Chuẩn bị dữ liệu)
Bước 1: Cài đặt phần mềm
Các phần mềm đề tài nghiên cứu sử dụng được giới thiệu tại mục 3.1.2. Phần 
mềm và thư viện
Bước 2: Cài đặt viện Python 3.12
Mở Anaconda Prompt
Xuất hiện cửa sổ lệnh Select Anaconda Prompt
Cài đặt các thư viện của Python

• Thư viện Numpy
• Thư viện pandas
• Thư viện Scipy
• Thư viện Pickle
• Thư viện Scikit-learn (Sklearn)
• Thư viện Streamlit
Bước 3: Phân tích dữ liệu
Quy trình phân tích dữ liệu gồm các bước được thực hiện tại mục 3.1.1.2. Phân 
tích và thống kê dữ liệu.
Bước 4: Chuẩn bị dữ liệu

❖ Mở phần mềm Jupyter Notebook
Hình 10: Giao diện phần mềm Jupyter Notebook
Sau khi mở phần mềm, tạo một thư mục mới tên “AI2”.
Hình 11: Giao diện web của phần mềm Jupyter Notebook
Mở thư mục AI2 và tải các tệp chứa thông tin của dữ liệu vào thư mục AI2.
38
Hình 12: Tải dữ liệu vào thư mục AI2
Tạo thêm một tệp Python 3 có định dạng .ipynb và đặt tên là 
MyAnimeList.ipynb.
Hình 13: Đặt tên cho tệp Python 3
Mở file MyAnimeList.ipynb.
❖ Gọi thư viện
• Thư viện Numpy
Hình 14: Lệnh gọi thư viện Numpy
• Thư viện Pandas
Hình 15: Lệnh gọi thư viện Pandas
• Thư viện Scipy

Hình 16: Lệnh gọi thư viện Scipy
• Thư viện Pickle
Hình 17: Lệnh gọi thư viện Pickle
• Thư viện Scikit-learn (Sklearn)
Hình 18: Lệnh gọi thư viện Sklearn
• Thư viện Streamlit
Hình 19: Lệnh gọi thư viện Streamlit
❖ Đọc dữ liệu


• animes.csv 
Hình 20: Lệnh đọc tệp animes.csv
Hình 21: Kết quả đọc tệp animes.csv
40
• users.csv
Hình 22: Lệnh đọc tệp users.csv
Hình 23: Kết quả đọc tệp users.csv
• user_watches.csv 
Hình 24: Lệnh đọc tệp user_watches.csv
41
Hình 25: Kết quả đọc tệp user_watches.csv
❖ Kích thước tệp
• animes.csv 
Hình 26: Lệnh xác định kích thước của tệp animes.csv
Hình 27: Kết quả kích thước của tệp animes.csv
• users.csv
Hình 28: Lệnh xác định kích thước của tệp users.csv
Hình 29: Kết quả kích thước của tệp users.csv
42
• user_watches.csv
Hình 30: Lệnh xác định kích thước của tệp user_watches.csv
Hình 31: Kết quả kích thước của tệp user_watches.csv
❖ Thống kê
• animes.csv 
Hình 32: Lệnh thống kê số cơ bản của tệp animes.csv làm tròn đến chữ số thập phân 
thứ 2
Hình 33: Kết quả thống kê số cơ bản của tệp animes.csv
• users.csv
Hình 34: Lệnh thống kê số cơ bản của tệp users.csv làm tròn đến chữ số thập phân thứ
2
43
Hình 35: Kết quả thống kê số cơ bản của tệp users.csv
• user_watches.csv
Hình 36 : Lệnh thống kê số cơ bản của tệp user_watches.csv làm tròn đến chữ số thập 
phân thứ 2
Hình 37: Kết quả thống kê số cơ bản của tệp user_watches.csv
1.3. Choosing model ( Chọn mô hình)
Mô hình đề tài nghiên cứu được giới thiệu tại mục 2.3. Tổng quan phương pháp 
nghiên cứu.
44
Value_count() trả về đối tượng chứa số lượng giá trị duy nhất. Ở đây có thể xác 
định được người dùng đã xếp hạng cho bao nhiêu phim hoạt hình, ví dụ cho user_id 
4053169 đã xếp hạng cho 17058 phim hoạt hình và user_id 323300 đã xếp hạng cho 1 
phim hoạt hình.
Hình 38: Lệnh Value_count()
Hình 39: Kết quả Value_count()
Kích thước Value_count() của cột user_id trong user_watches.csv.
Hình 40: Lệnh xác định kích thước Value_count() của cột user_id trong 
user_watches.csv
Hình 41: Kết quả kích thước Value_count() của cột user_id trong user_watches.csv
Kiểm tra giá trị duy nhất của cột user_id trong user_watches.csv.
45
Hình 42: Lệnh xác kích thước unique() của cột user_id trong user_watches.csv
Hình 43: Kết quả kích thước unique() của cột user_id trong user_watches.csv
Lọc để loại các giá trị nhỏ hơn 1000. Tiến hành lọc bỏ đi các user_id của người 
dùng đã xếp hạng cho ít hơn 10000 phim hoạt hình nhằm tăng độ tin cậy cho dữ liệu.
Hình 44: Lệnh lọc các giá trị lớn hơn 1000
Và kết quả lọc có 8840 user_id đã xếp hạng cho hơn 1000 phim hoạt hình.
Hình 45: Kết quả lọc
Tìm user_id của người dùng.
Hình 46: Lệnh tìm user_id của người dùng
Hình 47: Kết quả user_id của người dùng
Sắp xếp các xếp hạng và chuyển lại xếp hạng theo user_id.
Hình 48: Lệnh sắp xếp các xếp hạng theo user_id và trình bày 10 dòng đầu tiên
46
Hình 49: Kết quả sắp xếp các xếp hạng theo user_id
Kích thước của sắp xếp các xếp hạng theo user_id.
Hình 50: Lệnh xác định kích thước các xếp hạng theo user_id
Hình 51: Kết quả kích thước các xếp hạng theo user_id
Gộp tệp “animes.csv” và “user_watches.csv” theo cột anime_id.
Hình 52: Lệnh gộp và trình bày 10 dòng đầu tiên
47
Hình 53: Kết quả gộp
Kích thước sau khi gộp.
Hình 54: Lệnh xác định kích thước sau khi gộp
Hình 55:Kết quả kích thước sau khi gộp
Nhóm cột title và score. Số lượng các xếp hạng của phim hoạt hình.
Hình 56: Lệnh nhóm cột title và score
Hình 57: Kết quả nhóm cột title và score
48
Thay đổi tên cột score thành num_of_score.
Hình 58: Lệnh đổi tên cột score thành num_of_score
Hình 59: Kết quả đổi tên
Hợp nhất các cột theo cột title.
Hình 60: Lệnh gộp và trình bày 5 dòng đầu tiên
Hình 61: Kết quả gộp
Kích thước sau khi gộp.
Hình 62: Lệnh xác định kích thước sau khi gộp
49
Hình 63: Kết quả sau khi gộp
Lọc loại bỏ các phim hoạt hình có nhỏ hơn hoặc bằng 50 xếp hạng.
Hình 64: Lệnh lọc các phim hoạt hình có hơn 50 xếp hạng 
Hình 65: Kết quả các phim hoạt hình có hơn 50 xếp hạng
Kích thước sau khi lọc.
Hình 66: Lệnh xác định kích thước sau khi lọc
Hình 67: Kết quả sau khi lọc 
Tiêu đề của các cột.
Hình 68: Lệnh trả về các tiêu đề của các cột
Hình 69: Kết quả các tiêu đề cột
Điều chỉnh và loại bỏ một số cột không dùng.
50
Hình 70: Lệnh điều chỉnh cột
Hình 71: Kết quả điều chỉnh cột
Loại bỏ các giá trị trùng lặp ở cột user_id và title.
Hình 72: Lệnh loại bỏ các giá trị trùng lặp
Kích thước sau khi loại bỏ.
Hình 73: Lệnh xác định kích thước sau khi loại bỏ trùng lặp
Hình 74: Kết quả kích thước sau khi loại bỏ trùng lặp
PivotTable
Utility Matrix:
User_id
Title
36 228 540 ...
Aria the Avvenire 6 1 8 ...
Deca-Dence 6 0 NaN ...
51
11eyes: Momoiro Genmutan 6 10 6 ...
Cowboy Bebop 9 9 10 ...
... ... ... ... ...
Sử dụng PivotTable để nhanh chóng tóm tắt dữ liệu lớn. Ở đây việc xây dựng 
Utility Matrix là quan trọng để tập hợp tất cả điểm gồm các giá trị đã biết và chưa biết 
cần được dự đoán. Liệu người dùng 540 có thích “Deca-Dence” không? Dựa vào sự
tương đồng về xếp hạng điểm số của người dùng 540 với người dùng 36 về phim hoạt 
hình “11eyes: Momoiro Genmutan” là 6. Nếu đề xuất “Deca-Dence” thì điểm có thể là 
bao nhiêu? Mô hình sự phân cụm, một số người dùng có xếp hạng tương đồng cho một 
số phim hoạt hình có thể có sở thích hoặc hành vi tương đồng nhau. Có dự đoán xếp 
hạng điểm số của người dùng 540 cho phim hoạt hình “Deca-Dence”.
Tạo một bảng tổng hợp với các cột user_id, title và score để xây dựng ma trận.
Hình 75: Lệnh tạo ma trận
Hình 76: Kết quả tạo ma trận
Kiểm tra lại kích thước của ma trận.
Hình 77: Lệnh xác định kích thước ma trận
52
Hình 78: Kết quả kích thước ma trận
Thay thế các giá trị NaN thành 0 để mô hình có thể tính toán khoảng cách giữa 
các cột.
Hình 79: Lệnh chuyển đổi NaN thành 0
Hình 80: Kết quả chuyển đổi
Sử dụng csr_matrix hàng thưa thớt được nén để cắt hàng nhanh, sản phẩm 
vector ma trận nhanh hơn. 
Hình 81: Lệnh tạo hàng không gian nén
Hình 82: Lệnh kiểm tra loại kiểu nén
53
Hình 83: Kết quả loại kiểu nén
Xây dựng thuật toán KNN.
Hình 84: Lệnh gọi thuật toán
Hình 85: Lệnh truyền hàng không gian nén
Hình 86: Kết quả lệnh gọi thuật toán KNN
1.4. Tuning Parameter (Điều chỉnh thông số)
Khởi tạo biến distance và suggestion. Xây dựng mô hình có chức năng tìm KNN 
và k =11 với giá trị trả về là 10 kết quả khoảng cách và đề xuất cho mục chỉ định là 
anime_id là 30. 
Hình 87: Lệnh xây dựng mô hình
Khoảng cách 10 anime_id gần nhất với anime_id 30.
Hình 88: Lệnh gọi biến distance
54
Hình 89: Kết quả biến distance
Đề xuất 10 anime_id cho kết quả tìm kiếm với anime_id 30.
Hình 90: Lệnh gọi suggestion
Hình 91: Kết quả biến suggestion
Lọc điểm xếp hạng (trên thang điểm 10) của user_id dành cho anime_id 1.
Hình 92: Lệnh lọc điểm xếp hạng của user_id dành cho anime_id 1
Hình 93: Kết quả lọc điểm xếp hạng của user_id dành cho anime_id 1
Trình bày 10 đề xuất trên theo cột title.
Hình 94: Lệnh đề xuất tên phim hoạt hình
55
Hình 95: Kết quả đề xuất tên phim hoạt hình
Gọi tên sách thông qua anime_id. Thử với anime_id là 100.
Hình 96: Lệnh gọi tên phim hoạt hình
Hình 97: Kết quả gọi tên phim hoạt hình
Hình 98: Lệnh tạo biến tên phim hoạt hình
Hình 99: Lệnh gọi biến tên phim hoạt hình
Hình 100: Kết quả gọi biến tên phim hoạt hình
Gọi ngược lại từ title thì anime_id ở đâu.
Hình 101: Lệnh gọi anime_id bằng title
56
Hình 102: Kết quả anime_id trả về
Hình 103: Lệnh tạo biến gọi anime_id bằng title
❖ Tìm ảnh phim hoạt hình
Hình 104: Lệnh gọi đường dẫn ảnh phim hoạt hình
Hình 105: Kết quả đường dẫn ảnh phim hoạt hình
Hình 106: Lệnh đề xuất tên phim hoạt hình
Hình 107: Lệnh gọi anime_id bằng title
57
Hình 108: Lệnh gọi đường dẫn ảnh phim hoạt hình
Hình 109: Kết quả gọi đường dẫn ảnh phim hoạt hình
❖ Hàm đề xuất
Hình 110: Lệnh tạo hàm đề xuất
1.5. Making Prediction ( Đưa ra đề xuất)
❖ Đề xuất thử
Hình 111: Lệnh đề xuất cho “ Aria the Avvenire”
58
Hình 112: Kết quả đề xuất cho “ Aria the Avvenire”
Hình 113: Lệnh đề xuất cho “ Hanasaku Iroha”
Hình 114: Kết quả đề xuất cho “ Hanasaku Iroha”
Hình 115: Lệnh đề xuất cho “ Minami-ke”
59
Hình 116: Kết quả đề xuất cho “ Minami-ke”
❖ Xuất các tệp với định dạng .pkl
Hình 117: Lệnh xuất mô hình
2. Design ( Thiết kế)
Tạo một thư mục trống ngoài desktop đặt tên là “08032024”.
Hình 118: Tạo thư mục mới
Tiếp tục tạo một thư mục có tên là “interface” chứa 4 tệp .pkl vừa xuất.
Hình 119: Tạo thư mục “interface”
60
Hình 120: Mở thư mục “08032024”
Tải tệp “MyAnimeList.ipynb” từ Jupyter Notebook vào thư mục “08032024”.
Tải tệp “MyAnimeList.py” từ Jupyter Notebook vào thư mục “08032024”.
Tải thêm 4 tệp của bộ dữ liệu MyAnimeList gồm “animes.csv”, “users.csv”, 
“user_watches.csv” và “mal_db.dump” vào thư mục “08032024”.
Tạo thêm một tệp “app.py” và một hình ảnh để là chèn trang trí.
Kết quả: 
Hình 121: Mở thư mục “08032024” 
61
Mở phần mềm Visual Studio Code. Mở thư mục “08032024”.
Hình 122: Mở phần mềm Visual Studio Code
2.1. Web design ( Thiết kế Web)
Mở tệp “app.py”
❖ Chuẩn bị thư viện
Hình 123: Mở tệp “app.py”
Hình 124: Lệnh thiết lập tiêu đề trang
62
Hình 125: Kết quả thiết lập tiêu đề
Hình 126: Lệnh chèn ảnh
Hình 127: Kết quả chèn ảnh
Hình 128: Lệnh tạo tiêu đề web-app và gọi tệp chứa mô hình
Hình 129: Kết quả tiêu đề web-app
2.2. Fuction design ( Thiết kế chức năng)
63
Hình 130: Lệnh đề xuất ảnh phim hoạt hình
Hình 131: Lệnh đề xuất tên phim hoạt hình
Hình 132: Lệnh thiết lập thanh tìm kiếm
64
Hình 133: Kết quả thanh tìm kiếm
65
Hình 134: Lệnh thiết lập chức năng trình bày kết quả đề xuất
Hình 135: Giao diện đề xuất cho từ khóa “ Doraemon”
❖ Chạy “app.py”
Trên thanh công cụ tìm Terminal chọn New Terminal hoặc nhấn tổ hợp phím 
Ctrl+Shift+`.
66
Hình136: Tìm cửa sổ lệnh Terminal 
Tại cửa sổ lệnh “Terminal” gõ “streamlit run app.py” và nhấn phím “Enter”.
Hình137: Lệnh chạy trên cửa sổ Terminal
## By Nguyễn Thị Huỳnh Như
## Date: 25/07/2024
## Mail: 20166050@st.hcmuaf.edu.vn / nguyenthihuynhnhu271025@gmail.co1. Procedure Artificial Intelligence
1.1. Collecting Data ( Thu thập dữ liệu)
Bộ dữ liệu thứ cấp MyAnimeList của Kaggle được tải lên năm 2020 bởi 
QUANG-VINH DO tại https://www.kaggle.com/datasets/qvinhdo/myanimelist được 
thể hiện như Hình 1:
Hình 1: Dữ liệu thứ cấp MyAnimeList
Tập dữ liệu với dung lượng khoảng 943 MB chứa tập hợp các anime, người dùng 
và xếp hạng được lấy từ MyAnimeList.net. Tập dữ liệu này chứa 4 tệp.
- animes.csv: gồm 17058 phim hoạt hình chứa thông tin về tiêu đề, anime_id, 
trạng thái phát sóng, số tập và tóm tắt.
- user.csv: gồm 302674 người dùng chứa thông tin người dùng đơn giản như tên 
người dùng, giới tính, vị trí, ngày sinh và ngày tham gia.
33
- user_watches.csv: gồm 68235827 xếp hạng danh sách anime của người dùng 
cùng với điểm số và trạng thái xem.
- mal_db.dump - Tệp kết xuất của cơ sở dữ liệu postgresql chứa tất cả 3 thông tin 
csv ở trên cùng với Primary Key/ Foreign Key thích hợp, các ràng buộc và chỉ
mục khác.
1.2. Preparing Data ( Chuẩn bị dữ liệu)
Bước 1: Cài đặt phần mềm
Các phần mềm đề tài nghiên cứu sử dụng được giới thiệu tại mục 3.1.2. Phần 
mềm và thư viện
Bước 2: Cài đặt viện Python 3.12
Mở Anaconda Prompt
Hình 2: Phần mềm Anaconda Prompt
Xuất hiện cửa sổ lệnh Select Anaconda Prompt
Hình 3: Cửa số lệnh của phần mềm Anaconda Prompt
Cài đặt các thư viện của Python
34
• Thư viện Numpy
Hình 4: Cài đặt thư viện Numpy
• Thư viện pandas
Hình 5: Cài đặt thư viện Pandas
• Thư viện Scipy
35
Hình 6: Cài đặt thư viện Scipy
• Thư viện Pickle
Hình 7: Cài đặt thư viện Pickle5
• Thư viện Scikit-learn (Sklearn)
36
Hình 8: Cài đặt thư viện Scikit-learn
• Thư viện Streamlit
Hình 9: Cài đặt thư viên Streamlit
Bước 3: Phân tích dữ liệu
Quy trình phân tích dữ liệu gồm các bước được thực hiện tại mục 3.1.1.2. Phân 
tích và thống kê dữ liệu.
Bước 4: Chuẩn bị dữ liệu
37
❖ Mở phần mềm Jupyter Notebook
Hình 10: Giao diện phần mềm Jupyter Notebook
Sau khi mở phần mềm, tạo một thư mục mới tên “AI2”.
Hình 11: Giao diện web của phần mềm Jupyter Notebook
Mở thư mục AI2 và tải các tệp chứa thông tin của dữ liệu vào thư mục AI2.
38
Hình 12: Tải dữ liệu vào thư mục AI2
Tạo thêm một tệp Python 3 có định dạng .ipynb và đặt tên là 
MyAnimeList.ipynb.
Hình 13: Đặt tên cho tệp Python 3
Mở file MyAnimeList.ipynb.
❖ Gọi thư viện
• Thư viện Numpy
Hình 14: Lệnh gọi thư viện Numpy
• Thư viện Pandas
Hình 15: Lệnh gọi thư viện Pandas
• Thư viện Scipy
39
Hình 16: Lệnh gọi thư viện Scipy
• Thư viện Pickle
Hình 17: Lệnh gọi thư viện Pickle
• Thư viện Scikit-learn (Sklearn)
Hình 18: Lệnh gọi thư viện Sklearn
• Thư viện Streamlit
Hình 19: Lệnh gọi thư viện Streamlit
❖ Đọc dữ liệu
• animes.csv 
Hình 20: Lệnh đọc tệp animes.csv
Hình 21: Kết quả đọc tệp animes.csv
40
• users.csv
Hình 22: Lệnh đọc tệp users.csv
Hình 23: Kết quả đọc tệp users.csv
• user_watches.csv 
Hình 24: Lệnh đọc tệp user_watches.csv
41
Hình 25: Kết quả đọc tệp user_watches.csv
❖ Kích thước tệp
• animes.csv 
Hình 26: Lệnh xác định kích thước của tệp animes.csv
Hình 27: Kết quả kích thước của tệp animes.csv
• users.csv
Hình 28: Lệnh xác định kích thước của tệp users.csv
Hình 29: Kết quả kích thước của tệp users.csv
42
• user_watches.csv
Hình 30: Lệnh xác định kích thước của tệp user_watches.csv
Hình 31: Kết quả kích thước của tệp user_watches.csv
❖ Thống kê
• animes.csv 
Hình 32: Lệnh thống kê số cơ bản của tệp animes.csv làm tròn đến chữ số thập phân 
thứ 2
Hình 33: Kết quả thống kê số cơ bản của tệp animes.csv
• users.csv
Hình 34: Lệnh thống kê số cơ bản của tệp users.csv làm tròn đến chữ số thập phân thứ
2
43
Hình 35: Kết quả thống kê số cơ bản của tệp users.csv
• user_watches.csv
Hình 36 : Lệnh thống kê số cơ bản của tệp user_watches.csv làm tròn đến chữ số thập 
phân thứ 2
Hình 37: Kết quả thống kê số cơ bản của tệp user_watches.csv
1.3. Choosing model ( Chọn mô hình)
Mô hình đề tài nghiên cứu được giới thiệu tại mục 2.3. Tổng quan phương pháp 
nghiên cứu.
44
Value_count() trả về đối tượng chứa số lượng giá trị duy nhất. Ở đây có thể xác 
định được người dùng đã xếp hạng cho bao nhiêu phim hoạt hình, ví dụ cho user_id 
4053169 đã xếp hạng cho 17058 phim hoạt hình và user_id 323300 đã xếp hạng cho 1 
phim hoạt hình.
Hình 38: Lệnh Value_count()
Hình 39: Kết quả Value_count()
Kích thước Value_count() của cột user_id trong user_watches.csv.
Hình 40: Lệnh xác định kích thước Value_count() của cột user_id trong 
user_watches.csv
Hình 41: Kết quả kích thước Value_count() của cột user_id trong user_watches.csv
Kiểm tra giá trị duy nhất của cột user_id trong user_watches.csv.
45
Hình 42: Lệnh xác kích thước unique() của cột user_id trong user_watches.csv
Hình 43: Kết quả kích thước unique() của cột user_id trong user_watches.csv
Lọc để loại các giá trị nhỏ hơn 1000. Tiến hành lọc bỏ đi các user_id của người 
dùng đã xếp hạng cho ít hơn 10000 phim hoạt hình nhằm tăng độ tin cậy cho dữ liệu.
Hình 44: Lệnh lọc các giá trị lớn hơn 1000
Và kết quả lọc có 8840 user_id đã xếp hạng cho hơn 1000 phim hoạt hình.
Hình 45: Kết quả lọc
Tìm user_id của người dùng.
Hình 46: Lệnh tìm user_id của người dùng
Hình 47: Kết quả user_id của người dùng
Sắp xếp các xếp hạng và chuyển lại xếp hạng theo user_id.
Hình 48: Lệnh sắp xếp các xếp hạng theo user_id và trình bày 10 dòng đầu tiên
46
Hình 49: Kết quả sắp xếp các xếp hạng theo user_id
Kích thước của sắp xếp các xếp hạng theo user_id.
Hình 50: Lệnh xác định kích thước các xếp hạng theo user_id
Hình 51: Kết quả kích thước các xếp hạng theo user_id
Gộp tệp “animes.csv” và “user_watches.csv” theo cột anime_id.
Hình 52: Lệnh gộp và trình bày 10 dòng đầu tiên
47
Hình 53: Kết quả gộp
Kích thước sau khi gộp.
Hình 54: Lệnh xác định kích thước sau khi gộp
Hình 55:Kết quả kích thước sau khi gộp
Nhóm cột title và score. Số lượng các xếp hạng của phim hoạt hình.
Hình 56: Lệnh nhóm cột title và score
Hình 57: Kết quả nhóm cột title và score
48
Thay đổi tên cột score thành num_of_score.
Hình 58: Lệnh đổi tên cột score thành num_of_score
Hình 59: Kết quả đổi tên
Hợp nhất các cột theo cột title.
Hình 60: Lệnh gộp và trình bày 5 dòng đầu tiên
Hình 61: Kết quả gộp
Kích thước sau khi gộp.
Hình 62: Lệnh xác định kích thước sau khi gộp
49
Hình 63: Kết quả sau khi gộp
Lọc loại bỏ các phim hoạt hình có nhỏ hơn hoặc bằng 50 xếp hạng.
Hình 64: Lệnh lọc các phim hoạt hình có hơn 50 xếp hạng 
Hình 65: Kết quả các phim hoạt hình có hơn 50 xếp hạng
Kích thước sau khi lọc.
Hình 66: Lệnh xác định kích thước sau khi lọc
Hình 67: Kết quả sau khi lọc 
Tiêu đề của các cột.
Hình 68: Lệnh trả về các tiêu đề của các cột
Hình 69: Kết quả các tiêu đề cột
Điều chỉnh và loại bỏ một số cột không dùng.
50
Hình 70: Lệnh điều chỉnh cột
Hình 71: Kết quả điều chỉnh cột
Loại bỏ các giá trị trùng lặp ở cột user_id và title.
Hình 72: Lệnh loại bỏ các giá trị trùng lặp
Kích thước sau khi loại bỏ.
Hình 73: Lệnh xác định kích thước sau khi loại bỏ trùng lặp
Hình 74: Kết quả kích thước sau khi loại bỏ trùng lặp
PivotTable
Utility Matrix:
User_id
Title
36 228 540 ...
Aria the Avvenire 6 1 8 ...
Deca-Dence 6 0 NaN ...
51
11eyes: Momoiro Genmutan 6 10 6 ...
Cowboy Bebop 9 9 10 ...
... ... ... ... ...
Sử dụng PivotTable để nhanh chóng tóm tắt dữ liệu lớn. Ở đây việc xây dựng 
Utility Matrix là quan trọng để tập hợp tất cả điểm gồm các giá trị đã biết và chưa biết 
cần được dự đoán. Liệu người dùng 540 có thích “Deca-Dence” không? Dựa vào sự
tương đồng về xếp hạng điểm số của người dùng 540 với người dùng 36 về phim hoạt 
hình “11eyes: Momoiro Genmutan” là 6. Nếu đề xuất “Deca-Dence” thì điểm có thể là 
bao nhiêu? Mô hình sự phân cụm, một số người dùng có xếp hạng tương đồng cho một 
số phim hoạt hình có thể có sở thích hoặc hành vi tương đồng nhau. Có dự đoán xếp 
hạng điểm số của người dùng 540 cho phim hoạt hình “Deca-Dence”.
Tạo một bảng tổng hợp với các cột user_id, title và score để xây dựng ma trận.
Hình 75: Lệnh tạo ma trận
Hình 76: Kết quả tạo ma trận
Kiểm tra lại kích thước của ma trận.
Hình 77: Lệnh xác định kích thước ma trận
52
Hình 78: Kết quả kích thước ma trận
Thay thế các giá trị NaN thành 0 để mô hình có thể tính toán khoảng cách giữa 
các cột.
Hình 79: Lệnh chuyển đổi NaN thành 0
Hình 80: Kết quả chuyển đổi
Sử dụng csr_matrix hàng thưa thớt được nén để cắt hàng nhanh, sản phẩm 
vector ma trận nhanh hơn. 
Hình 81: Lệnh tạo hàng không gian nén
Hình 82: Lệnh kiểm tra loại kiểu nén
53
Hình 83: Kết quả loại kiểu nén
Xây dựng thuật toán KNN.
Hình 84: Lệnh gọi thuật toán
Hình 85: Lệnh truyền hàng không gian nén
Hình 86: Kết quả lệnh gọi thuật toán KNN
1.4. Tuning Parameter (Điều chỉnh thông số)
Khởi tạo biến distance và suggestion. Xây dựng mô hình có chức năng tìm KNN 
và k =11 với giá trị trả về là 10 kết quả khoảng cách và đề xuất cho mục chỉ định là 
anime_id là 30. 
Hình 87: Lệnh xây dựng mô hình
Khoảng cách 10 anime_id gần nhất với anime_id 30.
Hình 88: Lệnh gọi biến distance
54
Hình 89: Kết quả biến distance
Đề xuất 10 anime_id cho kết quả tìm kiếm với anime_id 30.
Hình 90: Lệnh gọi suggestion
Hình 91: Kết quả biến suggestion
Lọc điểm xếp hạng (trên thang điểm 10) của user_id dành cho anime_id 1.
Hình 92: Lệnh lọc điểm xếp hạng của user_id dành cho anime_id 1
Hình 93: Kết quả lọc điểm xếp hạng của user_id dành cho anime_id 1
Trình bày 10 đề xuất trên theo cột title.
Hình 94: Lệnh đề xuất tên phim hoạt hình
55
Hình 95: Kết quả đề xuất tên phim hoạt hình
Gọi tên sách thông qua anime_id. Thử với anime_id là 100.
Hình 96: Lệnh gọi tên phim hoạt hình
Hình 97: Kết quả gọi tên phim hoạt hình
Hình 98: Lệnh tạo biến tên phim hoạt hình
Hình 99: Lệnh gọi biến tên phim hoạt hình
Hình 100: Kết quả gọi biến tên phim hoạt hình
Gọi ngược lại từ title thì anime_id ở đâu.
Hình 101: Lệnh gọi anime_id bằng title
56
Hình 102: Kết quả anime_id trả về
Hình 103: Lệnh tạo biến gọi anime_id bằng title
❖ Tìm ảnh phim hoạt hình
Hình 104: Lệnh gọi đường dẫn ảnh phim hoạt hình
Hình 105: Kết quả đường dẫn ảnh phim hoạt hình
Hình 106: Lệnh đề xuất tên phim hoạt hình
Hình 107: Lệnh gọi anime_id bằng title
57
Hình 108: Lệnh gọi đường dẫn ảnh phim hoạt hình
Hình 109: Kết quả gọi đường dẫn ảnh phim hoạt hình
❖ Hàm đề xuất
Hình 110: Lệnh tạo hàm đề xuất
1.5. Making Prediction ( Đưa ra đề xuất)
❖ Đề xuất thử
Hình 111: Lệnh đề xuất cho “ Aria the Avvenire”
58
Hình 112: Kết quả đề xuất cho “ Aria the Avvenire”
Hình 113: Lệnh đề xuất cho “ Hanasaku Iroha”
Hình 114: Kết quả đề xuất cho “ Hanasaku Iroha”
Hình 115: Lệnh đề xuất cho “ Minami-ke”
59
Hình 116: Kết quả đề xuất cho “ Minami-ke”
❖ Xuất các tệp với định dạng .pkl
Hình 117: Lệnh xuất mô hình
2. Design ( Thiết kế)
Tạo một thư mục trống ngoài desktop đặt tên là “08032024”.
Hình 118: Tạo thư mục mới
Tiếp tục tạo một thư mục có tên là “interface” chứa 4 tệp .pkl vừa xuất.
Hình 119: Tạo thư mục “interface”
60
Hình 120: Mở thư mục “08032024”
Tải tệp “MyAnimeList.ipynb” từ Jupyter Notebook vào thư mục “08032024”.
Tải tệp “MyAnimeList.py” từ Jupyter Notebook vào thư mục “08032024”.
Tải thêm 4 tệp của bộ dữ liệu MyAnimeList gồm “animes.csv”, “users.csv”, 
“user_watches.csv” và “mal_db.dump” vào thư mục “08032024”.
Tạo thêm một tệp “app.py” và một hình ảnh để là chèn trang trí.
Kết quả: 
Hình 121: Mở thư mục “08032024” 
61
Mở phần mềm Visual Studio Code. Mở thư mục “08032024”.
Hình 122: Mở phần mềm Visual Studio Code
2.1. Web design ( Thiết kế Web)
Mở tệp “app.py”
❖ Chuẩn bị thư viện
Hình 123: Mở tệp “app.py”
Hình 124: Lệnh thiết lập tiêu đề trang
62
Hình 125: Kết quả thiết lập tiêu đề
Hình 126: Lệnh chèn ảnh
Hình 127: Kết quả chèn ảnh
Hình 128: Lệnh tạo tiêu đề web-app và gọi tệp chứa mô hình
Hình 129: Kết quả tiêu đề web-app
2.2. Fuction design ( Thiết kế chức năng)
63
Hình 130: Lệnh đề xuất ảnh phim hoạt hình
Hình 131: Lệnh đề xuất tên phim hoạt hình
Hình 132: Lệnh thiết lập thanh tìm kiếm
64
Hình 133: Kết quả thanh tìm kiếm
65
Hình 134: Lệnh thiết lập chức năng trình bày kết quả đề xuất
Hình 135: Giao diện đề xuất cho từ khóa “ Doraemon”
❖ Chạy “app.py”
Trên thanh công cụ tìm Terminal chọn New Terminal hoặc nhấn tổ hợp phím 
Ctrl+Shift+`.
66
Hình136: Tìm cửa sổ lệnh Terminal 
Tại cửa sổ lệnh “Terminal” gõ “streamlit run app.py” và nhấn phím “Enter”.
Hình137: Lệnh chạy trên cửa sổ Terminal
## By Nguyễn Thị Huỳnh Như
## Date: 25/07/2024
## Mail: 20166050@st.hcmuaf.edu.vn / nguyenthihuynhnhu271025@gmail.co1. Procedure Artificial Intelligence
1.1. Collecting Data ( Thu thập dữ liệu)
Bộ dữ liệu thứ cấp MyAnimeList của Kaggle được tải lên năm 2020 bởi 
QUANG-VINH DO tại https://www.kaggle.com/datasets/qvinhdo/myanimelist được 
thể hiện như Hình 1:
Hình 1: Dữ liệu thứ cấp MyAnimeList
Tập dữ liệu với dung lượng khoảng 943 MB chứa tập hợp các anime, người dùng 
và xếp hạng được lấy từ MyAnimeList.net. Tập dữ liệu này chứa 4 tệp.
- animes.csv: gồm 17058 phim hoạt hình chứa thông tin về tiêu đề, anime_id, 
trạng thái phát sóng, số tập và tóm tắt.
- user.csv: gồm 302674 người dùng chứa thông tin người dùng đơn giản như tên 
người dùng, giới tính, vị trí, ngày sinh và ngày tham gia.
33
- user_watches.csv: gồm 68235827 xếp hạng danh sách anime của người dùng 
cùng với điểm số và trạng thái xem.
- mal_db.dump - Tệp kết xuất của cơ sở dữ liệu postgresql chứa tất cả 3 thông tin 
csv ở trên cùng với Primary Key/ Foreign Key thích hợp, các ràng buộc và chỉ
mục khác.
1.2. Preparing Data ( Chuẩn bị dữ liệu)
Bước 1: Cài đặt phần mềm
Các phần mềm đề tài nghiên cứu sử dụng được giới thiệu tại mục 3.1.2. Phần 
mềm và thư viện
Bước 2: Cài đặt viện Python 3.12
Mở Anaconda Prompt
Hình 2: Phần mềm Anaconda Prompt
Xuất hiện cửa sổ lệnh Select Anaconda Prompt
Hình 3: Cửa số lệnh của phần mềm Anaconda Prompt
Cài đặt các thư viện của Python
34
• Thư viện Numpy
Hình 4: Cài đặt thư viện Numpy
• Thư viện pandas
Hình 5: Cài đặt thư viện Pandas
• Thư viện Scipy
35
Hình 6: Cài đặt thư viện Scipy
• Thư viện Pickle
Hình 7: Cài đặt thư viện Pickle5
• Thư viện Scikit-learn (Sklearn)
36
Hình 8: Cài đặt thư viện Scikit-learn
• Thư viện Streamlit
Hình 9: Cài đặt thư viên Streamlit
Bước 3: Phân tích dữ liệu
Quy trình phân tích dữ liệu gồm các bước được thực hiện tại mục 3.1.1.2. Phân 
tích và thống kê dữ liệu.
Bước 4: Chuẩn bị dữ liệu
37
❖ Mở phần mềm Jupyter Notebook
Hình 10: Giao diện phần mềm Jupyter Notebook
Sau khi mở phần mềm, tạo một thư mục mới tên “AI2”.
Hình 11: Giao diện web của phần mềm Jupyter Notebook
Mở thư mục AI2 và tải các tệp chứa thông tin của dữ liệu vào thư mục AI2.
38
Hình 12: Tải dữ liệu vào thư mục AI2
Tạo thêm một tệp Python 3 có định dạng .ipynb và đặt tên là 
MyAnimeList.ipynb.
Hình 13: Đặt tên cho tệp Python 3
Mở file MyAnimeList.ipynb.
❖ Gọi thư viện
• Thư viện Numpy
Hình 14: Lệnh gọi thư viện Numpy
• Thư viện Pandas
Hình 15: Lệnh gọi thư viện Pandas
• Thư viện Scipy
39
Hình 16: Lệnh gọi thư viện Scipy
• Thư viện Pickle
Hình 17: Lệnh gọi thư viện Pickle
• Thư viện Scikit-learn (Sklearn)
Hình 18: Lệnh gọi thư viện Sklearn
• Thư viện Streamlit
Hình 19: Lệnh gọi thư viện Streamlit
❖ Đọc dữ liệu
• animes.csv 
Hình 20: Lệnh đọc tệp animes.csv
Hình 21: Kết quả đọc tệp animes.csv
40
• users.csv
Hình 22: Lệnh đọc tệp users.csv
Hình 23: Kết quả đọc tệp users.csv
• user_watches.csv 
Hình 24: Lệnh đọc tệp user_watches.csv
41
Hình 25: Kết quả đọc tệp user_watches.csv
❖ Kích thước tệp
• animes.csv 
Hình 26: Lệnh xác định kích thước của tệp animes.csv
Hình 27: Kết quả kích thước của tệp animes.csv
• users.csv
Hình 28: Lệnh xác định kích thước của tệp users.csv
Hình 29: Kết quả kích thước của tệp users.csv
42
• user_watches.csv
Hình 30: Lệnh xác định kích thước của tệp user_watches.csv
Hình 31: Kết quả kích thước của tệp user_watches.csv
❖ Thống kê
• animes.csv 
Hình 32: Lệnh thống kê số cơ bản của tệp animes.csv làm tròn đến chữ số thập phân 
thứ 2
Hình 33: Kết quả thống kê số cơ bản của tệp animes.csv
• users.csv
Hình 34: Lệnh thống kê số cơ bản của tệp users.csv làm tròn đến chữ số thập phân thứ
2
43
Hình 35: Kết quả thống kê số cơ bản của tệp users.csv
• user_watches.csv
Hình 36 : Lệnh thống kê số cơ bản của tệp user_watches.csv làm tròn đến chữ số thập 
phân thứ 2
Hình 37: Kết quả thống kê số cơ bản của tệp user_watches.csv
1.3. Choosing model ( Chọn mô hình)
Mô hình đề tài nghiên cứu được giới thiệu tại mục 2.3. Tổng quan phương pháp 
nghiên cứu.
44
Value_count() trả về đối tượng chứa số lượng giá trị duy nhất. Ở đây có thể xác 
định được người dùng đã xếp hạng cho bao nhiêu phim hoạt hình, ví dụ cho user_id 
4053169 đã xếp hạng cho 17058 phim hoạt hình và user_id 323300 đã xếp hạng cho 1 
phim hoạt hình.
Hình 38: Lệnh Value_count()
Hình 39: Kết quả Value_count()
Kích thước Value_count() của cột user_id trong user_watches.csv.
Hình 40: Lệnh xác định kích thước Value_count() của cột user_id trong 
user_watches.csv
Hình 41: Kết quả kích thước Value_count() của cột user_id trong user_watches.csv
Kiểm tra giá trị duy nhất của cột user_id trong user_watches.csv.
45
Hình 42: Lệnh xác kích thước unique() của cột user_id trong user_watches.csv
Hình 43: Kết quả kích thước unique() của cột user_id trong user_watches.csv
Lọc để loại các giá trị nhỏ hơn 1000. Tiến hành lọc bỏ đi các user_id của người 
dùng đã xếp hạng cho ít hơn 10000 phim hoạt hình nhằm tăng độ tin cậy cho dữ liệu.
Hình 44: Lệnh lọc các giá trị lớn hơn 1000
Và kết quả lọc có 8840 user_id đã xếp hạng cho hơn 1000 phim hoạt hình.
Hình 45: Kết quả lọc
Tìm user_id của người dùng.
Hình 46: Lệnh tìm user_id của người dùng
Hình 47: Kết quả user_id của người dùng
Sắp xếp các xếp hạng và chuyển lại xếp hạng theo user_id.
Hình 48: Lệnh sắp xếp các xếp hạng theo user_id và trình bày 10 dòng đầu tiên
46
Hình 49: Kết quả sắp xếp các xếp hạng theo user_id
Kích thước của sắp xếp các xếp hạng theo user_id.
Hình 50: Lệnh xác định kích thước các xếp hạng theo user_id
Hình 51: Kết quả kích thước các xếp hạng theo user_id
Gộp tệp “animes.csv” và “user_watches.csv” theo cột anime_id.
Hình 52: Lệnh gộp và trình bày 10 dòng đầu tiên
47
Hình 53: Kết quả gộp
Kích thước sau khi gộp.
Hình 54: Lệnh xác định kích thước sau khi gộp
Hình 55:Kết quả kích thước sau khi gộp
Nhóm cột title và score. Số lượng các xếp hạng của phim hoạt hình.
Hình 56: Lệnh nhóm cột title và score
Hình 57: Kết quả nhóm cột title và score
48
Thay đổi tên cột score thành num_of_score.
Hình 58: Lệnh đổi tên cột score thành num_of_score
Hình 59: Kết quả đổi tên
Hợp nhất các cột theo cột title.
Hình 60: Lệnh gộp và trình bày 5 dòng đầu tiên
Hình 61: Kết quả gộp
Kích thước sau khi gộp.
Hình 62: Lệnh xác định kích thước sau khi gộp
49
Hình 63: Kết quả sau khi gộp
Lọc loại bỏ các phim hoạt hình có nhỏ hơn hoặc bằng 50 xếp hạng.
Hình 64: Lệnh lọc các phim hoạt hình có hơn 50 xếp hạng 
Hình 65: Kết quả các phim hoạt hình có hơn 50 xếp hạng
Kích thước sau khi lọc.
Hình 66: Lệnh xác định kích thước sau khi lọc
Hình 67: Kết quả sau khi lọc 
Tiêu đề của các cột.
Hình 68: Lệnh trả về các tiêu đề của các cột
Hình 69: Kết quả các tiêu đề cột
Điều chỉnh và loại bỏ một số cột không dùng.
50
Hình 70: Lệnh điều chỉnh cột
Hình 71: Kết quả điều chỉnh cột
Loại bỏ các giá trị trùng lặp ở cột user_id và title.
Hình 72: Lệnh loại bỏ các giá trị trùng lặp
Kích thước sau khi loại bỏ.
Hình 73: Lệnh xác định kích thước sau khi loại bỏ trùng lặp
Hình 74: Kết quả kích thước sau khi loại bỏ trùng lặp
PivotTable
Utility Matrix:
User_id
Title
36 228 540 ...
Aria the Avvenire 6 1 8 ...
Deca-Dence 6 0 NaN ...
51
11eyes: Momoiro Genmutan 6 10 6 ...
Cowboy Bebop 9 9 10 ...
... ... ... ... ...
Sử dụng PivotTable để nhanh chóng tóm tắt dữ liệu lớn. Ở đây việc xây dựng 
Utility Matrix là quan trọng để tập hợp tất cả điểm gồm các giá trị đã biết và chưa biết 
cần được dự đoán. Liệu người dùng 540 có thích “Deca-Dence” không? Dựa vào sự
tương đồng về xếp hạng điểm số của người dùng 540 với người dùng 36 về phim hoạt 
hình “11eyes: Momoiro Genmutan” là 6. Nếu đề xuất “Deca-Dence” thì điểm có thể là 
bao nhiêu? Mô hình sự phân cụm, một số người dùng có xếp hạng tương đồng cho một 
số phim hoạt hình có thể có sở thích hoặc hành vi tương đồng nhau. Có dự đoán xếp 
hạng điểm số của người dùng 540 cho phim hoạt hình “Deca-Dence”.
Tạo một bảng tổng hợp với các cột user_id, title và score để xây dựng ma trận.
Hình 75: Lệnh tạo ma trận
Hình 76: Kết quả tạo ma trận
Kiểm tra lại kích thước của ma trận.
Hình 77: Lệnh xác định kích thước ma trận
52
Hình 78: Kết quả kích thước ma trận
Thay thế các giá trị NaN thành 0 để mô hình có thể tính toán khoảng cách giữa 
các cột.
Hình 79: Lệnh chuyển đổi NaN thành 0
Hình 80: Kết quả chuyển đổi
Sử dụng csr_matrix hàng thưa thớt được nén để cắt hàng nhanh, sản phẩm 
vector ma trận nhanh hơn. 
Hình 81: Lệnh tạo hàng không gian nén
Hình 82: Lệnh kiểm tra loại kiểu nén
53
Hình 83: Kết quả loại kiểu nén
Xây dựng thuật toán KNN.
Hình 84: Lệnh gọi thuật toán
Hình 85: Lệnh truyền hàng không gian nén
Hình 86: Kết quả lệnh gọi thuật toán KNN
1.4. Tuning Parameter (Điều chỉnh thông số)
Khởi tạo biến distance và suggestion. Xây dựng mô hình có chức năng tìm KNN 
và k =11 với giá trị trả về là 10 kết quả khoảng cách và đề xuất cho mục chỉ định là 
anime_id là 30. 
Hình 87: Lệnh xây dựng mô hình
Khoảng cách 10 anime_id gần nhất với anime_id 30.
Hình 88: Lệnh gọi biến distance
54
Hình 89: Kết quả biến distance
Đề xuất 10 anime_id cho kết quả tìm kiếm với anime_id 30.
Hình 90: Lệnh gọi suggestion
Hình 91: Kết quả biến suggestion
Lọc điểm xếp hạng (trên thang điểm 10) của user_id dành cho anime_id 1.
Hình 92: Lệnh lọc điểm xếp hạng của user_id dành cho anime_id 1
Hình 93: Kết quả lọc điểm xếp hạng của user_id dành cho anime_id 1
Trình bày 10 đề xuất trên theo cột title.
Hình 94: Lệnh đề xuất tên phim hoạt hình
55
Hình 95: Kết quả đề xuất tên phim hoạt hình
Gọi tên sách thông qua anime_id. Thử với anime_id là 100.
Hình 96: Lệnh gọi tên phim hoạt hình
Hình 97: Kết quả gọi tên phim hoạt hình
Hình 98: Lệnh tạo biến tên phim hoạt hình
Hình 99: Lệnh gọi biến tên phim hoạt hình
Hình 100: Kết quả gọi biến tên phim hoạt hình
Gọi ngược lại từ title thì anime_id ở đâu.
Hình 101: Lệnh gọi anime_id bằng title
56
Hình 102: Kết quả anime_id trả về
Hình 103: Lệnh tạo biến gọi anime_id bằng title
❖ Tìm ảnh phim hoạt hình
Hình 104: Lệnh gọi đường dẫn ảnh phim hoạt hình
Hình 105: Kết quả đường dẫn ảnh phim hoạt hình
Hình 106: Lệnh đề xuất tên phim hoạt hình
Hình 107: Lệnh gọi anime_id bằng title
57
Hình 108: Lệnh gọi đường dẫn ảnh phim hoạt hình
Hình 109: Kết quả gọi đường dẫn ảnh phim hoạt hình
❖ Hàm đề xuất
Hình 110: Lệnh tạo hàm đề xuất
1.5. Making Prediction ( Đưa ra đề xuất)
❖ Đề xuất thử
Hình 111: Lệnh đề xuất cho “ Aria the Avvenire”
58
Hình 112: Kết quả đề xuất cho “ Aria the Avvenire”
Hình 113: Lệnh đề xuất cho “ Hanasaku Iroha”
Hình 114: Kết quả đề xuất cho “ Hanasaku Iroha”
Hình 115: Lệnh đề xuất cho “ Minami-ke”
59
Hình 116: Kết quả đề xuất cho “ Minami-ke”
❖ Xuất các tệp với định dạng .pkl
Hình 117: Lệnh xuất mô hình
2. Design ( Thiết kế)
Tạo một thư mục trống ngoài desktop đặt tên là “08032024”.
Hình 118: Tạo thư mục mới
Tiếp tục tạo một thư mục có tên là “interface” chứa 4 tệp .pkl vừa xuất.
Hình 119: Tạo thư mục “interface”
60
Hình 120: Mở thư mục “08032024”
Tải tệp “MyAnimeList.ipynb” từ Jupyter Notebook vào thư mục “08032024”.
Tải tệp “MyAnimeList.py” từ Jupyter Notebook vào thư mục “08032024”.
Tải thêm 4 tệp của bộ dữ liệu MyAnimeList gồm “animes.csv”, “users.csv”, 
“user_watches.csv” và “mal_db.dump” vào thư mục “08032024”.
Tạo thêm một tệp “app.py” và một hình ảnh để là chèn trang trí.
Kết quả: 
Hình 121: Mở thư mục “08032024” 
61
Mở phần mềm Visual Studio Code. Mở thư mục “08032024”.
Hình 122: Mở phần mềm Visual Studio Code
2.1. Web design ( Thiết kế Web)
Mở tệp “app.py”
❖ Chuẩn bị thư viện
Hình 123: Mở tệp “app.py”
Hình 124: Lệnh thiết lập tiêu đề trang
62
Hình 125: Kết quả thiết lập tiêu đề
Hình 126: Lệnh chèn ảnh
Hình 127: Kết quả chèn ảnh
Hình 128: Lệnh tạo tiêu đề web-app và gọi tệp chứa mô hình
Hình 129: Kết quả tiêu đề web-app
2.2. Fuction design ( Thiết kế chức năng)
63
Hình 130: Lệnh đề xuất ảnh phim hoạt hình
Hình 131: Lệnh đề xuất tên phim hoạt hình
Hình 132: Lệnh thiết lập thanh tìm kiếm
64
Hình 133: Kết quả thanh tìm kiếm
65
Hình 134: Lệnh thiết lập chức năng trình bày kết quả đề xuất
Hình 135: Giao diện đề xuất cho từ khóa “ Doraemon”
❖ Chạy “app.py”
Trên thanh công cụ tìm Terminal chọn New Terminal hoặc nhấn tổ hợp phím 
Ctrl+Shift+`.
66
Hình136: Tìm cửa sổ lệnh Terminal 
Tại cửa sổ lệnh “Terminal” gõ “streamlit run app.py” và nhấn phím “Enter”.
Hình137: Lệnh chạy trên cửa sổ Terminal
## By Nguyễn Thị Huỳnh Như
## Date: 25/07/2024
## Mail: 20166050@st.hcmuaf.edu.vn / nguyenthihuynhnhu271025@gmail.co
