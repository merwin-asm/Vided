"""
Vided 1.0.0
Vided is a small module to do video related things slow , fast and reverse...
Author : Merwin
"""

import cv2

class Vided:
    def __init__(self):
        pass
    def save_frames(self,file_name,frames,size):
        saver = cv2.VideoWriter(file_name,
                                 cv2.VideoWriter_fourcc(*'MJPG'),
                                 10, size)
        for e in frames:
            saver.write(e)
        saver.release()
    def inverse_list(self,frames):
        new_frames = []
        len_ = len(frames)
        for e in range(0, len_):
            new_frames.append(frames[-1 * e])
        return new_frames
    def reverse(self,file_name,output):
        vid_frames = []
        vid = cv2.VideoCapture(file_name)
        frame_width = int(vid.get(3))
        frame_height = int(vid.get(4))
        size = (frame_width, frame_height)
        while (True):
            ret, frame = vid.read()
            if not ret:
                break
            else:
                vid_frames.append(frame)
        vid.release()
        vid_frames = self.inverse_list(vid_frames)
        self.save_frames(output,vid_frames,size)
    def slow(self,file_name,output,repeat):
        vid_frames = []
        vid = cv2.VideoCapture(file_name)
        frame_width = int(vid.get(3))
        frame_height = int(vid.get(4))
        size = (frame_width, frame_height)
        while (True):
            ret, frame = vid.read()
            if not ret:
                break
            else:
                for e in range(0,repeat):
                    vid_frames.append(frame)
        vid.release()
        self.save_frames(output, vid_frames, size)
    def fast(self,file_name,output,reduce):
        vid_frames = []
        vid = cv2.VideoCapture(file_name)
        frame_width = int(vid.get(3))
        frame_height = int(vid.get(4))
        size = (frame_width, frame_height)
        c = 0
        while (True):
            ret, frame = vid.read()
            if not ret:
                break
            else:
                if c == reduce:
                    vid_frames.append(frame)
                    c = 0
                else:
                    c+=1
        vid.release()
        self.save_frames(output, vid_frames, size)

if __name__ == '__main__':

    vid = Vided()

    # vid.reverse("test_video.mp4","out_1.mp4")

    # vid.slow("test_video.mp4","out_2.mp4",5)

    # vid.fast("test_video.mp4","out_3.mp4",5)
