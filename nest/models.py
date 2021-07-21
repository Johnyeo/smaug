from django.db import models

# Create your models here.


class Staff(models.Model):
    real_name = models.CharField(max_length=200)

    # 手机号不用int而是用char
    # 原因在于手机号可能0开头，甚至可能包含其他字符
    phone = models.CharField(max_length=200)
    username = models.CharField(max_length=200)

    # 用于记录数据创建时间
    created = models.DateTimeField(auto_created=True)

    # 当调用model.save()的时候会更新，其他情况例如Queryset.update()不会更新
    # 用于记录数据最后更新时间
    updated = models.DateTimeField(auto_now=True)

    # 逻辑删除
    deleted = models.SmallIntegerField(default=0)

# 设备表
class Device(models.Model):
    # 设备名字
    name = models.CharField(max_length=200)

    # 资产编号
    asset_id = models.CharField(max_length=200)

    # 设备图
    img_path = models.CharField(max_length=2000)

    # 创建这条数据的用户
    # 这里选择不用外键关联用户表。外键约束太强。
    # 这里选择不记录设备的历史变更，只记录修改人
    modifier = models.CharField(max_length=200)

    # 资产类型 0 未知  1 Android  2 iOS  3 Android pad  4 iOS pad
    device_type = models.SmallIntegerField(default=0)

    # 系统版本例如  android 9.0
    device_os = models.CharField(blank=True)

    # 锁屏密码
    password = models.CharField(blank=True)

    # 苹果id或者其他
    account = models.CharField(blank=True)

    # 目前状态 0 损坏  1 正常  2 外借
    status = models.SmallIntegerField(default=1)

    # 备注
    comment = models.CharField(max_length=2000)

    # 格式代码
    deleted = models.SmallIntegerField(default=0)
    created = models.DateTimeField(auto_created=True)
    updated = models.DateTimeField(auto_now=True)

# 签入签出记录表
class CheckRecord(models.Model):
    # 设备的id
    # 使用设备表的id，设备表的自增主键查了一下就是一个普通的int，因此这里也用int类型
    device_id = models.IntegerField()

    # 当前使用者
    owner = models.CharField(max_length=200)

    # 从谁那里签入
    from_whom = models.CharField(max_length=200)
    # 签出到谁那里
    to_whom = models.CharField(max_length=200)

    # 从谁那里签入
    from_staff_id = models.IntegerField()
    # 签出到谁那里
    to_staff_id = models.IntegerField()

    # 格式代码
    deleted = models.SmallIntegerField(default=0)
    created = models.DateTimeField(auto_created=True)
    updated = models.DateTimeField(auto_now=True)


    # 设备的id
    # 使用设备表的id，设备表的自增主键查了一下就是一个普通的int，因此这里也用int类型
    device_id = models.IntegerField()

    # 当前使用者
    owner_id = models.IntegerField()

    # 当前使用者
    owner_name = models.CharField(max_length=200)

    # 格式代码
    deleted = models.SmallIntegerField(default=0)
    created = models.DateTimeField(auto_created=True)
    updated = models.DateTimeField(auto_now=True)