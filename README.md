# Web_Recommender_System
NTHN_KLTN
# Procedure Artificial Intelligence

## By Nguyễn Thị Huỳnh Như
## Date: 25/07/2024
## Mail: 20166050@st.hcmuaf.edu.vn / nguyenthihuynhnhu271025@gmail.com

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

## By Nguyễn Thị Huỳnh Như
## Date: 25/07/2024
## Mail: 20166050@st.hcmuaf.edu.vn / nguyenthihuynhnhu271025@gmail.com
