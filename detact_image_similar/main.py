'''
Desc:
File: /main.py
Project: detact_similar
File Created: Sunday, 11th September 2022 11:05:30 pm
Author: luxuemin2108@gmail.com
-----
Copyright (c) 2022 Camel Lu
'''
import os
from PIL import Image
from datetime import date, datetime, timedelta
import imagehash
from skimage import io
from sewar.full_ref import uqi, ssim, mse, psnr, msssim, sam, vifp

dir = os.getcwd() + '/detact_image_similar/'

img_dir = dir + 'img/'
samples_dir = dir + 'samples/'


def use_imagehash():
    # 分别计算两图片hash值
    imgs = os.listdir(img_dir)
    for img_file in imgs:
        print("img_file", img_file)
        img1 = Image.open(img_dir + img_file)
        hash_size = 8
        hash_size_w = 8
        mode = 'db4'
        image_scale = 8
        binbits = 3
        hash_av_1 = imagehash.average_hash(img1, hash_size=hash_size)
        hash_p_1 = imagehash.phash(img1, hash_size=hash_size)
        hash_w_1 = imagehash.whash(
            img1, image_scale=image_scale, hash_size=hash_size_w, mode=mode)
        hash_d_1 = imagehash.dhash(img1, hash_size=hash_size)
        hash_c_1 = imagehash.colorhash(img1, binbits=binbits)
        level1 = img_file[-10:-9]
        for filename in imgs:
            if img_file == filename:
                continue
            level2 = filename[-10:-9]

            img2 = Image.open(
                img_dir + filename)

            hash_d_2 = imagehash.dhash(img2, hash_size=hash_size)
            similar_d = 1 - (hash_d_1 - hash_d_2) / \
                len(hash_d_1.hash) ** 2
            diff_d = hash_d_1 - hash_d_2

            hash_p_2 = imagehash.phash(img2, hash_size=hash_size)
            similar_p = 1 - (hash_p_1 - hash_p_2) / \
                len(hash_p_1.hash) ** 2
            diff_p = hash_p_1 - hash_p_2

            # average_hash
            hash_av_2 = imagehash.average_hash(img2, hash_size=hash_size)
            similar_av = 1 - (hash_av_1 - hash_av_2)/len(hash_av_1.hash)**2
            diff_av = hash_av_1 - hash_av_2

            # colorhash
            hash_c_2 = imagehash.colorhash(img2, binbits=binbits)
            similar_c = 1 - (hash_c_1 - hash_c_2)/len(hash_c_1.hash)**2
            diff_c = hash_c_1 - hash_c_2

            # average_hash
            hash_av_2 = imagehash.average_hash(img2, hash_size=hash_size)
            similar_av = 1 - (hash_av_1 - hash_av_2)/len(hash_av_1.hash)**2
            diff_av = hash_av_1 - hash_av_2

            hash_w_2 = imagehash.whash(
                img2, image_scale=image_scale, hash_size=hash_size_w, mode=mode)
            diff_w = hash_w_1 - hash_w_2
            similar_w = 1 - (hash_w_1 - hash_w_2)/len(hash_w_1.hash)**2

            if level1 == level2:
                # if level1 == '1':
                #     print("similar_av", similar_av)
                if similar_p <= 0.8:
                    print("error", similar_p, level1, level2)
                if similar_av < 0.9:
                    print('error:similar_av', similar_av)
            elif similar_p >= 0.8:
                print("error", similar_p, level1, level2)
            elif similar_av > 0.9:
                print("error", similar_av, level1, level2)
            print('level', level1, ':', level2, 'similar_av:',
                  similar_av, 'similar_p:', similar_p)
            print('level', level1, ':', level2,
                  diff_p, diff_av, diff_w, diff_d, diff_c)

    hash1 = imagehash.average_hash(Image.open(
        dir + 'img/2022-09-12-00_40_22_3_code.png'))
    hash2 = imagehash.average_hash(Image.open(
        dir + '/img/2022-09-12-00_40_59_0_code.png'))
    # 比较哈希值
    dif = hash1 - hash2
    # 设定最大不同值（我这里是肉眼看两封面确实相同时，然后跑了几次case，发现10以内基本确保图片是一定一致的
    # 可以拿真实的case跑几次试一下，然后确定一个最大不同值
    max_dif = 10
    if dif < 0:
        dif = -dif
    # dif与最大值比较一下就可以了，返回结果可以随意设定
    if dif <= max_dif:
        return True
    else:
        return False


def use_sewar():
    imgs = os.listdir(img_dir)
    sample_imgs = os.listdir(samples_dir)
    for img_file in imgs:
        print("img_file", img_file)
        img_path_1 = img_dir + img_file
        # img1 = Image.open(img_path_1)
        img1 = io.imread(fname=img_path_1)
        level1 = img_file[-10:-9]
        for filename in sample_imgs:
            level2 = filename[-5:-4]
            img_path_2 = samples_dir + filename
            # img2 = Image.open(
            #     img_path_2)
            img2 = io.imread(fname=img_path_2)
            # res_ssim = ssim(img1, img2)
            # res_mse = mse(img1, img2)
            res_uqi = uqi(img1, img2)
            # res_psnr = psnr(img1, img2)  # 不适合
            res_sam = sam(img1, img2)
            # res_vifp = vifp(img1, img2)

            print("res", level1, level2, res_uqi, res_sam)
            if res_uqi > 0.98 and res_sam < 0.11:
                # res_level = level2
                assert level2 == level1, "level2 != level1"
            else:
                assert level2 != level1, "level2 == level1"


if __name__ == '__main__':
    res = use_sewar()
    print("res", res)
