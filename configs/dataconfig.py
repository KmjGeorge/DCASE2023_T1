"""
spectrum_config = {
    'sr': 32000,
    'n_fft': 2048,
    'win_length': 2048,
    'hop_length': 744,   # 744
    'n_mels': 256,
    'freqm': 30,  # specaugment 频率掩膜
    'timem': 5,  # specaugment 时间掩膜
    'fmin': 0.0,  # mel滤波器组的最小频率
    'fmax': None,  # mel滤波器组的最大频率，None为自动配置至sr // 2 - fmax_aug_range // 2
    'fmin_aug_range': 100,  # mel滤波器频率随机偏移范围 最小值
    'fmax_aug_range': 2000,  # mel滤波器频率随机偏移范围 最大值
    'timerolling': 16000,  # timerolling范围，0为不使用，单位为帧
    'gauss_snr': 0,  # gauss噪声信噪比，0为不使用
}
"""


spectrum_config = {
    'sr': 32000,
    'n_fft': 2048,
    'win_length': 2000,
    'hop_length': 500,
    'n_mels': 256,
    'freqm': 0,  # specaugment 频率掩膜
    'timem': 0,  # specaugment 时间掩膜
    'fmin': 0.0,  # mel滤波器组的最小频率
    'fmax': None,  # mel滤波器组的最大频率，None为自动配置至sr // 2 - fmax_aug_range // 2
    'fmin_aug_range': 1,  # mel滤波器频率随机偏移范围 最小值 1为不使用
    'fmax_aug_range': 1,  # mel滤波器频率随机偏移范围 最大值 1为不使用
    'timerolling': 16000,  # timerolling范围，0为不使用，单位为帧
    'gauss_snr': 0,  # gauss噪声信噪比，0为不使用
}


'''
dataset_config = {
    'name': 'tau2022',
    'batch_size': 64,
    'meta_path': 'D:/datasets/TAU-urban-acoustic-scenes-2022-mobile-development/meta.csv',
    'audio_path': 'D:/datasets/TAU-urban-acoustic-scenes-2022-mobile-development/',
    'h5path': 'D:/github/DCASE2023/dataset/h5/',
    'num_classes': 10,
    'shuffle': True,
}
'''


dataset_config = {
    'name': 'tau2022_random_slicing',
    'batch_size': 64,
    'meta_path': 'D:/datasets/TAU-urban-acoustic-scenes-2022-mobile-development-reassembled/meta.csv',
    'audio_path': 'D:/datasets/TAU-urban-acoustic-scenes-2022-mobile-development-reassembled/',
    'h5path': 'D:/github/DCASE2023/dataset/h5/',
    'num_classes': 10,
    'shuffle': True,
}


'''
dataset_config = {
    'name': 'tau2022_reassembled',
    'batch_size': 64,
    'meta_path': 'D:/datasets/TAU-urban-acoustic-scenes-2022-mobile-development-reassembled/meta.csv',
    'audio_path': 'D:/datasets/TAU-urban-acoustic-scenes-2022-mobile-development-reassembled/',
    'h5path': 'D:/github/DCASE2023/dataset/h5/',
    'num_classes': 10,
    'shuffle': True,
}
'''
