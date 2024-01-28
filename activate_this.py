import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Import dữ liệu vô với biến là df
df = pd.read_csv('ecommerce_customer_data_large.csv')

# Tiếp theo, chúng ta sẽ xem nhanh phần đầu của dữ liệu. Nó tương tự như việc lật qua vài trang đầu tiên của một cuốn sách để xem nó nói về cái gì. Chúng tôi muốn biết dữ liệu của mình trông như thế nào bằng cách hiển thị một số hàng đầu tiên

# Hiển thị một vài hàng đầu tiên của tập dữ liệu
df.head()

# Muốn biết những thứ như mức trung bình, phạm vi và các mẫu phổ biến. Vì vậy, ta sử dụng describe để tóm tắt các phần số của dữ liệu

# Nhận số liệu thống kê tóm tắt cơ bản
df.describe()

# **Tìm hiểu các ký tự:**
# Dữ liệu của chúng tôi có các loại thông tin khác nhau, như tên, danh mục và mô tả. Chúng tôi cũng quan tâm đến việc tìm hiểu những phần này. Nó giống như việc tìm ra các nhân vật trong một cuốn sách là ai. Vì vậy, chúng tôi đang tóm tắt các phần được phân loại trong dữ liệu của mình.
df.describe(include='O')

# **Kiểm tra các phần bị thiếu:**
# Nhận thông tin về kiểu dữ liệu và giá trị còn thiếu
df.info()

# Xóa các hàng trùng lặp
df.drop_duplicates(inplace=True)

# **Kiểm tra thông tin còn thiếu:**
# Kiểm tra các giá trị còn thiếu
missing_values = df.isnull().sum()
print("Thiếu giá trị:", missing_values)

# **Xử lý thông tin 'Returns' bị thiếu**
# Thay thế các giá trị 'Trả về' bị thiếu bằng một giá trị mặc định phù hợp, ví dụ: 0 nếu không trả về
default_return_value = 0
df['Returns'].fillna(default_return_value, inplace=True)

df.isnull().sum()

# Chuyển 'Purchase Date' sang định dạng ngày giờ
df['Purchase Date'] = pd.to_datetime(df['Purchase Date'])

# Trích xuất năm và tháng từ 'Purchase Date'
df['Purchase Year'] = df['Purchase Date'].dt.year
df['Purchase Month'] = df['Purchase Date'].dt.month

# **Tính giá từng giao dịch**
# Chúng tôi đang tính 'Tổng số tiền mua' cho mỗi giao dịch. Nó giống như tính tổng chi phí của tất cả các mặt hàng được mua trong xe đẩy hàng.

# Tính 'Tổng số tiền mua' trên mỗi giao dịch
df['Total Purchase Amount'] = df['Product Price'] * df['Quantity']

# **DỌN DẸP**
# Bỏ các cột không cần thiết
df.drop(['Payment Method'], axis=1, inplace=True)
df.drop(['Customer Name'], axis=1, inplace=True)
df.drop(['Age'], axis=1, inplace=True)
df.drop(['Returns'], axis=1, inplace=True)

df.head(10)

# **LƯU LẠI FILE MỚI**
# Lưu dữ liệu đã được làm sạch và thao tác vào tệp CSV mới
df.to_csv('cleaned_ecommerce_data.csv', index=False)

# **ĐỌC DỮ LIỆU ĐÃ LÀM SẠCH**
df = pd.read_csv('cleaned_ecommerce_data.csv')

# **XỬ LÝ NGÀY THÁNG**
# Bạn đã lấy cột 'Ngày mua' và chuyển nó sang định dạng ngày giờ. Điều này giống như dịch một phần câu chuyện sang ngôn ngữ mà bạn có thể hiểu rõ hơn. Giờ đây, bạn có thể dễ dàng làm việc với ngày và giờ.

df['Purchase Date'] = pd.to_datetime(df['Purchase Date'])

# **TÌM HIỂU DỮ LIỆU ĐÃ LÀM SẠCH**
# Giống như việc bạn xem xét một cuốn sách để hiểu cấu trúc của nó, bạn đang sử dụng mã để tìm hiểu thêm về tập dữ liệu của mình. Phương thức info() cung cấp một bản tóm tắt, hiển thị cho bạn các kiểu dữ liệu và sự hiện diện của các giá trị bị thiếu. Phương thức mô tả() cung cấp cho bạn các số liệu thống kê như giá trị trung bình, độ lệch chuẩn, giá trị tối thiểu và tối đa cho các cột số. Khi bạn sử dụng mô tả (bao gồm = 'tất cả'), bạn sẽ nhận được thông tin về cả cột số và phi số (phân loại).

df.info()

df.describe()

df.describe(include='O')

