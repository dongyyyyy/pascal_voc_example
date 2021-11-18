import xml.etree.ElementTree as elemTree
import os
import cv2
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    xml_path = 'C:/Users/woals/VOCdevkit/VOC2007/Annotations/'
    img_path = 'C:/Users/woals/VOCdevkit/VOC2007/JPEGImages/'
    img_list = os.listdir(img_path)
    xml_list = [f'{name.split(".jpg")[0]}.xml' for name in img_list]

    img_list = [f'{img_path}{name}' for name in img_list]
    xml_list = [f'{xml_path}{name}' for name in xml_list]



    for index in range(len(img_list)):
        print('path ',img_list[index])
        image = cv2.imread(img_list[index],cv2.IMREAD_COLOR)
        # print(image)
        tree = elemTree.parse(xml_list[index])
        root = tree.getroot()

        bb_list = []
        for user in tree.findall('object'):
            lists = []
            lists.append(user.findtext('name'))
            lists.append(int(user.find('bndbox').findtext('xmin')))
            lists.append(int(user.find('bndbox').findtext('ymin')))
            lists.append(int(user.find('bndbox').findtext('xmax')))
            lists.append(int(user.find('bndbox').findtext('ymax')))

            bb_list.append(lists)
        print(bb_list[0][1])
        for i in range(len(bb_list)):
            image = cv2.rectangle(image,(bb_list[i][1],bb_list[i][2]),(bb_list[i][3],bb_list[i][4]),color=(255,0,0), thickness=1)
        cv2.imshow('show results',image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        print(bb_list)
        exit(1)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
