import os
import shutil

import numpy as np
import cv2
import yaml
import torch
from yolov5_sp.models.experimental import attempt_load
from yolov5_sp.utils.general import check_img_size,non_max_suppression,scale_coords
from yolov5_sp.utils.datasets import letterbox


class YoloV5_Six:
    def __init__(self, model_dir):
        self.model_dir = model_dir
        self.__dict__ = self.parse_model_params(self.model_dir)
        cuda = torch.cuda.is_available()
        self.device = torch.device('cuda:0' if cuda else 'cpu')
        self.model = attempt_load(self.weights, map_location=self.device)
        stride = int(self.model.stride.max())  # model stride
        self.names = self.model.module.names if hasattr(self.model, 'module') else self.model.names  # get class names
        if self.half:
            self.model.half()  # to FP16
        self.imgsz = check_img_size(self.imgsz, s=stride)
    def parse_model_params(self, model_dir):
        yaml_file_path = os.path.join(model_dir, "opt.yaml")
        with open(yaml_file_path, "r", encoding="utf-8") as f:
            x = yaml.load(f, Loader=yaml.FullLoader)
        return x
    def infer(self, pred_img):
        img = letterbox(pred_img, new_shape=self.imgsz)[0]
        # 归一化与张量转换
        img = img[:, :, ::-1].transpose(2, 0, 1)  # BGR to RGB, to 3x416x416
        img = np.ascontiguousarray(img)
        img = torch.from_numpy(img).to(self.device)
        img = img.half() if self.half else img.float()  # uint8 to fp16/32
        img = img / 255.0  # 0 - 255 to 0.0 - 1.0
        if img.ndimension() == 3:
            img = img.unsqueeze(0)
        pred = self.model(img, augment=True)[0]
        # NMS
        pred = non_max_suppression(pred, self.conf_thres, self.iou_thres, classes=self.classes, agnostic=True, max_det=self.max_det)

        # 预测结果截留
        pred_res = []
        # 解析检测结果
        for i, det in enumerate(pred):  # detections per image
            # gn = torch.tensor(pred_img.shape)[[1, 0, 1, 0]]  # normalization gain whwh
            if det is not None and len(det):
                # 将检测框映射到原始图像大小
                det[:, :4] = scale_coords(img.shape[2:], det[:, :4], pred_img.shape).round()
                # 保存结果
                for *xyxy, conf, cls in reversed(det):
                    res_dict = {}
                    res_dict["class_label"] = f'{self.names[int(cls.item())]}'
                    res_dict["conf"] = conf.item()

                    res_dict["box"] = torch.Tensor(xyxy).tolist()
                    pred_res.append(res_dict)
            else:
                pred_res = [{'class_label': None, 'conf': None, 'box': None}]
        return pred_res

if __name__ == "__main__":
    image_folder = r'E:\ahs_project_code\ahs_test_code\cut\test_data'

    for image in os.listdir(image_folder):
        image_path = os.path.join(image_folder,image)
        pred_img = cv2.imdecode(np.fromfile(image_path,dtype=np.uint8),cv2.IMREAD_COLOR)
        yolov5 = YoloV5_Six('configs')
        re_list = yolov5.infer(pred_img)
        print(re_list)