# Vì vậy, trong phần này, bạn đã mở tập dữ liệu đã được làm sạch, làm cho ngày tháng dễ đọc hơn và hiểu sâu hơn về dữ liệu của mình. Điều này tương tự như việc đọc lại một cuốn sách để làm mới trí nhớ của bạn về nội dung của nó trước khi tiếp tục câu chuyện.
# **Phân loại khách hàng theo độ tuổi**
# Bạn đang chia khách hàng của mình thành các nhóm tuổi, tạo các nhóm từ 0 đến 10, 11 đến 20, v.v. Điều này tương tự như việc nhóm các nhân vật trong sách theo độ tuổi hoặc đặc điểm của họ, giúp bạn hiểu được các khía cạnh khác nhau của câu chuyện.

# Xác định độ tuổi
age_ranges = [0, 10, 20, 30, 40, 50, 60, np.inf]
age_labels = ['0-10', '11-20', '21-30', '31-40', '41-50', '51-60', '60+']

# Phân loại khách hàng theo nhóm tuổi
df['Age Group'] = pd.cut(df['Customer Age'], bins=age_ranges, labels=age_labels)

# Hình dung sự phân bố theo độ tuổi của khách hàng
# Để hiểu rõ hơn về sự phân bố độ tuổi của khách hàng, bạn đang sử dụng biểu đồ bar. Điều này giống như việc tạo một bản trình bày trực quan về hồ sơ nhân vật trong câu chuyện của bạn, cho thấy có bao nhiêu nhân vật thuộc các nhóm tuổi khác nhau.

# Trực quan hóa phân bổ độ tuổi của khách hàng dưới dạng barplot
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='Age Group', order=age_labels)
plt.title('Customer Age Distribution')
plt.xlabel('Age Group')
plt.ylabel('Count')
plt.show()

# **Phân tích phân bổ giới tính**
# Bạn đang xác định sự phân bổ giới tính giữa các khách hàng của mình. Điều này giống như việc hiểu được sự cân bằng giữa các nhân vật nam và nữ trong câu chuyện của bạn.

# Tính toán phân bổ giới tính
gender_distribution = df['Gender'].value_counts()

# **Hình dung sự phân bổ giới tính**
# Bạn đang sử dụng biểu đồ hình tròn để thể hiện sự phân bổ giới tính một cách trực quan. Đây là một cách để thể hiện tỷ lệ các loại nhân vật khác nhau trong câu chuyện của bạn.

# Tạo biểu đồ hình tròn để phân bổ giới tính
plt.figure(figsize=(6, 6))
plt.pie(gender_distribution, labels=gender_distribution.index, autopct='%1.1f%%', startangle=140)
plt.title('Gender Distribution')
plt.show()

# **Tính tổng doanh thu**
# Bạn đang tìm tổng của cột 'Tổng số tiền mua'. Hãy coi điều này như tính toán tổng thu nhập hoặc chi tiêu trong câu chuyện của bạn.

# Tính tổng doanh thu
total_revenue = df['Total Purchase Amount'].sum()
print(f'Total Revenue: ${total_revenue:.2f}')
# Các bước này giúp bạn có được bức tranh rõ ràng hơn về nhân khẩu học của khách hàng và tác động của họ đến hiệu quả tài chính của doanh nghiệp bạn, cũng như việc hiểu các nhân vật và đặc điểm của họ có thể cung cấp thông tin chi tiết sâu hơn về cốt truyện và động lực của câu chuyện.

# **PHÂN KHÚC KHÁCH HÀNG**
# **Phân khúc dựa trên tổng số tiền mua**
# Bạn đang phân loại khách hàng thành ba phân khúc: Giá trị thấp, Giá trị trung bình và Giá trị cao dựa trên tổng số tiền mua hàng của họ. Điều này giúp bạn hiểu khách hàng nào đóng góp nhiều nhất vào doanh thu của bạn. Hình ảnh trực quan giúp bạn hiểu rõ hơn.

# Phân khúc khách hàng theo tổng số tiền mua hàng
# Xác định ngưỡng để phân đoạn
low_value_threshold = 700
high_value_threshold = 1500


# Tạo hàm phân loại khách hàng theo tổng số tiền mua hàng
def categorize_customers(total_purchase_amount):
    if total_purchase_amount <= low_value_threshold:
        return "Low-Value"
    elif total_purchase_amount <= high_value_threshold:
        return "Mid-Value"
    else:
        return "High-Value"


# Áp dụng chức năng phân loại để tạo cột mới 'Phân khúc khách hàng'
df['Customer Segment'] = df['Total Purchase Amount'].apply(categorize_customers)

# In số lượng khách hàng theo từng phân khúc
segment_counts = df['Customer Segment'].value_counts()
print(segment_counts)

plt.figure(figsize=(6, 6))
plt.pie(segment_counts, labels=segment_counts.index, autopct='%1.1f%%', startangle=90)
plt.title('Segmentation Based on Total Purchase Amount')
plt.show()

