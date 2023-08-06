# -*- coding: utf-8 -*-

class DocumentAddRequest():
    """根据id获取临时下载地址"""
    def __init__(self):
        self.accessConfigName = None
        self.accessObjectName = None
        self.clientCode = None
        self.userCode = None
        self.fileName = None
        self.fileUri = None
        self.fileSize = 0
        self.name = None
        self.memo = None
        self.style = None
        self.watermark = None
        self.downloadLimit = None
        """文件过期时间（秒）"""
        self.expirySeconds = None
        self.checkExists = False

    def getApiMethod(self):
        return 'document/add'

