#include <opencv2/opencv.hpp>

int main() {
    int h = 300, w = 400;
    cv::Mat img(h, w, CV_8UC3);

    for (int y = 0; y < h; ++y)
        for (int x = 0; x < w; ++x)
            img.at<cv::Vec3b>(y, x) = cv::Vec3b(x % 256, y % 256, (x + y) % 256);

    cv::imwrite("gradient_cpp.png", img);
    return 0;
}