# **PHÂN TÍCH DANH MỤC SẢN PHẨM**
# Trong Phân tích danh mục sản phẩm, chúng tôi đi sâu vào thế giới sản phẩm của mình
# **Phân phối danh mục sản phẩm:**
# Đầu tiên chúng tôi xem xét danh mục sản phẩm nào phổ biến. Biểu đồ đường của chúng tôi cho chúng tôi thấy rằng một số danh mục có nhu cầu nhiều hơn những danh mục khác. Chúng tôi thậm chí còn đánh dấu số lượng sản phẩm trong từng danh mục trên các dòng cho rõ ràng.

# Tính toán phân bổ danh mục sản phẩm
product_category_distribution = df['Product Category'].value_counts().reset_index()
product_category_distribution.columns = ['Product Category', 'Count']

# Sắp xếp dữ liệu theo thứ tự giảm dần
product_category_distribution = product_category_distribution.sort_values(by='Count', ascending=False)
print(product_category_distribution)

# Tạo biểu đồ đường có số điểm đếm
plt.figure(figsize=(11, 6))
sns.lineplot(data=product_category_distribution, x='Count', y='Product Category', marker='o')
plt.title('Product Category Distribution')
plt.xlabel('Count')
plt.ylabel('Product Category')
plt.grid(True, linestyle='--', alpha=0.6)

# Thêm chú thích đếm trên các dòng
for index, row in product_category_distribution.iterrows():
    plt.text(row['Count'] + 5, index, f'{row["Count"]}', va='center', fontsize=10)

plt.show()

# **Tổng doanh số theo danh mục sản phẩm**
# Tiếp theo, chúng tôi xác định danh mục sản phẩm nào mang lại nhiều doanh thu nhất. Biểu đồ bar hiển thị tổng số tiền mua hàng và chúng tôi đã sử dụng thang đo log để xử lý nhiều loại doanh số bán hàng. Điều này cho phép chúng tôi thấy rõ sự phân bổ doanh thu.

# Tính tổng doanh số theo danh mục sản phẩm
product_category_sales = df.groupby('Product Category')['Total Purchase Amount'].sum().reset_index()
product_category_sales = product_category_sales.sort_values(by='Total Purchase Amount', ascending=False)
print(product_category_sales)

# Tạo biểu đồ cột dọc cho tổng doanh số bán hàng theo danh mục sản phẩm với độ rộng thanh được điều chỉnh và tỷ lệ log trên trục y
plt.figure(figsize=(10, 7))
ax = sns.barplot(data=product_category_sales, x='Product Category', y='Total Purchase Amount', palette='viridis', errcolor=None, width=0.5)
plt.title('Total Sales by Product Category (Log Scale)')
plt.xlabel('Product Category')
plt.ylabel('Total Purchase Amount (Log Scale)')

# Đặt thang đo log trên trục y
ax.set_yscale('log')

plt.xticks()
plt.tight_layout()
plt.show()

# **Phân phối doanh thu danh mục sản phẩm**
# Để làm cho nó dễ hiểu hơn, chúng tôi đã tạo một biểu đồ hình tròn. Nó thể hiện một cách trực quan sự phân bổ doanh thu trên các danh mục sản phẩm của chúng tôi.

# Tạo biểu đồ hình tròn
plt.figure(figsize=(8, 8))
plt.pie(product_category_sales['Total Purchase Amount'], labels=product_category_sales['Product Category'],
        autopct='%1.1f%%', startangle=75)

# Thêm tiêu đề
plt.title('Product Category Revenue Distribution')

# Hiển thị biểu đồ
plt.show()

# *Phân phối danh mục sản phẩm:*
# * Điện tử: 62.630 sản phẩm
# * Quần áo: 62.581 sản phẩm
# * Trang chủ: 62.542 sản phẩm
# * Sách: 62.247 sản phẩm

# *Tổng doanh số theo danh mục sản phẩm:*
# * Điện tử: 48.130.856 đô la
# * Quần áo: 47.977.746 Đô la
# * Nhà: 47.801.925 Đô la
# * Sách: 47.578.138 Đô la

# Từ những số liệu này, có thể thấy rõ sản phẩm “Home” không chỉ có số lượng nhiều nhất mà còn là sản phẩm đóng góp doanh thu nhiều nhất. "Quần áo" và "Điện tử" theo sát nhau với số liệu doanh thu tương tự. "Sách" cũng hoạt động tốt nhưng có doanh số thấp hơn một chút so với các danh mục khác.
# Bảng phân tích chi tiết này giúp chúng tôi hiểu được bối cảnh sản phẩm, cho phép chúng tôi tập trung nỗ lực tiếp thị và kiểm kê một cách hiệu quả. Nó không chỉ là về những gì phổ biến; đó cũng là về những gì mang lại lợi nhuận.
