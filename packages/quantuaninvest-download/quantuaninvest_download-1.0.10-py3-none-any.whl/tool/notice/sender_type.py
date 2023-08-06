import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from tool.common.qmt_enum import enum_holding_type, enum_notice_info


def send_email(ContextInfo, g, msg, title):
    # 发件人
    from_name, my_title = generate_send_header(ContextInfo)
    # 发件邮箱
    from_addr = "252992499@qq.com"
    # 发件邮箱授权码，注意不是QQ邮箱密码
    from_pwd = "fuitzhzgvylsbigj"
    # 收件邮箱
    to_addr = "252992499@qq.com"

    # 邮件标题
    my_title += str(title)
    # 邮件正文
    my_msg = msg

    # MIMEText三个主要参数
    # 1. 邮件内容
    # 2. MIME子类型，plain表示text类型
    # 3. 邮件编码格式，使用"utf-8"避免乱码
    msg = MIMEText(str(my_msg), 'plain', 'gbk')
    msg['From'] = formataddr([from_name, from_addr])
    # 邮件的标题
    msg['Subject'] = my_title

    # SMTP服务器地址，QQ邮箱的SMTP地址是"smtp.qq.com"
    smtp_srv = "smtp.qq.com"
    # 判断是否发送过错误信息,发送过信息则不再发送
    if is_sended(g, str(my_msg)):
        return

    try:
        # 不能直接使用smtplib.SMTP来实例化，第三方邮箱会认为它是不安全的而报错
        # 使用加密过的SMTP_SSL来实例化，它负责让服务器做出具体操作，它有两个参数
        # 第一个是服务器地址，但它是bytes格式，所以需要编码
        # 第二个参数是服务器的接受访问端口，SMTP_SSL协议默认端口是465
        srv = smtplib.SMTP_SSL(smtp_srv.encode(), 465)

        # 使用授权码登录QQ邮箱
        srv.login(from_addr, from_pwd)

        # 使用sendmail方法来发送邮件，它有三个参数
        # 第一个是发送地址
        # 第二个是接受地址，是list格式，可以同时发送给多个邮箱
        # 第三个是发送内容，作为字符串发送
        srv.sendmail(from_addr, [to_addr], msg.as_string())
        print('发送成功')
        g.last_send_error_msg = str(my_msg)

    except Exception as e:
        print('发送失败')
        print("error ", e)
    finally:
        # 无论发送成功还是失败都要退出你的QQ邮箱
        srv.quit()


def is_sended(g, msg_str):
    """
    是否发送了错误信息，避免重复发送
    """

    if len(msg_str) != len(g.last_send_error_msg):
        return False
    else:
        if msg_str == g.last_send_error_msg:
            return True
        else:
            return False


def generate_send_email_from_name(ContextInfo):
    return ContextInfo.strategy_version + "|" + ContextInfo.accID + "|" + ContextInfo.datatype + "|" + ContextInfo.holding_type


def generate_send_header(ContextInfo):
    from_name = generate_send_email_from_name(ContextInfo)
    title_summary = generate_email_title_summary(ContextInfo)
    return from_name, from_name + "|" + title_summary


def generate_email_title_summary(ContextInfo):
    if ContextInfo.holding_type == enum_holding_type.DBP.value:
        return enum_notice_info.DBP_FIRM_BARGAIN.value
    elif ContextInfo.holding_type == enum_holding_type.RZ.value:
        return enum_notice_info.RZ_FIRM_BARGAIN.value
    elif ContextInfo.holding_type == enum_holding_type.NORMAL.value:
        return enum_notice_info.NORMAL_FIRM_BARGAIN.value
