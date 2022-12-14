# Measure the distance
#
# This example shows off how to measure the distance through the size in imgage
# This example in particular looks for yellow pingpong ball.

import sensor, image, time

# For color tracking to work really well you should ideally be in a very, very,
# very, controlled enviroment where the lighting is constant...
pink_threshold   =(38, 60, 18, 55, -20, 11) #设置测距识别的色块颜色阈值，更换色块时需要重设
# You may need to tweak the above settings for tracking green things...
# Select an area in the Framebuffer to copy the color settings.

sensor.reset() # Initialize the camera sensor.
sensor.set_pixformat(sensor.RGB565) # use RGB565.
sensor.set_framesize(sensor.QQVGA) # use QQVGA for speed.
sensor.skip_frames(10) # Let new settings take affect.
sensor.set_auto_whitebal(False) # turn this off.
clock = time.clock() # Tracks FPS.

K=685#the value should be measured:该系数与识别的色块大小有关，故更换色块之后也需重新测量，根据length = k/Bpix，用该K值运行程序时print的length与实际测量的length比较，按比例进行修改即可

while(True):
    clock.tick() # Track elapsed milliseconds between snapshots().
    img = sensor.snapshot() # Take a picture and return the image.

    blobs = img.find_blobs([pink_threshold])  #返回识别到的色块对象的索引，注意参数要填的是一个元素为元组的列表
    if len(blobs) == 1:
        # Draw a rect around the blob.
        b = blobs[0]    #blobs[0]表示识别到的第一个色块对象
        img.draw_rectangle(b[0:4]) # rect
        img.draw_cross(b[5], b[6]) # cx, cy
        Bpix = (b[2]+b[3])/2  #b[2]、b[3]是框的长宽像素，该程序识别的物体是球，球的长宽大致相等，该式取平均值，获取球的直径像素
        length = K/Bpix #要理解时该式时可再次查看官方教程中的解析
        print(length)

    #print(clock.fps()) # Note: Your OpenMV Cam runs about half as fast while
    # connected to your computer. The FPS should increase once disconnected.
