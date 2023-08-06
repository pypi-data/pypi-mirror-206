#!/usr/bin/python
# encoding=utf-8

"""Can only be modified by the administrator. Only Core pipeline are provided..
"""
import os
import shutil

from loguru import logger
from monitors.dynamic import predict
from monitors.page.reporter import gen_report
from monitors.page.toolbox import copyfile, find_all_cases


def engine(original_path, video_path, format_video_path, monitors_report_path, model_path, summary_report_path,
           width=888,
           height=1920, device_name='Xiaomi9 Android 10'):
    """

    :param summary_report_path:
    :param model_path:
    :param monitors_report_path:
    :param format_video_path:
    :param video_path:
    :param height: video resolution
    :param width: video resolution
    :param original_path: first-hand video path
    :param device_name: device name
    :return:
    """
    global end, start
    # end = 0
    # start = 0

    if len(list(find_all_cases(base=original_path, types='files', mark='.mp4'))) == 0:
        logger.warning(f'{original_path} No video files to analyze !')
        return

    if os.path.isdir(video_path):
        shutil.rmtree(video_path)
        shutil.rmtree(format_video_path)
        os.makedirs(video_path)
        os.makedirs(format_video_path)

    target_size = (width, height)

    [copyfile(srcfile, video_path + '/') for srcfile in
     [i for i in find_all_cases(base=original_path, types='files', mark='.mp4')]]

    for video in find_all_cases(base=video_path, mark='mp4', types='files'):
        logger.info(video)
        cmd = f'/usr/local/bin/ffmpeg -i {video} -r 60 {format_video_path + "/" + video.split(".")[0].split("/")[-1]}.mp4'
        os.system(cmd)
    detail = []
    report_results = [{'devices': device_name, 'result': detail}]

    for case in find_all_cases(base=format_video_path, mark='mp4', types='files'):
        case_name = case.split(".")[0].split("/")[-1]
        result_dict = predict(video_path=case, model_file=model_path + f'/{case_name}.h5', target_size=target_size,
                              report_path=monitors_report_path + f'/{case_name}.html')

        # 0阶段中的倒序第一个时间段0。如果0是最后几帧，就用倒序第二个时间段 以此类推
        # 如果分析后产生的数据中并没有0阶段，取下一个阶段1。以此类推
        try:
            reversed_result = result_dict['0']
        except KeyError as e:
            logger.error(f"第0阶段不存在：{e}")
            reversed_result = result_dict.get('1')
            if not reversed_result:
                reversed_result = result_dict.get('2')
        for i in reversed(reversed_result):
            if float(str(i[-1]).replace('>', '').split('timestamp=')[1]) < 1:
                start = i
                break
            else:
                start = reversed_result[-1]
        if isinstance(start, list):
            start = str(start[-1]).replace('>', '').split('timestamp=')[1]
        else:
            start = str(start).replace('>', '').split('timestamp=')[1]
        logger.info(f'start collection: {reversed_result}')
        logger.info(f'start time: {start}')

        # 2阶段中的第一个时间段0。如果0是前几帧，就用第二个时间段 以此类推
        try:
            positive_order_result = result_dict['2']
            for s in positive_order_result:
                if float(str(s[0]).replace('>', '').split('timestamp=')[1]) > 0.5:
                    end = s
                    break
                else:
                    end = positive_order_result[0]
            logger.info(f'end collection: {positive_order_result}')
            logger.info(f'end time: {end}')

            if isinstance(end, list):
                end = str(end[0]).replace('>', '').split('timestamp=')[1]
            else:
                end = str(end).replace('>', '').split('timestamp=')[1]
            logger.info(end)
        except KeyError as e:
            logger.error(f"第2阶段不存在: {e}")
            positive_order_result = result_dict['1']
            end = positive_order_result[-1]
            logger.info(f'end collection: {positive_order_result}')
            logger.info(f'end time: {end}')

            if isinstance(end, list):
                end = str(end[-1]).replace('>', '').split('timestamp=')[1]
            else:
                end = str(end).replace('>', '').split('timestamp=')[1]
            logger.info(end)
        try:
            cost = abs(round((float(end) - float(start)) * 1000))
            logger.info(f'cost time: {cost}')
        except ValueError:
            cost = 'abnormal video'
            logger.error(f'cost time: {cost}')

        # 取正整数，保证报告数据展示正常
        detail.append({'name': case_name, 'cost': cost})

    gen_report(results=report_results, report_path=summary_report_path)
    logger.info(detail)
    logger.info('end of prediction！')
    return detail
