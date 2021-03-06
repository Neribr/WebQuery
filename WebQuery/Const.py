# region Bytes
BYTES_ITEMS = bytearray(
    b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x10\x00\x00\x00\x10\x08\x06\x00\x00\x00\x1f'
    b'\xf3\xffa\x00\x00\x00\x04sBIT\x08\x08\x08\x08|\x08d\x88\x00\x00\x00\tpHYs\x00\x00\x0b\x13'
    b'\x00\x00\x0b\x13\x01\x00\x9a\x9c\x18\x00\x00\x00MIDAT8\x8d\xd5\x91\xc1\t\xc00\x0c\xc4TO'
    b'\x96\rL6\xf2F\x877\xc8d\xa6\xafB\x9f!P\xd2\xe8\x7fpB\xb0\x9b\x0b\xa0\xf7\x1e\x92\xc2\xdd'
    b'\x9b\x99\xb5\xd9\xb1\xa4\xb0\xaf\x9eM\xb3\xa4PU#3\x07\xc0\xa1\n\x0f\x87Vx\x17\x80?T\xd8'
    b'\xcf\r\xa5\x9e(\r0\x19&\xcc\x00\x00\x00\x00IEND\xaeB`\x82')

BYTES_GEAR = bytearray(b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x10\x00\x00\x00\x10'
                       b'\x08\x06\x00\x00\x00\x1f\xf3\xffa\x00\x00\x00\x04sBIT\x08\x08\x08'
                       b'\x08|\x08d\x88\x00\x00\x00\tpHYs\x00\x00\x0b\x13\x00\x00\x0b'
                       b'\x13\x01\x00\x9a\x9c\x18\x00\x00\x01PIDAT8\x8d}\xd3MKVQ\x14\x05'
                       b'\xe0\xc7\xab\xf9A\x86\xf9AX"\xf5+D"\x10\xfa\x13\x82\x93\x10'
                       b'\xc4\x89\x08\x82\x88`?A\x0b\x9c\xd8$P\x82h\xd0 B\x85\xd0\x818s*'
                       b"\x89\x8a\xa2\x98P\x13'\xa2)\x0e\xf2cp\xf7\x85\x83\xdd\xf7]p"
                       b'8\x9b\xb3\xd6Yg\xef\xbb\xef\xaeQ\x19\xb7\xb8\x8e\xb8\x165U\xb4'
                       b'\xa5\xf8\x17{]\x98\x95"\x8b\xbd\x1bSh\x8c5^\xa2\x1dC\x03'
                       b'\x9a\xf0\x16\xcfR\xf2\x0b\xb6q\x88\x1d|Eo\xc2\xbf\xc47l\xe1(4\x9f\n'
                       b'\xf2\x15~\x85s\x1f\xdeT)k0\xf4\xcd\xf8]<\xf2\x03\xab\xe8'
                       b'H\x84\x8d\xf8\x80s\xfc\xc5\\\xa4_\xe0\t\xd6\xb1\x98\xa1\x1f?\xb1'
                       b'\x9b\xd4\xf5.D/\xf0\x1c\x9d\x98\t\xae;J\xd8\xc0@\x9a\xde\x15'
                       b'\xea#>\r\x83\xf4\xc5\xd3\x88\x9bqY\x10\x99r\xdc\xefy\x86\x9b2a\x86V'
                       b'\xcc\xe2\x0c\xedq>\x8f\x8fQRW\xc4\xf3\xc1=\xc6\x05\xde\xa3\x85'
                       b'\xfc#\xae\xa0-1\xae\x0f\xc1I\xaci<H\xf8\x0e\xaca\x89\xbc'
                       b'\xc7\xc7x\x88\xd7\x18\xaaP\x16\x0c\xcb[\xfd\x08\x7f\xd0'
                       b'S\x10\x9f\xb1\x87}\xf9\xcf\xf2]\xde\xef\x02}X\xc6&\x0eB\xbb\x90:wa'
                       b'"Ro\xc0\xa8\xffga$\xe1\'\xf1\xb4J\xa6\x84A]\\\xa88L\xd5F'
                       b'\xf4\xfe\xa5R\xed\x1d\xd81A\xc9\x94\x9bY}\x00\x00\x00\x00IEND\xaeB'
                       b'`\x82')

# endregion

TRANS = {
    "WEB QUERY": {"zh_CN": "微波颗粒", "en": "Web Query"},
    "OPTIONS": {"zh_CN": "选项", "en": "Options"},
    "WEB QUERY TAB VISIBILITY": {"zh_CN": "微波颗粒标签页管理", "en": "Web Query Tab Visibility"},
    "QUERY FIELD": {"zh_CN": "查询字段", "en": "Query Field"},
    "IMAGE CAPTURE": {"zh_CN": "截图", "en": "Image Capture"},
    "TEXT CAPTURE": {"zh_CN": "文本摘取", "en": "Text Capture"},
    "CAPTURE IMAGE (C)": {"zh_CN": "截图（C）", "en": "Capture Image (C)"},
    "SAVE (C)": {"zh_CN": "保存（C）", "en": "Save (C)"},
    "SAVE TEXT (T)": {"zh_CN": "保存文本（T）", "en": "Save Text (T)"},
    "RETURN": {"zh_CN": "返回", "en": "Return"},
    "APPEND MODE": {"zh_CN": "追加模式", "en": "Append Mode"},
    "AUTO SAVE": {"zh_CN": "自动保存", "en": "Auto Save"},
    "RIGHT-CLICK MODE": {"zh_CN": "右键模式", "en": "Right-Click Mode"},
    "TRIGGER EDIT": {"zh_CN": "触发编辑", "en": "Trigger Edit"},
    "TOGGLE WEBQUERY": {"zh_CN": "启动", "en": "Toggle WebQuery"},
    "TOGGLE VISIBILITY": {"zh_CN": "微波颗粒标签页管理", "en": "Toggle Visibility"},
    "SAVE TO FIELD [{}] (T)": {"zh_CN": "保存至字段 [{}]（T）", "en": "Save to field [{}] (T)"},
    "<B>LOADING ... </B>": {"zh_CN": "<b>正在载入 ... </b>", "en": "<b>Loading ... </b>"},
    "SAVED IMAGE TO CURRENT CARD: {}": {"zh_CN": "以保存至当前笔记：{}", "en": "Saved image to current card: {}"},
    "USER CONFIG": {"zh_CN": "用户设置", "en": "User Config"},
}
