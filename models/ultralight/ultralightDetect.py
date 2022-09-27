import cv2
import onnx
import onnxruntime as ort
from onnx_tf.backend import prepare
import numpy as np
# import time

onnx_path = './weights/ultralight_onnx/ultralight.onnx'
onnx_model = onnx.load(onnx_path)
predictor = prepare(onnx_model)
ort_session = ort.InferenceSession(onnx_path)
input_name = ort_session.get_inputs()[0].name

#
def area_of(left_top, right_bottom):
    hw = np.clip(right_bottom - left_top, 0.0, None)
    return hw[..., 0] * hw[..., 1]

def iou_of(boxes0, boxes1, eps=1e-5):
    overlap_left_top = np.maximum(boxes0[..., :2], boxes1[..., :2])
    overlap_right_bottom = np.minimum(boxes0[..., 2:], boxes1[..., 2:])

    overlap_area = area_of(overlap_left_top, overlap_right_bottom)
    area0 = area_of(boxes0[..., :2], boxes0[..., 2:])
    area1 = area_of(boxes1[..., :2], boxes1[..., 2:])
    return overlap_area / (area0 + area1 - overlap_area + eps)

def hard_nms(box_scores, iou_threshold, top_k=-1, candidate_size=200):
    scores = box_scores[:, -1]
    boxes = box_scores[:, :-1]
    picked = []
    indexes = np.argsort(scores)
    indexes = indexes[-candidate_size:]
    while len(indexes) > 0:
        current = indexes[-1]
        picked.append(current)
        if 0 < top_k == len(picked) or len(indexes) == 1:
            break
        current_box = boxes[current, :]
        indexes = indexes[:-1]
        rest_boxes = boxes[indexes, :]
        iou = iou_of(
            rest_boxes,
            np.expand_dims(current_box, axis=0),
        )
        indexes = indexes[iou <= iou_threshold]

    return box_scores[picked, :]
    

def predict(width, height, confidences, boxes, prob_threshold, iou_threshold=0.5, top_k=-1):
    boxes = boxes[0]
    confidences = confidences[0]
    picked_box_probs = []
    for class_index in range(1, confidences.shape[1]):
        probs = confidences[:, class_index]
        mask = probs > prob_threshold
        probs = probs[mask]
        if probs.shape[0] == 0:
            continue
        subset_boxes = boxes[mask, :]
        box_probs = np.concatenate([subset_boxes, probs.reshape(-1, 1)], axis=1)
        box_probs = hard_nms(box_probs,
           iou_threshold=iou_threshold,
           top_k=top_k,
           )
        picked_box_probs.append(box_probs)
    if not picked_box_probs: # can not detect face
        return np.array([]), np.array([]), False
    picked_box_probs = np.concatenate(picked_box_probs)
    picked_box_probs[:, 0] *= width
    picked_box_probs[:, 1] *= height
    picked_box_probs[:, 2] *= width
    picked_box_probs[:, 3] *= height
    return picked_box_probs[:, :4].astype(np.int32), picked_box_probs[:, 4], True

def load_img(dir):
    img = cv2.imread(dir)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img

def Handle_img(image):
    # img_raw = image
    # h, w, _ = img_raw.shape
    # img = img_raw
    h, w, _ = image.shape #replace
    img = image #replace
    img = cv2.resize(img, (640, 480))
    img_mean = np.array([127, 127, 127])
    img = (img - img_mean) / 128
    img = np.transpose(img, [2, 0, 1])
    img = np.expand_dims(img, axis=0)
    img = img.astype(np.float32)
    return h, w, img


def Detect_face(image): #0.022s
    h, w, img = Handle_img(image) #0.008s #optimized best
    confidences, boxes = ort_session.run(None, {input_name: img}) #0.012s #optimized best
    boxes, probs, status = predict(w, h, confidences, boxes, 0.8) #0.001s
    if (status):
        return boxes, True
    return 0, False
    
def crop_face(image, boxes):
    # for i in range(boxes.shape[0]):
    #     box = boxes[i, :]
    #     img_crop = image[box[1]: box[3], box[0]: box[2]]
    # return img_crop
    x1, y1, x2, y2 = boxes[0]
    img_crop = image[y1: y2, x1: x2]
    return img_crop