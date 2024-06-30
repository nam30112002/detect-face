# Detect Face

![License](https://img.shields.io/github/license/nam30112002/detect-face) ![Issues](https://img.shields.io/github/issues/nam30112002/detect-face) ![Stars](https://img.shields.io/github/stars/nam30112002/detect-face) ![Forks](https://img.shields.io/github/forks/nam30112002/detect-face)

Detect Face là một dự án mã nguồn mở tập trung vào việc nhận diện và định danh khuôn mặt sử dụng các mô hình học sâu. Dự án này cung cấp một công cụ mạnh mẽ để phát hiện khuôn mặt trong hình ảnh và video, hỗ trợ nhiều ứng dụng trong lĩnh vực an ninh, y tế, và nhiều lĩnh vực khác.

## Tính Năng

- **Nhận diện khuôn mặt**: Phát hiện khuôn mặt trong hình ảnh và video một cách chính xác và hiệu quả.
- **Định danh khuôn mặt**: Xác định danh tính của khuôn mặt dựa trên một cơ sở dữ liệu có sẵn.
- **Hỗ trợ đa nền tảng**: Chạy được trên cả Windows, macOS và Linux.
- **API thân thiện**: Cung cấp API dễ sử dụng để tích hợp vào các ứng dụng khác.
- **Mở rộng dễ dàng**: Dễ dàng mở rộng và tùy chỉnh cho các nhu cầu cụ thể của bạn.

## Yêu Cầu Hệ Thống

- Python 3.7 hoặc mới hơn
- Các thư viện cần thiết (xem [requirements.txt](requirements.txt) để biết thêm chi tiết)

## Cài Đặt

1. **Clone repo**:
    ```bash
    git clone https://github.com/nam30112002/detect-face.git
    cd detect-face
    ```

2. **Cài đặt các thư viện cần thiết**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Chạy chương trình**:
    ```bash
    python detect_face.py
    ```

## Hướng Dẫn Sử Dụng

### Nhận Diện Khuôn Mặt Từ Hình Ảnh

Bạn có thể nhận diện khuôn mặt từ một hình ảnh bằng cách sử dụng lệnh sau:

```bash
python detect_face.py --image path/to/your/image.jpg
