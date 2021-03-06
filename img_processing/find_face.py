import cv2
import mediapipe as mp



class FaceDetection:
    def __init__(self, i, pg):
        super().__init__()
        self.xmin = float()
        self.ymin = float()
        self.width = float()
        self.height = float()

        self.x = float()
        self.y = float()
        self.z = float()

        self.cnt = 0
        self.pg = pg    #progress bar

        self.faces = list() #3d array
        self.oneface = list()   #2d array

        ###########
        self.cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        self.cam.set(3, 1080)
        self.cam.set(4, 720)

        if i == 0:
            self.detect_both()
        elif i == 1:
            self.detect_roi()
        elif i == 2:
            self.detect_mesh()
        elif i == 3:
            self.detect_both1()
        else:
            pass


    def detect_both(self):
        self.mpFaceDetection = mp.solutions.face_detection
        self.mpDraw = mp.solutions.drawing_utils
        self.faceDetection = self.mpFaceDetection.FaceDetection()

        self.mpFaceMesh = mp.solutions.face_mesh
        self.mpDraw = mp.solutions.drawing_utils
        self.faceMesh = self.mpFaceMesh.FaceMesh(max_num_faces=2)

        while True:
            success, img = self.cam.read()
            imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            roi_results = self.faceDetection.process(imgRGB)
            mesh_results = self.faceMesh.process(imgRGB)


            if (roi_results.detections):
                if(mesh_results.multi_face_landmarks):

                    if ((len(roi_results.detections) == 1) & (len(mesh_results.multi_face_landmarks) == 1)):

                        self.cnt += 1
                        self.pg.setValue(self.cnt)

                        for detection in roi_results.detections:
                            bboxC = detection.location_data.relative_bounding_box
                            self.xmin = bboxC.xmin
                            self.ymin = bboxC.ymin
                            self.width = bboxC.width
                            self.height = bboxC.height

                        for faceLMS in mesh_results.multi_face_landmarks:
                            full_mesh = list()
                            for lm in faceLMS.landmark:
                                # img relative point
                                x = lm.x
                                y = lm.y
                                z = lm.z

                                # face relative point
                                rel_x = x - self.xmin
                                rel_y = y - self.ymin
                                rel_z = z

                                # normalize point
                                normal_x = rel_x / self.width
                                normal_y = rel_y / self.height
                                normal_z = rel_z / self.width   #use width
                                normal_list = [normal_x, normal_y, normal_z]
                                full_mesh.append(normal_list)   #1 face

                            self.faces.append(full_mesh)    # faces, 3d list


            if self.cnt == 50:  #how many faces
                break
            #cv2.imshow("vid", img)
                                #save

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        #########################################################

    def detect_both1(self):
        self.mpFaceDetection = mp.solutions.face_detection
        self.mpDraw = mp.solutions.drawing_utils
        self.faceDetection = self.mpFaceDetection.FaceDetection()

        self.pg.setValue(30)

        self.mpFaceMesh = mp.solutions.face_mesh
        self.mpDraw = mp.solutions.drawing_utils
        self.faceMesh = self.mpFaceMesh.FaceMesh(max_num_faces=2)

        self.pg.setValue(40)

        while True:
            success, img = self.cam.read()
            imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            roi_results = self.faceDetection.process(imgRGB)
            mesh_results = self.faceMesh.process(imgRGB)


            if (roi_results.detections):
                if(mesh_results.multi_face_landmarks):

                    if ((len(roi_results.detections) == 1) & (len(mesh_results.multi_face_landmarks) == 1)):

                        self.cnt += 1
                        self.pg.setValue(50)

                        for detection in roi_results.detections:
                            bboxC = detection.location_data.relative_bounding_box
                            self.xmin = bboxC.xmin
                            self.ymin = bboxC.ymin
                            self.width = bboxC.width
                            self.height = bboxC.height

                        self.pg.setValue(60)

                        for faceLMS in mesh_results.multi_face_landmarks:
                            full_mesh = list()
                            for lm in faceLMS.landmark:
                                # img relative point
                                x = lm.x
                                y = lm.y
                                z = lm.z

                                # face relative point
                                rel_x = x - self.xmin
                                rel_y = y - self.ymin
                                rel_z = z

                                # normalize point
                                normal_x = rel_x / self.width
                                normal_y = rel_y / self.height
                                normal_z = rel_z / self.width   #use width
                                normal_list = [normal_x, normal_y, normal_z]
                                full_mesh.append(normal_list)   #1 face
                                self.oneface = full_mesh

                        self.pg.setValue(90)

            if self.cnt >= 1:  #how many faces
                self.cnt = 0
                break
            #cv2.imshow("vid", img)
                                #save

            if cv2.waitKey(1) & 0xFF == ord('q'):
                self.cnt = 0
                break


    def detect_roi(self):
        self.mpFaceDetection = mp.solutions.face_detection
        self.mpDraw = mp.solutions.drawing_utils
        self.faceDetection = self.mpFaceDetection.FaceDetection()

        while True:
            success, img = self.cam.read()
            imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            roi_results = self.faceDetection.process(imgRGB)
            if roi_results.detections:
                for detection in roi_results.detections:
                    self.mpDraw.draw_detection(img, detection)
            cv2.imshow("vid", img)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break


    def detect_mesh(self):
        self.mpFaceMesh = mp.solutions.face_mesh
        self.mpDraw = mp.solutions.drawing_utils
        self.faceMesh = self.mpFaceMesh.FaceMesh(max_num_faces=2)

        while True:
            success, img = self.cam.read()
            imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            break



if __name__ == '__main__':
    fd = FaceDetection(1, 0)
