class Weed :
    count = 0
    # {key : ID , value : [confidence , last_timestamp , bb =[] , features]}
    weeds = {}
    def __init__(self, id , confidence , last_timestamp ,bounding_box = None, features=None) :
        self.id = Weed.count 
        self.confidence = confidence
        self.last_timestamp = last_timestamp
        self.bounding_box = bounding_box if bounding_box is not None else []
        self.features = features if features is not None else []

    # also Improve the clustering of the bounding boxes

    def getDetails(self,results,frame):
        for box in results[0].boxes :
        # Get ID
            # if not in the list 
            Weed.count+=1
        # Get BB
            x1 ,y1 ,x2 ,y2 = box.xyxy[0]
            x1 , y1 , x2 ,y2 = map(int , [x1 ,y1 ,x2 ,y2])
            x , y , w , h = box.xywh[0]
            x , y , w , h = map(int , [x,y,w,h])
            # add the features with ID to dictionary

        # Get Features
            roi = frame[y1:y2, x1:x2]
            if roi.size == 0:
                continue



        # Get confidence
        conf = box.conf


        # Get last Timestamps
        
        pass

    def getfeatures(self):
        pass

    

    def trackFeatures(self):
        pass

    def validateBB(self):
        pass