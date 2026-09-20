class Video:
    def __init__(self, stream):
        self.stream = stream
        self.likes = 0
        self.dislikes = 0
        self.views = 0

class VideoSharingPlatform:

    def __init__(self):
        self.videoMap = {}
        self.delHeap = []
        self.curId = 0

    def upload(self, video: str) -> int:
        curId = -1
        if self.delHeap:
            curId = heapq.heappop(self.delHeap)
        else:
            curId = self.curId
            self.curId += 1
        self.videoMap[curId] = Video(video)
        return curId

    def remove(self, videoId: int) -> None:
        if videoId in self.videoMap:
            del self.videoMap[videoId]
            heapq.heappush(self.delHeap, videoId)

    def watch(self, videoId: int, startMinute: int, endMinute: int) -> str:
        if videoId in self.videoMap:
            video = self.videoMap[videoId]
            stream = video.stream
            startMin, endMin = startMinute, min(len(stream), endMinute + 1)
            video.views += 1
            return stream[startMin:endMin]
        return "-1"

    def like(self, videoId: int) -> None:
        if videoId in self.videoMap:
            video = self.videoMap[videoId]
            video.likes += 1

    def dislike(self, videoId: int) -> None:
        if videoId in self.videoMap:
            video = self.videoMap[videoId]
            video.dislikes += 1

    def getLikesAndDislikes(self, videoId: int) -> List[int]:
        if videoId in self.videoMap:
            video = self.videoMap[videoId]
            return [video.likes, video.dislikes]
        return [-1]

    def getViews(self, videoId: int) -> int:
        if videoId in self.videoMap:
            video = self.videoMap[videoId]
            return video.views
        return -1


# Your VideoSharingPlatform object will be instantiated and called as such:
# obj = VideoSharingPlatform()
# param_1 = obj.upload(video)
# obj.remove(videoId)
# param_3 = obj.watch(videoId,startMinute,endMinute)
# obj.like(videoId)
# obj.dislike(videoId)
# param_6 = obj.getLikesAndDislikes(videoId)
# param_7 = obj.getViews(videoId)